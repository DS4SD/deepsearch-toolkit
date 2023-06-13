from __future__ import annotations

from typing import Tuple, Union, cast

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

    def _get_model(self) -> BaseDSModel:
        return self._model

    def get_kind(self) -> str:
        return Kind.QAGen

    def dispatch_predict(self, spec: ControllerInput) -> ControllerOutput:
        # TODO: use Pydantic objects instead of dicts
        if isinstance(spec, QAGenReqSpec):
            gen_answers = cast(QAGenReqSpec, spec).generateAnswers
            gen_answers_dict = gen_answers.dict()
            self._validate_and_parse_input(gen_answers_dict)
            answers = self._model.generate_answers(
                [(c, q) for c, q in zip(gen_answers.contexts, gen_answers.questions)]
            )
            return QAGenControllerOutput(
                answers=answers,
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Unexpected spec type",
            )

    # TODO replace with pydantic
    @staticmethod
    def _validate_and_parse_input(body_part) -> Union[HTTPException, Tuple[dict, dict]]:
        if (
            "contexts" not in body_part
            or "questions" not in body_part
            or len(body_part["questions"]) != len(body_part["contexts"])
        ):
            raise HTTPException(
                status_code=500,
                detail="Internal Server Error",
            )

        return body_part["contexts"], body_part["questions"]
