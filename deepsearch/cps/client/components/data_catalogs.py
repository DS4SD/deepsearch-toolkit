from __future__ import annotations

import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Any, Dict, List, Optional

from deepsearch.cps.apis import public as sw_client
from deepsearch.cps.apis.public.exceptions import ApiException
from deepsearch.cps.apis.public.models.create_data_catalog_collection_options import (
    CreateDataCatalogCollectionOptions,
)
from deepsearch.cps.apis.public.models.data_catalog_category_schema import (
    DataCatalogCategorySchema,
)
from deepsearch.cps.apis.public.models.data_catalog_collection import (
    DataCatalogCollection,
)
from deepsearch.cps.apis.public.models.data_catalog_data_flow import DataCatalogDataFlow
from deepsearch.cps.apis.public.models.data_catalogue import DataCatalogue
from deepsearch.cps.apis.public.models.task import Task
from deepsearch.cps.apis.public.models.token_response import TokenResponse
from deepsearch.cps.client.components.api_object import ApiConnectedObject

if TYPE_CHECKING:
    from deepsearch.cps.client import CpsApi


class CpsApiDataCatalogs:
    def __init__(self, api: CpsApi) -> None:
        self.api = api
        self.sw_api: sw_client.DataCatalogsApi = sw_client.DataCatalogsApi(
            self.api.client.swagger_client
        )

    def list(self, project: str) -> List[CpsApiDataCatalog]:
        catalogs: list[DataCatalogue] = self.sw_api.list_project_data_catalogs(project)

        return [self._load(c) for c in catalogs]

    def get(self, project: str, key: str) -> Optional[CpsApiDataCatalog]:
        try:
            catalog: DataCatalogue = self.sw_api.get_project_data_catalog(project, key)
        except ApiException as api_ex:
            if api_ex.status == 404:
                return None

            raise api_ex

        return self._load(catalog)

    def _load(self, value: DataCatalogue) -> CpsApiDataCatalog:
        c_schemas: dict[str, DataCatalogCategorySchema] = {
            v.key: v for v in value.category_schemas
        }
        c_collections: dict[str, DataCatalogCollection] = {
            v.name: v for v in value.collections
        }
        c_data_flows: dict[str, DataCatalogDataFlow] = {
            v.key: v for v in value.collections_data_flows
        }

        collections: list[CatalogCollection] = []

        for name, collection in c_collections.items():
            c_schema = c_schemas.get(name)
            c_data_flow = c_data_flows.get(name)

            collections.append(
                CatalogCollection(
                    name=name,
                    schema=None if c_schema is None else c_schema.schema,
                    data_flows=[] if c_data_flow is None else c_data_flow.data_flows,
                )
            )

        return CpsApiDataCatalog(
            api=self.api,
            project=value.proj_key,
            key=value.dc_key,
            name=value.name,
            collections=collections,
        )


@dataclass
class CpsApiDataCatalog(ApiConnectedObject):
    project: str
    key: str

    name: str

    collections: List[CatalogCollection]

    def create_collection(self, name: str) -> None:
        body = CreateDataCatalogCollectionOptions(collection_name=name)

        self.api.data_catalogs.sw_api.create_project_data_catalog_collection(
            self.project, self.key, body
        )

        self.collections.append(CatalogCollection(name=name, schema={}, data_flows=[]))

    def delete_collection(self, name: str) -> None:
        self.api.data_catalogs.sw_api.delete_project_data_catalog_collection(
            self.project,
            self.key,
            name,
        )

        self.collections = [c for c in self.collections if c.name != name]

    def upload_file(self, path: Path, collection: Optional[str] = None) -> None:
        if not path.is_file():
            raise ValueError(f"Path {path} is not a file")

        task: Task
        if collection is None:
            # Upload to catalog (must be a zip)
            if not zipfile.is_zipfile(path):
                raise ValueError(f"Path {path} is not a zip file")

            task = self.api.data_catalogs.sw_api.upload_project_data_catalog_data(
                self.project,
                self.key,
                path,
            )
        else:
            # Upload to collection
            task = self.api.data_catalogs.sw_api.upload_project_data_catalog_collection_data(
                self.project,
                self.key,
                collection,
                path,
            )

        return self.api.tasks.wait_for(self.project, task.task_id)

    def delete(self) -> None:
        token_res: TokenResponse = (
            self.api.data_catalogs.sw_api.create_project_data_catalog_delete_token(
                self.project, self.key
            )
        )

        self.api.data_catalogs.sw_api.delete_project_data_catalog(
            self.project, self.key, token_res.token
        )

    def to_resource(self) -> Dict[str, Any]:
        return {"type": "catalogue", "proj_key": self.project, "dc_key": self.key}


@dataclass
class CatalogCollection:
    name: str

    data_flows: List[Dict[str, Any]]
    schema: Optional[Dict[str, Any]] = None
