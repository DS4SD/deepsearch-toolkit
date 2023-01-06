import typer

from deepsearch.core.util.cli_output import OutputEnum, OutputOption, cli_output
from deepsearch.cps.client.api import CpsApi
from deepsearch.cps.client.components.projects import RoleEnum

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


@app.command(name="assign", help="Assign a user to a project")
def assign_user(
    proj_key: str,
    username: str,
    role: RoleEnum = typer.Argument(RoleEnum.viewer),
):
    api = CpsApi.default_from_env()
    project = api.projects.get(key=proj_key)
    if project is not None:
        api.projects.assign_user(
            project=project,
            username=username,
            role=role,
        )
    else:
        print("Project not found")
        raise typer.Exit(code=1)


@app.command(name="remove", help="Remove a project")
def remove(
    proj_key: str,
):
    api = CpsApi.default_from_env()
    project = api.projects.get(key=proj_key)
    if project is not None:
        api.projects.remove(project=project)
    else:
        print("Project not found")
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
