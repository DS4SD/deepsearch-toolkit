from abc import ABC, abstractmethod

from pydantic import parse_obj_as

from deepsearch.model.base.types import BaseModelConfig, BaseModelInfo, BaseModelMetadata


class BaseDSModel(ABC):
    @abstractmethod
    def get_config(self) -> BaseModelConfig:
        raise NotImplementedError()

    def get_definition_spec(self) -> BaseModelInfo:
        cfg = self.get_config()
        spec_metadata = BaseModelMetadata(
            name=cfg.name,
            version=cfg.version,
            url=cfg.url,
            author=cfg.author,
            description=cfg.description,
            expected_compute_time=cfg.expected_compute_time
        )
        spec = BaseModelInfo(metadata=spec_metadata)
        return spec
