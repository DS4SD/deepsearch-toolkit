from abc import ABC, abstractmethod
from typing import Any, Optional

# from deepsearch.model.base.base_annotator import BaseAnnotator


class BaseTextEntityAnnotator:
    @abstractmethod
    def key(self) -> str:
        pass

    @abstractmethod
    def description(self) -> str:
        pass

    def initialize(self):
        return

    @abstractmethod
    def annotate_entities_text(self, text: str) -> list:
        pass
