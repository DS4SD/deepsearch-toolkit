import typer

from .data_indices_typer import app as data_indices_app
from .elastic_data import app as elastic_app
from .kgs import app as kgs_app
from .projects import app as projects_app

app = typer.Typer(no_args_is_help=True, add_completion=False)
app.add_typer(projects_app, name="projects", help="Manage CPS projects")
app.add_typer(elastic_app, name="elastic-data", help="Manage Elastic data collections")
app.add_typer(kgs_app, name="kgs", help="Manage CPS KGs")
app.add_typer(data_indices_app, name="data-indices", help="Manage CPS data indices")


if __name__ == "__main__":
    app()
