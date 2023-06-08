from abc import abstractmethod
from copy import deepcopy
from typing import List, Optional

from pydantic import BaseModel

from deepsearch.model.base.base_annotator import BaseDSModel


class Entity(BaseModel):
    key: str
    description: str


class RelationshipColumn(BaseModel):
    key: str
    entities: List[str]


class Relationship(BaseModel):
    key: str
    description: str
    columns: List[RelationshipColumn]


class Property(BaseModel):  # TODO verify
    key: str
    description: str


class Labels(BaseModel):
    entities: List[Entity]
    relationships: List[Relationship]
    properties: List[Property]


class BaseNLPModel(BaseDSModel):

    kind = "NLPModel"

    def __init__(self):
        super().__init__()

        self._cached_def_spec = None

    @abstractmethod
    def get_labels(self) -> Labels:
        pass

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

    def get_definition_spec(self) -> dict:
        if self._cached_def_spec is None:
            self._cached_def_spec = deepcopy(super().get_definition_spec())
            self._cached_def_spec["definition"] = self.get_labels().dict()
        return self._cached_def_spec
