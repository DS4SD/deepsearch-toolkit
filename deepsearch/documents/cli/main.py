import urllib

import urllib3

from deepsearch.core.cli.utils import cli_handler

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from pathlib import Path

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
from deepsearch.documents.core.utils import create_root_dir, read_lines, write_taskids

app = typer.Typer(no_args_is_help=True)


@app.command(
    name="convert",
    help="Convert pdf documents using Deep Search Technology",
    no_args_is_help=True,
)
@cli_handler()
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
    api = CpsApi.from_env()

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
    write_taskids(result_dir=result_dir, list_to_write=result.task_ids)
    result.download_all(progress_bar=True, result_dir=result_dir)
    typer.echo(
        f"""
        Converted documents and additional metadata are saved here:
        {result_dir.absolute()}
        """
    )

    if get_report:
        info = result.generate_report(result_dir=result_dir, progress_bar=True)
        for key in info:
            pad = 35
            typer.echo(f"{key:<{pad}}{info[key]}")
    else:
        typer.echo(
            f"""
        Reports can be generated after document conversion:
        deepsearch documents get-report -p {proj_key} -t {result_dir.joinpath("task_ids.txt").absolute()}

        To automatically generate report after document conversion use the "--report" flag:
        deepsearch documents convert -p PROJ_KEY -i INPUT_FILES --report
        """
        )

    return


@app.command(
    name="get-report",
    help="Generate report of document conversion",
    no_args_is_help=True,
)
@cli_handler()
def get_report(proj_key: str = PROJ_KEY, source_taskids: Path = TASK_IDS):
    """
    Generate report of document conversion.

    Inputs
    ------
    source_taskids : path
        path to text file containing text ids generated during document conversion
    """
    api = CpsApi.from_env()
    task_ids = read_lines(source_taskids)
    result_dir = Path(source_taskids).parent.expanduser().resolve()
    info = get_multiple_reports(
        api=api,
        cps_proj_key=proj_key,
        task_ids=task_ids,
        source_files=None,
        result_dir=result_dir,
        progress_bar=True,
    )
    for key in info:
        pad = 35
        typer.echo(f"{key:<{pad}}{info[key]}")
    typer.echo(
        f"""
        Document conversion report is saved here:
        {result_dir.absolute()}
        """
    )
    return


if __name__ == "__main__":
    app()
