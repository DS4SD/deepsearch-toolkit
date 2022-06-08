from enum import Enum
from pathlib import Path

import typer

from deepsearch.core.util.cli_output import OutputEnum, OutputOption, cli_output
from deepsearch.cps.apis.public.rest import ApiException
from deepsearch.cps.cli.cli_options import INDEX_KEY, LOCAL_FILE, PROJ_KEY, URL
from deepsearch.cps.client.api import CpsApi
from deepsearch.cps.client.components.elastic import ElasticProjectDataCollectionSource
from deepsearch.cps.data_indices import utils
from deepsearch.documents.core.common_routines import (
    ERROR_MSG,
    WELCOME,
    progressbar_padding,
    success_message,
)

app = typer.Typer(no_args_is_help=True)


class TypeInput(str, Enum):
    document = "Document"
    db_record = "DB Record"
    generic = "Generic"
    experiment = "Experiment"


@app.command(name="list", help="List data indices in project", no_args_is_help=True)
def list(
    proj_key: str = PROJ_KEY,
    output: OutputEnum = OutputOption,
):
    api = CpsApi.default_from_env()

    try:
        indices = api.data_indices.list(proj_key=proj_key)
        results = [
            {
                "Index key": index.source.index_key,
                "Index name": index.name,
                "Documents": index.documents,
                "Type": index.type,
                "Schema": index.schema_key,
            }
            for index in indices
        ]
    except ValueError as e:
        print(f"Error occurred: {e}")

    cli_output(results, output, headers="keys")
    return


@app.command(name="create", help="Create data index in project", no_args_is_help=True)
def create(
    proj_key: str = PROJ_KEY,
    name: str = typer.Option(..., "-n", "--name", help="Name of data index"),
    desc: str = typer.Option("", "-d", "-desc", help="Describe your data index"),
    type: TypeInput = typer.Option(
        TypeInput.document.value,
        "--type",
        case_sensitive=False,
        help="Type of Data Index",
    ),
):
    api = CpsApi.default_from_env()

    try:
        api.data_indices.create(
            proj_key=proj_key,
            name=name,
            desc=desc,
            type=type.value,
        )
        typer.echo("Data Index Created.")
    except ValueError as e:
        typer.echo(f"Uh Oh! {e}")
        typer.echo(ERROR_MSG)
        raise typer.Abort()
    return


@app.command(name="delete", help="Delete data index in a project", no_args_is_help=True)
def delete_data_index(
    proj_key: str = PROJ_KEY,
    index_key: str = INDEX_KEY,
):
    api = CpsApi.default_from_env()
    delete = typer.confirm("Are you sure you want to delete this data index?")

    coords = ElasticProjectDataCollectionSource(proj_key=proj_key, index_key=index_key)

    if not delete:
        typer.echo("Cancelling delete operation.")
        raise typer.Abort()
    elif delete:
        # get confirmation token
        try:
            api.data_indices.delete(coords)
            typer.echo("Deleted!")
        except ApiException as e:
            typer.echo(f"Uh Oh! {e}")
            typer.echo(ERROR_MSG)
            raise typer.Abort()
    return


@app.command(name="upload", help="Upload files/urls to index", no_args_is_help=True)
def upload_files(
    proj_key: str = PROJ_KEY,
    url: str = URL,
    local_file: Path = LOCAL_FILE,
    index_key: str = INDEX_KEY,
):
    """
    Upload pdfs, zips, or online documents to a data index in a project
    """
    coords = ElasticProjectDataCollectionSource(proj_key=proj_key, index_key=index_key)
    utils.upload_files(coords=coords, url=url, local_file=local_file)
    return


if __name__ == "__main__":
    app()
