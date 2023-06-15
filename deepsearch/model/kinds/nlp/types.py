from enum import Enum
from typing import List, Literal, Optional, Union

from deepsearch.model.base.types import BaseInfReq, BaseModelConfig, Kind, StrictModel


class NLPType(str, Enum):
    # currently only supporting "text"
    text = "text"


class FindEntitiesText(StrictModel):
    entityNames: Optional[List[str]] = None
    objectType: Literal[NLPType.text]
    texts: List[str]


class FindPropertiesText(StrictModel):
    propertyNames: Optional[List[str]] = None
    entities: Optional[List[dict]] = None
    objectType: Literal[NLPType.text]
    texts: List[str]


class FindRelationshipsText(StrictModel):
    relationshipNames: Optional[List[str]] = None
    entities: List[dict]
    objectType: Literal[NLPType.text]
    texts: List[str]


class NLPEntitiesReqSpec(StrictModel):
    findEntities: FindEntitiesText


class NLPPropertiesReqSpec(StrictModel):
    findProperties: FindPropertiesText


class NLPRelationshipsReqSpec(StrictModel):
    findRelationships: FindRelationshipsText


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
