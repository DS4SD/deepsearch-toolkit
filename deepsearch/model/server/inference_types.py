from typing import Union

from deepsearch.model.kinds.nlp.types import (
    NLPControllerOutput,
    NLPInfoOutput,
    NLPModelInfo,
    NLPReqSpec,
    NLPRequest, NLPInfoOutputDefinitions,
)
from deepsearch.model.kinds.qagen.types import (
    QAGenControllerOutput,
    QAGenInfoOutput,
    QAGenModelInfo,
    QAGenReqSpec,
    QAGenRequest, QAGenInfoOutputDefinitions,
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

ModelInfoOutput = Union[
    NLPInfoOutput,
    QAGenInfoOutput
]

ModelInfoOutputDefinitions = Union[
    NLPInfoOutputDefinitions,
    QAGenInfoOutputDefinitions
]


