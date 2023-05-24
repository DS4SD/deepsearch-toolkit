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
        """Annotate entities in given items batch.

        Args:
            object_type (str): type of objects to annotate, e.g. "text"; must be included
                in `supports` property
            items (List[str]): batch of input items to annotate
            entity_names (Optional[List[str]]): entities to annotate

        Returns:
            List[dict]: a list, which, for each item in `items`, contains a dict with keys
                being the various entity names each mapped to a list of its annotations
                (can be empty) in the item, each annotation being a dict like:
                    {
                        "type": <entity_name>,
                        "match": <match>,
                        "original": <original>,
                        "range": [<range_start>, <range_end>]
                    }
        """
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
