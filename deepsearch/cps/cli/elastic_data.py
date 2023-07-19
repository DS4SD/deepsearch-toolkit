import typer

from deepsearch.core.cli.utils import cli_handler
from deepsearch.core.util.cli_output import OutputEnum, OutputOption, cli_output
from deepsearch.cps.client.api import CpsApi
from deepsearch.cps.client.components.elastic import ElasticDataCollectionSource

app = typer.Typer(no_args_is_help=True)


@app.command(name="list", help="List Elastic Data Collections")
@cli_handler()
def list(
    domain: str = typer.Option("all"),
    output: OutputEnum = OutputOption,
):
    api = CpsApi.from_env()
    collections = api.elastic.list(domain=domain)

    results = [
        {
            "name": c.name,
            "instance": ElasticDataCollectionSource.parse_obj(c.source).elastic_id,
            "index": c.source.index_key,
            "domains": c.metadata.domain,
            "documents": c.documents,
            "created": c.metadata.created,
        }
        for c in collections
    ]
    # TODO: fix JSON serialize of datetime
    cli_output(results, output, headers="keys")


if __name__ == "__main__":
    app()
