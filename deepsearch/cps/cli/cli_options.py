import typer

PROJ_KEY = typer.Option(
    ...,
    "--proj-key",
    "-p",
    help="Provide project key",
)

WAIT = typer.Option(
    False,
    "--wait",
    "-w",
    is_flag=True,
    help="Wait for the operation to finish",
)

URL = typer.Option(
    None,
    "--url",
    "-u",
    help="""Provide single url or
            absolute path to file containing 
            multiple urls separated by empty lines.""",
)

SOURCE_PATH = typer.Option(
    None,
    "--input-file",
    "-i",
    help="""Provide absolute path to local file or directory
    containing pdf documents, zip files, or both.""",
)

INDEX_KEY = typer.Option(..., "-x", "--index-key", help="index_key of data index")

PROGRESS_BAR = typer.Option(
    True,
    "--progress-bar",
    "-pbar",
    is_flag=True,
    help="Show progress bar",
)

GET_REPORT = typer.Option(
    False,
    "--report",
    "-r",
    is_flag=True,
    help="Generate report after document conversion",
)

TASK_IDS = typer.Option(
    None,
    "--task-ids",
    "-t",
    help="""Provide path to file containing task ids generated during document conversion.""",
)
