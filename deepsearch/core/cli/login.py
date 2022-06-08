from pathlib import Path

import typer

from deepsearch.core.client import DeepSearchConfig, DeepSearchKeyAuth
from deepsearch.core.util.config_paths import config_file_path

app = typer.Typer(invoke_without_command=True)


@app.callback(help="Save authentication configuration")
def save_auth(
    *,
    host: str = typer.Option("https://cps.foc-deepsearch.zurich.ibm.com", prompt=True),
    email: str = typer.Option(..., prompt=True),
    api_key: str = typer.Option(..., prompt=True, hide_input=True),
    verify_ssl: bool = typer.Option(True, prompt=True),
    output: str = typer.Option(
        str(config_file_path()),
        help="Where to save configuration to. Use '-' to print to stdout",
    ),
):

    config = DeepSearchConfig(
        host=host,
        auth=DeepSearchKeyAuth(username=email, api_key=api_key),
        verify_ssl=verify_ssl,
    )

    contents = config.json(indent=2)

    if output == "-":
        typer.echo(contents)
        return

    output_file = Path(output)

    if not output_file.is_file():
        output_file.parent.mkdir(parents=True, exist_ok=True)

    output_file.write_text(contents, encoding="utf-8")

    typer.secho(f"File {output_file} updated!", fg=typer.colors.GREEN)


if __name__ == "__main__":
    app()
