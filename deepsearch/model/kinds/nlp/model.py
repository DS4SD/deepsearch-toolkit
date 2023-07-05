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
    _is_def_spec_cached: bool = False

    def __init__(self):
        self._cached_def_spec = None

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
        if not self._is_def_spec_cached:
            base_model_info = super().get_definition_spec().dict()
            base_model_info["metadata"]["supported_object_types"] = cfg.supported_types
            self._cached_def_spec = NLPModelInfo(
                **base_model_info, definition=cfg.labels
            )
            print(self._cached_def_spec)
        return self._cached_def_spec

    @abstractmethod
    def get_nlp_config(self) -> NLPConfig:
        raise NotImplementedError()

    def get_config(self) -> BaseModelConfig:
        return self.get_nlp_config()
