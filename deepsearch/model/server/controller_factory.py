from deepsearch.model.base.controller import BaseController
from deepsearch.model.base.model import BaseDSModel
from deepsearch.model.kinds.nlp.controller import NLPController
from deepsearch.model.kinds.nlp.model import BaseNLPModel
from deepsearch.model.kinds.qagen.controller import QAGenController
from deepsearch.model.kinds.qagen.model import BaseQAGenerator


class ControllerFactory:
    def create_controller(self, model: BaseDSModel) -> BaseController:
        if isinstance(model, BaseNLPModel):
            return NLPController(model)
        elif isinstance(model, BaseQAGenerator):
            return QAGenController(model)
        else:
            raise RuntimeError(f"No controller defined for model type {type(model)}")
