import typer

from deepsearch.model.model_download.artifact_management_typer import artifact_download_app

app = typer.Typer(no_args_is_help=True, add_completion=False)
app.add_typer(
    artifact_download_app, name="library", help="Artifact library related commands"
)

if __name__ == "__main__":
    app()
