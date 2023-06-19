from abc import ABC, abstractmethod
from typing import Optional

from deepsearch.model.base.model import BaseDSModel
from deepsearch.model.base.types import BaseModelConfig
from deepsearch.model.server.inference_types import ControllerInput, ControllerOutput


class BaseController(ABC):
    _config: Optional[BaseModelConfig] = None

    def get_info(self) -> dict:
        model = self._get_model()
        cfg = self._get_config()
        result = {  # TODO refactor with pydantic
            "definitions": {
                "apiVersion": "v1",
                "kind": cfg.kind,
                "spec": model.get_definition_spec(),
            }
        }
        return result

    def _get_config(self):
        if self._config is None:
            self._config = self._get_model().get_config()
        return self._config

    @abstractmethod
    def dispatch_predict(self, spec: ControllerInput) -> ControllerOutput:
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
