from __future__ import annotations

from typing import Tuple, Union, cast

from fastapi import HTTPException

from deepsearch.model.base.base_qa_generator import BaseQAGenerator
from deepsearch.model.controllers.base_controller import BaseController
from deepsearch.model.server.request_schemas import InferenceReqSpec, QAGenReqSpec


class QAGenController(BaseController):
    def dispatch_predict(self, spec: InferenceReqSpec) -> dict:
        model = cast(BaseQAGenerator, self._model)

        if isinstance(spec, QAGenReqSpec):
            gen_answers = cast(QAGenReqSpec, spec).generateAnswers
            generate_answers_part = gen_answers.dict()
            self._validate_and_parse_input(generate_answers_part)
            answers = model.generate_answers(
                [(c, q) for c, q in zip(gen_answers.contexts, gen_answers.questions)]
            )
            return {"answers": answers}
        else:
            raise HTTPException(
                status_code=500, detail="Internal Server Error", headers={}
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
