import typer

from deepsearch.core.util.cli_output import OutputEnum, OutputOption, cli_output
from deepsearch.cps.client.api import CpsApi

app = typer.Typer(no_args_is_help=True)


@app.command(name="list", help="List projects")
def list(
    output: OutputEnum = OutputOption,
):
    api = CpsApi.default_from_env()
    projects = api.projects.list()
    results = [{"key": proj.key, "name": proj.name} for proj in projects]

    cli_output(results, output, headers="keys")


@app.command(name="create", help="Create a project")
def create(
    proj_name: str,
    output: OutputEnum = OutputOption,
):
    api = CpsApi.default_from_env()
    proj = api.projects.create(name=proj_name)
    results = [{"key": proj.key, "name": proj.name}]

    cli_output(results, output, headers="keys")


if __name__ == "__main__":
    app()
