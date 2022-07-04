from pathlib import Path
from typing import List, Optional, Union
import urllib
from deepsearch.cps.client.api import CpsApi
from deepsearch.documents.core.input_process import (
    process_local_input,
    process_urls_input,
)
from .utils import get_urls


def convert_documents(
    proj_key: str,
    url: Optional[Union[str, List[str]]] = None,
    source_file: Optional[Path] = None,
    api: Optional[CpsApi] = None,
    progress_bar=False,
    cli_use=False,
):
    """
    Document conversion via Deep Search Technology. Function to orchestrate document conversion.

    Inputs
    ------
    proj_key : string [REQUIRED]
    Your DeepSearch CPS Project Key. Contact DeepSearch Developers to request one.

    url : string [OPTIONAL]
    For converting a document from the web, please provide its url.

    source_file : path [OPTIONAL]
    For converting local files, please provide absolute path to file or to directory
    containing multiple files.

    progress_bar : Boolean (default is False in code, True in CLI)
    Show progress bar for processing, submitting, converting input and
    downloading converted document.

    cli_use : Boolean (default is False in code, True in CLI)
    A flag that allows automatic download of converted document and
    generation of conversion report when used via CLI.

    NOTE: Either url or local_file should be supplied.
    """

    # initialize default Api if not specified
    if api is None:
        api = CpsApi.default_from_env()

    # check required inputs are present
    if url is None and source_file is None:
        raise ValueError(
            "No input provided. Please provide either a url or a local file for conversion."
        )
    elif url is not None and source_file is None:
        if urllib.parse.urlparse(url).scheme in ("http", "https"):
            urls = [url]
        else:
            urls = get_urls(Path(url))

        return process_urls_input(
            api=api,
            cps_proj_key=proj_key,
            urls=urls,
            progress_bar=progress_bar,
            cli_use=cli_use,
        )
    elif url is None and source_file is not None:
        return process_local_input(
            api=api,
            cps_proj_key=proj_key,
            local_file=Path(source_file),
            progress_bar=progress_bar,
            cli_use=cli_use,
        )

    raise ValueError("Please provide only one input: url or local file.")
