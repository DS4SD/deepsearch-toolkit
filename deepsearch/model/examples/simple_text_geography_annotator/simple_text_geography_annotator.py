# IBM Corpus Processing Service
# (C) Copyright IBM Corporation 2019, 2021
# ALL RIGHTS RESERVED

## Sample External API Annotator
## Apart from initialization of provided entities and model loading,
## the only function you really have to change here is "annotate_entities_text".

import logging

from fastapi import HTTPException

from deepsearch.model.base.base_annotator import BaseDSModel
from deepsearch.model.base.base_nlp_annotator import (
    BaseNLPModel,
    Entity,
    Labels,
    Property,
    Relationship,
)
from deepsearch.model.factories.base_nlp_factory import BaseNLPFactory

logger = logging.getLogger("cps-nlp")
from typing import List, Optional

from .entities.cities_annotator import CitiesAnnotator  # type: ignore
from .entities.countries_annotator import CountriesAnnotator  # type: ignore
from .entities.provincies_annotator import ProvinciesAnnotator  # type: ignore
from .relationships.cities_to_countries_annotator import (  # type: ignore
    CitiesToCountriesAnnotator,
)
from .relationships.cities_to_provincies_annotator import (  # type: ignore
    CitiesToProvinciesAnnotator,
)
from .relationships.provincies_to_countries_annotator import (  # type: ignore
    ProvinciesToCountriesAnnotator,
)


class SimpleTextGeographyFactory(BaseNLPFactory):
    def create_model(self) -> BaseDSModel:
        return SimpleTextGeographyAnnotator()


class SimpleTextGeographyAnnotator(BaseNLPModel):

    name = "SimpleTextGeographyAnnotator"
    supports = ["text"]

    _ent_annotator_classes = [
        CitiesAnnotator,
        CountriesAnnotator,
        ProvinciesAnnotator,
    ]

    _rel_annotator_classes = [
        CitiesToCountriesAnnotator,
        CitiesToProvinciesAnnotator,
        ProvinciesToCountriesAnnotator,
    ]

    def __init__(self):
        super().__init__()

        self._ent_annots = {}
        self._rel_annots = {}
        self._initialize_annotators()

        self.entity_names = list(self._ent_annots.keys())
        self.relationship_names = list(self._rel_annots.keys())
        self.property_names = []

    def get_labels(self) -> Labels:
        # Derive entity labels from classes
        entities = [
            Entity(key=annot.key(), description=annot.description())
            for annot in self._ent_annots.values()
        ]

        # Dummy implementation of property labels
        properties = [
            Property(key=property, description=f"Property of type {property}")
            for property in self.property_names
        ]

        # Derive relationships labels from classes
        relationships = [
            Relationship(
                key=annot.key(),
                description=annot.description(),
                columns=annot.columns(),
            )
            for annot in self._rel_annots.values()
        ]

        return Labels(
            entities=entities,
            relationships=relationships,
            properties=properties,
        )

    def _initialize_annotators(self):
        # Initialize dict of annotator instances `self._ent_annots`
        for cls in self._ent_annotator_classes:
            annot = cls()
            self._ent_annots[annot.key()] = annot

        # Initialize dict of annotator instances `self._rel_annots`
        for cls in self._rel_annotator_classes:
            annot = cls()
            self._rel_annots[annot.key()] = annot

    def annotate_batched_entities(
        self, object_type, items: List[str], entity_names: Optional[List[str]]
    ) -> List[dict]:
        ## An item is a string if object_type == "text", and List[List[dict]] if object_type == "table"
        if entity_names is None:
            # This means that the user did not explicitly specify which entities they want.
            # So, assume our list.
            desired_entities = self.entity_names
        else:
            desired_entities = [
                entity for entity in entity_names if entity in self.entity_names
            ]

        results = []

        ## Iterate over all items, provide all desired entities,
        ## and sort them by category.
        ## (Because many NER models provide multiple entities.)
        for item in items:
            entity_map = {}
            try:
                cps_entities = self.annotate_entities_in_item(
                    object_type, item, desired_entities
                )
            except Exception as exc:
                cps_entities = []
                logger.exception(
                    "Error in annotator for object_type "
                    + object_type
                    + " with this content: "
                    + str(item)
                )
            for entity_name in desired_entities:
                entity_map[entity_name] = [
                    entity for entity in cps_entities if entity["type"] == entity_name
                ]
            results.append(entity_map)

        # print("Entities returned from 'annotate_batched_entities', for type " + object_type)
        # pprint.pprint(results)

        return results

    def annotate_entities_in_item(
        self, object_type: str, item: str, entity_names: Optional[List[str]]
    ) -> List[dict]:
        # In this case entity_names is never None, however since BaseAnnotator defines the signature of this method as
        # Optionally having entity names we must ensure that they are defined.
        if entity_names is None:
            entity_names = []

        ## Annotate one item with the desired entities.
        ## Output: List of entities in CPS format, different for text, table, or images
        if object_type == "text":
            matched_entities = []
            for entity_name in entity_names:
                matched_entities.extend(
                    self._ent_annots[entity_name].annotate_entities_text(item)
                )
            return matched_entities
        # elif object_type == "table":
        #     return self.annotate_entities_table(item, desired_entities)
        # There is already validation in place in the caller (annotate_controller class) so this case will never happen
        # Regardless a return statement is needed for code validation purposes
        return []

    def annotate_batched_relationships(
        self,
        object_type: str,
        items: List[str],
        entities: List[dict],
        relationship_names: Optional[List[str]],
    ) -> List[dict]:
        if relationship_names is None:
            # This means that the user did not explicitly specify which relationships they want.
            # So, assume our list.
            relationship_names = self.relationship_names

        results = []

        # Loop over the text snippets and the entities already matched in those
        for text, entity_map in zip(items, entities):
            result = {}
            # Iterate over all relationships requested by the user
            for relation in relationship_names:
                if relation in self.relationship_names:
                    result[relation] = self._rel_annots[
                        relation
                    ].annotate_relationships_text(text, entity_map)

            if result:
                results.append(result)

        return results

    def annotate_batched_properties(
        self,
        object_type: str,
        items: List,
        entities: List[dict],
        property_names: Optional[List[str]],
    ) -> List[dict]:
        # raise HTTP 501 to indicate method not supported
        raise HTTPException(status_code=501, detail="Property annotation not supported")
