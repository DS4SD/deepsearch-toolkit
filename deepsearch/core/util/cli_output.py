import json
import typing
from enum import Enum

import tabulate
import typer


class OutputEnum(str, Enum):
    table = "table"
    json = "json"


OutputOption = typer.Option(OutputEnum.table, "--output", "-o", help="Output format")


def cli_output(
    results: typing.Union[typing.Iterable, typing.Mapping], output: OutputEnum, **kwargs
):
    if output == OutputEnum.table:
        typer.echo(tabulate.tabulate(results, **kwargs))
    else:
        typer.echo(json.dumps(results))
