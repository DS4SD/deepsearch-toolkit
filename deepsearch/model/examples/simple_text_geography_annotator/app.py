from deepsearch.model.examples.simple_text_geography_annotator.simple_text_geography_annotator import (  # type: ignore
    SimpleTextGeographyAnnotator,
)
from deepsearch.model.server.deepsearch_annotator_app import DeepSearchAnnotatorApp


def run():
    app = DeepSearchAnnotatorApp()
    app.register_annotator(SimpleTextGeographyAnnotator())
    app.run()


if __name__ == "__main__":
    run()
