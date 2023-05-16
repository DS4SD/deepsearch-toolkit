import json
import shutil

import typer

from .model_download import (
    check_artifact_index,
    download_file,
    get_artifacts_in_store,
    get_model_meta,
    infer_target_directory,
    process_downloaded_file,
    default_cache_location,
    default_download_directory
)

model_download_app = typer.Typer(no_args_is_help=True, add_completion=False)


@model_download_app.command()
def download(
    model: str = typer.Option(None, "--model", "-m"),
    list_models: bool = typer.Option(False, "--list", "-l"),
):
    artifact_store = infer_target_directory()
    index_info = check_artifact_index(artifact_store)
    typer.echo("Artifact store details:")
    typer.echo(f"{json.dumps(index_info, indent=4, separators=(',', ': '))}\n")

    if list_models:
        artifacts = get_artifacts_in_store(artifact_store)
        for artifact in artifacts:
            typer.echo(artifact[1])
    elif model is not None:
        model_meta = get_model_meta(artifact_store, model)
        typer.echo(json.dumps(model_meta, indent=4, separators=(",", ": ")))
        typer.echo(f"Downloading {model}")
        downloaded_file_path = download_file(
            model_meta, default_download_directory
        )
        typer.echo(f"Extracting {model} to {default_cache_location}")
        process_downloaded_file(downloaded_file_path, default_cache_location, model)
        typer.echo(f"Cleaning up {default_download_directory}")
        shutil.rmtree(default_download_directory)


@model_download_app.command()
def manage():
    typer.echo("Executing 'manage' command.")


if __name__ == "__main__":
    model_download_app()
