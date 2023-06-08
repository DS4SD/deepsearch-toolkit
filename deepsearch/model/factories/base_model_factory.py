from abc import ABC, abstractmethod

from deepsearch.model.base.base_annotator import BaseDSModel
from deepsearch.model.controllers.base_controller import BaseController


class BaseModelFactory(ABC):
    @abstractmethod
    def create_model(self) -> BaseDSModel:
        pass

    @abstractmethod
    def create_controller(self, model: BaseDSModel) -> BaseController:
        pass
