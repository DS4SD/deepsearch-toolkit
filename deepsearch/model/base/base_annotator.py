from abc import ABC, abstractmethod
from typing import List


class BaseAnnotator(ABC):

    version: str = "undefined"
    url: str = "undefined"
    author: str = "undefined"
    description: str = "undefined"
    expected_compute_time: float = 1.0
    labels: dict = {}

    @property
    @abstractmethod
    def kind(self) -> str:
        return self.kind

    @property
    @abstractmethod
    def name(self) -> str:
        return self.name

    @property
    @abstractmethod
    def supports(self) -> List[str]:
        return self.supports

    def get_annotator_info(self) -> dict:
        annotator_info = {
            "definitions": {
                "apiVersion": "v1",
                "kind": self.kind,
                "spec": {
                    "metadata": {
                        "name": self.name,
                        "version": self.version,
                        "url": self.url,
                        "author": self.author,
                        "description": self.description,
                        "expected_compute_time": self.expected_compute_time,
                        "supported_object_types": self.supports,
                    },
                    "definition": self.labels,
                },
            }
        }

        return annotator_info
