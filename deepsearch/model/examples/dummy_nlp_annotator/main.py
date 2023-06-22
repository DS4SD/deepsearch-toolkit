from deepsearch.model.examples.dummy_nlp_annotator.model import DummyNLPAnnotator
from deepsearch.model.server.config import Settings
from deepsearch.model.server.model_app import ModelApp


def run():
    settings = Settings(api_key="example123")
    app = ModelApp(settings)
    app.register_model(DummyNLPAnnotator())
    app.run()


if __name__ == "__main__":
    run()
