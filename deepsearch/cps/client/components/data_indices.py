from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List, Optional

from deepsearch.cps.apis import public as sw_client
from deepsearch.cps.apis.public.models.token_response import TokenResponse
from deepsearch.cps.client.components.api_object import ApiConnectedObject
from deepsearch.cps.client.components.elastic import ElasticProjectDataCollectionSource

if TYPE_CHECKING:
    from deepsearch.cps.client import CpsApi


class CpsApiDataIndices:
    def __init__(self, api: CpsApi) -> None:
        self.api = api
        self.sw_api = sw_client.DataIndicesApi(self.api.client.swagger_client)

    # define methods:
    def list(self, proj_key: str):
        try:
            projects = self.sw_api.get_project_data_indices(proj_key=proj_key)
            return projects
        except ValueError as e:
            print(f"Uh oh! {e}\nAborting!")
            raise

    # def create(self, proj_key: str, data: Dict[str, str]):
    #     return self.sw_api.create_project_data_index(proj_key=proj_key, data=data)
    def create(
        self,
        proj_key: str,
        name: str,
        desc: str = "",
        type: Optional[str] = None,
        schema_key: Optional[str] = None,
    ):
        """
        Method to create a new index.

        Input
        -----
        proj_key : string
            key of project in which index is created
        name : string
            name of data index
        desc : string, OPTIONAL
            description of data index
        type : string, OPTIONAL
            type of data index, default is "Document"
            possible values: "Document", "DB Records", "Generic", "Experiment"
        schema_key : string, OPTIONAL
            schema of data index, default is "deepsearch_doc"
            possible values: "deepsearch-doc", "deepsearch-db", "generic"
        """

        if type is None:
            type = "Document"

        if type == "Document":
            schema_key = "deepsearch-doc"
        elif type == "DB Records":
            schema_key = "deepsearch-db"
        elif type == "Generic":
            schema_key = "generic"
        elif type == "Experiment":
            schema_key = "generic"

        data = {
            "name": name,
            "description": desc,
            "schema_key": schema_key,
            "type": type,
        }
        return self.sw_api.create_project_data_index(proj_key=proj_key, data=data)

    def delete(
        self,
        coords: ElasticProjectDataCollectionSource,
    ):
        request_confirmation_token: TokenResponse = (
            self.sw_api.create_project_data_index_delete_token(
                proj_key=coords.proj_key, index_key=coords.index_key
            )
        )
        confirmation_token = request_confirmation_token.token
        return self.sw_api.delete_project_data_index(
            proj_key=coords.proj_key,
            index_key=coords.index_key,
            confirmation_token=confirmation_token,
        )

    def upload_file(
        self,
        coords: ElasticProjectDataCollectionSource,
        body: Dict[str, str],
    ) -> str:
        """
        Call api for converting and uploading file to a project's data index.
        """
        task_id = self.sw_api.ccs_convert_upload_file_project_data_index(
            proj_key=coords.proj_key, index_key=coords.index_key, body=body
        ).task_id
        return task_id


@dataclass
class CpsApiDataIndex(ApiConnectedObject):
    project: str
