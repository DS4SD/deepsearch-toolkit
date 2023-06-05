from deepsearch.model.examples.minimal_annotator.minimal_annotator import (
    MinimalAnnotator,
)
from deepsearch.model.server.deepsearch_annotator_app import DeepSearchAnnotatorApp


def run():
    app = DeepSearchAnnotatorApp()
    app.register_annotator(MinimalAnnotator())
    app.run()


if __name__ == "__main__":
    run()
