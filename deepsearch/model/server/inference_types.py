from typing import Union

from deepsearch.model.kinds.nlp.types import (
    NLPAppPredInput,
    NLPCtrlPredOutput,
    NLPInfoOutput,
    NLPReqSpec,
)
from deepsearch.model.kinds.qagen.types import (
    QAGenAppPredInput,
    QAGenCtrlPredOutput,
    QAGenInfoOutput,
    QAGenReqSpec,
)

AppPredInput = Union[
    NLPAppPredInput,
    QAGenAppPredInput,
]

CtrlPredInput = Union[
    NLPReqSpec,
    QAGenReqSpec,
]

CtrlPredOutput = Union[
    NLPCtrlPredOutput,
    QAGenCtrlPredOutput,
]

AppModelInfoOutput = Union[
    NLPInfoOutput,
    QAGenInfoOutput,
]
