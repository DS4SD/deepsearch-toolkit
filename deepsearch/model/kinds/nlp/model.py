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
    NLPModelInfo,
)


class BaseNLPModel(BaseDSModel):
    _cached_def_spec: Optional[NLPModelInfo] = None

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

    def get_definition_spec(self) -> NLPModelInfo:
        cfg = self.get_nlp_config()
        if not self._cached_def_spec:
            temp = deepcopy(super().get_definition_spec()).dict()
            temp["definition"] = cfg.labels
            temp["metadata"]["supported_object_types"] = cfg.supported_types
            self._cached_def_spec = NLPModelInfo(temp)
        return self._cached_def_spec

    @abstractmethod
    def get_nlp_config(self) -> NLPConfig:
        raise NotImplementedError()

    def get_config(self) -> BaseModelConfig:
        return self.get_nlp_config()
