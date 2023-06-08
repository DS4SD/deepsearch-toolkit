from abc import ABC, abstractmethod

from deepsearch.model.base.base_annotator import BaseDSModel
from deepsearch.model.server.request_schemas import InferenceReqSpec


class BaseController(ABC):
    def __init__(self, model: BaseDSModel):
        self._model = model

    def get_info(self) -> dict:
        result = {  # TODO refactor with pydantic
            "definitions": {
                "apiVersion": "v1",
                "kind": self._model.kind,
                "spec": self._model.get_definition_spec(),
            }
        }
        return result

    @abstractmethod
    def dispatch_predict(self, spec: InferenceReqSpec) -> dict:
        pass

    def get_model(self) -> BaseDSModel:
        return self._model
