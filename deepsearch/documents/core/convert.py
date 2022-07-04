import glob
import os
import pathlib
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

from .common_routines import ERROR_MSG, progressbar_padding
from .utils import download_url

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# set up basic urls
url_user_management = "/user/v1"
url_public_apis = "/public/v4"


def make_payload(url_document: str, collection_name: str = "_default"):
    """
    Create payload for requesting conversion
    """
    payload = {
        "source": {
            "type": "url",
            "download_url": url_document,
        },
        "context": {
            "collection_name": collection_name,
            "keep_documents": "false",
        },
        "target": {"type": "zip", "content_type": "json", "add_cells": "true"},
    }
    return payload


def check_single_task_status(api: CpsApi, ccs_proj_key: str, task_id: str):
    """
    Check status of individual tasks.
    """
    url_host = api.client.swagger_client.configuration.host
    url_linked_ccs = url_host.rstrip("/public/v1").rstrip("cps") + "linked-ccs"
    current_state = False
    while current_state is False:
        wait = 5
        url_request_status = f"{url_linked_ccs}{url_public_apis}/projects/{ccs_proj_key}/tasks/{task_id}/status?wait={wait}"
        request_status = api.client.session.get(url=url_request_status)
        current_state = request_status.json()["done"]

    return request_status


def get_ccs_project_key(api: CpsApi, cps_proj_key: str):
    """
    Given a cps project key, returns ccs project key and collection name.
    """
    sw_api = sw_client.ProjectApi(api.client.swagger_client)

    # TODO: Do we actually need to handle these exceptions here?
    # If yes, let's chain a custom-exception, e.g. CcsClientException

    # try:
    #     request_ccs_project_key = sw_api.get_project_default_values(
    #         proj_key=cps_proj_key
    #     )
    #     ccs_proj_key = request_ccs_project_key.ccs_project.proj_key
    #     collection_name = request_ccs_project_key.ccs_project.collection_name
    # except requests.exceptions.HTTPError as err:
    #     print(f"HTTPError {err}.\n{ERROR_MSG}")
    #     print("Aborting!")
    #     return
    # except KeyError as err:
    #     print(f"Error: Received unexpected response.\n{ERROR_MSG}")
    #     print("Aborting!")
    #     return
    # except urllib3.exceptions.MaxRetryError as err:
    #     print(f"Error: err.\n{ERROR_MSG}")
    #     print("Aborting!")
    #     return

    request_ccs_project_key = sw_api.get_project_default_values(proj_key=cps_proj_key)
    ccs_proj_key = request_ccs_project_key.ccs_project.proj_key
    collection_name = request_ccs_project_key.ccs_project.collection_name
    return (ccs_proj_key, collection_name)


def get_converted_doc(api: CpsApi, ccs_proj_key: str, task_id: str):
    """
    Download converted document
    """
    url_host = api.client.swagger_client.configuration.host
    url_linked_ccs = url_host.rstrip("/public/v1").rstrip("cps") + "linked-ccs"
    url_result = f"{url_linked_ccs}{url_public_apis}/projects/{ccs_proj_key}/document_conversions/{task_id}/result"
    request_result = api.client.session.get(url=url_result)
    request_result.raise_for_status()

    try:
        url_converted_document = request_result.json()["packages"][0]["url"]
        if request_result.json()["done"]:
            print(
                "Document Conversion is finished. Downloading your converted document."
            )
            download_url(url_converted_document, Path("./converted_document.zip"))
            print("Your converted document is now downloaded. Ciao!")
            return
    except IndexError:
        print(f"Error: Empty package received.\n{ERROR_MSG}")
        print("Aborting!")
        return


def submit_url_for_conversion(
    api: CpsApi,
    cps_proj_key: str,
    url: str,
) -> str:
    """
    Convert an online pdf using DeepSearch Technology.
    """
    # define urls
    url_host = api.client.swagger_client.configuration.host
    url_linked_ccs = url_host.rstrip("/public/v1").rstrip("cps") + "linked-ccs"

    # get ccs project key and collection name
    ccs_proj_key, collection_name = get_ccs_project_key(
        api=api, cps_proj_key=cps_proj_key
    )

    # submit conversion request
    payload = make_payload(url, collection_name)

    try:
        request_conversion_task_id = api.client.session.post(
            url=f"{url_linked_ccs}{url_public_apis}/projects/{ccs_proj_key}/pipelines/convert",
            json=payload,
        )
        request_conversion_task_id.raise_for_status()

    except requests.exceptions.HTTPError as err:
        print(f"HTTPError {err}.\n{ERROR_MSG}\nAborting!")
        raise

    task_id = list(request_conversion_task_id.json().values())[0]

    return task_id


def send_files_for_conversion(
    api: CpsApi, cps_proj_key: str, local_file: Path, root_dir: Path, progress_bar=False
) -> list:
    """
    Send multiple files for conversion.
    """
    # collect'em all
    files_zip: List[Any] = []
    if os.path.isdir(local_file):
        files_zip = glob.glob(os.path.join(local_file, "**/*.zip"), recursive=True)
    elif os.path.isfile(local_file):
        file_extension = pathlib.Path(local_file).suffix
        if file_extension == ".zip":
            files_zip = [local_file]

    if root_dir is not None:
        files_tmpzip = glob.glob(
            os.path.join(root_dir, "tmpzip/**/*.zip"), recursive=True
        )
        files_zip = files_zip + files_tmpzip
    count_total_files = len(files_zip)

    # container for task_ids
    task_ids = []

    # start loop
    with tqdm(
        total=count_total_files,
        desc=f'{"Submitting input:":<{progressbar_padding}}',
        disable=not (progress_bar),
    ) as progress:
        # loop over all files
        for single_zip in files_zip:
            # upload file
            private_download_url = upload_single_file(
                api=api, cps_proj_key=cps_proj_key, file=Path(single_zip)
            )
            # submit url for conversion
            task_id = submit_url_for_conversion(
                api=api, cps_proj_key=cps_proj_key, url=private_download_url
            )
            task_ids.append(task_id)
            progress.update(1)

    return task_ids


