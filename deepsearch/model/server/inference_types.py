from typing import Union

from deepsearch.model.kinds.nlp.types import NLPControllerOutput, NLPReqSpec, NLPRequest
from deepsearch.model.kinds.qagen.types import (
    QAGenControllerOutput,
    QAGenReqSpec,
    QAGenRequest,
)

AppInferenceInput = Union[
    NLPRequest,
    QAGenRequest,
]

ControllerInput = Union[
    NLPReqSpec,
    QAGenReqSpec,
]

ControllerOutput = Union[
    NLPControllerOutput,
    QAGenControllerOutput,
]
