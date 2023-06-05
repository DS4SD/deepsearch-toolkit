from deepsearch.artifacts.cli.main import app as artifacts_app
from deepsearch.core.cli.main import app
from deepsearch.core.cli.plugins import get_cli_groups
from deepsearch.cps.cli.main import app as cps_app
from deepsearch.documents.cli.main import app as documents_app
from deepsearch.query.cli.main import app as query_app

app.add_typer(cps_app, name="cps", help="Interact with DeepSearch CPS component")
app.add_typer(query_app, name="query", help="Interact with DeepSearch Query component")
app.add_typer(
    documents_app,
    name="documents",
    help="Interact with DeepSearch Document Conversion component",
)
app.add_typer(artifacts_app, name="artifacts", help="Manage artifacts")

for group in get_cli_groups():
    app.add_typer(group)


if __name__ == "__main__":
    app()
