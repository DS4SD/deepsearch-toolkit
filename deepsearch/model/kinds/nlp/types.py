from enum import Enum
from typing import List, Literal, Optional, Union

from deepsearch.model.base.types import BaseInfReq, BaseModelConfig, Kind, StrictModel


class NLPType(str, Enum):
    text = "text"
    table = "table"
    image = "image"


class FindEntitiesText(StrictModel):
    entityNames: Optional[List[str]]
    objectType: Literal[NLPType.text]
    texts: List[str]


class FindPropertiesText(StrictModel):
    propertyNames: Optional[List[str]]
    entities: Optional[List[dict]]
    objectType: Literal[NLPType.text]
    texts: List[str]


class FindRelationshipsText(StrictModel):
    relationshipNames: Optional[List[str]]
    entities: List[dict]
    objectType: Literal[NLPType.text]
    texts: List[str]


class FindEntitiesImage(StrictModel):
    entityNames: Optional[List[str]]
    objectType: Literal[NLPType.image]
    images: List[dict]


class FindPropertiesImage(StrictModel):
    propertyNames: Optional[List[str]]
    entities: Optional[List[dict]]
    objectType: Literal[NLPType.image]
    images: List[dict]


class FindRelationshipsImage(StrictModel):
    relationshipNames: Optional[List[str]]
    entities: List[dict]
    objectType: Literal[NLPType.image]
    images: List[dict]


class FindEntitiesTable(StrictModel):
    entityNames: Optional[List[str]]
    objectType: Literal[NLPType.table]
    tables: List[List]


class FindPropertiesTable(StrictModel):
    propertyNames: Optional[List[str]]
    entities: Optional[List[dict]]
    objectType: Literal[NLPType.table]
    tables: List[List]


class FindRelationshipsTable(StrictModel):
    relationshipNames: Optional[List[str]]
    entities: List[dict]
    objectType: Literal[NLPType.table]
    tables: List[List]


class NLPEntitiesReqSpec(StrictModel):
    findEntities: Union[FindEntitiesText, FindEntitiesImage, FindEntitiesTable]


class NLPPropertiesReqSpec(StrictModel):
    findProperties: Union[FindPropertiesText, FindPropertiesImage, FindPropertiesTable]


class NLPRelationshipsReqSpec(StrictModel):
    findRelationships: Union[
        FindRelationshipsText, FindRelationshipsImage, FindRelationshipsTable
    ]


NLPReqSpec = Union[
    NLPEntitiesReqSpec,
    NLPRelationshipsReqSpec,
    NLPPropertiesReqSpec,
]


class NLPRequest(BaseInfReq):
    kind: Literal[Kind.NLPModel]
    spec: NLPReqSpec


class EntityLabel(StrictModel):
    key: str
    description: str


class RelationshipColumn(StrictModel):
    key: str
    entities: List[str]


class RelationshipLabel(StrictModel):
    key: str
    description: str
    columns: List[RelationshipColumn]


class PropertyLabel(StrictModel):
    key: str
    description: str


class AnnotationLabels(StrictModel):
    entities: List[EntityLabel]
    relationships: List[RelationshipLabel]
    properties: List[PropertyLabel]


# TODO Annotate*Input pydantic models needed?

AnnotateEntitiesOutput = List[dict]  # TODO provide real implementation
AnnotateRelationshipsOutput = List[dict]  # TODO provide real implementation
AnnotatePropertiesOutput = List[dict]  # TODO provide real implementation


class NLPEntitiesControllerOutput(StrictModel):
    entities: AnnotateEntitiesOutput


class NLPRelationshipsControllerOutput(StrictModel):
    relationships: AnnotateRelationshipsOutput


class NLPPropertiesControllerOutput(StrictModel):
    properties: AnnotatePropertiesOutput


NLPControllerOutput = Union[
    NLPEntitiesControllerOutput,
    NLPRelationshipsControllerOutput,
    NLPPropertiesControllerOutput,
]


class NLPConfig(BaseModelConfig):
    kind: Literal[Kind.NLPModel]
    supported_types: List[NLPType]
    labels: AnnotationLabels
