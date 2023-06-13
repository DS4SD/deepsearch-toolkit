from typing import Coroutine, Dict, List, Optional, Union

from pydantic import BaseModel, Extra, Field, ValidationError, root_validator, validator


class Annotations(BaseModel):
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


class Metadata(BaseModel):
    annotations: Annotations


from typing import List, Optional

from pydantic import BaseModel, root_validator


class BaseSpec(BaseModel):
    objectType: str
    texts: Optional[List[str]]
    images: Optional[List[dict]]
    tables: Optional[List[str]]

    @root_validator()
    def must_contain_correct_content_for_object_type(cls, values):
        print(values)
        if values["objectType"] == "text":
            if values["texts"] is None:
                raise ValueError("Text objectType with no field 'texts'")
            return values
        if values["objectType"] == "table":
            if values["tables"] is None:
                raise ValueError("table objectType with no field 'tables'")
            return values
        if values["objectType"] == "image":
            if values["images"] is None:
                raise ValueError("image objectType with no field 'images'")
            return values
        raise ValueError("Unknown objectType")


class SpecFindEntities(BaseSpec):
    entityNames: Optional[str]


class SpecFindRelationships(BaseSpec):
    relationshipNames: Optional[str]


class SpecFindProperties(BaseSpec):
    propertyNames: Optional[str]


class SpecEntities(BaseModel):
    findEntities: SpecFindEntities


class SpecProperties(BaseModel):
    findProperties: SpecFindProperties


class SpecRelationships(BaseModel):
    findRelationships: SpecFindRelationships


class AnnotateRequestModel(BaseModel):
    apiVersion: str
    kind: str
    metadata: Metadata
    spec: Union[SpecRelationships, SpecProperties, SpecEntities]
