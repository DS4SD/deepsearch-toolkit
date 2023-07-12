from typing import Union

from deepsearch.model.kinds.nlp.types import (
    NLPControllerOutput,
    NLPInfoOutput,
    NLPInfoOutputDefinitions,
    NLPModelInfo,
    NLPReqSpec,
    NLPRequest,
)
from deepsearch.model.kinds.qagen.types import (
    QAGenControllerOutput,
    QAGenInfoOutput,
    QAGenInfoOutputDefinitions,
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

ModelInfoOutput = Union[NLPInfoOutput, QAGenInfoOutput]

ModelInfoOutputDefinitions = Union[NLPInfoOutputDefinitions, QAGenInfoOutputDefinitions]
