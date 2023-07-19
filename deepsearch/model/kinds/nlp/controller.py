import logging

logger = logging.getLogger("root.model")

from fastapi import HTTPException, status

from deepsearch.model.base.controller import BaseController
from deepsearch.model.base.model import BaseDSModel
from deepsearch.model.base.types import Kind
from deepsearch.model.kinds.nlp.model import BaseNLPModel
from deepsearch.model.kinds.nlp.types import (
    FindEntitiesText,
    FindPropertiesText,
    FindRelationshipsText,
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
        logger.info("NLPController Initialized")

    def get_kind(self) -> str:
        logger.info("NLPController return kind")
        return Kind.NLPModel

    def _get_model(self) -> BaseDSModel:
        logger.info("NLPController return model")
        return self._model

    def dispatch_predict(self, spec: ControllerInput) -> ControllerOutput:
        logger.info("NLPModel Dispatching predict")
        cfg = self._model.get_nlp_config()
        type_ok = True

        # currently only addressing text object types
        if (
            isinstance(spec, NLPEntitiesReqSpec)
            and isinstance(spec.findEntities, FindEntitiesText)
            and (type_ok := (spec.findEntities.objectType in cfg.supported_types))
        ):
            logger.info("NLPModel Annotating batched entities")
            entities = self._model.annotate_batched_entities(
                object_type=spec.findEntities.objectType,
                items=spec.findEntities.texts,
                entity_names=spec.findEntities.entityNames,
            )
            return NLPEntitiesControllerOutput(entities=entities)
        elif (
            isinstance(spec, NLPRelationshipsReqSpec)
            and isinstance(spec.findRelationships, FindRelationshipsText)
            and (type_ok := (spec.findRelationships.objectType in cfg.supported_types))
        ):
            logger.info("NLPModel Annotating batched relationships")
            relationships = self._model.annotate_batched_relationships(
                object_type=spec.findRelationships.objectType,
                items=spec.findRelationships.texts,
                entities=spec.findRelationships.entities,
                relationship_names=spec.findRelationships.relationshipNames,
            )
            return NLPRelationshipsControllerOutput(relationships=relationships)
        elif (
            isinstance(spec, NLPPropertiesReqSpec)
            and isinstance(spec.findProperties, FindPropertiesText)
            and (type_ok := (spec.findProperties.objectType in cfg.supported_types))
        ):
            if spec.findProperties.entities is None:
                entities = [{}] * len(spec.findProperties.texts)
            else:
                entities = spec.findProperties.entities
            logger.info("NLPModel Annotating batched properties")
            properties = self._model.annotate_batched_properties(
                object_type=spec.findProperties.objectType,
                items=spec.findProperties.texts,
                entities=entities,
                property_names=spec.findProperties.propertyNames,
            )
            return NLPPropertiesControllerOutput(properties=properties)
        elif not type_ok:
            logger.error("Requested object type not supported by model")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Requested object type not supported by model",
            )
        else:
            logger.error("Unexpected spec type")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Unexpected spec type",
            )
