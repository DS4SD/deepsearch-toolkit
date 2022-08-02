import urllib
from pathlib import Path

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import typer

from deepsearch.cps.cli.cli_options import (
    GET_REPORT,
    PROGRESS_BAR,
    PROJ_KEY,
    SOURCE_PATH,
    TASK_IDS,
    URL,
)
from deepsearch.cps.client.api import CpsApi
from deepsearch.documents.core.create_report import get_multiple_reports
from deepsearch.documents.core.main import convert_documents
from deepsearch.documents.core.utils import create_root_dir, read_lines, write_lines

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
    progress_bar: bool = PROGRESS_BAR,
    get_report: bool = GET_REPORT,
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
            input_urls = read_lines(Path(urls))

    result = convert_documents(
        proj_key=proj_key,
        urls=input_urls,
        source_path=source_path,
        progress_bar=progress_bar,
        api=api,
    )
    result_dir = create_root_dir()
    # save task ids
    write_lines(result_dir=result_dir, list_to_write=result.task_ids)
    result.download_all(progress_bar=True, result_dir=result_dir)

    if get_report:
        info = result.generate_report(result_dir=result_dir)
        for key in info:
            pad = 35
            typer.echo(f"{key:<{pad}}{info[key]}")
    else:
        typer.echo(
            """
        To automatically generate report after document conversion use "-report" flag:
        deepsearch documents convert -p PROJ_KEY -i INPUT_FILES -report 

        Reports can also be generated after document conversion:
        deepsearch documents report -p PROJ_KEY -t TASK_IDS
        """
        )

    return


@app.command(
    name="report",
    help="Generate report of document conversion",
    no_args_is_help=True,
)
def report(proj_key: str = PROJ_KEY, source_taskids: Path = TASK_IDS):
    """
    Generate report of document conversion.

    Inputs
    ------
    source_taskids : path
        path to text file containing text ids generated during document conversion
    """
    api = CpsApi.default_from_env()
    task_ids = read_lines(source_taskids)
    info = get_multiple_reports(
        api=api,
        cps_proj_key=proj_key,
        task_ids=task_ids,
        source_files=None,
        result_dir=Path("./result2/").parent.expanduser().resolve(),
        progress_bar=True,
    )
    for key in info:
        pad = 35
        typer.echo(f"{key:<{pad}}{info[key]}")


if __name__ == "__main__":
    app()
