from abc import ABC, abstractmethod

from deepsearch.model.base.types import BaseModelConfig


class BaseDSModel(ABC):
    @abstractmethod
    def get_config(self) -> BaseModelConfig:
        raise NotImplementedError()
