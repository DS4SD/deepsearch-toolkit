from enum import Enum
from typing import Dict, List, Literal, Optional, Union

from deepsearch.model.base.types import (
    BaseAppPredInput,
    BaseModelConfig,
    BaseModelMetadata,
    CtrlInfoOutput,
    CtrlInfoOutputDefs,
    Kind,
    ModelInfoOutputDefsSpec,
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


class NLPAppPredInput(BaseAppPredInput):
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


class AnnotateEntitiesEntry(StrictModel):
    type: str
    match: str
    original: str
    range: List[int]


class AnnotateRelationshipsEntry(StrictModel):
    header: list
    data: list


AnnotateEntitiesOutput = List[Dict[str, List[AnnotateEntitiesEntry]]]
AnnotateRelationshipsOutput = List[Dict[str, AnnotateRelationshipsEntry]]
AnnotatePropertiesOutput = List[Dict]  # TODO specify


class NLPEntsCtrlPredOuput(StrictModel):
    entities: AnnotateEntitiesOutput


class NLPRelsCtrlPredOutput(StrictModel):
    relationships: AnnotateRelationshipsOutput


class NLPPropsCtrlPredOutput(StrictModel):
    properties: AnnotatePropertiesOutput


NLPCtrlPredOutput = Union[
    NLPEntsCtrlPredOuput,
    NLPRelsCtrlPredOutput,
    NLPPropsCtrlPredOutput,
]


class NLPConfig(BaseModelConfig):
    kind: Literal[Kind.NLPModel]
    supported_types: List[NLPType]
    labels: AnnotationLabels


class NLPModelMetadata(BaseModelMetadata):
    supported_object_types: List[Literal["text", "table", "image"]]


class NLPInfoOutputDefinitionsSpec(ModelInfoOutputDefsSpec):
    metadata: NLPModelMetadata


class NLPInfoOutputDefinitions(CtrlInfoOutputDefs):
    kind: Literal[Kind.NLPModel]
    spec: NLPInfoOutputDefinitionsSpec


class NLPInfoOutput(CtrlInfoOutput):
    definitions: NLPInfoOutputDefinitions
