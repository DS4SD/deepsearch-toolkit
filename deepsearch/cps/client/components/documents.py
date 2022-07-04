from __future__ import annotations
from pathlib import Path

from typing import TYPE_CHECKING, Any, Dict, List, Optional
from deepsearch.documents.core.convert import (
    get_download_url,
    download_converted_documents,
)
from deepsearch.documents.core.create_report import report_docs, report_urls

if TYPE_CHECKING:
    from deepsearch.cps.client import CpsApi


class DocumentConversionResult:
    """
    An instance of DocumentConversionResult is generated when document conversion is requested.
    """

    def __init__(
        self,
        proj_key: str,
        task_ids: list,
        statuses: List[str],
        source_file: Optional[Path] = None,
        source_urls: Optional[List[str]] = None,
    ) -> None:
        self.proj_key = proj_key
        self.task_ids = task_ids
        self.statuses = statuses
        self._source_file = source_file
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
            result_dir=result_dir,
            download_urls=urls,
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
                local_file=self._source_file,
            )

        if self._source_file == None:
            report_urls(
                result_dir=result_dir,
                urls=self._source_urls,
                statuses=self.statuses,
                task_ids=self.task_ids,
            )

        return

    # __iter__ --> objects of class DocumentResult


# class DocumentResult:
#     def __init__():
#         pass
