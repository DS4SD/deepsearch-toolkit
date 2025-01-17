import os
from pathlib import Path
from typing import Optional

import urllib3

from deepsearch.cps.apis import public_v2 as sw_client
from deepsearch.cps.client.api import CpsApi
from deepsearch.documents.core.results import DocumentConversionResult

from .models import ConversionSettings

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from .convert import (
    get_wait_task_result,
    send_file_for_conversion,
    send_url_for_conversion,
)


def process_local_input(
    api: CpsApi,
    cps_proj_key: str,
    source_path: Path,
    conversion_settings: Optional[ConversionSettings],
    progress_bar=False,
    export_md=False,
) -> DocumentConversionResult:
    """
    Classify the user provided local input and take appropriate action.
    """
    if not os.path.exists(source_path):
        raise ValueError("File not found. Check input.")
    else:
        task_id = send_file_for_conversion(
            api=api,
            cps_proj_key=cps_proj_key,
            source_path=source_path,
            conversion_settings=conversion_settings,
            progress_bar=progress_bar,
        )
        sw_api = sw_client.ProjectApi(api.client.swagger_client_v2)
        result = get_wait_task_result(
            sw_api=sw_api, cps_proj_key=cps_proj_key, task_id=task_id
        )
        return DocumentConversionResult(
            proj_key=cps_proj_key,
            task_id=task_id,
            result=result,
            source_path=source_path,
            api=api,
            export_md=export_md,
        )


def process_url_input(
    api: CpsApi,
    cps_proj_key: str,
    url: str,
    conversion_settings: Optional[ConversionSettings],
    progress_bar=False,
    export_md=False,
):
    """
    Classify user provided url(s) and take appropriate action.
    """
    task_id = send_url_for_conversion(
        api=api,
        cps_proj_key=cps_proj_key,
        url=url,
        conversion_settings=conversion_settings,
        progress_bar=progress_bar,
    )
    sw_api = sw_client.ProjectApi(api.client.swagger_client_v2)
    result = get_wait_task_result(
        sw_api=sw_api, cps_proj_key=cps_proj_key, task_id=task_id
    )
    return DocumentConversionResult(
        proj_key=cps_proj_key,
        task_id=task_id,
        result=result,
        source_url=url,
        api=api,
        export_md=export_md,
    )
