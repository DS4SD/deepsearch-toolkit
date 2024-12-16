from pathlib import Path
from typing import Optional

import urllib3

from deepsearch.cps.client.api import CpsApi
from deepsearch.documents.core.convert import download_converted_documents
from deepsearch.documents.core.create_report import generate_report_csv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class DocumentConversionResult:
    """
    An instance of DocumentConversionResult is generated when document conversion is requested.
    """

    def __init__(
        self,
        proj_key: str,
        task_id: str,
        result: dict,
        api: CpsApi,
        source_path: Optional[Path] = None,
        source_url: Optional[str] = None,
        batched_files=None,
        export_md: bool = False,
    ) -> None:
        self.proj_key = proj_key
        self.task_id = task_id
        self.result = result
        self._source_path = source_path
        self._source_url = source_url
        self._api = api
        self._batched_files = batched_files
        self.export_md = export_md

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
        urls = []
        urls.append(self.result.get("result", {}).get("json_file_url"))
        if self.export_md:
            urls.append(self.result.get("result", {}).get("md_file_url"))

        download_converted_documents(
            result_dir=result_dir, download_urls=urls, progress_bar=progress_bar
        )
        return

    def generate_report(self, result_dir: Path, progress_bar=False):
        """
        Saves a csv report file for detailed information about the document conversion job.
        Returns a dictionary object containing counts of files/urls converted.

        """
        result_dir = Path(result_dir)
        result_dir.mkdir(parents=True, exist_ok=True)

        return generate_report_csv(
            task_result=self.result.get("result", {}),
            task_id=self.task_id,
            result_dir=result_dir,
            progress_bar=progress_bar,
        )
