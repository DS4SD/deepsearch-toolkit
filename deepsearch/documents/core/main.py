from pathlib import Path
from typing import List, Optional, Union

from deepsearch.cps.client.api import CpsApi
from deepsearch.documents.core.input_process import (
    process_local_input,
    process_urls_input,
)


def convert_documents(
    proj_key: str,
    url: Optional[Union[str, List[str]]] = None,
    local_file: Optional[Path] = None,
    api: Optional[CpsApi] = None,
):
    """
    Document conversion via Deep Search Technology. Function to orchestrate document conversion.

    Inputs
    ------
    proj_key : string [REQUIRED]
    Your DeepSearch CPS Project Key. Contact DeepSearch Developers to request one.

    url : string [OPTIONAL]
    For converting a document from the web, please provide its url.

    local_file : path [OPTIONAL]
    For converting local files, please provide absolute path to file or to directory
    containing multiple files.

    NOTE: Either url or local_file should be supplied.
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

        return process_urls_input(api=api, cps_proj_key=proj_key, urls=urls)
    elif url is None and local_file is not None:
        return process_local_input(
            api=api, cps_proj_key=proj_key, local_file=Path(local_file)
        )

    raise ValueError("Please provide only one input: url or local file.")
