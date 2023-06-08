from typing import cast

from fastapi import HTTPException

from deepsearch.model.base.base_nlp_annotator import BaseNLPModel
from deepsearch.model.controllers.base_controller import BaseController
from deepsearch.model.server.request_schemas import (
    InferenceReqSpec,
    NLPEntitiesReqSpec,
    NLPPropertiesReqSpec,
    NLPRelationshipsReqSpec,
)


class NLPController(BaseController):
    def dispatch_predict(self, spec: InferenceReqSpec) -> dict:
        model = cast(BaseNLPModel, self._model)

        if isinstance(spec, NLPEntitiesReqSpec):
            find_entities_part = cast(NLPEntitiesReqSpec, spec).findEntities.dict()
            items = self._validate_and_parse_input(find_entities_part)
            entities = model.annotate_batched_entities(
                find_entities_part["objectType"],
                items,
                find_entities_part["entityNames"],
            )
            return {"entities": entities}
        elif isinstance(spec, NLPRelationshipsReqSpec):
            find_relationships_part = cast(
                NLPRelationshipsReqSpec, spec
            ).findRelationships.dict()
            items = self._validate_and_parse_input(find_relationships_part)
            relationships = model.annotate_batched_relationships(
                find_relationships_part["objectType"],
                items,
                find_relationships_part["entities"],
                find_relationships_part["relationshipNames"],
            )
            return {"relationships": relationships}
        elif isinstance(spec, NLPPropertiesReqSpec):
            find_properties_part = cast(
                NLPPropertiesReqSpec, spec
            ).findProperties.dict()
            items = self._validate_and_parse_input(find_properties_part)

            if isinstance(items, dict):
                if find_properties_part.get("entities", None) is None:
                    find_properties_part["entities"] = [{}] * len(items)
            else:
                raise KeyError("items is not a dictionary")

            properties = model.annotate_batched_properties(
                find_properties_part["objectType"],
                items,
                find_properties_part["entities"],
                find_properties_part["propertyNames"],
            )

            return {"properties": properties}
        else:
            raise HTTPException(
                status_code=500, detail=f"Internal Server Error", headers={}
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

        if object_type not in self._model.supports:
            raise HTTPException(
                status_code=400,
                detail=f"Unsupported object type for this model. Supports: {self._model.supports}",
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
