from abc import abstractmethod
from typing import List, Tuple

from deepsearch.model.base.base_annotator import BaseDSModel


class BaseQAGenerator(BaseDSModel):

    kind = "QAGenerator"

    @abstractmethod
    def generate_answers(self, texts: List[Tuple[List[str], str]]) -> List[str]:
        """Generate a list of answer from a batch of (context, questions) pairs.
        Args:
            texts: a list of context, question pairs.
        """
        pass
