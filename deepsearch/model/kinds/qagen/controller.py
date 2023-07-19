from __future__ import annotations

import logging

logger = logging.getLogger("root.model")

from fastapi import HTTPException, status

from deepsearch.model.base.controller import BaseController
from deepsearch.model.base.model import BaseDSModel
from deepsearch.model.base.types import Kind
from deepsearch.model.kinds.qagen.model import BaseQAGenerator
from deepsearch.model.kinds.qagen.types import QAGenControllerOutput, QAGenReqSpec
from deepsearch.model.server.inference_types import ControllerInput, ControllerOutput


class QAGenController(BaseController):
    def __init__(self, model: BaseQAGenerator):
        self._model = model
        logger.info("QAGenController Initialized")

    def _get_model(self) -> BaseDSModel:
        logger.info("QAGenController return model")
        return self._model

    def get_kind(self) -> str:
        logger.info("QAGenController return kind")
        return Kind.QAGenModel

    def dispatch_predict(self, spec: ControllerInput) -> ControllerOutput:
        logger.info("QAGenController Dispatching predict")
        if isinstance(spec, QAGenReqSpec):
            gen_answers = spec.generateAnswers
            answers = self._model.generate_answers(
                [(c, q) for c, q in zip(gen_answers.contexts, gen_answers.questions)]
            )
            logger.info("QAGenController returning predictions")
            return QAGenControllerOutput(
                answers=answers,
            )
        else:
            logger.error("Unexpected spec type")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Unexpected spec type",
            )
