import collections
from enum import Enum
from textwrap import dedent
from typing import Dict, List, Literal, Optional, Set, Union

from pydantic import BaseModel, Field, ValidationError, parse_obj_as

from deepsearch import CpsApi
from deepsearch.core.util.ccs_utils import get_ccs_project_key
from deepsearch.cps.apis import public as sw_client
from deepsearch.documents.core.utils import URLNavigator


class S3Coordinates(BaseModel):
    host: str
    port: int

    ssl: bool
    verify_ssl: bool

    access_key: str
    secret_key: str

    bucket: str
    location: str
    key_prefix: str = ""

    external_endpoint: Optional[str] = None

    key_infix_format: str = Field(
        "",
        description=dedent(
            """
            Control the infix of the object keys that are saved on the document's `_s3_data`, after `key_prefix`, 
            and before `PDFDocuments/{document_hash}.pdf` or `PDFPages/{page_hash}.pdf`.

            By default, the infix is empty.
            For using the name of the index in the coordinates, you can use `key_infix_format = "{index_name}"`.

            For example, if: 

            ```
            key_prefix = "my_prefix/"
            key_infix_format = "{index_name}"
            index_name = "my_elastic_index"

            document_hash = "123"
            ```

            Then, the document above would be uploaded to: `my_prefix/my_elastic_index/PDFDocuments/123.pdf`.

            If one were to set `key_infix_format = ""`, it would be uploaded to `my_prefix/PDFDocuments/123.pdf`.

            If one were to set `key_infix_format = "foo"`, it would be uploaded to `my_prefix/foo/PDFDocuments/123.pdf`

            Finally, one can combine `{index_name}` with constants and even path separators.

            So, `{index_name}/test` would produce `my_prefix/my_elastic_index/test/PDFDocuments/123.pdf`
            """
        ),
    )


class DocumentExistsInTargetAction(str, Enum):
    """
    What to do if the document already exists on the target.

    - `replace` will replace the document, destroying any external modifications.
    - `merge` will try to merge the updated contents with the already-present document.
    - `skip` will not touch the document on the target, leaving it as-is.

    Using `skip` will incur in a performance increase, however, if the document
    is modified externally, CCS will not update it back to the original state.
    """

    REPLACE = "replace"
    MERGE = "merge"
    SKIP = "skip"


class MongoCollectionCoordinates(BaseModel):
    uri: str
    database: str
    collection: str


class MongoS3TargetCoordinates(BaseModel):
    """Coordinates to a Mongo collection, and optionally, an S3 bucket"""

    mongo: MongoCollectionCoordinates
    s3: Optional[S3Coordinates]


class MongoS3Target(BaseModel):
    type: Literal["mongo_s3"] = "mongo_s3"

    # Coordinates for the export
    coordinates: MongoS3TargetCoordinates

    if_document_exists: DocumentExistsInTargetAction = (
        DocumentExistsInTargetAction.MERGE
    )


class ZipPackageContentType(str, Enum):
    """Specify the content type for the documents in the Zip file."""

    JSON = "json"
    HTML = "html"


class ZipTarget(BaseModel):
    """
    Specify how the documents should be exported to a Zip file.
    If the [coordinates] are not specified, the project's coordinates
    will be used.
    """

    type: Literal["zip"] = "zip"

    content_type: ZipPackageContentType = ZipPackageContentType.JSON

    add_cells: bool = True


class ElasticIndexCoordinates(BaseModel):
    hosts: List[str]
    dangerously_disable_ssl_validation: bool = False
    ca_certificate_base64: Optional[str] = None
    index: str


class ElasticS3TargetCoordinates(BaseModel):
    elastic: ElasticIndexCoordinates
    s3: Optional[S3Coordinates]


class ElasticS3Target(BaseModel):
    type: Literal["elastic_s3"] = "elastic_s3"

    coordinates: ElasticS3TargetCoordinates

    if_document_exists: DocumentExistsInTargetAction = (
        DocumentExistsInTargetAction.MERGE
    )

    add_cells: bool = False

    add_raw_pages: bool = False

    add_annotations: bool = False

    escape_ref_fields: bool = Field(
        default=True,
        description="If true, `$ref` fields are renamed to `__ref`. This allows the data to then be written into a MongoDB collection.",
    )


class COSTarget(BaseModel):
    type: Literal["cos"] = "cos"

    coordinates: S3Coordinates

    add_raw_pages: bool = False

    add_annotations: bool = False


ExportTarget = Union[
    ZipTarget,
    MongoS3Target,
    ElasticS3Target,
    COSTarget,
]


class ProjectConversionModel(BaseModel):
    name: Optional[str]  # named model (config)
    config_id: str  # the model config key. Validate with available models CCS project.
    proj_key: str

    @classmethod
    def get_models(
        cls, api: CpsApi, proj_key: str
    ) -> Dict[
        str, List["ProjectConversionModel"]
    ]:  # get list of available project models

        stages_to_models = collections.defaultdict(list)

        proj_key, _ = get_ccs_project_key(api, proj_key)

        request_project_models = api.client.session.get(
            url=URLNavigator(api).url_project_models(proj_key)
        )
        request_project_models.raise_for_status()
        models_dict = request_project_models.json()

        for elem in models_dict:
            for stage in elem["supported_stages"]:
                stages_to_models[stage].append(
                    ProjectConversionModel.from_ccs_spec(elem)
                )

        return stages_to_models  # FIXME: Dummy

    def to_ccs_spec(self):
        obj = {
            "name": self.name,
            "description": "",
            "proj_key": self.proj_key,
            "model_config_key": self.config_id,
        }

        return obj

    @classmethod
    def from_ccs_spec(cls, obj):
        return cls(
            name=obj.get("name"),
            config_id=obj.get("model_config_key"),
            proj_key=obj.get("proj_key"),
        )


