from pathlib import Path
from typing import List, Optional, Union

import urllib3

from deepsearch.cps.client.api import CpsApi
from deepsearch.documents.core.input_process import (
    process_cos_input,
    process_local_input,
    process_urls_input,
)
from deepsearch.documents.core.models import (
    ConversionSettings,
    ExportTarget,
    S3Coordinates,
)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def convert_documents(
    proj_key: str,
    api: CpsApi,
    urls: Optional[Union[str, List[str]]] = None,
    source_path: Optional[Path] = None,
    source_cos: Optional[S3Coordinates] = None,
    target: Optional[ExportTarget] = None,
    conversion_settings: Optional[ConversionSettings] = None,
    progress_bar=False,
):
    """
    Document conversion via Deep Search Technology. Function to orchestrate document conversion.

    Inputs
    ------
    proj_key : string [REQUIRED]
    Your DeepSearch CPS Project Key. Contact DeepSearch Developers to request one.

    url : string [OPTIONAL]
    For converting documents from the web, please provide a single url or list of urls.

    source_file : path [OPTIONAL]
    For converting local files, please provide absolute path to file or to directory
    containing multiple files.

    source_cos : S3Coordinates [OPTIONAL]
    For converting all documents in a COS bucket, please provide the S3 credentials, including bucket and key_prefix.

    target : deepsearch.documents.core.models.ExportTargets [OPTIONAL]
    Specify to which target the documents should be exported. Available options: ZIP file,
    Elastic index, MongoDB collection

    progress_bar : Boolean (default is False in code, True in CLI)
    Show progress bar for processing, submitting, converting input and
    downloading converted document.

    NOTE: Either url or source_path should be supplied.
    """
    # check required inputs are present
    if urls is None and source_path is None and source_cos is None:
        raise ValueError(
            "No input provided. Please provide either a url, a local file or references to an object store for conversion."
        )
    elif urls is not None and source_path is None and source_cos is None:
        if isinstance(urls, str):
            urls = [urls]

        return process_urls_input(
            api=api,
            cps_proj_key=proj_key,
            urls=urls,
            target=target,
            conversion_settings=conversion_settings,
            progress_bar=progress_bar,
        )
    elif urls is None and source_path is not None and source_cos is None:
        return process_local_input(
            api=api,
            cps_proj_key=proj_key,
            source_path=Path(source_path).expanduser().resolve(),
            target=target,
            conversion_settings=conversion_settings,
            progress_bar=progress_bar,
        )
    elif urls is None and source_path is None and source_cos is not None:
        return process_cos_input(
            api=api,
            cps_proj_key=proj_key,
            source_cos=source_cos,
            target=target,
            conversion_settings=conversion_settings,
            progress_bar=progress_bar,
        )

    raise ValueError("Please provide only one input: url or local file.")
