from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Union

import requests
from pydantic.v1 import BaseModel

from deepsearch.cps.apis import public as sw_client
from deepsearch.cps.apis.public.models.temporary_upload_file_result import (
    TemporaryUploadFileResult,
)
from deepsearch.cps.client.components.projects import Project

if TYPE_CHECKING:
    from deepsearch.cps.client import CpsApi


class UploadedFile(BaseModel):
    download_url: str
    internal_url: str


class DSApiUploader:
    def __init__(self, api: CpsApi) -> None:
        self.api = api
        self.upload_api = sw_client.UploadsApi(self.api.client.swagger_client)

    def upload_file(
        self,
        project: Union[Project, str],
        source_path: Union[Path, str],
        tls_verify: bool = True,
    ) -> UploadedFile:
        """
        Upload a file to the scratch storage of Deep Search.
        The returned object provides the `download_url` and `internal_url` which can be
        use for retrieving the file or submitting to other Deep Search APIs, respectively.
        """

        proj_key = project.key if isinstance(project, Project) else project
        source_path = Path(source_path)

        # Register file
        source_basename = source_path.name
        scratch_specs: TemporaryUploadFileResult = (
            self.upload_api.create_project_scratch_file(
                proj_key=proj_key, filename=source_basename
            )
        )

        # Upload file
        upload_specs = scratch_specs.upload
        with source_path.open("rb") as f:
            files = {"file": (source_basename, f)}
            request_upload = requests.post(
                url=upload_specs.url,
                data=upload_specs.fields,
                files=files,
                verify=tls_verify,
            )
            request_upload.raise_for_status()

        return UploadedFile(
            download_url=scratch_specs.download.url,
            internal_url=scratch_specs.download_private.url,
        )
