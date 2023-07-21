from typing import List, Literal

from pydantic import root_validator

from deepsearch.model.base.types import (
    BaseAppPredInput,
    BaseModelConfig,
    CtrlInfoOutputDefs,
    Kind,
    StrictModel,
)


class GenerateAnswers(StrictModel):
    contexts: List[List[str]]
    questions: List[str]

    @root_validator
    def check_lengths_match(cls, values):
        contx, quest = values.get("contexts"), values.get("questions")
        if len(contx) != len(quest):
            raise ValueError("Fields have different lengths: contexts, questions")
        return values


class QAGenReqSpec(StrictModel):
    generateAnswers: GenerateAnswers


class QAGenAppPredInput(BaseAppPredInput):
    kind: Literal[Kind.QAGenModel]
    spec: QAGenReqSpec


GenerateAnswersOutput = List[str]


class QAGenCtrlPredOutput(StrictModel):
    answers: GenerateAnswersOutput


class QAGenConfig(BaseModelConfig):
    kind: Literal[Kind.QAGenModel]


class QAGenInfoOutputDefinitions(CtrlInfoOutputDefs):
    kind: Literal[Kind.QAGenModel]


class QAGenInfoOutput(StrictModel):
    definitions: QAGenInfoOutputDefinitions
