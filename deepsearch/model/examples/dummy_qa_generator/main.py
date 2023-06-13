from deepsearch.model.examples.dummy_qa_generator.model import DummyQAGenerator
from deepsearch.model.server.model_app import ModelApp


def run():
    app = ModelApp()
    app.register_model(DummyQAGenerator())
    app.run()


if __name__ == "__main__":
    run()
