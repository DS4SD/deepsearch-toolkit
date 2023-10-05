import os
import tempfile
from pathlib import Path
from typing import List, Optional

import urllib3

from deepsearch.cps.client.api import CpsApi
from deepsearch.documents.core.results import DocumentConversionResult

from .models import ConversionSettings, ExportTarget, S3Coordinates
from .utils import batch_single_files

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from .convert import (
    check_status_running_tasks,
    send_files_for_conversion,
    send_urls_for_conversion,
    submit_conversion_payload,
)


def process_local_input(
    api: CpsApi,
    cps_proj_key: str,
    source_path: Path,
    target: Optional[ExportTarget],
    conversion_settings: Optional[ConversionSettings],
    progress_bar=False,
) -> DocumentConversionResult:
    """
    Classify the user provided local input and take appropriate action.
    """
    if not os.path.exists(source_path):
        raise ValueError("File not found. Check input.")
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
                target=target,
                conversion_settings=conversion_settings,
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
            api=api,
            batched_files=batched_files,
        )


def process_urls_input(
    api: CpsApi,
    cps_proj_key: str,
    urls: List[str],
    target: Optional[ExportTarget],
    conversion_settings: Optional[ConversionSettings],
    progress_bar=False,
):
    """
    Classify user provided url(s) and take appropriate action.
    """
    task_ids = send_urls_for_conversion(
        api=api,
        cps_proj_key=cps_proj_key,
        urls=urls,
        target=target,
        conversion_settings=conversion_settings,
        progress_bar=progress_bar,
    )
    statuses = check_status_running_tasks(
        api=api, cps_proj_key=cps_proj_key, task_ids=task_ids, progress_bar=progress_bar
    )
    return DocumentConversionResult(
        proj_key=cps_proj_key,
        task_ids=task_ids,
        statuses=statuses,
        source_urls=urls,
        api=api,
    )


def process_cos_input(
    api: CpsApi,
    cps_proj_key: str,
    source_cos: S3Coordinates,
    target: Optional[ExportTarget],
    conversion_settings: Optional[ConversionSettings],
    progress_bar=False,
):
    """
    Classify user provided url(s) and take appropriate action.
    """

    task_id = submit_conversion_payload(
        api=api,
        cps_proj_key=cps_proj_key,
        source={
            "type": "s3",
            "coordinates": source_cos.dict(),
        },
        target=target,
        conversion_settings=conversion_settings,
    )

    task_ids = [task_id]
    statuses = check_status_running_tasks(
        api=api, cps_proj_key=cps_proj_key, task_ids=task_ids, progress_bar=progress_bar
    )
    return DocumentConversionResult(
        proj_key=cps_proj_key,
        task_ids=task_ids,
        statuses=statuses,
        api=api,
    )
