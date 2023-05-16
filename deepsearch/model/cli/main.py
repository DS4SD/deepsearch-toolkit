import typer

from ..model_download.model_download_typer import model_download_app

app = typer.Typer(no_args_is_help=True, add_completion=False)
app.add_typer(
    model_download_app, name="library", help="Artifact library related commands"
)

if __name__ == "__main__":
    app()
