from __future__ import annotations

import base64
import json
import urllib.parse
from typing import TYPE_CHECKING, Any, Dict, Optional, Union

from pydantic.v1 import BaseModel

from deepsearch.cps.apis.public_v2 import SemanticApi
from deepsearch.cps.apis.public_v2.models.cps_task import CpsTask
from deepsearch.cps.apis.public_v2.models.semantic_ingest_req_params import (
    SemanticIngestReqParams,
)
from deepsearch.cps.apis.public_v2.models.semantic_ingest_request import (
    SemanticIngestRequest,
)
from deepsearch.cps.apis.public_v2.models.semantic_ingest_source_private_data_collection import (
    SemanticIngestSourcePrivateDataCollection,
)
from deepsearch.cps.apis.public_v2.models.semantic_ingest_source_private_data_document import (
    SemanticIngestSourcePrivateDataDocument,
)
from deepsearch.cps.apis.public_v2.models.semantic_ingest_source_public_data_document import (
    SemanticIngestSourcePublicDataDocument,
)
from deepsearch.cps.apis.public_v2.models.source1 import Source1
from deepsearch.cps.client.components.data_indices import (
    ElasticProjectDataCollectionSource,
)
from deepsearch.cps.client.components.elastic import ElasticDataCollectionSource
from deepsearch.cps.client.components.projects import Project

if TYPE_CHECKING:
    from deepsearch.cps.client import CpsApi


class PublicDataDocumentSource(BaseModel):
    source: ElasticDataCollectionSource
    document_hash: str


class PrivateDataDocumentSource(BaseModel):
    source: ElasticProjectDataCollectionSource
    document_hash: str


class PrivateDataCollectionSource(BaseModel):
    source: ElasticProjectDataCollectionSource


DataSource = Union[
    PublicDataDocumentSource,
    PrivateDataDocumentSource,
    PrivateDataCollectionSource,
]


class DSApiDocuments:
    def __init__(self, api: CpsApi) -> None:
        self.api = api
        self.semantic_api = SemanticApi(self.api.client.swagger_client_v2)

    def semantic_ingest(
        self,
        project: Union[Project, str],
        data_source: DataSource,
        skip_ingested_docs: bool = True,
    ) -> CpsTask:

        proj_key = project.key if isinstance(project, Project) else project
        api_src_data: Any
        if isinstance(data_source, PublicDataDocumentSource):
            api_src_data = SemanticIngestSourcePublicDataDocument(
                type="public_data_document",
                elastic_id=data_source.source.elastic_id,
                index_key=data_source.source.index_key,
                document_hash=data_source.document_hash,
            )
        elif isinstance(data_source, PrivateDataDocumentSource):
            api_src_data = SemanticIngestSourcePrivateDataDocument(
                type="private_data_document",
                proj_key=data_source.source.proj_key,
                index_key=data_source.source.index_key,
                document_hash=data_source.document_hash,
            )
        elif isinstance(data_source, PrivateDataCollectionSource):
            api_src_data = SemanticIngestSourcePrivateDataCollection(
                type="private_data_collection",
                proj_key=data_source.source.proj_key,
                index_key=data_source.source.index_key,
            )
        else:
            raise RuntimeError("Unknown data source format for semantic_ingest")

        semantic_ingest_request = SemanticIngestRequest(
            source=Source1(
                actual_instance=api_src_data,
            ),
            parameters=SemanticIngestReqParams(
                skip_ingested_docs=skip_ingested_docs,
            ),
        )
        task = self.semantic_api.ingest(
            proj_key=proj_key,
            semantic_ingest_request=semantic_ingest_request,
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
