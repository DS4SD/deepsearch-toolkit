from pathlib import Path

import typer

from deepsearch.core.util.config_paths import (
    CONFIG_FILE_NAME,
    ENV_VAR_NAME,
    config_file_path,
    default_config_file_path,
)

app = typer.Typer(no_args_is_help=True)


@app.command(
    name="config-file-path",
    help=f"Get current configuration file path. This takes into account the environment variable {ENV_VAR_NAME!r} and the presence of a file named {CONFIG_FILE_NAME!r} unless '--default' is passed",
)
def get_config_file_path(default: bool = typer.Option(default=False)):
    if default:
        typer.echo(default_config_file_path())
    else:
        typer.echo(config_file_path().absolute())


@app.callback()
def callback():
    pass


if __name__ == "__main__":
    app()
