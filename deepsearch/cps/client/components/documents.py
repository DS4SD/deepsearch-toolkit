from __future__ import annotations

import base64
import json
import urllib.parse
from typing import TYPE_CHECKING, Any, Dict, Literal, Optional, Union

from pydantic.v1 import BaseModel, Field
from typing_extensions import Annotated

from deepsearch.cps.apis import public as sw_client
from deepsearch.cps.apis.public.models.semantic_ingest_request import (
    SemanticIngestRequest,
)
from deepsearch.cps.apis.public.models.task import Task
from deepsearch.cps.client.components.data_indices import (
    ElasticProjectDataCollectionSource,
)
from deepsearch.cps.client.components.elastic import ElasticDataCollectionSource
from deepsearch.cps.client.components.projects import Project

if TYPE_CHECKING:
    from deepsearch.cps.client import CpsApi


class SemIngestPublicDataDocumentSource(BaseModel):
    source: ElasticDataCollectionSource
    document_hash: str


class SemIngestPrivateDataDocumentSource(BaseModel):
    source: ElasticProjectDataCollectionSource
    document_hash: str


class SemIngestPrivateDataCollectionSource(BaseModel):
    source: ElasticProjectDataCollectionSource


SemIngestSource = Union[
    SemIngestPublicDataDocumentSource,
    SemIngestPrivateDataDocumentSource,
    SemIngestPrivateDataCollectionSource,
]


class _APISemanticIngestSourceUrl(BaseModel):
    type: Literal["url"] = "url"
    url: str


class _APISemanticIngestSourcePublicDataDocument(BaseModel):
    type: Literal["public_data_document"] = "public_data_document"
    elastic_id: str
    index_key: str
    document_hash: str


class _APISemanticIngestSourcePrivateDataDocument(BaseModel):
    type: Literal["private_data_document"] = "private_data_document"
    proj_key: str
    index_key: str
    document_hash: str


class _APISemanticIngestSourcePrivateDataCollection(BaseModel):
    type: Literal["private_data_collection"] = "private_data_collection"
    proj_key: str
    index_key: str


_APISemanticIngestSourceType = Annotated[
    Union[
        _APISemanticIngestSourceUrl,
        _APISemanticIngestSourcePublicDataDocument,
        _APISemanticIngestSourcePrivateDataDocument,
        _APISemanticIngestSourcePrivateDataCollection,
    ],
    Field(discriminator="type"),
]


class DSApiDocuments:
    def __init__(self, api: CpsApi) -> None:
        self.api = api
        self.semantic_api = sw_client.SemanticApi(self.api.client.swagger_client)

    def semantic_ingest(
        self,
        project: Union[Project, str],
        data_source: SemIngestSource,
    ) -> Task:

        proj_key = project.key if isinstance(project, Project) else project
        api_src_data: _APISemanticIngestSourceType
        if isinstance(data_source, SemIngestPublicDataDocumentSource):
            api_src_data = _APISemanticIngestSourcePublicDataDocument(
                elastic_id=data_source.source.elastic_id,
                index_key=data_source.source.index_key,
                document_hash=data_source.document_hash,
            )
        elif isinstance(data_source, SemIngestPrivateDataDocumentSource):
            api_src_data = _APISemanticIngestSourcePrivateDataDocument(
                proj_key=data_source.source.proj_key,
                index_key=data_source.source.index_key,
                document_hash=data_source.document_hash,
            )
        elif isinstance(data_source, SemIngestPrivateDataCollectionSource):
            api_src_data = _APISemanticIngestSourcePrivateDataCollection(
                proj_key=data_source.source.proj_key,
                index_key=data_source.source.index_key,
            )
        else:
            raise RuntimeError("Unknown data source format for ingest_for_qa")

        task: Task = self.semantic_api.ingest(
            proj_key=proj_key,
            body=SemanticIngestRequest(source=api_src_data.dict()),
        )

        return task

    def generate_url(
        self,
        document_hash: str,
        data_source: Union[
            ElasticDataCollectionSource, ElasticProjectDataCollectionSource
        ],
        item_index: Optional[int] = None,
    ) -> str:
        """
        Generate a URL pointing to the document search in the Deep Search UI
        """

        host = self.api.client.config.host.rstrip("/")

        select_coords: Dict[str, Any] = {}
        url = ""
        if isinstance(data_source, ElasticProjectDataCollectionSource):
            proj_key = data_source.proj_key
            index_key = data_source.index_key
            select_coords = {
                "privateCollection": index_key,
            }
            url = f"{host}/projects/{proj_key}/library/private/{index_key}"
        elif isinstance(data_source, ElasticDataCollectionSource):
            # TODO: remove hardcoding of community project
            proj_key = "1234567890abcdefghijklmnopqrstvwyz123456"
            index_key = data_source.index_key
            select_coords = {
                "collections": [index_key],
            }
            url = f"{host}/projects/{proj_key}/library/public"

        hash_expr = f'file-info.document-hash: "{document_hash}"'
        search_query = {
            **select_coords,
            "type": "Document",
            "expression": hash_expr,
            "filters": [],
            "select": [
                "_name",
                "description.collection",
                "prov",
                "description.title",
                "description.publication_date",
                "description.url_refs",
            ],
            "itemIndex": 0,
            "pageSize": 10,
            "searchAfterHistory": [],
            "viewType": "snippets",
            "recordSelection": {
                "record": {
                    "id": document_hash,
                },
            },
        }
        if item_index is not None:
            search_query["recordSelection"]["itemIndex"] = item_index

        encoded_query = urllib.parse.quote(
            base64.b64encode(
                urllib.parse.quote(
                    json.dumps(search_query, separators=(",", ":"))
                ).encode("utf8")
            ).decode("utf8")
        )

        url = f"{url}?search={encoded_query}"

        return url
