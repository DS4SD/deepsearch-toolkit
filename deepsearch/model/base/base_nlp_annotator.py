from abc import abstractmethod
from typing import List, Optional

from deepsearch.model.base.base_annotator import BaseAnnotator


class BaseNLPAnnotator(BaseAnnotator):

    kind: str = "NLPModel"

    @abstractmethod
    def annotate_batched_entities(
        self,
        object_type: str,
        items: List[str],
        entity_names: Optional[List[str]],
    ) -> List[dict]:
        return []

    @abstractmethod
    def annotate_batched_relationships(
        self,
        object_type: str,
        items: List[str],
        entities: List[dict],
        relationship_names: Optional[List[str]],
    ) -> List[dict]:
        return []

    @abstractmethod
    def annotate_batched_properties(
        self,
        object_type: str,
        items: List[str],
        entities: List[dict],
        property_names: Optional[List[str]],
    ) -> List[dict]:
        return []
