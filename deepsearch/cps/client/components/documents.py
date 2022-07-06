from __future__ import annotations
from pathlib import Path
import urllib3

from typing import TYPE_CHECKING, Any, Dict, List, Optional
from deepsearch.documents.core.convert import (
    get_download_url,
    download_converted_documents,
)
from deepsearch.documents.core.create_report import report_docs, report_urls

if TYPE_CHECKING:
    from deepsearch.cps.client import CpsApi
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
        source_path: Optional[Path] = None,
        source_urls: Optional[List[str]] = None,
    ) -> None:
        self.proj_key = proj_key
        self.task_ids = task_ids
        self.statuses = statuses
        self._source_path = source_path
        self._source_urls = source_urls

    def download_json(self, result_dir: Path, progress_bar=False):
        """
        Download all converted documents.

        Input
        -----
        result_dir : path
            local directory where converted documents are stored
        progress_bar: boolean, optional (default = False)
            shows progress bar is True
        """
        urls = get_download_url(cps_proj_key=self.proj_key, task_ids=self.task_ids)
        download_converted_documents(
            result_dir=result_dir, download_urls=urls, progress_bar=progress_bar
        )
        return

    def generate_report(
        self,
        result_dir: Path,
    ):
        """
        Generate csv report file for detailed information about the document conversion job.
        """
        if self._source_urls == None:
            report_docs(
                result_dir=result_dir,
                task_ids=self.task_ids,
                statuses=self.statuses,
                source_path=self._source_path,
            )

        if self._source_path == None:
            report_urls(
                result_dir=result_dir,
                urls=self._source_urls,
                statuses=self.statuses,
                task_ids=self.task_ids,
            )

        return

    def __iter__(self):
        for index in range(len(self.task_ids)):
            yield DocumentResult(
                proj_key=self.proj_key,
                task_id=self.task_ids[index],
                status=self.statuses[index],
            )


class DocumentResult:
    """
    Instance of an individual DocumentConversionResult.
    """

    def __init__(
        self,
        proj_key: str,
        task_id: str,
        status: str,
    ):
        self.proj_key = proj_key
        self.task_id = task_id
        self.status = status

    def url_json(self):
        """
        Returns the url of a converted json object.
        """
        return get_download_url(cps_proj_key=self.proj_key, task_ids=[self.task_id])[0]

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
        urls = get_download_url(cps_proj_key=self.proj_key, task_ids=[self.task_id])
        download_converted_documents(
            result_dir=result_dir, download_urls=urls, progress_bar=progress_bar
        )
        return
