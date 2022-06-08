from pathlib import Path, PosixPath

import typer

from deepsearch.cps.cli.cli_options import LOCAL_FILE, PROJ_KEY, URL
from deepsearch.documents.core.common_routines import WELCOME
from deepsearch.documents.core.main import convert_document

app = typer.Typer(no_args_is_help=True)


@app.command(
    name="convert",
    help="Convert pdf documents using DeepSearch Technology",
    no_args_is_help=True,
)
def convert(
    proj_key: str = PROJ_KEY,
    url: str = URL,
    local_file: Path = LOCAL_FILE,
):
    """
    Document conversion via DeepSearch Technology.

    Inputs
    ------
    proj_key : string [REQUIRED]
    Your DeepSearch CPS Project Key. Contact DeepSearch Developers to request one.

    url : string [OPTIONAL]
    For converting a document from the web, please provide its url.

    local_file : string/path [OPTIONAL]
    For converting local files, please provide absolute path to file or to directory
    containing multiple files.

    NOTE: Either url or local_file should be supplied.
    """
    convert_document(proj_key=proj_key, url=url, local_file=local_file)
    return


if __name__ == "__main__":
    app()
