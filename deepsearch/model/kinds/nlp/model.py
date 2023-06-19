from abc import abstractmethod
from copy import deepcopy
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
    _cached_def_spec: dict = {}

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

    def get_definition_spec(self) -> dict:
        cfg = self.get_nlp_config()
        if not self._cached_def_spec:
            self._cached_def_spec = deepcopy(super().get_definition_spec())
            self._cached_def_spec["definition"] = cfg.labels
            self._cached_def_spec["metadata"][
                "supported_object_types"
            ] = cfg.supported_types
        return self._cached_def_spec

    @abstractmethod
    def get_nlp_config(self) -> NLPConfig:
        raise NotImplementedError()

    def get_config(self) -> BaseModelConfig:
        return self.get_nlp_config()
