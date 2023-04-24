# Interface -> defines mandatory functions for annotators
from abc import ABCMeta, abstractproperty
from typing import List, Optional, Union

from fastapi import HTTPException
from pydantic import BaseModel, ValidationError


class BaseAnnotator_properties(ABCMeta):

    supports = (
        entities
    ) = (
        relationships
    ) = (
        properties
    ) = (
        name
    ) = version = url = author = description = expected_compute_time = abstractproperty

    def __call__(self, *args, **kwargs):
        obj = super(BaseAnnotator_properties, self).__call__(*args, **kwargs)
        try:
            getattr(obj, "supports")
        except AttributeError:
            self.supports = []
        try:
            getattr(obj, "entities")
        except AttributeError:
            self.entities = []
        try:
            getattr(obj, "relationships")
        except AttributeError:
            self.relationships = []
        try:
            getattr(obj, "properties")
        except AttributeError:
            self.properties = []
        try:
            getattr(obj, "name")
        except AttributeError:
            self.name = "undefined"
        try:
            getattr(obj, "version")
        except AttributeError:
            self.version = "undefined"
        try:
            getattr(obj, "url")
        except AttributeError:
            self.url = "undefined"
        try:
            getattr(obj, "author")
        except AttributeError:
            self.author = "undefined"
        try:
            getattr(obj, "description")
        except AttributeError:
            self.description = "undefined"
        try:
            getattr(obj, "expected_compute_time")
        except AttributeError:
            self.expected_compute_time = 1.0
        try:
            getattr(obj, "kind")
        except AttributeError:
            self.kind = "undefined"

        return obj


class BaseAnnotator(metaclass=BaseAnnotator_properties):

    kind: str
    supports: Union[tuple, list]
    name: str
    version: str
    url: str
    author: str
    description: str
    expected_compute_time: float
    labels: dict

    def annotate_batched_entities(
        self, object_type: str, items: List, entity_names: Optional[List[str]]
    ) -> List[dict]:
        results = []
        for item in items:
            try:
                results.append(
                    self.annotate_entities(object_type, item, entity_names)[0]
                )
            except HTTPException as e:
                raise e
        return results

    def annotate_batched_properties(
        self,
        object_type: str,
        items: List,
        entities: List[dict],
        property_names: Optional[List[str]],
    ) -> List[dict]:
        results = []
        for item, entity in zip(items, entities):
            try:
                results.append(
                    self.annotate_properties(object_type, item, entity, property_names)[
                        0
                    ]
                )
            except HTTPException as e:
                raise e
        return results

    def annotate_batched_relationships(
        self,
        object_type: str,
        items: List,
        entities: List[dict],
        relationship_names: Optional[List[str]],
    ) -> List[dict]:
        results = []
        for item, entity in zip(items, entities):
            try:
                results.append(
                    self.annotate_relationships(
                        object_type, item, entity, relationship_names
                    )[0]
                )
            except HTTPException as e:
                raise e
        return results

    def annotate_entities(
        self, object_type: str, item: List, entity_names: Optional[List[str]]
    ) -> List[dict]:
        raise HTTPException(
            status_code=501, detail="Unsuported Operation for annotator: findEntities"
        )

    def annotate_properties(
        self,
        object_type: str,
        item: str,
        entity: dict,
        property_names: Optional[List[str]],
    ) -> List[dict]:
        # Incomplete
        raise HTTPException(
            status_code=501, detail="Unsuported Operation for annotator: findProperties"
        )

    def annotate_relationships(
        self,
        object_type: str,
        item: str,
        entity: dict,
        relationship_names: Optional[List[str]],
    ) -> List[dict]:
        # Incomplete
        raise HTTPException(
            status_code=501,
            detail="Unsuported Operation for annotator: findRelationships",
        )

    def get_annotator_info(self) -> dict:
        annotator_info = {
            "definitions": {
                # The extensive url in the issue proposition
                "apiVersion": "v1",
                "kind": self.kind,
                "spec": {
                    "metadata": {
                        "name": self.name,
                        "version": self.version,
                        "url": self.url,
                        "author": self.author,
                        "description": self.description,
                        "expected_compute_time": self.expected_compute_time,
                        "supported_object_types": self.supports,
                    },
                    "definition": self.labels,
                },
            }
        }

        return annotator_info

    # def get_entity_names(self):
    #     return self.annotator_info["spec"]["definition"]["entities"]
    #
    # def get_relationship_names(self):
    #     return self.annotator_info["spec"]["definition"]["entities"]
    #
    # def get_property_names(self):
    #     return self.annotator_info["spec"]["definition"]["entities"]
