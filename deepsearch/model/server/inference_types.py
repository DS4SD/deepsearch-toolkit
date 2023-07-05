from typing import Union

from deepsearch.model.kinds.nlp.types import (
    NLPControllerOutput,
    NLPInfoOutput,
    NLPModelInfo,
    NLPReqSpec,
    NLPRequest,
)
from deepsearch.model.kinds.qagen.types import (
    QAGenControllerOutput,
    QAGenInfoOutput,
    QAGenModelInfo,
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

ModelInfo = Union[
    NLPModelInfo,
    QAGenModelInfo,
]
