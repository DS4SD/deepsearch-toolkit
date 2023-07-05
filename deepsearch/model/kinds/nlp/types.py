from enum import Enum
from typing import Any, Dict, List, Literal, Optional, Union

from pydantic import BaseModel, validator

from deepsearch.model.base.types import (
    BaseInfReq,
    BaseModelConfig,
    BaseModelInfo,
    BaseModelMetadata,
    InfoOutput,
    InfoOutputDefinitions,
    InfoOutputDefinitionsSpec,
    Kind,
    StrictModel,
)


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
class AnnotateEntitiesRequiredProperties(StrictModel):
    type: str
    match: str
    original: str
    range: List[int]


class AnnotateRelationshipsRequiredProperties(StrictModel):
    header: list
    data: list


AnnotateEntitiesOutput = List[
    Dict[str, List[Union[None, AnnotateEntitiesRequiredProperties]]]
]
AnnotateRelationshipsOutput = List[
    Dict[str, Union[None, AnnotateRelationshipsRequiredProperties]]
]
AnnotatePropertiesOutput = List[Dict]
# TODO RE: This appears to be a real implementation, without more samples of property annotation it is hard to tell


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


class NLPModelMetadata(BaseModelMetadata):
    supported_object_types: List[Literal["text", "table", "image"]]


class NLPInfoOutputDefinitionsSpec(InfoOutputDefinitionsSpec):
    metadata: NLPModelMetadata


class NLPInfoOutputDefinitions(InfoOutputDefinitions):
    kind: Literal[Kind.NLPModel]
    spec: NLPInfoOutputDefinitionsSpec


class NLPInfoOutput(InfoOutput):
    definitions: NLPInfoOutputDefinitions


class NLPModelInfo(BaseModelInfo):
    metadata: NLPModelMetadata
    definition: Dict
