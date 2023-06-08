from deepsearch.model.examples.simple_text_geography_annotator.simple_text_geography_annotator import (  # type: ignore
    SimpleTextGeographyFactory,
)
from deepsearch.model.server.deepsearch_annotator_app import ModelApp


def run():
    app = ModelApp()
    app.register_model_factory(factory=SimpleTextGeographyFactory())
    app.run()


if __name__ == "__main__":
    run()
