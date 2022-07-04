from __future__ import annotations
from pathlib import Path

from typing import TYPE_CHECKING, Any, Dict, List, Optional
from deepsearch.documents.core.convert import (
    get_download_url,
    download_converted_documents,
)

if TYPE_CHECKING:
    from deepsearch.cps.client import CpsApi


class DocumentConversionResult:
    """
    An instance of DocumentConversionResult is generated when document conversion is requested.
    """

    def __init__(self, proj_key: str, task_ids: list, statuses: List[str]) -> None:
        self.proj_key = proj_key
        self.task_ids = task_ids
        self.statuses = statuses

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

    # some of the methods are
    # def download_json(self, )
    # download_converted_docs(
    #     api=api, cps_proj_key=cps_proj_key, task_ids=task_ids, root_dir=root_dir
    # )
    # number converted
    # number successful
    # number failed
    # download_all
    # __iter__ --> objects of class DocumentResult


# class DocumentResult:
#     def __init__():
#         pass
