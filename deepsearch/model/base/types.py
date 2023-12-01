from datetime import datetime
from enum import Enum
from typing import Any, Dict, Optional

from pydantic.v1 import BaseModel, Extra, Field, PositiveFloat


class StrictModel(BaseModel, extra=Extra.forbid):
    # TODO use only where needed
    pass


class Annotations(StrictModel):
    deepsearch_res_ibm_com_x_deadline: datetime = Field(
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
    NLPModel = "NLPModel"
    QAGenModel = "QAGenModel"


class Metadata(StrictModel):
    annotations: Annotations


class BaseAppPredInput(StrictModel):
    apiVersion: str
    kind: Kind
    metadata: Metadata
    spec: Any


class BaseModelMetadata(StrictModel):
    name: str
    version: str
    url: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    expected_compute_time: Optional[PositiveFloat] = None


class BaseModelConfig(BaseModelMetadata):
    kind: Kind


class ModelInfoOutputDefsSpec(BaseModel):
    definition: Dict
    metadata: BaseModelMetadata


class CtrlInfoOutputDefs(BaseModel):
    apiVersion: str
    kind: Kind
    spec: ModelInfoOutputDefsSpec


class CtrlInfoOutput(BaseModel):
    definitions: CtrlInfoOutputDefs
