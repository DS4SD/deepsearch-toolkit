from deepsearch.model.base.base_annotator import BaseDSModel
from deepsearch.model.controllers.base_controller import BaseController
from deepsearch.model.controllers.nlp_controller import NLPController
from deepsearch.model.factories.base_model_factory import BaseModelFactory


class BaseNLPFactory(BaseModelFactory):
    def create_controller(self, model: BaseDSModel) -> BaseController:
        return NLPController(model=model)
