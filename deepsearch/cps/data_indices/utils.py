import glob
import logging
import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from tqdm import tqdm

from deepsearch.cps.client.api import CpsApi
from deepsearch.cps.client.components.data_indices import S3Coordinates
from deepsearch.cps.client.components.elastic import ElasticProjectDataCollectionSource
from deepsearch.documents.core import convert, input_process
from deepsearch.documents.core.common_routines import progressbar
from deepsearch.documents.core.models import ConversionSettings
from deepsearch.documents.core.utils import cleanup, create_root_dir

logger = logging.getLogger(__name__)


def upload_files(
    api: CpsApi,
    coords: ElasticProjectDataCollectionSource,
    url: Optional[Union[str, List[str]]] = None,
    local_file: Optional[Union[str, Path]] = None,
    s3_coordinates: Optional[S3Coordinates] = None,
    conv_settings: Optional[ConversionSettings] = None,
):
    """
    Orchestrate document conversion and upload to an index in a project
    """

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

        return process_url_input(api=api, coords=coords, urls=urls)
    elif url is None and local_file is not None and s3_coordinates is None:
        return process_local_file(
            api=api,
            coords=coords,
            local_file=Path(local_file),
            conv_settings=conv_settings,
        )
    elif url is None and local_file is None and s3_coordinates is not None:
        return process_external_cos(
            api=api, coords=coords, s3_coordinates=s3_coordinates
        )
    raise ValueError(
        "Please provide only one input: url, local file, or coordinates to COS."
    )


def process_url_input(
    api: CpsApi,
    coords: ElasticProjectDataCollectionSource,
    urls: List[str],
    progress_bar: bool = False,
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
            file_url_array = [url]
            payload = {"file_url": file_url_array}
            task_id = api.data_indices.upload_file(coords=coords, body=payload)
            task_ids.append(task_id)
            progress.update(1)

    # check status
    # TODO: add failure handling
    statuses = convert.check_cps_status_running_tasks(
        api=api, cps_proj_key=coords.proj_key, task_ids=task_ids
    )

    return


def process_local_file(
    api: CpsApi,
    coords: ElasticProjectDataCollectionSource,
    local_file: Path,
    progress_bar: bool = False,
    conv_settings: Optional[ConversionSettings] = None,
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
    task_ids: List[str] = []

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
            uploaded_file = api.uploader.upload_file(
                project=coords.proj_key, source_path=Path(single_zip)
            )
            file_url_array = [uploaded_file.internal_url]
            payload: Dict[str, Any] = {
                "file_url": file_url_array,
            }
            if conv_settings is not None:
                payload["conversion_settings"] = conv_settings.to_ccs_spec()

            task_id = api.data_indices.upload_file(coords=coords, body=payload)
            task_ids.append(task_id)
            progress.update(1)

    # check status of running tasks
    # TODO: add failure handling
    statuses = convert.check_cps_status_running_tasks(
        api=api, cps_proj_key=coords.proj_key, task_ids=task_ids
    )
    cleanup(root_dir=root_dir)
    return


def process_external_cos(
    api: CpsApi,
    coords: ElasticProjectDataCollectionSource,
    s3_coordinates: S3Coordinates,
    progress_bar=False,
):
    """
    Individual files are processed before upload.
    """
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
        payload = {"s3_source": {"coordinates": s3_coordinates.dict()}}
        task_id = api.data_indices.upload_file(
            coords=coords,
            body=payload,
        )
        task_ids.append(task_id)
        progress.update(1)

    # check status of running tasks
    # TODO: add failure handling
    statuses = convert.check_cps_status_running_tasks(
        api=api, cps_proj_key=coords.proj_key, task_ids=task_ids
    )
    return
