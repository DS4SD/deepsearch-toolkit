from abc import ABC, abstractmethod
from typing import List


class BaseDSModel(ABC):

    version: str = ""
    url: str = ""
    author: str = ""
    description: str = ""
    expected_compute_time: float = 1.0

    @property
    @abstractmethod
    def kind(self) -> str:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def supports(self) -> List[str]:
        pass

    def get_definition_spec(self) -> dict:
        spec = {  # TODO refactor with pydantic
            "metadata": {
                "name": self.name,
                "version": self.version,
                "url": self.url,
                "author": self.author,
                "description": self.description,
                "expected_compute_time": self.expected_compute_time,
                "supported_object_types": self.supports,
            },
        }
        return spec
