from typing import Any, Dict, List, Literal

from pydantic import BaseModel, root_validator

from deepsearch.model.base.types import (
    BaseAppPredInput,
    BaseModelConfig,
    CtrlInfoOutputDefs,
    Kind,
    StrictModel,
)


class ContextEntry(StrictModel):
    text: str
    type: str
    representation_type: str


class GenerateAnswers(StrictModel):
    contexts: List[List[ContextEntry]]
    questions: List[str]

    @root_validator
    def check_lengths_match(cls, values):
        contx, quest = values.get("contexts"), values.get("questions")
        if len(contx) != len(quest):
            raise ValueError("Fields have different lengths: contexts, questions")
        return values


class QAGenReqSpec(BaseModel):
    generateAnswers: GenerateAnswers


class QAGenAppPredInput(BaseAppPredInput):
    kind: Literal[Kind.QAGenModel]
    spec: QAGenReqSpec


class GenerateAnswersOutEntry(StrictModel):
    answer: str
    metadata: Dict[str, Any]


GenerateAnswersOutput = List[GenerateAnswersOutEntry]


class QAGenCtrlPredOutput(StrictModel):
    answers: GenerateAnswersOutput


class QAGenConfig(BaseModelConfig):
    kind: Literal[Kind.QAGenModel]


class QAGenInfoOutputDefinitions(CtrlInfoOutputDefs):
    kind: Literal[Kind.QAGenModel]


class QAGenInfoOutput(StrictModel):
    definitions: QAGenInfoOutputDefinitions
