import json
import shutil
import tempfile

import typer

from deepsearch.model.model_download.artifact_manager import ArtifactManager

artifact_download_app = typer.Typer(no_args_is_help=True, add_completion=False)
artifact_manager = ArtifactManager()


@artifact_download_app.command()
def download(
    artifact_name: str = typer.Option(None, "--artifact", "-a"),
    list_artifacts: bool = typer.Option(False, "--list", "-l"),
):

    if list_artifacts:
        artifacts = artifact_manager.get_index_artifact_list()
        for artifact in artifacts:
            typer.echo(artifact["folder_name"])
    elif artifact_name is not None:
        artifact_manager.download_artifact_to_cache(
            artifact_name, with_progess_bar=True
        )


@artifact_download_app.command()
def manage(
    list_artifacts: bool = typer.Option(False, "--list", "-l"),
    del_artifact: str = typer.Option(None, "--delete", "-d"),
):
    if list_artifacts:
        for artifact in artifact_manager.get_artifact_cache_list():
            typer.echo(artifact["folder_name"])

    if del_artifact is not None:
        target_artifacts = []
        for artifact in artifact_manager.get_artifact_cache_list():
            if "folder_name" in artifact and artifact["folder_name"] == del_artifact:
                target_artifacts.append(artifact)

        for artifact in target_artifacts:
            artifact_manager.delete_artifact_from_cache(artifact)
            typer.echo(f"Succefully deleted {artifact}")


if __name__ == "__main__":
    artifact_download_app()
