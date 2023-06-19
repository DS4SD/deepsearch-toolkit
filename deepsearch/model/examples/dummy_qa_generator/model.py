from typing import List, Tuple

from deepsearch.model.base.types import Kind
from deepsearch.model.kinds.qagen.model import BaseQAGenerator
from deepsearch.model.kinds.qagen.types import GenerateAnswersOutput, QAGenConfig


class DummyQAGenerator(BaseQAGenerator):
    """A dummy QA generator which answers a question with the question itself."""

    _config = QAGenConfig(
        kind=Kind.QAGenModel,
        name="DummyQAGenerator",
        version="0.1.0",
    )

    def get_qagen_config(self) -> QAGenConfig:
        return self._config

    def generate_answers(
        self, texts: List[Tuple[List[str], str]]
    ) -> GenerateAnswersOutput:
        """Just answers with the question itself.
        Args:
            texts: a list of context, question pairs.
        """
        return [question for _, question in texts]
