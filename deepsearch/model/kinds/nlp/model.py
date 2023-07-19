from abc import abstractmethod
from typing import List, Optional

from deepsearch.model.base.model import BaseDSModel
from deepsearch.model.base.types import BaseModelConfig
from deepsearch.model.kinds.nlp.types import (
    AnnotateEntitiesOutput,
    AnnotatePropertiesOutput,
    AnnotateRelationshipsOutput,
    NLPConfig,
)


class BaseNLPModel(BaseDSModel):
    @abstractmethod
    def annotate_batched_entities(
        self,
        object_type: str,
        items: List[str],
        entity_names: Optional[List[str]],
    ) -> AnnotateEntitiesOutput:
        raise NotImplementedError()

    @abstractmethod
    def annotate_batched_relationships(
        self,
        object_type: str,
        items: List[str],
        entities: List[dict],
        relationship_names: Optional[List[str]],
    ) -> AnnotateRelationshipsOutput:
        raise NotImplementedError()

    @abstractmethod
    def annotate_batched_properties(
        self,
        object_type: str,
        items: List[str],
        entities: List[dict],
        property_names: Optional[List[str]],
    ) -> AnnotatePropertiesOutput:
        raise NotImplementedError()

    @abstractmethod
    def get_nlp_config(self) -> NLPConfig:
        raise NotImplementedError()

    def get_config(self) -> BaseModelConfig:
        return self.get_nlp_config()
