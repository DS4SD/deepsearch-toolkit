import logging

logger = logging.getLogger("root.core")


import typer

import deepsearch as ds

from .config import app as config_app
from .login import app as login_app

app = typer.Typer(no_args_is_help=True, add_completion=False)
app.add_typer(config_app, name="config", help="Manage CLI config files")
logger.info("Config module initialized")
app.add_typer(login_app, name="login", help="Login to DeepSearch platform")
logger.info("Login module initialized")
logger.info("Core module finished initialization")


@app.command(name="version", help=f"Print the client and server version")
def get_version():
    logger.info("Getting DeepSearch version")
    versions = ds.version()
    typer.echo(f"Client: {versions.client}")
    typer.echo(f"Server: {versions.server}")


if __name__ == "__main__":
    app()
