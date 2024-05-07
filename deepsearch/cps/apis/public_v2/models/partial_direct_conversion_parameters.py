# coding: utf-8

"""
    Deep Search (DS) API

    API for Deep Search.  **WARNING**: This API is subject to change without warning!

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from deepsearch.cps.apis.public_v2.models.assemble_settings import AssembleSettings
from deepsearch.cps.apis.public_v2.models.collection_metadata_settings import CollectionMetadataSettings
from deepsearch.cps.apis.public_v2.models.model_pipeline_settings import ModelPipelineSettings
from deepsearch.cps.apis.public_v2.models.ocr_settings import OcrSettings
from typing import Optional, Set
from typing_extensions import Self

class PartialDirectConversionParameters(BaseModel):
    """
    Specify conversion settings (OCR, Assemble, ML Models) directly.  Fields left null are set to platform defaults.
    """ # noqa: E501
    type: Optional[StrictStr] = 'direct'
    ocr: Optional[OcrSettings] = None
    assemble: Optional[AssembleSettings] = None
    metadata: Optional[CollectionMetadataSettings] = None
    page_labels: Optional[Dict[str, Dict[str, Any]]] = None
    model_pipeline: Optional[ModelPipelineSettings] = None
    __properties: ClassVar[List[str]] = ["type", "ocr", "assemble", "metadata", "page_labels", "model_pipeline"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['direct']):
            raise ValueError("must be one of enum values ('direct')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PartialDirectConversionParameters from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of ocr
        if self.ocr:
            _dict['ocr'] = self.ocr.to_dict()
        # override the default output from pydantic by calling `to_dict()` of assemble
        if self.assemble:
            _dict['assemble'] = self.assemble.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of model_pipeline
        if self.model_pipeline:
            _dict['model_pipeline'] = self.model_pipeline.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PartialDirectConversionParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type") if obj.get("type") is not None else 'direct',
            "ocr": OcrSettings.from_dict(obj["ocr"]) if obj.get("ocr") is not None else None,
            "assemble": AssembleSettings.from_dict(obj["assemble"]) if obj.get("assemble") is not None else None,
            "metadata": CollectionMetadataSettings.from_dict(obj["metadata"]) if obj.get("metadata") is not None else None,
            "model_pipeline": ModelPipelineSettings.from_dict(obj["model_pipeline"]) if obj.get("model_pipeline") is not None else None
        })
        return _obj

