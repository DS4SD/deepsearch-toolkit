from __future__ import annotations

import ast
import os
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union
from urllib.parse import urlparse

import requests
from pydantic.v1 import BaseModel

from deepsearch.cps.apis import public as sw_client
from deepsearch.cps.apis.public.models.attachment_upload_data import (
    AttachmentUploadData,
)
from deepsearch.cps.apis.public.models.task import Task
from deepsearch.cps.apis.public.models.token_response import TokenResponse
from deepsearch.cps.client.components.api_object import ApiConnectedObject

if TYPE_CHECKING:
    from deepsearch.cps.client import CpsApi


class CpsApiDataIndices:
    def __init__(self, api: CpsApi) -> None:
        self.api = api
        self.sw_api = sw_client.DataIndicesApi(self.api.client.swagger_client)

    def list(self, proj_key: str) -> List[DataIndex]:
        response: list[
            sw_client.ProjectDataIndexWithStatus
        ] = self.sw_api.get_project_data_indices(proj_key=proj_key)

        # filter out saved searchs index
        return [
            DataIndex.parse_obj(item.to_dict())
            for item in response
            if item.to_dict()["type"] != "View"
        ]

    def create(
        self,
        proj_key: str,
        name: str,
        desc: str = "",
        type: Optional[str] = None,
        schema_key: Optional[str] = None,
    ) -> DataIndex:
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
        response: sw_client.ProjectDataIndexWithStatus = (
            self.sw_api.create_project_data_index(proj_key=proj_key, data=data)
        )

        return DataIndex.parse_obj(response.to_dict())

    def delete(
        self,
        coords: ElasticProjectDataCollectionSource,
    ) -> None:
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
        body: Dict[str, Any],
    ) -> str:
        """
        Deprecated. Use upload_and_convert() instead.
        """
        return self.upload_and_convert(coords, body).task_id

    def upload_and_convert(
        self,
        coords: ElasticProjectDataCollectionSource,
        body: Dict[str, Any],
    ) -> Task:
        """
        Call api for converting and uploading file to a project's data index.
        """
        task: Task = self.sw_api.ccs_convert_upload_file_project_data_index(
            proj_key=coords.proj_key, index_key=coords.index_key, body=body
        )
        return task

    def upload(
        self,
        coords: ElasticProjectDataCollectionSource,
        source: Union[Path, str],
    ) -> Task:
        """
        Call api for uploading files to a project's data index.
        The source files can be provided by local path or URL via `source`.
        """

        parsed = urlparse(str(source))
        if parsed.scheme and parsed.netloc:  # is url
            source_url = source
        else:
            uploaded_file = self.api.uploader.upload_file(
                project=coords.proj_key, source_path=source
            )
            source_url = uploaded_file.internal_url

        task = self.sw_api.upload_project_data_index_file(
            proj_key=coords.proj_key,
            index_key=coords.index_key,
            params={
                "file_url": source_url,
            },
        )
        return task


class ElasticProjectDataCollectionSource(BaseModel):
    proj_key: str
    index_key: str

    def to_resource(self) -> Dict[str, Any]:
        return {"type": "elastic", "proj_key": self.proj_key, "index": self.index_key}


class DataIndex(BaseModel):

    source: ElasticProjectDataCollectionSource
    name: str
    description: str
    documents: int
    health: str
    status: str
    schema_key: str
    type: str

    def add_item_attachment(
        self,
        api: CpsApi,
        index_item_id: str,
        attachment_path: Union[str, Path],
        attachment_key: Optional[str] = None,
    ) -> None:
        """
        Method to upload attachments to an index item.

        Input
        -----
        api : CpsApi
            CpsApi Class
        index_item_id : string
            id of the index item
        attachment_path : string | Path
            path to file on local folder
        attachment_key : string, OPTIONAL
            key to put on index document where attachment info will be saved.
            string must me snake_case and start with 'usr_'.
            example: 'usr_your_attachment_key'
        """

        sw_api = sw_client.DataIndicesApi(api.client.swagger_client)

        filename = os.path.basename(attachment_path)

        attachment_upload_data: AttachmentUploadData = (
            sw_api.get_attachment_upload_data(
                proj_key=self.source.proj_key,
                index_key=self.source.index_key,
                index_item_id=index_item_id,
                filename=filename,
            )
        )

        with open(attachment_path, "rb") as f:
            files = {"file": (os.path.basename(attachment_path), f.read())}
        request_upload = requests.post(
            url=attachment_upload_data.upload_data.url,
            data=attachment_upload_data.upload_data.fields,
            files=files,
            verify=False,
        )
        request_upload.raise_for_status()

        params = {
            "attachment_path": attachment_upload_data.attachment_path,
        }

        if attachment_key is not None:
            params["attachment_key"] = attachment_key

        sw_api.register_attachment(
            proj_key=self.source.proj_key,
            index_key=self.source.index_key,
            index_item_id=index_item_id,
            params=params,
        )


@dataclass
class CpsApiDataIndex(ApiConnectedObject):
    project: str


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
