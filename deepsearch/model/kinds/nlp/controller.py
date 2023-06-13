from typing import cast

from fastapi import HTTPException, status

from deepsearch.model.base.controller import BaseController
from deepsearch.model.base.model import BaseDSModel
from deepsearch.model.base.types import Kind
from deepsearch.model.kinds.nlp.model import BaseNLPModel
from deepsearch.model.kinds.nlp.types import (
    NLPEntitiesControllerOutput,
    NLPEntitiesReqSpec,
    NLPPropertiesControllerOutput,
    NLPPropertiesReqSpec,
    NLPRelationshipsControllerOutput,
    NLPRelationshipsReqSpec,
)
from deepsearch.model.server.inference_types import ControllerInput, ControllerOutput


class NLPController(BaseController):
    def __init__(self, model: BaseNLPModel):
        self._model = model

    def get_kind(self) -> str:
        return Kind.NLPModel

    def _get_model(self) -> BaseDSModel:
        return self._model

    def dispatch_predict(self, spec: ControllerInput) -> ControllerOutput:
        # TODO: use Pydantic objects instead of dicts
        if isinstance(spec, NLPEntitiesReqSpec):
            find_entities_part = cast(NLPEntitiesReqSpec, spec).findEntities
            find_entities_dict = find_entities_part.dict()
            items = self._validate_and_parse_input(find_entities_dict)
            entities = self._model.annotate_batched_entities(
                find_entities_dict["objectType"],
                items,
                find_entities_dict["entityNames"],
            )
            return NLPEntitiesControllerOutput(entities=entities)
        elif isinstance(spec, NLPRelationshipsReqSpec):
            find_relationships_part = cast(
                NLPRelationshipsReqSpec, spec
            ).findRelationships
            find_relationships_dict = find_relationships_part.dict()
            items = self._validate_and_parse_input(find_relationships_dict)
            relationships = self._model.annotate_batched_relationships(
                find_relationships_dict["objectType"],
                items,
                find_relationships_dict["entities"],
                find_relationships_dict["relationshipNames"],
            )
            return NLPRelationshipsControllerOutput(relationships=relationships)
        elif isinstance(spec, NLPPropertiesReqSpec):
            find_properties_part = cast(NLPPropertiesReqSpec, spec).findProperties
            find_properties_dict = find_properties_part.dict()
            items = self._validate_and_parse_input(find_properties_dict)

            if isinstance(items, dict):
                if find_properties_dict.get("entities", None) is None:
                    find_properties_dict["entities"] = [{}] * len(items)
            else:
                raise KeyError("items is not a dictionary")

            properties = self._model.annotate_batched_properties(
                find_properties_dict["objectType"],
                items,
                find_properties_dict["entities"],
                find_properties_dict["propertyNames"],
            )

            return NLPPropertiesControllerOutput(properties=properties)
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Unexpected spec type",
            )

    # TODO replace with pydantic
    def _validate_and_parse_input(self, spec_part) -> list:
        object_type = spec_part.get("objectType", "text")
        expected = ("text", "image", "table")

        if object_type not in expected:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid object type. Expected one of: {expected}",
            )

        if object_type not in (
            supported := self._model.get_nlp_config().supported_types
        ):
            raise HTTPException(
                status_code=400,
                detail=f"Unsupported object type for this model. Supports: {supported}",
            )

        if object_type == "text":
            if not isinstance(spec_part.get("texts"), list):
                raise HTTPException(
                    status_code=400, detail="Invalid input: Missing 'texts'"
                )
            return spec_part["texts"]

        if object_type == "image":
            if not isinstance(spec_part.get("images"), list):
                raise HTTPException(
                    status_code=400, detail="Invalid input: Missing 'images'"
                )

            return spec_part["images"]

        if object_type == "table":
            if not isinstance(spec_part.get("tables"), list):
                raise HTTPException(
                    status_code=400, detail="Invalid input: Missing 'tables'"
                )

            return spec_part["tables"]

        raise HTTPException(
            status_code=500,
            detail=f"Internal Server Error",
        )
