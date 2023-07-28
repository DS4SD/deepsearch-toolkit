from deepsearch.model.examples.dummy_nlp_annotator.model import DummyNLPAnnotator
from deepsearch.model.server.config import ModelAppSettings
from deepsearch.model.server.model_app import ModelApp


def run():
    app = ModelApp(settings=ModelAppSettings(api_key="example123"))
    app.register_model(DummyNLPAnnotator())
    app.run()


if __name__ == "__main__":
    run()
