import os
from pathlib import Path
from typing import Any, List, Optional, Union

import urllib3

from deepsearch.cps.client.api import CpsApi
from deepsearch.documents.core.convert import (
    download_converted_documents,
    get_download_url,
)
from deepsearch.documents.core.create_report import get_multiple_reports
from deepsearch.documents.core.models import S3Coordinates

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class DocumentConversionResult:
    """
    An instance of DocumentConversionResult is generated when document conversion is requested.
    """

    def __init__(
        self,
        proj_key: str,
        task_ids: list,
        statuses: List[str],
        api: CpsApi,
        source_path: Optional[Path] = None,
        source_urls: Optional[List[str]] = None,
        batched_files=None,
    ) -> None:
        self.proj_key = proj_key
        self.task_ids = task_ids
        self.statuses = statuses
        self._source_path = source_path
        self._source_urls = source_urls
        self._api = api
        self._batched_files = batched_files

    def download_all(self, result_dir: Path, progress_bar=False):
        """
        Download all converted documents.

        Input
        -----
        result_dir : path
            local directory where converted documents will be saved
        progress_bar: boolean, optional (default = False)
            shows progress bar is True
        """

        result_dir = Path(result_dir)
        result_dir.mkdir(parents=True, exist_ok=True)

        urls = get_download_url(
            cps_proj_key=self.proj_key, task_ids=self.task_ids, api=self._api
        )
        download_converted_documents(
            result_dir=result_dir, download_urls=urls, progress_bar=progress_bar
        )
        return

    def generate_report(self, result_dir: Path, progress_bar=False):
        """
        Saves a csv report file for detailed information about the document conversion job.
        Returns a dictionary object containing counts of files/urls converted.

        progress_bar: boolean, optional (default = False)
            shows progress bar is True

        """
        result_dir = Path(result_dir)
        result_dir.mkdir(parents=True, exist_ok=True)

        if self._source_path is not None:
            info = get_multiple_reports(
                api=self._api,
                cps_proj_key=self.proj_key,
                task_ids=self.task_ids,
                source_files=self._batched_files,
                result_dir=result_dir,
                progress_bar=progress_bar,
            )
            return info
        elif self._source_urls is not None:
            info = get_multiple_reports(
                api=self._api,
                cps_proj_key=self.proj_key,
                task_ids=self.task_ids,
                source_files=self._source_urls,
                result_dir=result_dir,
                progress_bar=progress_bar,
            )
            return info
        else:
            info = get_multiple_reports(
                api=self._api,
                cps_proj_key=self.proj_key,
                task_ids=self.task_ids,
                source_files=None,
                result_dir=result_dir,
                progress_bar=progress_bar,
            )
            return info

    def __iter__(self):
        for index in range(len(self.task_ids)):
            yield DocumentResult(
                proj_key=self.proj_key,
                task_id=self.task_ids[index],
                status=self.statuses[index],
                api=self._api,
            )


class DocumentResult:
    """
    Instance of an individual DocumentConversionResult.
    """

    def __init__(self, proj_key: str, task_id: str, status: str, api: CpsApi):
        self.proj_key = proj_key
        self.task_id = task_id
        self.status = status
        self._api = api

    def url_json(self):
        """
        Returns the url of a converted json object.
        """
        return get_download_url(
            cps_proj_key=self.proj_key, task_ids=[self.task_id], api=self._api
        )[0]

    def download(self, result_dir: Path, progress_bar=False):
        """
        Download result of an individual conversion task.

        Input
        -----
        result_dir : path
            local directory where converted documents are stored
        progress_bar: boolean, optional (default = False)
            shows progress bar is True
        """
        if not os.path.isdir(result_dir):
            os.makedirs(result_dir)
        url = get_download_url(
            cps_proj_key=self.proj_key, task_ids=[self.task_id], api=self._api
        )
        download_converted_documents(
            result_dir=result_dir,
            download_urls=url,
            progress_bar=progress_bar,
        )
        return
