import json
import shutil
import tempfile

import typer

from .model_download import (
    check_artifact_index,
    download_file,
    get_artifacts_in_store,
    get_model_meta,
    infer_target_directory,
    process_downloaded_file,
    infer_cache_directory,
    get_artifacts_in_cache,
    default_cache_location
)

model_download_app = typer.Typer(no_args_is_help=True, add_completion=False)


@model_download_app.command()
def download(
    model: str = typer.Option(None, "--model", "-m"),
    list_models: bool = typer.Option(False, "--list", "-l"),
):
    artifact_store = infer_target_directory()

    if list_models:
        artifacts = get_artifacts_in_store(artifact_store)
        for artifact in artifacts:
            typer.echo(artifact["folder_name"])
    elif model is not None:
        model_meta = get_model_meta(artifact_store, model)
        typer.echo(json.dumps(model_meta, indent=4, separators=(",", ": ")))
        typer.echo(f"Downloading {model}")
        temp_file = tempfile.TemporaryDirectory()
        downloaded_file_path = download_file(
            model_meta, temp_file
        )
        typer.echo(f"Extracting {model} to {default_cache_location}")
        process_downloaded_file(downloaded_file_path, default_cache_location, model, artifact_store)


@model_download_app.command()
def manage(
    list_models: bool = typer.Option(False, "--list", "-l"),
    del_model: str = typer.Option(None, "--delete", "-d")
):
    cache_dir = infer_cache_directory()
    artifact_list = get_artifacts_in_cache(cache_dir)

    typer.echo(f"Infered artifact directory {cache_dir}")

    if list_models:
        for artifact in artifact_list:
            typer.echo(artifact["folder_name"])

    if del_model is not None:
        target_artifacts = []
        for artifact in artifact_list:
            if "folder_name" in artifact and artifact["folder_name"] == del_model:
                target_artifacts.append(artifact)

        for artifact in target_artifacts:
            shutil.rmtree(artifact["full_path"])
            typer.echo(f"Succefully deleted {artifact['folder_name']}")


if __name__ == "__main__":
    model_download_app()
