from typing import Dict, List, Optional

import typer

from deepsearch.core.cli.utils import cli_handler
from deepsearch.core.util.cli_output import OutputEnum, OutputOption, cli_output
from deepsearch.cps.cli.cli_options import PROJ_KEY, WAIT
from deepsearch.cps.client.api import CpsApi

app = typer.Typer(no_args_is_help=True)

KG_KEY = typer.Option(..., "--kg-key", "-k", help="Knowledge Graph")
FLAVOUR = typer.Option(
    ...,
    "--flavour",
    help="Name of the Flavour/Capacity of the snapshot. Use 'list-flavours' to get a list",
)


@app.command(name="list", help="List KGs")
@cli_handler()
def list_knowledge_graphs(
    proj_key: str = PROJ_KEY,
    output: OutputEnum = OutputOption,
):
    api = CpsApi.from_env()
    kgs = api.knowledge_graphs.list(project=proj_key)
    results = [{"key": kg.key, "name": kg.name} for kg in kgs]
    # TODO: augment with topology details
    cli_output(results, output, headers="keys")


@app.command(name="list-flavours", help="List KG flavours for a project")
@cli_handler()
def list_flavours(
    proj_key: str = PROJ_KEY,
    output: OutputEnum = OutputOption,
):
    api = CpsApi.from_env()

    flavours = api.knowledge_graphs.list_flavours(proj_key)

    results = [
        {"name": f.name, "backend": f.backend, "description": f.description}
        for f in flavours
    ]

    cli_output(results, output, headers="keys")


@app.command(name="save-snapshot", help="Save a snapshot from an assembled Data Set")
@cli_handler()
def save_snapshot_of_data_flow(
    proj_key: str = PROJ_KEY,
    kg_key: str = KG_KEY,
    wait: bool = WAIT,
    flavour_names: List[str] = FLAVOUR,
    load_after_assembled: bool = typer.Option(
        True,
        "--load-after-assembled",
        is_flag=True,
    ),
    snapshot_name: Optional[str] = typer.Option(None, "--snapshot-name"),
):

    if len(flavour_names) == 0:
        raise typer.BadParameter(
            "At least one flavour is required", param_hint="--flavour-name"
        )

    api = CpsApi.from_env()

    all_flavours = api.knowledge_graphs.list_flavours(proj_key)

    flavours: Dict[str, str] = {}

    for name in flavour_names:
        flavour = next((f for f in all_flavours if f.name == name), None)

        if flavour is None:
            raise typer.BadParameter(
                f"Unknown flavour {name!r}", param_hint="--flavour-name"
            )

        if flavour.backend in flavours:
            raise typer.BadParameter(
                f"A flavour for backend {flavour.backend!r} has already been set: {flavours[flavour.backend]!r}",
                param_hint="--flavour-name",
            )

        flavours[flavour.backend] = flavour.name

    kg = api.knowledge_graphs.get(proj_key, kg_key)

    if kg is None:
        raise typer.BadParameter(
            f"Unknown Knowledge Graph {kg_key!r} in project {proj_key!r}",
            param_hint="-k",
        )

    typer.echo(f"Going to create a snapshot from the KG {kg.name}...")

    task = kg.save_snapshot_of_data_flow(
        flavours,
        load_after_assembled=load_after_assembled,
        name=snapshot_name,
    )

    if wait:
        typer.echo(f"Waiting for snapshot task {task.task_id!r}...")
        api.tasks.wait_for(proj_key, task.task_id)
    else:
        typer.echo(f"A snapshot is being taken, see task {task.task_id!r}")


@app.command(name="download", help="Download KG")
@cli_handler()
def download_knowledge_graph(
    proj_key: str = PROJ_KEY,
    kg_key: str = KG_KEY,
    output: OutputEnum = OutputOption,
):
    api = CpsApi.from_env()
    kg = api.knowledge_graphs.get(project=proj_key, key=kg_key)
    if kg is None:
        raise typer.BadParameter(
            f"Unknown Knowledge Graph {kg_key!r} in project {proj_key!r}"
        )
    url = kg.download()

    results = [{"url": url}]
    # TODO: augment with topology details
    cli_output(results, output, headers="keys")


if __name__ == "__main__":
    app()
