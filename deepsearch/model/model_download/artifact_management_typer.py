import json
import shutil
import tempfile

import typer

from deepsearch.model.model_download.artifact_manager import ArtifactManager

model_download_app = typer.Typer(no_args_is_help=True, add_completion=False)
artifact_manager = ArtifactManager()

@model_download_app.command()
def download(
    model: str = typer.Option(None, "--model", "-m"),
    list_models: bool = typer.Option(False, "--list", "-l"),
):

    if list_models:
        artifacts = artifact_manager.get_artifact_store_list()
        for artifact in artifacts:
            typer.echo(artifact["folder_name"])
    elif model is not None:
        artifact_manager.download_artifact_to_cache(model, with_progess_bar=True)


@model_download_app.command()
def manage(
    list_models: bool = typer.Option(False, "--list", "-l"),
    del_model: str = typer.Option(None, "--delete", "-d"),
):
    if list_models:
        for artifact in artifact_manager.get_artifact_cache_list():
            typer.echo(artifact["folder_name"])

    if del_model is not None:
        target_artifacts = []
        for artifact in artifact_manager.get_artifact_cache_list():
            if "folder_name" in artifact and artifact["folder_name"] == del_model:
                target_artifacts.append(artifact)

        for artifact in target_artifacts:
            artifact_manager.delete_artifact_from_cache(artifact)
            typer.echo(f"Succefully deleted {artifact}")


if __name__ == "__main__":
    model_download_app()
