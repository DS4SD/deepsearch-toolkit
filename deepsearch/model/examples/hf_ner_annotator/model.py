import os
from typing import List, Optional, Union

from fastapi import HTTPException, status
from transformers import AutoModelForTokenClassification, AutoTokenizer, pipeline
from transformers.pipelines.token_classification import AggregationStrategy

from deepsearch.model.base.types import Kind, StrictModel
from deepsearch.model.kinds.nlp.model import BaseNLPModel
from deepsearch.model.kinds.nlp.types import (
    AnnotateEntitiesOutput,
    AnnotatePropertiesOutput,
    AnnotateRelationshipsOutput,
    AnnotationLabels,
    EntityLabel,
    NLPConfig,
)


class HuggingFaceNERAnnotator(BaseNLPModel):
    class Config(StrictModel):
        model_name_or_path: Union[str, os.PathLike]
        aggregation_strategy: Optional[AggregationStrategy] = AggregationStrategy.NONE

        class Config:
            arbitrary_types_allowed = True

    def __init__(self, config: Config) -> None:
        super().__init__()

        self._pipeline = pipeline(
            task="token-classification",
            model=AutoModelForTokenClassification.from_pretrained(
                config.model_name_or_path
            ),
            tokenizer=AutoTokenizer.from_pretrained(config.model_name_or_path),
            aggregation_strategy=config.aggregation_strategy,
        )

        label2id = self._pipeline.model.config.label2id
        if config.aggregation_strategy == AggregationStrategy.NONE:
            self._supported_entities = [
                EntityLabel(key=k, description=k) for k in label2id
            ]
            self._label_name = "entity"
        else:
            entity_groups = {lbl.split("-")[-1] for lbl in label2id}
            self._supported_entities = [
                EntityLabel(key=k, description=k) for k in entity_groups
            ]
            self._label_name = "entity_group"

        self._supported_ents_set = {k.key for k in self._supported_entities}

        self._config = NLPConfig(
            kind=Kind.NLPModel,
            name="HuggingFaceNERAnnotator",
            version="0.1.0",
            supported_types=["text"],
            labels=AnnotationLabels(
                entities=self._supported_entities,
                relationships=[],
                properties=[],
            ),
        )

    def get_nlp_config(self) -> NLPConfig:
        return self._config

    def annotate_batched_entities(
        self, object_type: str, items: List[str], entity_names: Optional[List[str]]
    ) -> AnnotateEntitiesOutput:
        relevant_entities = self._resolve_relevant_entities(entity_names)
        results = [
            {
                entity: [
                    {
                        "type": entity,
                        "match": pip_res_entry["word"],
                        "original": pip_res_entry["word"],
                        "range": [pip_res_entry["start"], pip_res_entry["end"]],
                    }
                    for pip_res_entry in item_pip_res
                    if pip_res_entry[self._label_name] == entity
                ]
                for entity in relevant_entities
            }
            for item_pip_res in [self._pipeline(item) for item in items]
        ]
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

    def _resolve_relevant_entities(
        self, entity_names: Optional[List[str]]
    ) -> List[str]:
        if not entity_names:
            result = [x for x in self._supported_ents_set]
        else:
            result = []
            for ent in entity_names:
                if ent not in self._supported_ents_set:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"Requested entity '{ent}' not supported",
                    )
                else:
                    result.append(ent)
        return result
