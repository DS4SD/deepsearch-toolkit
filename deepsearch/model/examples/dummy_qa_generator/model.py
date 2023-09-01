from typing import Any, Dict, List, Tuple

from deepsearch.model.base.types import Kind
from deepsearch.model.kinds.qagen.model import BaseQAGenerator
from deepsearch.model.kinds.qagen.types import (
    GenerateAnswersOutEntry,
    GenerateAnswersOutput,
    QAGenConfig,
)


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
        self,
        texts: List[Tuple[List[Dict], str]],
        extras: Dict[str, Any],
    ) -> GenerateAnswersOutput:
        """Just answers with the question itself.
        Args:
            texts: a list of context, question pairs.
            extras: any extras to pass.
        """
        return [
            GenerateAnswersOutEntry(
                answer=question,
                metadata={"foo": "bar"},
            )
            for _, question in texts
        ]
