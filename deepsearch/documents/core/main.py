from pathlib import Path
from typing import Optional

from deepsearch.documents.core.common_routines import WELCOME
from deepsearch.documents.core.input_process import (
    process_local_input,
    process_url_input,
)


def convert_document(
    proj_key: str, url: Optional[str] = None, local_file: Optional[Path] = None
):
    """
    Document conversion via DeepSearch Technology. Function to orchestrate document conversion.

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
    print(WELCOME)
    # check required inputs are present
    if url is None and local_file is None:
        # if type(url) is not str and type(local_file) is not PosixPath:
        print("Please provide either a url or a local file for conversion.")
        print("Aborting!")
        return
    elif url is not None and local_file is not None:
        # elif type(url) is str and type(local_file) is PosixPath:
        print("Please provide only one input: url or local file.")
        print("Aborting!")
        return
    elif url is not None and local_file is None:
        # elif type(url) is str and type(local_file) is not PosixPath:
        process_url_input(cps_proj_key=proj_key, url=url)
    elif url is None and local_file is not None:
        # elif type(url) is not str and type(local_file) is PosixPath:
        process_local_input(cps_proj_key=proj_key, local_file=Path(local_file))

    return
