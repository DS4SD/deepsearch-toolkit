from fastapi import HTTPException, status

from deepsearch.model.base.controller import BaseController
from deepsearch.model.base.model import BaseDSModel
from deepsearch.model.base.types import Kind, ModelInfoOutputDefsSpec
from deepsearch.model.kinds.qagen.model import BaseQAGenerator
from deepsearch.model.kinds.qagen.types import (
    QAGenCtrlPredOutput,
    QAGenInfoOutput,
    QAGenInfoOutputDefinitions,
    QAGenReqSpec,
)
from deepsearch.model.server.inference_types import CtrlPredInput, CtrlPredOutput


class QAGenController(BaseController):
    def __init__(self, model: BaseQAGenerator):
        self._model = model

    def get_info(self) -> QAGenInfoOutput:
        spec = ModelInfoOutputDefsSpec(
            definition={},
            metadata=self._get_metadata(),
        )
        definitions = QAGenInfoOutputDefinitions(
            apiVersion=super()._get_api_version(),
            kind=self.get_kind(),  # type: ignore[arg-type]
            spec=spec,
        )
        return QAGenInfoOutput(definitions=definitions)

    def _get_model(self) -> BaseDSModel:
        return self._model

    def get_kind(self) -> str:
        return Kind.QAGenModel

    def dispatch_predict(self, spec: CtrlPredInput) -> CtrlPredOutput:
        if isinstance(spec, QAGenReqSpec):
            gen_answers = spec.generateAnswers
            answers = self._model.generate_answers(
                texts=[
                    ([ctx_entry.dict() for ctx_entry in ctx_list], q)
                    for ctx_list, q in zip(gen_answers.contexts, gen_answers.questions)
                ],
                extras=gen_answers.extras or {},
            )
            return QAGenCtrlPredOutput(
                answers=answers,
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Unexpected spec type",
            )
