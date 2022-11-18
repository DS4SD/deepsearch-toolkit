from enum import Enum
from typing import List, Literal, Optional, Set, Union

from pydantic import BaseModel, Field

from deepsearch import CpsApi


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

    escape_ref_fields: bool = Field(
        default=True,
        description="If true, `$ref` fields are renamed to `__ref`. This allows the data to then be written into a MongoDB collection.",
    )


ExportTarget = Union[
    ZipTarget,
    MongoS3Target,
    ElasticS3Target,
]


class ProjectConversionModel(BaseModel):
    name: Optional[str]  # named model (config)
    config_id: str  # the model config key. Validate with available models CCS project.
    proj_key: str

    @classmethod
    def get_models(
        cls, api: CpsApi, proj_key: str
    ) -> List["ProjectConversionModel"]:  # get list of available project models
        return []  # FIXME: Dummy

    def to_ccs_spec(self):
        obj = {
            "name": self.name,
            "description": "",
            "proj_key": self.proj_key,
            "model_config_key": self.config_id,
        }

        return obj

    """
    # project model config
    { 
        "config_id": "c0e64f4db662d96a222f38174bd22312",
        "name": "table-test-1",
        "proj_key": "93907db9fb895f868f9310512e273b8e1a3991bd"
    },
    """


class DefaultConversionModel(BaseModel):
    type: str  # system model "type". Validate with available options on CCS API.
    config: dict  # model configuration dict

    @classmethod
    def get_models(
        cls, api: CpsApi
    ) -> List["DefaultConversionModel"]:  # get list of available default models
        return []  # FIXME: Dummy

    def to_ccs_spec(self):
        return self.dict()

    """
    # default system model config
    { 
        "config": {},
        "type": "LayoutSegmentationModel"    
    }
    """


ConversionModel = Union[DefaultConversionModel, ProjectConversionModel]


class ConversionPipelineSettings(BaseModel):
    clusters: ConversionModel
    tables: Optional[ConversionModel]

    @classmethod
    def from_defaults(cls, api: CpsApi) -> "ConversionPipelineSettings":
        return cls()  # FIXME: Dummy

    @classmethod
    def from_project(cls, api: CpsApi, proj_key: str) -> "ConversionPipelineSettings":
        return cls()  # FIXME: Dummy

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
    merge_mode: OCRModeEnum = OCRModeEnum.prioritize_ocr

    @classmethod
    def from_defaults(cls, api: CpsApi) -> "OCRSettings":
        return cls()  # FIXME: Dummy

    @classmethod
    def from_project(cls, api: CpsApi, proj_key: str) -> "OCRSettings":
        return cls()  # FIXME: Dummy

    @classmethod
    def get_backends(
        cls, api: CpsApi
    ) -> List[str]:  # get list of available OCR backends
        return []  # FIXME: Dummy

    @classmethod
    def get_backend_config(
        cls, api: CpsApi, backend: str
    ) -> dict:  # get available config options for given backend
        return {}  # FIXME: Dummy

    def to_ccs_spec(self):
        return self.dict()


class ConversionMetadata(BaseModel):
    description: str = ""
    display_name: str = ""
    license: str = ""
    source: str = ""
    version: str = ""

    @classmethod
    def from_defaults(cls) -> "ConversionMetadata":
        return cls()

    @classmethod
    def from_project(cls, api: CpsApi, proj_key: str) -> "ConversionMetadata":
        return cls()  # FIXME: Dummy

    def to_ccs_spec(self):
        return self.dict()


class ConversionSettings(BaseModel):
    pipeline: Optional[ConversionPipelineSettings]
    ocr: Optional[OCRSettings]
    metadata: Optional[ConversionMetadata]

    @classmethod
    def from_project(cls, api: CpsApi, proj_key: str) -> "ConversionSettings":
        conv_settings = cls()

        conv_settings.pipeline = ConversionPipelineSettings.from_project(api, proj_key)
        conv_settings.ocr = OCRSettings.from_project(api, proj_key)
        conv_settings.metadata = ConversionMetadata.from_project(api, proj_key)

        return conv_settings

    @classmethod
    def from_defaults(cls, api: CpsApi) -> "ConversionSettings":
        conv_settings = cls()

        conv_settings.pipeline = ConversionPipelineSettings.from_defaults(api)
        conv_settings.ocr = OCRSettings.from_defaults(api)
        conv_settings.metadata = ConversionMetadata.from_defaults()

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
