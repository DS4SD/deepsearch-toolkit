from abc import ABC, abstractmethod

from deepsearch.model.base.types import BaseModelConfig


class BaseDSModel(ABC):
    @abstractmethod
    def get_config(self) -> BaseModelConfig:
        raise NotImplementedError()

    def get_definition_spec(self) -> dict:
        cfg = self.get_config()
        spec = {  # TODO refactor with pydantic
            "metadata": {
                "name": cfg.name,
                "version": cfg.version,
                "url": cfg.url,
                "author": cfg.author,
                "description": cfg.description,
                "expected_compute_time": cfg.expected_compute_time,
            },
        }
        return spec
