from __future__ import annotations

import base64
import json
import urllib.parse
from typing import TYPE_CHECKING, Any, Dict, Optional, Union

from deepsearch.cps.apis import public as sw_client
from deepsearch.cps.apis.public.models.task import Task
from deepsearch.cps.client.components.data_indices import (
    ElasticProjectDataCollectionSource,
)
from deepsearch.cps.client.components.elastic import ElasticDataCollectionSource
from deepsearch.cps.client.components.projects import Project

if TYPE_CHECKING:
    from deepsearch.cps.client import CpsApi


class DSApiDocuments:
    def __init__(self, api: CpsApi) -> None:
        self.api = api
        self.ingest_api = sw_client.DocumentInspectionApi(
            self.api.client.swagger_client
        )

    def ingest_for_qa(
        self,
        project: Union[Project, str],
        data_source: Union[
            ElasticDataCollectionSource, ElasticProjectDataCollectionSource
        ],
        document_hash: str,
    ) -> Task:

        proj_key = project.key if isinstance(project, Project) else project

        payload: Dict[str, Any] = {"source": {}}
        if isinstance(data_source, ElasticDataCollectionSource):
            payload["source"] = {
                "type": "public_data",
                "index_key": data_source.index_key,
                "document_hash": document_hash,
                "elastic_id": data_source.elastic_id,
            }
        elif isinstance(data_source, ElasticProjectDataCollectionSource):
            payload["source"] = {
                "type": "private_data",
                "index_key": data_source.index_key,
                "proj_key": data_source.proj_key,
                "document_hash": document_hash,
            }

        task: Task = self.ingest_api.ingest_documentqa(proj_key, payload)

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
