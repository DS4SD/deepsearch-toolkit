import typer

import deepsearch as ds
from deepsearch.core.cli.profile_utils import MSG_LOGIN_DEPRECATION

from .login import app as login_app
from .profile import app as profile_app

app = typer.Typer(
    no_args_is_help=True,
    add_completion=False,
    pretty_exceptions_enable=False,
)
app.add_typer(profile_app, name="profile", help="Manage profile configuration")
app.add_typer(login_app, name="login", help=MSG_LOGIN_DEPRECATION)


@app.command(name="version", help=f"Print the client and server version")
def get_version():
    versions = ds.version()
    typer.echo(f"Client: {versions.client}")
    typer.echo(f"Server: {versions.server}")


if __name__ == "__main__":
    app()
