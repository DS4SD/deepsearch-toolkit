from deepsearch.model.examples.simple_geo_nlp_annotator.model import (  # type: ignore
    SimpleGeoNLPAnnotator,
)
from deepsearch.model.server.model_app import ModelApp


def run():
    app = ModelApp()
    app.register_model(SimpleGeoNLPAnnotator())
    app.run()


if __name__ == "__main__":
    run()
