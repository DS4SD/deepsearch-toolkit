from __future__ import annotations

import logging

from fastapi import HTTPException, status

logger = logging.getLogger("root.model")


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
        logger.info("QAGenController Initialized")

    def get_info(self) -> QAGenInfoOutput:
        spec = ModelInfoOutputDefsSpec(
            definition={},
            metadata=self._get_metadata(),
        )
        definitions = QAGenInfoOutputDefinitions(
            apiVersion=super()._get_api_version(),
            kind=self.get_kind(),
            spec=spec,
        )
        return QAGenInfoOutput(definitions=definitions)

    def _get_model(self) -> BaseDSModel:
        logger.info("QAGenController return model")
        return self._model

    def get_kind(self) -> str:
        logger.info("QAGenController return kind")
        return Kind.QAGenModel

    def dispatch_predict(self, spec: CtrlPredInput) -> CtrlPredOutput:
        logger.info("QAGenController Dispatching predict")
        if isinstance(spec, QAGenReqSpec):
            gen_answers = spec.generateAnswers
            answers = self._model.generate_answers(
                [(c, q) for c, q in zip(gen_answers.contexts, gen_answers.questions)]
            )
            logger.info("QAGenController returning predictions")
            return QAGenCtrlPredOutput(
                answers=answers,
            )
        else:
            logger.error("Unexpected spec type")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Unexpected spec type",
            )
