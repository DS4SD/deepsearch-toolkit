from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Union

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

    def ingest_documentqa(
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
