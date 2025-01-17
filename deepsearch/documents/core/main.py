from pathlib import Path
from typing import Optional

import urllib3

from deepsearch.cps.client.api import CpsApi
from deepsearch.documents.core.input_process import (
    process_local_input,
    process_url_input,
)
from deepsearch.documents.core.models import ConversionSettings

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def convert_documents(
    proj_key: str,
    api: CpsApi,
    url: Optional[str] = None,
    source_path: Optional[Path] = None,
    conversion_settings: Optional[ConversionSettings] = None,
    progress_bar=False,
    export_md=False,
):
    """
    Document conversion via Deep Search Technology. Function to orchestrate document conversion.

    Inputs
    ------
    proj_key : string [REQUIRED]
    Your DeepSearch CPS Project Key. Contact DeepSearch Developers to request one.

    url : string [OPTIONAL]
    For converting documents from the web, please provide a single url.

    source_file : path [OPTIONAL]
    For converting local files, please provide absolute path to file or to directory
    containing multiple files.

    progress_bar : Boolean (default is False in code, True in CLI)
    Show progress bar for processing, submitting, converting input and
    downloading converted document.

    NOTE: Either url or source_path should be supplied.
    """
    # check required inputs are present
    if url is None and source_path is None:
        raise ValueError(
            "No input provided. Please provide either a url or a local file."
        )
    elif url is not None and source_path is None:
        return process_url_input(
            api=api,
            cps_proj_key=proj_key,
            url=url,
            conversion_settings=conversion_settings,
            progress_bar=progress_bar,
            export_md=export_md,
        )
    elif url is None and source_path is not None:
        return process_local_input(
            api=api,
            cps_proj_key=proj_key,
            source_path=Path(source_path).expanduser().resolve(),
            conversion_settings=conversion_settings,
            progress_bar=progress_bar,
            export_md=export_md,
        )
    raise ValueError("Please provide only one input: url or local file.")
