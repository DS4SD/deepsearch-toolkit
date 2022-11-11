from enum import Enum
from typing import List, Literal, Optional, Set, Union

from pydantic import BaseModel, Field


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


class ConversionModel(BaseModel):
    name: Optional[
        str
    ]  # named model (config), or model "type". validate with available options on CCS API and project.
    config: Union[dict, str]  # config dict, or model_config_key

    """
    # In CCS-API:
        { # project model config
            "model_config_key": "c0e64f4db662d96a222f38174bd22312",
            "name": "yolo-test-1",
            "proj_key": "93907db9fb895f868f9310512e273b8e1a3991bd"
        },
        { # default system model
            "config": {},
            "type": "LayoutSegmentationModel"    
        }
    """


class ConversionPipelineSettings(BaseModel):
    clusters: ConversionModel
    tables: Optional[ConversionModel]


class OCRSettings(BaseModel):
    enabled: bool = False
    backend: str = "tesseract-ocr"  # validate with available options on CCS API
    config: dict = {}
    merge_mode: str = "prioritize-ocr"  # turn into enum with default

    """
    {
      "backend": "tesseract-ocr",
      "backend_settings": {},
      "enabled": false,
      "merge_mode": "prioritize-ocr"
    }
    """


class ConversionMetadata(BaseModel):
    description: str = ""
    display_name: str = ""
    license: str = ""
    source: str = ""
    version: str = ""

    """
    {
      "description": "",
      "display_name": "",
      "license": "",
      "source": "",
      "version": ""
    }
    """


class ConversionSettings(BaseModel):
    pipeline: Optional[ConversionPipelineSettings]
    ocr: Optional[OCRSettings]
    metadata: Optional[ConversionMetadata]
