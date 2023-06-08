from deepsearch.model.base.base_annotator import BaseDSModel
from deepsearch.model.controllers.base_controller import BaseController
from deepsearch.model.controllers.qa_gen_controller import QAGenController
from deepsearch.model.factories.base_model_factory import BaseModelFactory


class BaseQAGeneratorFactory(BaseModelFactory):
    def create_controller(self, model: BaseDSModel) -> BaseController:
        return QAGenController(model=model)
