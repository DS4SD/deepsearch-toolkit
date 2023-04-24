from typing import Coroutine, Dict, List, Optional, Union

from pydantic import BaseModel, Field


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


class FindEntitiesText(BaseModel):
    entityNames: Optional[List[str]]
    objectType: str
    texts: List[str]


class FindPropertiesText(BaseModel):
    propertyNames: Optional[List[str]]
    entities: Optional[List[dict]]
    objectType: str
    texts: List[str]


class FindRelationshipsText(BaseModel):
    relationshipNames: Optional[List[str]]
    entities: List[dict]
    objectType: str
    texts: List[str]


class FindEntitiesImage(BaseModel):
    entityNames: Optional[List[str]]
    objectType: str
    images: List[dict]


class FindPropertiesImage(BaseModel):
    propertyNames: Optional[List[str]]
    entities: Optional[List[dict]]
    objectType: str
    images: List[dict]


class FindRelationshipsImage(BaseModel):
    relationshipNames: Optional[List[str]]
    entities: List[dict]
    objectType: str
    images: List[dict]


class FindEntitiesTable(BaseModel):
    entityNames: Optional[List[str]]
    objectType: str
    tables: List[List]


class FindPropertiesTable(BaseModel):
    propertyNames: Optional[List[str]]
    entities: Optional[List[dict]]
    objectType: str
    tables: List[List]


class FindRelationshipsTable(BaseModel):
    relationshipNames: Optional[List[str]]
    entities: List[dict]
    objectType: str
    tables: List[List]


class SpecEntities(BaseModel):
    findEntities: Union[FindEntitiesText, FindEntitiesImage, FindEntitiesTable]


class SpecProperties(BaseModel):
    findProperties: Union[FindPropertiesText, FindPropertiesImage, FindPropertiesTable]


class SpecRelationships(BaseModel):
    findRelationships: Union[
        FindRelationshipsText, FindRelationshipsImage, FindRelationshipsTable
    ]


class AnnotateRequestModel(BaseModel):
    apiVersion: str
    kind: str
    metadata: Metadata
    spec: Union[SpecRelationships, SpecProperties, SpecEntities]
