import urllib
from pathlib import Path

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import typer

from deepsearch.cps.cli.cli_options import PROGRESS_BAR, PROJ_KEY, SOURCE_PATH, URL
from deepsearch.cps.client.api import CpsApi
from deepsearch.documents.core.main import convert_documents
from deepsearch.documents.core.utils import create_root_dir, get_urls

app = typer.Typer(no_args_is_help=True)


@app.command(
    name="convert",
    help="Convert pdf documents using Deep Search Technology",
    no_args_is_help=True,
)
def convert(
    proj_key: str = PROJ_KEY,
    urls: str = URL,
    source_path: Path = SOURCE_PATH,
    progress_bar=PROGRESS_BAR,
):
    """
    Document conversion via Deep Search Technology.

    Inputs
    ------
    proj_key : string [REQUIRED]
    Your Deep Search CPS Project Key.

    url : string [OPTIONAL]
    For converting a document from the web, please provide its url.

    source_path : string/path [OPTIONAL]
    For converting local files, please provide absolute path to file or to directory
    containing multiple files.

    NOTE: Either url or source_path should be supplied.
    """
    api = CpsApi.default_from_env()

    input_urls = None
    if urls is not None:
        if urllib.parse.urlparse(urls).scheme in ("http", "https"):
            input_urls = [urls]
        else:
            input_urls = get_urls(Path(urls))

    result = convert_documents(
        proj_key=proj_key,
        urls=input_urls,
        source_path=source_path,
        progress_bar=progress_bar,
        api=api,
    )
    result_dir = create_root_dir()
    result.download_all(progress_bar=True, result_dir=result_dir)
    info = result.generate_report(result_dir=result_dir)
    for key in info:
        pad = 35
        typer.echo(f"{key:<{pad}}{info[key]}")
    return


if __name__ == "__main__":
    app()
