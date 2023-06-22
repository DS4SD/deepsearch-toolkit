from deepsearch.model.examples.simple_geo_nlp_annotator.model import (  # type: ignore
    SimpleGeoNLPAnnotator,
)
from deepsearch.model.server.config import Settings
from deepsearch.model.server.model_app import ModelApp


def run():
    settings = Settings(api_key="example123")
    app = ModelApp(settings)
    app.register_model(SimpleGeoNLPAnnotator())
    app.run()


if __name__ == "__main__":
    run()
