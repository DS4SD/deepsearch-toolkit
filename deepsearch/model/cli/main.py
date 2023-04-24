import importlib.util
import os

import typer
import uvicorn

from deepsearch.model.examples.simple_text_geography_annotator.simple_text_geography_annotator import (  # type: ignore
    SimpleTextGeographyAnnotator,
)
from deepsearch.model.server.deepsearch_annotator_app import DeepSearchAnnotatorApp

app = typer.Typer(no_args_is_help=True)


@app.command(name="serve", help="Serve an annotator instance")
def serve(
    port: int = typer.Option(8000, "-p", "--port", help="The port to listen on"),
    annotator: str = typer.Option(None, "-a", "--annotator", help="Not implemented"),
):
    # Load the Annotator App
    deepsearch_annotator_app = DeepSearchAnnotatorApp()

    # register annotators
    deepsearch_annotator_app.register_annotator(SimpleTextGeographyAnnotator())

    # Run
    uvicorn.run(deepsearch_annotator_app.app, host="0.0.0.0", port=port)


if __name__ == "__main__":
    app()
