from enum import Enum
from textwrap import dedent
from typing import List, Literal, Optional, Union

from pydantic import BaseModel, Field, model_validator


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
    - `skip` will not touch the document on the target, leaving it as-is.
    Using `skip` will incur in a performance increase, however, if the document
    is modified externally, CCS will not update it back to the original state.
    """

    REPLACE = "replace"
    SKIP = "skip"


class MongoCollectionCoordinates(BaseModel):
    uri: str
    database: str
    collection: str


class MongoS3TargetCoordinates(BaseModel):
    """Coordinates to a Mongo collection, and optionally, an S3 bucket"""

    mongo: MongoCollectionCoordinates
    s3: Optional[S3Coordinates] = None


class MongoS3Target(BaseModel):
    type: Literal["mongo_s3"] = "mongo_s3"

    # Coordinates for the export
    coordinates: MongoS3TargetCoordinates

    if_document_exists: DocumentExistsInTargetAction = (
        DocumentExistsInTargetAction.REPLACE
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

    add_cells: bool = False


class ElasticIndexCoordinates(BaseModel):
    hosts: List[str]
    dangerously_disable_ssl_validation: bool = False
    ca_certificate_base64: Optional[str] = None
    index: str


class ElasticS3TargetCoordinates(BaseModel):
    elastic: ElasticIndexCoordinates
    s3: Optional[S3Coordinates] = None


class ElasticS3Target(BaseModel):
    type: Literal["elastic_s3"] = "elastic_s3"

    coordinates: ElasticS3TargetCoordinates

    if_document_exists: DocumentExistsInTargetAction = (
        DocumentExistsInTargetAction.REPLACE
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


class TableStructureOptions(BaseModel):
    do_table_structure: bool = True
    table_structure_mode: Literal["fast", "accurate"] = "fast"


class OCROptions(BaseModel):
    do_ocr: bool = True
    kind: Literal["easyocr", "tesserocr"] = "easyocr"


class ConversionSettings(BaseModel):
    ocr: OCROptions = OCROptions()
    table_structure: TableStructureOptions = TableStructureOptions()


class TargetSettings(BaseModel):
    add_raw_pages: Optional[bool] = None
    add_annotations: Optional[bool] = None

    @model_validator(mode="after")
    def check_raw_or_ann(self):
        if self.add_raw_pages is None and self.add_annotations is None:
            raise ValueError("either 'add_raw_pages' or 'add_annotations' is required")
        return self
