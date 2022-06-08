"""
A toy example plugin for the DeepSearch CLI.
"""

import typer

# Get the hookimpl that you will use to hook into the DeepSearch CLI
from deepsearch.core.cli.plugins import deepsearch_cli_hookimpl


# Implement the function to return a group.
# We're defining an 'example' group,
# using the Typer library.
# It will be available as 'deepsearch example'.
# Note: the name of the function is important!
@deepsearch_cli_hookimpl
def deepsearch_cli_add_group() -> typer.Typer:
    app = typer.Typer(name="example")

    # Define one or more commands.
    @app.command("test")
    def test(name: str):
        typer.echo(f"Hello, {name}!")

    return app
