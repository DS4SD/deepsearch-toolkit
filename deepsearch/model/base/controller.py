from abc import ABC, abstractmethod
from typing import Optional

from deepsearch.model.base.model import BaseDSModel
from deepsearch.model.base.types import BaseModelConfig, BaseModelMetadata
from deepsearch.model.server.inference_types import (
    AppModelInfoOutput,
    CtrlPredInput,
    CtrlPredOutput,
)


class BaseController(ABC):
    _config: Optional[BaseModelConfig] = None

    @abstractmethod
    def get_info(self) -> AppModelInfoOutput:
        raise NotImplementedError()

    def _get_api_version(self) -> str:
        return "v1"

    def _get_metadata(self) -> BaseModelMetadata:
        cfg = self._get_config()
        return BaseModelMetadata(
            name=cfg.name,
            version=cfg.version,
            url=cfg.url,
            author=cfg.author,
            description=cfg.description,
            expected_compute_time=cfg.expected_compute_time,
        )

    def _get_config(self):
        if self._config is None:
            self._config = self._get_model().get_config()
        return self._config

    @abstractmethod
    def dispatch_predict(self, spec: CtrlPredInput) -> CtrlPredOutput:
        raise NotImplementedError()

    @abstractmethod
    def _get_model(self) -> BaseDSModel:
        raise NotImplementedError()

    @abstractmethod
    def get_kind(self) -> str:
        raise NotImplementedError()

    def get_model_kind(self) -> str:
        return self._get_config().kind

    def get_model_name(self) -> str:
        return self._get_config().name

    def get_model_exec_time(self) -> float:
        return self._get_config().expected_compute_time or 0
