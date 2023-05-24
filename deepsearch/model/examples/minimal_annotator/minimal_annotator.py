from typing import List, Optional

from fastapi import HTTPException

from deepsearch.model.base.base_nlp_annotator import BaseNLPAnnotator


class MinimalAnnotator(BaseNLPAnnotator):

    name = "MinimalAnnotator"
    supports = ["text"]

    def annotate_batched_entities(
        self,
        object_type: str,
        items: List[str],
        entity_names: Optional[List[str]],
    ) -> List[dict]:
        _entity_names = entity_names or ["entity_foo", "entity_bar"]
        results = []
        for item in items:
            results.append(
                {
                    k: [
                        {
                            "type": k,
                            "match": f"a '{k}' match in '{item}'",
                            "original": f"a '{k}' original in '{item}'",
                            "range": [1, 5],
                        },
                        {
                            "type": k,
                            "match": f"another '{k}' match in '{item}'",
                            "original": f"another '{k}' original in '{item}'",
                            "range": [12, 42],
                        },
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
    ) -> List[dict]:
        # raise HTTP 501 to indicate method not supported
        raise HTTPException(
            status_code=501, detail="Relationship annotation not supported"
        )

    def annotate_batched_properties(
        self,
        object_type: str,
        items: List[str],
        entities: List[dict],
        property_names: Optional[List[str]],
    ) -> List[dict]:
        # raise HTTP 501 to indicate method not supported
        raise HTTPException(status_code=501, detail="Property annotation not supported")