def check_status_running_tasks(
    cps_proj_key: str, task_ids, api: Optional[CpsApi] = None, progress_bar=False
) -> List[str]:
    """
    Check status of multiple running tasks and display progress with progress bar.
    """
    if api is None:
        api = CpsApi.default_from_env()
    count_total = len(task_ids)

    # get ccs proj keys
    ccs_proj_key, collection_name = get_ccs_project_key(
        api=api, cps_proj_key=cps_proj_key
    )
    statuses = []

    with tqdm(
        total=count_total,
        desc=f'{"Converting input:":<{progressbar_padding}}',
        disable=not (progress_bar),
    ) as progress:
        for task_id in task_ids:
            request_status = check_single_task_status(
                api=api, ccs_proj_key=ccs_proj_key, task_id=task_id
            )
            if request_status.json()["done"]:
                progress.update(1)
                statuses.append(str(request_status.json()["state"]))

    return statuses


def get_download_url(
    cps_proj_key: str,
    task_ids: list,
    api: Optional[CpsApi] = None,
) -> List[str]:
    """
    Get the url of converted document.
    """
    if api is None:
        api = CpsApi.default_from_env()

    url_host = api.client.swagger_client.configuration.host
    url_linked_ccs = url_host.rstrip("/public/v1").rstrip("cps") + "linked-ccs"

    # get ccs proj keys
    ccs_proj_key, collection_name = get_ccs_project_key(
        api=api, cps_proj_key=cps_proj_key
    )
    urls = []
    for task_id in task_ids:
        url_result = f"{url_linked_ccs}{url_public_apis}/projects/{ccs_proj_key}/document_conversions/{task_id}/result"
        request_result = api.client.session.get(url=url_result)
        request_result.raise_for_status()
        try:
            packages = request_result.json()["packages"]
            for p in packages:
                urls.append(p["url"])
        except IndexError:
            print(f"Error: Empty package received.\n{ERROR_MSG}")
    return urls


def download_converted_documents(
    result_dir: Path, download_urls: List[str], progress_bar=False
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
        desc=f'{"Downloading result:":<{progressbar_padding}}',
        disable=not (progress_bar),
    ) as progress:
        count = 1
        for url in download_urls:
            download_name = Path(os.path.join(result_dir, f"json_{count:06}.zip"))
            download_url(url, download_name),
            count += 1
            progress.update(1)
    return


# def download_converted_docs(
#     api: CpsApi, cps_proj_key: str, task_ids: list, root_dir: Path
# ):
#     """
#     Download all converted documents
#     """
#     url_host = api.client.swagger_client.configuration.host
#     url_linked_ccs = url_host.rstrip("/public/v1").rstrip("cps") + "linked-ccs"

#     # get ccs proj keys
#     ccs_proj_key, collection_name = get_ccs_project_key(
#         api=api, cps_proj_key=cps_proj_key
#     )

#     # setup result directory
#     result_dir = root_dir
#     if not os.path.isdir(result_dir):
#         os.makedirs(result_dir)

#     count_taskids = len(task_ids)

#     with tqdm(
#         total=count_taskids, desc=f'{"Downloading result:":<{progressbar_padding}}'
#     ) as progress:
#         count = 1
#         for task_id in task_ids:
#             url_result = f"{url_linked_ccs}{url_public_apis}/projects/{ccs_proj_key}/document_conversions/{task_id}/result"
#             request_result = api.client.session.get(url=url_result)
#             request_result.raise_for_status()

#             try:
#                 packages = request_result.json()["packages"]
#                 for p in packages:
#                     url_converted_document = p["url"]
#                     download_name = Path(
#                         os.path.join(result_dir, f"json_{count:06}.zip")
#                     )
#                     download_url(url_converted_document, download_name),
#                     count += 1
#                     progress.update(1)
#             except IndexError:
#                 print(f"Error: Empty package received.\n{ERROR_MSG}")
#     return


def upload_single_file(api: CpsApi, cps_proj_key: str, file: Path) -> str:
    """
    Uploads a single file. Return internal download url.
    """
    filename = os.path.basename(file)
    # url_host = api.client.swagger_client.configuration.host
    sw_api = sw_client.UploadsApi(api.client.swagger_client)

    get_pointer: TemporaryUploadFileResult = sw_api.create_project_scratch_file(
        proj_key=cps_proj_key, filename=filename
    )
    # upload file
    upload = get_pointer.upload
    private_download_url = get_pointer.download_private.url

    with open(file, "rb") as f:
        files = {"file": (os.path.basename(file), f)}
        request_upload = requests.post(
            url=upload.url, data=upload.fields, files=files, verify=False
        )
        request_upload.raise_for_status()

    return private_download_url


def send_urls_for_conversion(
    api: CpsApi, cps_proj_key: str, urls: List[str], progress_bar=False
) -> List[Any]:
    """
    Send multiple online documents for conversion.
    """
    count_urls = len(urls)
    task_ids = []
    with tqdm(
        total=count_urls,
        desc=f'{"Submitting input:":<{progressbar_padding}}',
        disable=not (progress_bar),
    ) as progress:
        for url in urls:
            task_id = submit_url_for_conversion(
                api=api, cps_proj_key=cps_proj_key, url=url
            )
            task_ids.append(task_id)
            progress.update(1)
    return task_ids
