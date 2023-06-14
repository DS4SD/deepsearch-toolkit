from typing import List, Literal

from pydantic import root_validator

from deepsearch.model.base.types import BaseInfReq, BaseModelConfig, Kind, StrictModel


class GenerateAnswers(StrictModel):  # TODO rename?
    contexts: List[List[str]]
    questions: List[str]

    @root_validator
    def check_lengths_match(cls, values):
        contx, quest = values.get("contexts"), values.get("questions")
        if len(contx) != len(quest):
            raise ValueError("Fields have different lengths: contexts, questions")
        return values


class QAGenReqSpec(StrictModel):
    generateAnswers: GenerateAnswers  # TODO rename?


class QAGenRequest(BaseInfReq):
    kind: Literal[Kind.QAGenModel]
    spec: QAGenReqSpec


# TODO GenerateAnswersInput pydantic model needed?

GenerateAnswersOutput = List[str]  # TODO provide real implementation


class QAGenControllerOutput(StrictModel):
    answers: GenerateAnswersOutput


class QAGenConfig(BaseModelConfig):
    kind: Literal[Kind.QAGenModel]
