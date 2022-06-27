from pathlib import Path, PosixPath
from typing import List

import typer

from deepsearch.cps.cli.cli_options import LOCAL_FILE, PROJ_KEY, URL
from deepsearch.documents.core.common_routines import WELCOME
from deepsearch.documents.core.main import convert_documents

app = typer.Typer(no_args_is_help=True)


def get_urls(path: Path) -> List[str]:
    """
    Returns list of url from input file.
    """

    lines = path.read_text()
    urls = [line.strip() for line in lines.split("\n") if line.strip() != ""]
    return urls


@app.command(
    name="convert",
    help="Convert pdf documents using Deep Search Technology",
    no_args_is_help=True,
)
def convert(
    proj_key: str = PROJ_KEY,
    url: str = URL,
    local_file: Path = LOCAL_FILE,
):
    """
    Document conversion via Deep Search Technology.

    Inputs
    ------
    proj_key : string [REQUIRED]
    Your Deep Search CPS Project Key.

    url : string [OPTIONAL]
    For converting a document from the web, please provide its url.

    local_file : string/path [OPTIONAL]
    For converting local files, please provide absolute path to file or to directory
    containing multiple files.

    NOTE: Either url or local_file should be supplied.
    """
    typer.echo(WELCOME)

    urls = None
    if url is not None:
        p = Path(url)
        urls = get_urls(p) if p.exists() else [url]

    documents = convert_documents(proj_key=proj_key, url=urls, local_file=local_file)
    return


if __name__ == "__main__":
    app()