class DefaultConversionModel(BaseModel):
    type: str  # system model "type". Validate with available options on CCS API.
    config: dict = {}  # model configuration dict

    @classmethod
    def get_models(
        cls, api: CpsApi
    ) -> Dict[
        str, List["DefaultConversionModel"]
    ]:  # get list of available default models

        stages_to_models = collections.defaultdict(list)

        request_system_models = api.client.session.get(
            url=URLNavigator(api).url_system_models()
        )
        request_system_models.raise_for_status()
        models_dict = request_system_models.json()

        for elem in models_dict:
            for stage in elem["supported_stages"]:
                stages_to_models[stage].append(
                    DefaultConversionModel.from_ccs_spec(elem)
                )

        return stages_to_models  # FIXME: Dummy

    def to_ccs_spec(self):
        return self.dict()

    @classmethod
    def from_ccs_spec(cls, obj):
        return cls.parse_obj(obj)


ConversionModel = Union[DefaultConversionModel, ProjectConversionModel]


class ConversionPipelineSettings(BaseModel):
    clusters: ConversionModel
    tables: Optional[ConversionModel]

    @classmethod
    def from_ccs_spec(cls, obj):
        if obj is None:
            raise ValueError("CCS spec can not be None")
        if obj.get("clusters") and len(obj.get("clusters")):
            model_dict = obj.get("clusters")[0]

            clusters = cls._make_conversion_model(model_dict)

            instance = cls(clusters=clusters)
            if obj.get("tables") and len(obj.get("tables")):
                model_dict = obj.get("tables")[0]

                instance.tables = cls._make_conversion_model(model_dict)

            return instance
        else:
            raise ValueError("CCS spec must have non-empty clusters")

    @classmethod
    def _make_conversion_model(cls, model_dict):
        if "model_config_key" in model_dict.keys():
            return ProjectConversionModel.from_ccs_spec(model_dict)
        else:
            return DefaultConversionModel.from_ccs_spec(model_dict)

    def to_ccs_spec(self):
        obj = {
            "clusters": [self.clusters.to_ccs_spec()],
            "page": [],
            "tables": [self.tables.to_ccs_spec()] if self.tables else [],
            "normalization": [],
        }

        return obj


class OCRModeEnum(str, Enum):
    auto = "auto"
    keep_only_ocr = "keep-only-ocr"
    prioritize_programmatic = "prioritize-programmatic"
    prioritize_ocr = "prioritize-ocr"


class OCRSettings(BaseModel):
    enabled: bool = False
    backend: str = "tesseract-ocr"  # validate with available options on CCS API
    config: dict = {}  # implementation specific to OCR backend
    merge_mode: Optional[OCRModeEnum] = OCRModeEnum.prioritize_ocr

    @classmethod
    def get_backends(
        cls, api: CpsApi
    ) -> List[Dict]:  # get list of available OCR backends
        request_backends = api.client.session.get(
            url=URLNavigator(api).url_conversion_defaults()
        )
        request_backends.raise_for_status()
        return request_backends.json()

    def to_ccs_spec(self):
        return self.dict()

    @classmethod
    def from_ccs_spec(cls, obj):
        return cls.parse_obj(obj or {})


class ConversionMetadata(BaseModel):
    description: str = ""
    display_name: str = ""
    license: str = ""
    source: str = ""
    version: str = ""

    @classmethod
    def from_ccs_spec(cls, obj):
        return cls.parse_obj(obj or {})

    def to_ccs_spec(self):
        return self.dict()


class ConversionSettings(BaseModel):
    pipeline: Optional[ConversionPipelineSettings]
    ocr: Optional[OCRSettings]
    metadata: Optional[ConversionMetadata]

    @classmethod
    def from_project(cls, api: CpsApi, proj_key: str) -> "ConversionSettings":
        conv_settings = cls()

        proj_key, _ = get_ccs_project_key(api, proj_key)

        request_conv_settings = api.client.session.get(
            url=URLNavigator(api).url_collection_settings(proj_key, "_default")
        )
        request_conv_settings.raise_for_status()
        settings_dict = request_conv_settings.json()

        conv_settings.pipeline = ConversionPipelineSettings.from_ccs_spec(
            settings_dict.get("model_pipeline")
        )
        conv_settings.ocr = OCRSettings.from_ccs_spec(settings_dict.get("ocr"))
        conv_settings.metadata = ConversionMetadata.from_ccs_spec(
            settings_dict.get("metadata")
        )
        return conv_settings

    @classmethod
    def from_defaults(cls, api: CpsApi) -> "ConversionSettings":
        conv_settings = cls()

        request_conv_settings = api.client.session.get(
            url=URLNavigator(api).url_conversion_defaults()
        )
        request_conv_settings.raise_for_status()
        settings_dict = request_conv_settings.json()

        conv_settings.pipeline = ConversionPipelineSettings.from_ccs_spec(
            settings_dict.get("model_pipeline")
        )
        conv_settings.ocr = OCRSettings.from_ccs_spec(settings_dict.get("ocr"))
        conv_settings.metadata = ConversionMetadata.from_ccs_spec(
            settings_dict.get("metadata")
        )

        return conv_settings

    def to_ccs_spec(self):
        obj = {}

        if self.pipeline:
            obj["model_pipeline"] = self.pipeline.to_ccs_spec()
        if self.ocr:
            obj["ocr"] = self.ocr.to_ccs_spec()
        if self.metadata:
            obj["metadata"] = self.metadata.to_ccs_spec()

        return obj
