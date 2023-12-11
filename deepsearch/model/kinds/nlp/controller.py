from fastapi import HTTPException, status

from deepsearch.model.base.controller import BaseController
from deepsearch.model.base.model import BaseDSModel
from deepsearch.model.base.types import Kind
from deepsearch.model.kinds.nlp.model import BaseNLPModel
from deepsearch.model.kinds.nlp.types import (
    FindEntitiesText,
    FindPropertiesText,
    FindRelationshipsText,
    NLPEntitiesReqSpec,
    NLPEntsCtrlPredOuput,
    NLPInfoOutput,
    NLPInfoOutputDefinitions,
    NLPInfoOutputDefinitionsSpec,
    NLPModelMetadata,
    NLPPropertiesReqSpec,
    NLPPropsCtrlPredOutput,
    NLPRelationshipsReqSpec,
    NLPRelsCtrlPredOutput,
)
from deepsearch.model.server.inference_types import CtrlPredInput, CtrlPredOutput


class NLPController(BaseController):
    def __init__(self, model: BaseNLPModel):
        self._model = model

    def get_info(self) -> NLPInfoOutput:
        cfg = self._model.get_nlp_config()
        metadata = NLPModelMetadata(
            supported_object_types=cfg.supported_types,  # type: ignore[arg-type]
            **self._get_metadata().dict(),  # passing parent metadata dict as kwargs
        )
        spec = NLPInfoOutputDefinitionsSpec(
            definition=cfg.labels.dict(),
            metadata=metadata,
        )
        definitions = NLPInfoOutputDefinitions(
            apiVersion=self._get_api_version(),
            kind=self.get_kind(),  # type: ignore[arg-type]
            spec=spec,
        )
        return NLPInfoOutput(definitions=definitions)

    def get_kind(self) -> str:
        return Kind.NLPModel

    def _get_model(self) -> BaseDSModel:
        return self._model

    def dispatch_predict(self, spec: CtrlPredInput) -> CtrlPredOutput:
        cfg = self._model.get_nlp_config()
        type_ok = True

        # currently only addressing text object types
        if (
            isinstance(spec, NLPEntitiesReqSpec)
            and isinstance(spec.findEntities, FindEntitiesText)
            and (type_ok := (spec.findEntities.objectType in cfg.supported_types))
        ):
            entities = self._model.annotate_batched_entities(
                object_type=spec.findEntities.objectType,
                items=spec.findEntities.texts,
                entity_names=spec.findEntities.entityNames,
            )
            return NLPEntsCtrlPredOuput(entities=entities)
        elif (
            isinstance(spec, NLPRelationshipsReqSpec)
            and isinstance(spec.findRelationships, FindRelationshipsText)
            and (type_ok := (spec.findRelationships.objectType in cfg.supported_types))
        ):
            relationships = self._model.annotate_batched_relationships(
                object_type=spec.findRelationships.objectType,
                items=spec.findRelationships.texts,
                entities=spec.findRelationships.entities,
                relationship_names=spec.findRelationships.relationshipNames,
            )
            return NLPRelsCtrlPredOutput(relationships=relationships)
        elif (
            isinstance(spec, NLPPropertiesReqSpec)
            and isinstance(spec.findProperties, FindPropertiesText)
            and (type_ok := (spec.findProperties.objectType in cfg.supported_types))
        ):
            if spec.findProperties.entities is None:
                entities = [{}] * len(spec.findProperties.texts)
            else:
                entities = spec.findProperties.entities
            properties = self._model.annotate_batched_properties(
                object_type=spec.findProperties.objectType,
                items=spec.findProperties.texts,
                entities=entities,
                property_names=spec.findProperties.propertyNames,
            )
            return NLPPropsCtrlPredOutput(properties=properties)
        elif not type_ok:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Requested object type not supported by model",
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Unexpected spec type",
            )
