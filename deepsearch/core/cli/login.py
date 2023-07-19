import typer

from deepsearch.core.cli.profile_utils import MSG_LOGIN_DEPRECATION

app = typer.Typer(invoke_without_command=True)


@app.callback(help=MSG_LOGIN_DEPRECATION)
def save_auth(
    *,
    host: str = typer.Option(""),
    email: str = typer.Option(""),
    api_key: str = typer.Option("", hide_input=True),
    verify_ssl: bool = typer.Option(True),
    output: str = typer.Option(""),
):
    print(MSG_LOGIN_DEPRECATION)
    raise typer.Exit(code=1)
