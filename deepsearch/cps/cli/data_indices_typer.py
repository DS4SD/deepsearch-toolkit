import json
from enum import Enum
from pathlib import Path
from typing import List, Optional

import typer

from deepsearch.core.cli.utils import cli_handler
from deepsearch.core.util.cli_output import OutputEnum, OutputOption, cli_output
from deepsearch.cps.apis.public.rest import ApiException
from deepsearch.cps.cli.cli_options import (
    ATTACHMENT_KEY,
    ATTACHMENT_PATH,
    CONV_SETTINGS,
    COORDINATES_PATH,
    INDEX_ITEM_ID,
    INDEX_KEY,
    PROJ_KEY,
    SOURCE_PATH,
    URL,
)
from deepsearch.cps.client.api import CpsApi
from deepsearch.cps.client.components.data_indices import S3Coordinates
from deepsearch.cps.client.components.elastic import ElasticProjectDataCollectionSource
from deepsearch.cps.data_indices import utils
from deepsearch.documents.core.common_routines import ERROR_MSG
from deepsearch.documents.core.models import ConversionSettings

app = typer.Typer(no_args_is_help=True)


class TypeInput(str, Enum):
    document = "Document"
    db_record = "DB Record"
    generic = "Generic"
    experiment = "Experiment"


@app.command(name="list", help="List data indices in project", no_args_is_help=True)
@cli_handler()
def list(
    proj_key: str = PROJ_KEY,
    output: OutputEnum = OutputOption,
):
    api = CpsApi.from_env()

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
@cli_handler()
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
    api = CpsApi.from_env()

    try:
        api.data_indices.create(
            proj_key=proj_key,
            name=name,
            desc=desc,
            type=type.value,
        )
        typer.echo("Data Index Created.")
    except ValueError as e:
        typer.echo(f"Error occurred: {e}")
        typer.echo(ERROR_MSG)
        raise typer.Abort()
    return


@app.command(name="delete", help="Delete data index in a project", no_args_is_help=True)
@cli_handler()
def delete_data_index(
    proj_key: str = PROJ_KEY,
    index_key: str = INDEX_KEY,
):
    api = CpsApi.from_env()
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
            typer.echo(f"Error occurred: {e}")
            typer.echo(ERROR_MSG)
            raise typer.Abort()
    return


def get_urls(path: Path) -> List[str]:
    """
    Returns list of url from input file.
    """

    lines = path.read_text()
    urls = [line.strip() for line in lines.split("\n") if line.strip() != ""]
    return urls


@app.command(name="upload", help="Upload files/urls to index", no_args_is_help=True)
@cli_handler()
def upload_files(
    proj_key: str = PROJ_KEY,
    url: str = URL,
    local_file: Path = SOURCE_PATH,
    index_key: str = INDEX_KEY,
    s3_coordinates: Path = COORDINATES_PATH,
    conv_settings: Optional[str] = CONV_SETTINGS,
):
    """
    Upload pdfs, zips, or online documents to a data index in a project
    """

    api = CpsApi.from_env()

    urls = None
    if url is not None:
        p = Path(url)
        urls = get_urls(p) if p.exists() else [url]

    cos_coordinates: Optional[S3Coordinates] = None
    if s3_coordinates is not None:
        try:
            cos_coordinates = S3Coordinates.parse_file(s3_coordinates)
        except Exception as e:
            typer.echo(f"Error occurred: {e}")
            typer.echo(ERROR_MSG)
            raise typer.Abort()

    coords = ElasticProjectDataCollectionSource(proj_key=proj_key, index_key=index_key)

    if conv_settings is not None:
        try:
            final_conv_settings = ConversionSettings.parse_obj(
                json.loads(conv_settings)
            )
        except json.JSONDecodeError:
            raise ValueError(
                "Could not parse a ConversionSettings object from --conv-settings flag"
            )
    else:
        final_conv_settings = None

    utils.upload_files(
        api=api,
        coords=coords,
        url=urls,
        local_file=local_file,
        s3_coordinates=cos_coordinates,
        conv_settings=final_conv_settings,
    )

    typer.echo("Tasks have been queued successfully")


@app.command(
    name="add-attachment", help="Add attachment to a index item", no_args_is_help=True
)
@cli_handler()
def add_attachment(
    proj_key: str = PROJ_KEY,
    index_key: str = INDEX_KEY,
    index_item_id: str = INDEX_ITEM_ID,
    attachment_path: Path = ATTACHMENT_PATH,
    attachment_key: str = ATTACHMENT_KEY,
):
    """
    Add attachment to a index item
    """
    api = CpsApi.from_env()

    # get indices of the project
    indices = api.data_indices.list(proj_key)

    # get specific index to add attachment
    index = next((x for x in indices if x.source.index_key == index_key), None)

    if index is not None:
        try:
            index.add_item_attachment(
                api=api,
                index_item_id=index_item_id,
                attachment_path=attachment_path,
                attachment_key=attachment_key,
            )
            typer.echo("Attachment added successfully.")
        except ValueError as e:
            typer.echo(f"Error occurred: {e}")
            typer.echo(ERROR_MSG)
            raise typer.Abort()
        return
    else:
        typer.echo("Index key not found")
        raise typer.Abort()


if __name__ == "__main__":
    app()
