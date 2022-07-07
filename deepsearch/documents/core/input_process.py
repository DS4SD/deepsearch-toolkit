import logging
import os
import tempfile
from pathlib import Path
from typing import Any, List

import urllib3
from tqdm import tqdm

from deepsearch.cps.client.api import CpsApi
from deepsearch.cps.client.components.documents import DocumentConversionResult
from .utils import batch_single_files, create_root_dir

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from .common_routines import success_message
from .convert import (
    check_status_running_tasks,
    download_converted_documents,
    get_download_url,
    send_files_for_conversion,
    send_urls_for_conversion,
)
from .create_report import report_docs, report_urls

logger = logging.getLogger(__name__)


def process_local_input(
    api: CpsApi, cps_proj_key: str, source_path: Path, progress_bar=False
) -> DocumentConversionResult:
    """
    Classify the user provided local input and take appropriate action.
    """
    if not os.path.exists(source_path):
        logger.error("Error: File not found. Check input.")
    else:
        with tempfile.TemporaryDirectory() as tmpdir:
            batched_files = batch_single_files(
                source_path=source_path,
                root_dir=Path(tmpdir),
                progress_bar=progress_bar,
            )
            task_ids = send_files_for_conversion(
                api=api,
                cps_proj_key=cps_proj_key,
                source_path=source_path,
                root_dir=Path(tmpdir),
                progress_bar=progress_bar,
            )
            statuses = check_status_running_tasks(
                api=api,
                cps_proj_key=cps_proj_key,
                task_ids=task_ids,
                progress_bar=progress_bar,
            )
        return DocumentConversionResult(
            proj_key=cps_proj_key,
            task_ids=task_ids,
            statuses=statuses,
            source_path=source_path,
        )


def process_urls_input(
    api: CpsApi, cps_proj_key: str, urls: List[str], progress_bar=False
):
    """
    Classify user provided url(s) and take appropriate action.
    """
    task_ids = send_urls_for_conversion(
        api=api, cps_proj_key=cps_proj_key, urls=urls, progress_bar=progress_bar
    )
    statuses = check_status_running_tasks(
        api=api, cps_proj_key=cps_proj_key, task_ids=task_ids, progress_bar=progress_bar
    )
    return DocumentConversionResult(
        proj_key=cps_proj_key,
        task_ids=task_ids,
        statuses=statuses,
        source_urls=urls,
    )
