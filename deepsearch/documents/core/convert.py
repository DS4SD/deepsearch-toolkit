import logging
import os
import time
import urllib.parse
from pathlib import Path
from typing import List, Optional, Union

import urllib3
from tqdm import tqdm

from deepsearch.cps.apis import public_v2 as sw_client
from deepsearch.cps.apis.public_v2.models.api_server_fastapi_server_public_models_project_models_http_source import (
    ApiServerFastapiServerPublicModelsProjectModelsHttpSource,
)
from deepsearch.cps.apis.public_v2.models.convert_document_request import (
    ConvertDocumentRequest,
)
from deepsearch.cps.apis.public_v2.models.convert_document_request_http_source import (
    ConvertDocumentRequestHttpSource,
)
from deepsearch.cps.client.api import CpsApi

from .common_routines import progressbar
from .models import ConversionSettings
from .utils import download_url

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logger = logging.getLogger(__name__)


TASK_STOP_STATUS = ["SUCCESS", "FAILURE"]


def make_payload(
    url: str,
    conversion_settings: Optional[ConversionSettings],
) -> ConvertDocumentRequest:
    """
    Create payload for requesting conversion
    """

    doc_conv_settings: Optional[dict] = None
    if conversion_settings is not None:
        doc_conv_settings = conversion_settings.model_dump()

    return ConvertDocumentRequest(
        http_source=ConvertDocumentRequestHttpSource(
            ApiServerFastapiServerPublicModelsProjectModelsHttpSource(
                url=url, headers={}
            )
        ),
        settings=doc_conv_settings,
    )


def get_wait_task_result(
    sw_api: sw_client.ProjectApi, cps_proj_key: str, task_id: str, wait: int = 2
):
    """
    Wait and get task result that.
    """
    while True:
        r: sw_client.TaskResult = sw_api.get_convert_task(
            proj_key=cps_proj_key, task_id=task_id
        )
        request_status = r.to_dict()
        if request_status["task_status"] in TASK_STOP_STATUS:
            return request_status
        else:
            time.sleep(wait)


def check_cps_single_task_status(
    sw_api: sw_client.TasksApi, cps_proj_key: str, task_id: str, wait: int = 2
):
    """
    Check cps status of individual tasks.
    """
    while True:
        r: sw_client.TaskResult = sw_api.get_project_celery_task(
            proj_key=cps_proj_key, task_id=task_id
        )
        request_status = r.to_dict()
        if request_status["task_status"] in TASK_STOP_STATUS:
            return request_status
        else:
            time.sleep(wait)


def submit_conversion_payload(
    api: CpsApi,
    cps_proj_key: str,
    url: str,
    conversion_settings: Optional[ConversionSettings],
) -> str:
    """
    Convert an online pdf using DeepSearch Technology.
    """
    sw_api = sw_client.ProjectApi(api.client.swagger_client_v2)

    # submit conversion request
    payload = make_payload(url, conversion_settings)

    r: sw_client.CpsTask = sw_api.convert_document(
        proj_key=cps_proj_key, convert_document_request=payload
    )

    return r.task_id


def send_file_for_conversion(
    api: CpsApi,
    cps_proj_key: str,
    source_path: Path,
    conversion_settings: Optional[ConversionSettings],
    progress_bar: bool = False,
) -> str:
    """
    Send file for conversion.
    """

    with tqdm(
        total=1,
        desc=f"{'Submitting input:': <{progressbar.padding}}",
        disable=not (progress_bar),
        colour=progressbar.colour,
        bar_format=progressbar.bar_format,
    ) as progress:
        # upload file
        uploaded_file = api.uploader.upload_file(
            project=cps_proj_key, source_path=source_path
        )
        # submit url for conversion
        task_id = submit_conversion_payload(
            api=api,
            cps_proj_key=cps_proj_key,
            url=uploaded_file.internal_url,
            conversion_settings=conversion_settings,
        )
        progress.update(1)

    return task_id


def check_cps_status_running_tasks(
    api: CpsApi, cps_proj_key: str, task_ids: List[str], progress_bar: bool = False
) -> List[str]:
    """
    Check status of multiple running cps tasks and optionally display progress with progress bar.
    """

    sw_api = sw_client.TasksApi(api.client.swagger_client_v2)
    count_total = len(task_ids)

    statuses = []

    with tqdm(
        total=count_total,
        desc=f"{'Converting input:': <{progressbar.padding}}",
        disable=not (progress_bar),
        colour=progressbar.colour,
        bar_format=progressbar.bar_format,
    ) as progress:
        for task_id in task_ids:
            request_status = check_cps_single_task_status(
                sw_api=sw_api, cps_proj_key=cps_proj_key, task_id=task_id
            )
            progress.update(1)
            statuses.append(request_status["task_status"])

    return statuses


def download_converted_documents(
    result_dir: Path, download_urls: List[str], progress_bar: bool = False
):
    """
    Download converted documents.

    Input
    -----

    result_dir : path
        directory for saving converted json doc
    download_urls: list
        url of converted json
    progress_bar: boolean (default False)
        shows progress bar if True
    """

    with tqdm(
        total=len(download_urls),
        desc=f"{'Downloading result:': <{progressbar.padding}}",
        disable=not (progress_bar),
        colour=progressbar.colour,
        bar_format=progressbar.bar_format,
    ) as progress:
        count = 1
        for url in download_urls:
            filename = Path(urllib.parse.urlparse(url).path).name
            download_name = Path(os.path.join(result_dir, filename[-10:]))
            download_url(url, download_name),
            count += 1
            progress.update(1)
    return


def send_url_for_conversion(
    api: CpsApi,
    cps_proj_key: str,
    url: str,
    conversion_settings: Optional[ConversionSettings],
    progress_bar: bool = False,
) -> str:
    """
    Send online document for conversion.
    """
    with tqdm(
        total=1,
        desc=f"{'Submitting input:': <{progressbar.padding}}",
        disable=not (progress_bar),
        colour=progressbar.colour,
        bar_format=progressbar.bar_format,
    ) as progress:
        task_id = submit_conversion_payload(
            api=api,
            cps_proj_key=cps_proj_key,
            url=url,
            conversion_settings=conversion_settings,
        )
        progress.update(1)
        return task_id
