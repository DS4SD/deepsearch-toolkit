import glob
import logging
import os
from pathlib import Path
from typing import TYPE_CHECKING, Any, List, Literal, Optional, Union

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from tqdm import tqdm

from deepsearch.cps.client.api import CpsApi
from deepsearch.cps.client.components.data_indices import DATA_INDEX_TYPE, S3Coordinates
from deepsearch.cps.client.components.elastic import ElasticProjectDataCollectionSource
from deepsearch.documents.core import convert, input_process
from deepsearch.documents.core.common_routines import progressbar, success_message
from deepsearch.documents.core.utils import (
    ALLOWED_FILE_EXTENSIONS,
    ALLOWED_JSON_TYPE_FILE_EXTENSION,
    cleanup,
    create_root_dir,
)

logger = logging.getLogger(__name__)


def upload_files(
    coords: ElasticProjectDataCollectionSource,
    index_type: DATA_INDEX_TYPE,
    url: Optional[Union[str, List[str]]] = None,
    local_file: Optional[Union[str, Path]] = None,
    s3_coordinates: Optional[S3Coordinates] = None,
    api: Optional[CpsApi] = None,
):
    """
    Orchestrate document conversion and upload to an index in a project
    """

    # initialize default Api if not specified
    if api is None:
        api = CpsApi.default_from_env()

    # check required inputs are present
    if url is None and local_file is None and s3_coordinates is None:
        raise ValueError(
            "No input provided. Please provide either a url, a local file, or coordinates to COS."
        )
    elif url is not None and local_file is None and s3_coordinates is None:
        if isinstance(url, str):
            urls = [url]
        else:
            urls = url

        if index_type == "Document":
            return process_url_input(
                api=api, coords=coords, urls=urls, index_type=index_type
            )
        else:
            raise ValueError("Url is only allowed on index with type Document.")
    elif url is None and local_file is not None and s3_coordinates is None:
        return process_local_file(
            api=api, coords=coords, local_file=Path(local_file), index_type=index_type
        )
    elif url is None and local_file is None and s3_coordinates is not None:
        return process_external_cos(
            api=api, coords=coords, s3_coordinates=s3_coordinates, index_type=index_type
        )

    raise ValueError(
        "Please provide only one input: url, local file, or s3_coordinates"
    )


def process_url_input(
    api: CpsApi,
    coords: ElasticProjectDataCollectionSource,
    urls: List[str],
    index_type: DATA_INDEX_TYPE,
    progress_bar=False,
):
    """
    Individual urls are uploaded for conversion and storage in data index.
    """

    # filter urls to match allowed extensions
    filtered_urls = []
    if index_type == "Document":
        filtered_urls = [
            url for url in urls if "." + url.split(".")[-1] in ALLOWED_FILE_EXTENSIONS
        ]
    else:
        raise ValueError("Url is only allowed on index type Document.")

    if len(filtered_urls) == 0:
        raise ValueError(
            f"Please provide at least one url with allowed file extension '{' , '.join(ALLOWED_FILE_EXTENSIONS)}'."
        )

    root_dir = create_root_dir()

    # container list for task_ids
    task_ids = []
    # submit urls
    count_urls = len(filtered_urls)
    with tqdm(
        total=count_urls,
        desc=f"{'Submitting input:': <{progressbar.padding}}",
        disable=not (progress_bar),
        colour=progressbar.colour,
        bar_format=progressbar.bar_format,
    ) as progress:
        for url in filtered_urls:
            file_url_array = [url]
            payload = {"file_url": file_url_array}
            task_id = api.data_indices.upload_file(
                coords=coords, body=payload, index_type=index_type
            )
            task_ids.append(task_id)
            progress.update(1)

    # check status
    statuses = convert.check_cps_status_running_tasks(
        api=api, cps_proj_key=coords.proj_key, task_ids=task_ids
    )
    print(success_message)

    return


def process_local_file(
    api: CpsApi,
    coords: ElasticProjectDataCollectionSource,
    local_file: Path,
    index_type: DATA_INDEX_TYPE,
    progress_bar=False,
):
    """
    Individual files are processed before upload.
    """

    if index_type == "Generic" or index_type == "DB Record":
        if (
            os.path.isfile(local_file)
            and Path(local_file).suffix in ALLOWED_JSON_TYPE_FILE_EXTENSION
        ):
            # container for task_ids
            task_ids = []

            with tqdm(
                total=1,
                desc=f"{'Submitting input:': <{progressbar.padding}}",
                disable=not (progress_bar),
                colour=progressbar.colour,
                bar_format=progressbar.bar_format,
            ) as progress:
                # upload file
                private_download_url = convert.upload_single_file(
                    api=api, cps_proj_key=coords.proj_key, source_path=Path(local_file)
                )
                payload_generic = {"file_url": private_download_url}
                task_id = api.data_indices.upload_file(
                    coords=coords, body=payload_generic, index_type=index_type
                )
                task_ids.append(task_id)
                progress.update(1)

            # send files to upload and check status of running tasks
            statuses = convert.check_cps_status_running_tasks(
                api=api, cps_proj_key=coords.proj_key, task_ids=task_ids
            )

            print(success_message)
            return
        else:
            raise ValueError(
                f"""For an index type {index_type}, 
                please provide a file with allowed extensions:
                {' , '.join(ALLOWED_JSON_TYPE_FILE_EXTENSION)}."""
            )
    elif index_type == "Document":
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

        if len(files_zip) == 0:
            raise ValueError(
                f"""For an index type {index_type}, 
                please provide a file with allowed extensions:
                {' , '.join(ALLOWED_FILE_EXTENSIONS)}."""
            )

        count_total_files = len(files_zip)

        # container for task_ids
        task_ids = []

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
                file_url_array = [private_download_url]
                payload_document = {"file_url": file_url_array}
                task_id = api.data_indices.upload_file(
                    coords=coords, body=payload_document, index_type=index_type
                )
                task_ids.append(task_id)
                progress.update(1)

        # send files to upload and check status of running tasks
        statuses = convert.check_cps_status_running_tasks(
            api=api, cps_proj_key=coords.proj_key, task_ids=task_ids
        )

        print(success_message)
        cleanup(root_dir=root_dir)
        return
    else:
        raise ValueError(
            "At the moment only index with type Document or Generic are supported"
        )


def process_external_cos(
    api: CpsApi,
    coords: ElasticProjectDataCollectionSource,
    s3_coordinates: S3Coordinates,
    index_type: DATA_INDEX_TYPE,
    progress_bar=False,
):
    """
    Individual files are processed before upload.
    """
    if index_type == "Document":
        # container for task_ids
        task_ids = []

        with tqdm(
            total=1,
            desc=f"{'Submitting input:': <{progressbar.padding}}",
            disable=not (progress_bar),
            colour=progressbar.colour,
            bar_format=progressbar.bar_format,
        ) as progress:
            # upload using coordinates
            payload = {"s3_source": {"coordinates": s3_coordinates}}
            task_id = api.data_indices.upload_file(
                coords=coords, body=payload, index_type=index_type
            )
            task_ids.append(task_id)
            progress.update(1)

        # NOTE: it throws error, will run ok after cps-api pr merge
        # return after status of running tasks are done
        return convert.check_cps_status_running_tasks(
            api=api, cps_proj_key=coords.proj_key, task_ids=task_ids
        )

    else:
        raise ValueError("COS coordinates is only allowed on index type Document.")
