import glob
import logging
import os
from pathlib import Path
from typing import Any, List, Optional, Union

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from tqdm import tqdm

from deepsearch.cps.client.api import CpsApi
from deepsearch.cps.client.components.elastic import ElasticProjectDataCollectionSource
from deepsearch.documents.core import convert, input_process
from deepsearch.documents.core.common_routines import progressbar, success_message
from deepsearch.documents.core.utils import (
    cleanup,
    collect_all_local_files,
    create_root_dir,
)

logger = logging.getLogger(__name__)


def upload_files(
    coords: ElasticProjectDataCollectionSource,
    url: Optional[Union[str, List[str]]] = None,
    local_file: Optional[Union[str, Path]] = None,
    api: Optional[CpsApi] = None,
):
    """
    Orchestrate document conversion and upload to an index in a project
    """

    # initialize default Api if not specified
    if api is None:
        api = CpsApi.default_from_env()

    # check required inputs are present
    if url is None and local_file is None:
        raise ValueError(
            "No input provided. Please provide either a url or a local file for conversion."
        )
    elif url is not None and local_file is None:
        if isinstance(url, str):
            urls = [url]
        else:
            urls = url

        return process_url_input(api=api, coords=coords, urls=urls)
    elif url is None and local_file is not None:
        return process_local_file(
            api=api,
            coords=coords,
            local_file=Path(local_file),
        )

    raise ValueError("Please provide only one input: url or local file.")


def process_url_input(
    api: CpsApi,
    coords: ElasticProjectDataCollectionSource,
    urls: List[str],
    progress_bar=False,
):
    """
    Individual urls are uploaded for conversion and storage in data index.
    """

    root_dir = create_root_dir()

    # container list for task_ids
    task_ids = []
    # submit urls
    count_urls = len(urls)
    with tqdm(
        total=count_urls,
        desc=f"{'Submitting input:': <{progressbar.padding}}",
        disable=not (progress_bar),
        colour=progressbar.colour,
        bar_format=progressbar.bar_format,
    ) as progress:
        for url in urls:
            payload = {"file_url": url}
            task_id = api.data_indices.upload_file(coords=coords, body=payload)
            task_ids.append(task_id)
            progress.update(1)

    # check status
    statuses = convert.check_status_running_tasks(
        api=api, cps_proj_key=coords.proj_key, task_ids=task_ids
    )
    print(success_message)

    return


def process_local_file(
    api: CpsApi,
    coords: ElasticProjectDataCollectionSource,
    local_file: Path,
    progress_bar=False,
):
    """
    Individual files are uploaded for conversion and storage in data index.
    """

    # process multiple files from local directory
    root_dir = create_root_dir()
    # batch individual pdfs into zips and add them to root_dir
    batched_files = input_process.batch_single_files(
        source_path=local_file, root_dir=root_dir
    )

    # collect'em all
    files_zip: List[Any] = []
    if os.path.isdir(local_file):
        files_zip = glob.glob(os.path.join(local_file, "**/*.zip"), recursive=True)
    elif os.path.isfile(local_file):
        file_extension = Path(local_file).suffix
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
        desc=f"{'Submitting input:': <{progressbar.padding}}",
        disable=not (progress_bar),
        colour=progressbar.colour,
        bar_format=progressbar.bar_format,
    ) as progress:
        # loop over all files
        for single_zip in files_zip:
            # upload file
            private_download_url = convert.upload_single_file(
                api=api, cps_proj_key=coords.proj_key, source_path=Path(single_zip)
            )
            payload = {"file_url": private_download_url}
            task_id = api.data_indices.upload_file(coords=coords, body=payload)
            task_ids.append(task_id)
            progress.update(1)

    # check status of running tasks
    statuses = convert.check_status_running_tasks(
        api=api, cps_proj_key=coords.proj_key, task_ids=task_ids
    )
    print(success_message)
    cleanup(root_dir=root_dir)
    return
