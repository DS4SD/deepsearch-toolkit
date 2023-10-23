import logging
import os
import time
from pathlib import Path
from typing import Any, List, Optional

import requests
import urllib3
from tqdm import tqdm

from deepsearch.cps.apis import public as sw_client
from deepsearch.cps.apis.public.models.temporary_upload_file_result import (
    TemporaryUploadFileResult,
)
from deepsearch.cps.client.api import CpsApi

from ...core.util.ccs_utils import get_ccs_project_key
from .common_routines import ERROR_MSG, progressbar
from .models import ConversionSettings, ExportTarget, ZipTarget
from .utils import URLNavigator, collect_all_local_files, download_url

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logger = logging.getLogger(__name__)


TASK_STOP_STATUS = ["SUCCESS", "FAILURE"]


def make_payload(
    source: dict,
    target: Optional[ExportTarget],
    conversion_settings: Optional[ConversionSettings],
    collection_name: str = "_default",
):
    """
    Create payload for requesting conversion
    """

    target = target or ZipTarget()

    ccs_conv_settings: Optional[dict] = None
    if conversion_settings is not None:
        ccs_conv_settings = conversion_settings.to_ccs_spec()

    payload = {
        "source": {**source},
        "context": {
            "collection_name": collection_name,
            "conversion_settings": ccs_conv_settings,
            "keep_documents": "false",
        },
        "target": target.dict(),
    }
    return payload


def check_ccs_single_task_status(api: CpsApi, ccs_proj_key: str, task_id: str):
    """
    Check status of individual tasks.
    """
    current_state = False
    while current_state is False:
        request_status = api.client.session.get(
            url=URLNavigator(api).url_request_status(
                ccs_proj_key=ccs_proj_key, task_id=task_id
            )
        )
        current_state = request_status.json()["done"]
    return request_status


def check_cps_single_task_status(
    sw_api: sw_client.TasksApi, cps_proj_key: str, task_id: str, wait: int = 2
):
    """
    Check cps status of individual tasks.
    """
    while True:
        r: sw_client.CpsTask = sw_api.get_project_celery_task(
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
    source: dict,
    target: Optional[ExportTarget],
    conversion_settings: Optional[ConversionSettings],
) -> str:
    """
    Convert an online pdf using DeepSearch Technology.
    """
    # get ccs project key and collection name
    ccs_proj_key, collection_name = get_ccs_project_key(
        api=api, cps_proj_key=cps_proj_key
    )

    # submit conversion request
    payload = make_payload(source, target, conversion_settings, collection_name)

    try:
        request_conversion_task_id = api.client.session.post(
            url=URLNavigator(api).url_convert(ccs_proj_key=ccs_proj_key),
            json=payload,
        )
        request_conversion_task_id.raise_for_status()

    except requests.exceptions.HTTPError as err:
        logger.error(f"HTTPError {err}.\n{ERROR_MSG}\nAborting!")
        raise

    task_id = list(request_conversion_task_id.json().values())[0]

    return task_id


def send_files_for_conversion(
    api: CpsApi,
    cps_proj_key: str,
    source_path: Path,
    target: Optional[ExportTarget],
    conversion_settings: Optional[ConversionSettings],
    root_dir: Path,
    progress_bar: bool = False,
) -> list:
    """
    Send multiple files for conversion.
    """
    files_zip = collect_all_local_files(source_path=source_path, root_dir=root_dir)

    # container for task_ids
    task_ids = []

    # start loop
    with tqdm(
        total=len(files_zip),
        desc=f"{'Submitting input:': <{progressbar.padding}}",
        disable=not (progress_bar),
        colour=progressbar.colour,
        bar_format=progressbar.bar_format,
    ) as progress:
        # loop over all files
        for single_zip in files_zip:
            # upload file
            uploaded_file = api.uploader.upload_file(
                project=cps_proj_key, source_path=Path(single_zip)
            )
            # submit url for conversion
            task_id = submit_conversion_payload(
                api=api,
                cps_proj_key=cps_proj_key,
                source={
                    "type": "url",
                    "download_url": uploaded_file.internal_url,
                },
                target=target,
                conversion_settings=conversion_settings,
            )
            task_ids.append(task_id)
            progress.update(1)

    return task_ids


def check_status_running_tasks(
    cps_proj_key: str,
    task_ids: List[str],
    api: Optional[CpsApi] = None,
    progress_bar: bool = False,
) -> List[str]:
    """
    Check status of multiple running tasks and optionally display progress with progress bar.
    """
    if api is None:
        api = CpsApi.from_env()
    count_total = len(task_ids)

    # get ccs proj keys
    ccs_proj_key, collection_name = get_ccs_project_key(
        api=api, cps_proj_key=cps_proj_key
    )
    statuses = []

    with tqdm(
        total=count_total,
        desc=f"{'Converting input:': <{progressbar.padding}}",
        disable=not (progress_bar),
        colour=progressbar.colour,
        bar_format=progressbar.bar_format,
    ) as progress:
        for task_id in task_ids:
            request_status = check_ccs_single_task_status(
                api=api, ccs_proj_key=ccs_proj_key, task_id=task_id
            )
            if request_status.json()["done"]:
                progress.update(1)
                statuses.append(str(request_status.json()["state"]))

    return statuses


def check_cps_status_running_tasks(
    api: CpsApi, cps_proj_key: str, task_ids: List[str], progress_bar: bool = False
) -> List[str]:
    """
    Check status of multiple running cps tasks and optionally display progress with progress bar.
    """

    sw_api = sw_client.TasksApi(api.client.swagger_client)
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


def get_download_url(
    cps_proj_key: str,
    task_ids: list,
    api: Optional[CpsApi] = None,
) -> List[str]:
    """
    Get the urls of converted documents.
    """
    if api is None:
        api = CpsApi.from_env()
    # get ccs proj keys
    ccs_proj_key, collection_name = get_ccs_project_key(
        api=api, cps_proj_key=cps_proj_key
    )
    urls = []
    for task_id in task_ids:
        request_result = api.client.session.get(
            url=URLNavigator(api).url_result(ccs_proj_key=ccs_proj_key, task_id=task_id)
        )
        request_result.raise_for_status()
        try:
            packages = request_result.json()["packages"]
            for p in packages:
                urls.append(p["url"])
        except IndexError:
            logger.error(f"Error: Empty package received.\n{ERROR_MSG}")
    return urls


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
            download_name = Path(os.path.join(result_dir, f"json_{count:06}.zip"))
            download_url(url, download_name),
            count += 1
            progress.update(1)
    return


def send_urls_for_conversion(
    api: CpsApi,
    cps_proj_key: str,
    urls: List[str],
    target: Optional[ExportTarget],
    conversion_settings: Optional[ConversionSettings],
    progress_bar: bool = False,
) -> List[Any]:
    """
    Send multiple online documents for conversion.
    """
    count_urls = len(urls)
    task_ids = []
    with tqdm(
        total=count_urls,
        desc=f"{'Submitting input:': <{progressbar.padding}}",
        disable=not (progress_bar),
        colour=progressbar.colour,
        bar_format=progressbar.bar_format,
    ) as progress:
        for url in urls:
            task_id = submit_conversion_payload(
                api=api,
                cps_proj_key=cps_proj_key,
                source={
                    "type": "url",
                    "download_url": url,
                },
                target=target,
                conversion_settings=conversion_settings,
            )
            task_ids.append(task_id)
            progress.update(1)
    return task_ids
