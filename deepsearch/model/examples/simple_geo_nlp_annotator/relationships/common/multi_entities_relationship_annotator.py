import logging

logger = logging.getLogger("cps-nlp")
import itertools
from dataclasses import dataclass
from typing import List

from .base_text_relationship_annotator import BaseTextRelationshipAnnotator


@dataclass
class Config:
    entities: List[str]


class MultiEntitiesRelationshipAnnotator(BaseTextRelationshipAnnotator):
    """
    Create a relationship if all entitiy types are in the given text input.
    """

    def key(self) -> str:
        return "-to-".join(self._entities)

    def columns(self) -> list:
        return list(
            [{"key": entity, "entities": [entity]} for entity in self._entities]
        )

    def description(self) -> str:
        return f"Relationship between entities {self._entities}"

    def __init__(self, config: Config):
        self._entities = config.entities

    def annotate_relationships_text(
        self, text: str, entity_map: dict, relationship_name: str
    ) -> dict:
        header = [*self._entities, "weight", "source"]
        data = []

        matches = []
        for entity_name in self._entities:
            if entity_name in entity_map and len(entity_map[entity_name]) > 0:
                matches.append(
                    [
                        f"{entity_name}.{i}"
                        for i, _ in enumerate(entity_map[entity_name])
                    ]
                )

        ## If all entity types have been found, create relationships between all of them
        if len(matches) == len(self._entities):
            for t in itertools.product(*matches):
                row = [*t, 1.0, "entities"]
                data.append(row)

        return {"header": header, "data": data}
