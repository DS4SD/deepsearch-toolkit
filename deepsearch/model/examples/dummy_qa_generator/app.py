from deepsearch.model.examples.dummy_qa_generator.dummy_qa_generator import (
    DummyQAFactory,
)
from deepsearch.model.server.deepsearch_annotator_app import ModelApp


def run():
    app = ModelApp()
    app.register_model_factory(DummyQAFactory())
    app.run()


if __name__ == "__main__":
    run()
