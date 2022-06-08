import glob
import os
import pathlib
from pathlib import Path
from typing import Any, List

import requests
import urllib3
from tqdm import tqdm

from deepsearch.cps.apis import public as sw_client
from deepsearch.cps.apis.public.models.temporary_upload_file_result import (
    TemporaryUploadFileResult,
)
from deepsearch.cps.cli.cli_options import PROJ_KEY, URL
from deepsearch.cps.client.api import CpsApi

from .common_routines import ERROR_MSG, progressbar_padding

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


def download_url(url: str, save_path: Path, chunk_size=128):
    """
    Download contents from a url.
    """
    r = requests.get(url, stream=True, verify=False)
    with open(save_path, "wb") as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)
    return


def check_single_task_status(ccs_proj_key: str, task_id: str):
    """
    Check status of individual tasks.
    """
    api = CpsApi.default_from_env()
    url_host = api.client.swagger_client.configuration.host
    url_linked_ccs = url_host.rstrip("/public/v1").rstrip("cps") + "linked-ccs"
    current_state = False
    while current_state is False:
        wait = 5
        url_request_status = f"{url_linked_ccs}{url_public_apis}/projects/{ccs_proj_key}/tasks/{task_id}/status?wait={wait}"
        request_status = api.client.session.get(url=url_request_status)
        current_state = request_status.json()["done"]

    return request_status


def get_ccs_project_key(cps_proj_key: str):
    """
    Given a cps project key, returns ccs project key and collection name.
    """
    api = CpsApi.default_from_env()
    sw_api = sw_client.ProjectApi(api.client.swagger_client)
    try:
        request_ccs_project_key = sw_api.get_project_default_values(
            proj_key=cps_proj_key
        )
        ccs_proj_key = request_ccs_project_key.ccs_project.proj_key
        collection_name = request_ccs_project_key.ccs_project.collection_name

    except requests.exceptions.HTTPError as err:
        print(f"HTTPError {err}.\n{ERROR_MSG}")
        print("Aborting!")
        return
    except KeyError as err:
        print(f"Error: Received unexpected response.\n{ERROR_MSG}")
        print("Aborting!")
        return
    except urllib3.exceptions.MaxRetryError as err:
        print(f"Error: err.\n{ERROR_MSG}")
        print("Aborting!")
        return
    return (ccs_proj_key, collection_name)


def get_converted_doc(ccs_proj_key: str, task_id: str):
    """
    Download converted document
    """
    api = CpsApi.default_from_env()
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
    cps_proj_key: str = PROJ_KEY,
    url: str = URL,
) -> str:
    """
    Convert an online pdf using DeepSearch Technology.
    """
    api = CpsApi.default_from_env()

    # define urls
    url_host = api.client.swagger_client.configuration.host
    url_linked_ccs = url_host.rstrip("/public/v1").rstrip("cps") + "linked-ccs"

    # get ccs project key and collection name
    ccs_proj_key, collection_name = get_ccs_project_key(cps_proj_key=cps_proj_key)

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
    cps_proj_key: str, local_file: Path, root_dir: Path
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
    ) as progress:
        # loop over all files
        for single_zip in files_zip:
            # upload file
            private_download_url = upload_single_file(
                cps_proj_key=cps_proj_key, file=Path(single_zip)
            )
            # submit url for conversion
            task_id = submit_url_for_conversion(
                cps_proj_key=cps_proj_key, url=private_download_url
            )
            task_ids.append(task_id)
            progress.update(1)

    return task_ids


def check_status_running_tasks(cps_proj_key: str, task_ids) -> List[str]:
    """
    Check status of multiple running tasks and display progress with progress bar.
    """
    count_total = len(task_ids)
    api = CpsApi.default_from_env()

    # get ccs proj keys
    ccs_proj_key, collection_name = get_ccs_project_key(cps_proj_key=cps_proj_key)

    statuses = []

    with tqdm(
        total=count_total, desc=f'{"Converting input:":<{progressbar_padding}}'
    ) as progress:
        for task_id in task_ids:
            request_status = check_single_task_status(
                ccs_proj_key=ccs_proj_key, task_id=task_id
            )
            if request_status.json()["done"]:
                progress.update(1)
                statuses.append(str(request_status.json()["state"]))

    return statuses


def download_converted_docs(cps_proj_key: str, task_ids: list, root_dir: Path):
    """
    Download all converted documents
    """
    api = CpsApi.default_from_env()
    url_host = api.client.swagger_client.configuration.host
    url_linked_ccs = url_host.rstrip("/public/v1").rstrip("cps") + "linked-ccs"

    # get ccs proj keys
    ccs_proj_key, collection_name = get_ccs_project_key(cps_proj_key=cps_proj_key)

    # setup result directory
    result_dir = root_dir
    if not os.path.isdir(result_dir):
        os.makedirs(result_dir)

    count_taskids = len(task_ids)

    with tqdm(
        total=count_taskids, desc=f'{"Downloading result:":<{progressbar_padding}}'
    ) as progress:
        count = 1
        for task_id in task_ids:
            url_result = f"{url_linked_ccs}{url_public_apis}/projects/{ccs_proj_key}/document_conversions/{task_id}/result"
            request_result = api.client.session.get(url=url_result)
            request_result.raise_for_status()

            try:
                packages = request_result.json()["packages"]
                for p in packages:
                    url_converted_document = p["url"]
                    download_name = Path(
                        os.path.join(result_dir, f"json_{count:06}.zip")
                    )
                    download_url(url_converted_document, download_name),
                    count += 1
                    progress.update(1)
            except IndexError:
                print(f"Error: Empty package received.\n{ERROR_MSG}")
    return


def upload_single_file(cps_proj_key: str, file: Path) -> str:
    """
    Uploads a single file. Return internal download url.
    """
    filename = os.path.basename(file)
    api = CpsApi.default_from_env()
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


def send_urls_for_conversion(cps_proj_key: str, urls: List[str]) -> List[Any]:
    """
    Send multiple online documents for conversion.
    """
    count_urls = len(urls)
    task_ids = []
    with tqdm(
        total=count_urls,
        desc=f'{"Submitting input:":<{progressbar_padding}}',
    ) as progress:
        for url in urls:
            task_id = submit_url_for_conversion(cps_proj_key=cps_proj_key, url=url)
            task_ids.append(task_id)
            progress.update(1)
    return task_ids
