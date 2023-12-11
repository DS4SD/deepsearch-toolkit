from typing import List, Optional

from fastapi import HTTPException, status

from deepsearch.model.base.types import Kind
from deepsearch.model.kinds.nlp.model import BaseNLPModel
from deepsearch.model.kinds.nlp.types import (
    AnnotateEntitiesEntry,
    AnnotateEntitiesOutput,
    AnnotatePropertiesOutput,
    AnnotateRelationshipsOutput,
    AnnotationLabels,
    EntityLabel,
    NLPConfig,
)


class DummyNLPAnnotator(BaseNLPModel):
    def __init__(self) -> None:
        super().__init__()

        self._config = NLPConfig(
            kind=Kind.NLPModel,
            name="DummyNLPAnnotator",
            version="0.1.0",
            supported_types=["text"],  # type: ignore[list-item]
            labels=self._generate_labels(),
        )

    def get_nlp_config(self) -> NLPConfig:
        return self._config

    def annotate_batched_entities(
        self,
        object_type: str,
        items: List[str],
        entity_names: Optional[List[str]],
    ) -> AnnotateEntitiesOutput:
        _entity_names = entity_names or ["entity_foo", "entity_bar"]
        results = []
        for item in items:
            results.append(
                {
                    k: [
                        AnnotateEntitiesEntry(
                            type=k,
                            match=f"a '{k}' match in '{item}'",
                            original=f"a '{k}' original in '{item}'",
                            range=[1, 5],
                        ),
                        AnnotateEntitiesEntry(
                            type=k,
                            match=f"another '{k}' match in '{item}'",
                            original=f"another '{k}' original in '{item}'",
                            range=[12, 42],
                        ),
                    ]
                    for k in _entity_names
                }
            )
        return results

    def annotate_batched_relationships(
        self,
        object_type: str,
        items: List[str],
        entities: List[dict],
        relationship_names: Optional[List[str]],
    ) -> AnnotateRelationshipsOutput:
        raise HTTPException(
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            detail="Relationship annotation not supported",
        )

    def annotate_batched_properties(
        self,
        object_type: str,
        items: List[str],
        entities: List[dict],
        property_names: Optional[List[str]],
    ) -> AnnotatePropertiesOutput:
        raise HTTPException(
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            detail="Property annotation not supported",
        )

    def _generate_labels(self) -> AnnotationLabels:
        entities = [
            EntityLabel(key="entity_foo", description="some entity"),
            EntityLabel(key="entity_bar", description="another entity"),
        ]
        return AnnotationLabels(
            entities=entities,
            relationships=[],
            properties=[],
        )
