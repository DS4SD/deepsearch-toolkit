import glob
import os
from pathlib import Path
from typing import Any, List, Optional, Union

from tqdm import tqdm

from deepsearch.cps.client.api import CpsApi
from deepsearch.cps.client.components.elastic import ElasticProjectDataCollectionSource
from deepsearch.documents.core import convert, input_process
from deepsearch.documents.core.common_routines import (
    ERROR_MSG,
    WELCOME,
    progressbar_padding,
    success_message,
)
from deepsearch.documents.core.create_report import report_docs, report_urls


def upload_files(
    coords: ElasticProjectDataCollectionSource,
    url: Optional[str] = None,
    local_file: Optional[Union[str, Path]] = None,
):
    """
    Orchestrate document conversion and upload to an index in a project
    """

    print(WELCOME)
    if url is None and local_file is None:
        print("Please provide either a url or a local file for conversion.")
        print("Aborting!")
        return
    elif url is not None and local_file is not None:
        print("Please provide only one input: url or local file.")
        print("Aborting!")
        return
    elif url is not None and local_file is None:
        process_url_input(coords=coords, url=url)
    elif url is None and local_file is not None:
        process_local_file(
            coords=coords,
            local_file=Path(local_file),
        )
    return


def process_url_input(coords: ElasticProjectDataCollectionSource, url: str):
    """
    Individual urls are uploaded for conversion and storage in data index.
    """
    api = CpsApi.default_from_env()

    root_dir = input_process.create_root_dir()

    # single vs multiple urls
    if not os.path.isfile(url):
        # deal with single url input
        urls = [url]
    elif os.path.isfile(url):
        # deal with file
        urls = input_process.get_urls(url)

    # container list for task_ids
    task_ids = []
    # submit urls
    count_urls = len(urls)
    with tqdm(
        total=count_urls,
        desc=f'{"Submitting input:":<{progressbar_padding}}',
    ) as progress:
        for url in urls:
            payload = {"file_url": url}
            task_id = api.data_indices.upload_file(coords=coords, body=payload)
            task_ids.append(task_id)
            progress.update(1)

    # check status
    statuses = convert.check_status_running_tasks(
        cps_proj_key=coords.proj_key, task_ids=task_ids
    )
    print(success_message)
    report_urls(root_dir=root_dir, urls=urls, task_ids=task_ids, statuses=statuses)

    return


def process_local_file(coords: ElasticProjectDataCollectionSource, local_file: Path):
    """
    Individual files are uploaded for conversion and storage in data index.
    """
    api = CpsApi.default_from_env()

    # process multiple files from local directory
    root_dir = input_process.create_root_dir()
    # batch individual pdfs into zips and add them to root_dir
    batched_files = input_process.batch_single_files(
        local_file=local_file, root_dir=root_dir
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
        desc=f'{"Submitting input:":<{progressbar_padding}}',
    ) as progress:
        # loop over all files
        for single_zip in files_zip:
            # upload file
            private_download_url = convert.upload_single_file(
                cps_proj_key=coords.proj_key, file=Path(single_zip)
            )
            payload = {"file_url": private_download_url}
            task_id = api.data_indices.upload_file(coords=coords, body=payload)
            task_ids.append(task_id)
            progress.update(1)

    # check status of running tasks
    statuses = convert.check_status_running_tasks(
        cps_proj_key=coords.proj_key, task_ids=task_ids
    )
    print(success_message)
    report_docs(
        root_dir=root_dir,
        batched_files=batched_files,
        task_ids=task_ids,
        statuses=statuses,
        local_file=local_file,
    )
    input_process.cleanup(root_dir=root_dir)
    return
