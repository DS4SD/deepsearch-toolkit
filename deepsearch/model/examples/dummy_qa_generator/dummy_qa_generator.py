from typing import List, Tuple

from deepsearch.model.base.base_annotator import BaseDSModel
from deepsearch.model.base.base_qa_generator import BaseQAGenerator
from deepsearch.model.factories.base_qa_gen_factory import BaseQAGeneratorFactory


class DummyQAFactory(BaseQAGeneratorFactory):
    def create_model(self) -> BaseDSModel:
        return DummyQAGenerator()


class DummyQAGenerator(BaseQAGenerator):
    """A dummy QA generator which answers a question with a question itself."""

    name = "DummyQAGenerator"
    supports = ["text"]

    def generate_answers(self, texts: List[Tuple[List[str], str]]) -> List[str]:
        """Just answers with the question itself.
        Args:
            texts: a list of context, question pairs.
        """
        return [question for _, question in texts]
