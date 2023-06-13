from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel, Extra, Field, PositiveFloat


class StrictModel(BaseModel, extra=Extra.forbid):
    # TODO use only where needed
    pass


class Annotations(StrictModel):
    deepsearch_res_ibm_com_x_deadline: str = Field(
        ..., alias="deepsearch.res.ibm.com/x-deadline"
    )
    deepsearch_res_ibm_com_x_transaction_id: str = Field(
        ..., alias="deepsearch.res.ibm.com/x-transaction-id"
    )
    deepsearch_res_ibm_com_x_attempt_number: str = Field(
        ..., alias="deepsearch.res.ibm.com/x-attempt-number"
    )
    deepsearch_res_ibm_com_x_max_attempts: str = Field(
        ..., alias="deepsearch.res.ibm.com/x-max-attempts"
    )


class Kind(str, Enum):
    # TODO: review values
    NLP = "NLP"
    QAGen = "QAGen"


class Metadata(StrictModel):
    annotations: Annotations


class BaseInfReq(StrictModel):
    apiVersion: str
    kind: Kind
    metadata: Metadata
    spec: Any


class BaseModelConfig(StrictModel):
    kind: Kind
    name: str
    version: str
    url: Optional[str]
    author: Optional[str]
    description: Optional[str]
    expected_compute_time: Optional[PositiveFloat]
