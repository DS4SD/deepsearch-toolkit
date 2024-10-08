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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from deepsearch.cps.apis.public_v2.models.partial_direct_conversion_parameters import PartialDirectConversionParameters
from deepsearch.cps.apis.public_v2.models.target_conversion_parameters import TargetConversionParameters
from typing import Optional, Set
from typing_extensions import Self

class ConvertDocumentsRequestBody(BaseModel):
    """
    ConvertDocumentsRequestBody
    """ # noqa: E501
    conversion_settings: Optional[PartialDirectConversionParameters] = Field(default=None, description="Specify the conversion settings to use.")
    target_settings: Optional[TargetConversionParameters] = Field(default=None, description="Specify the target settings to use.")
    document_hashes: Optional[List[StrictStr]] = Field(default=None, description="List of document hashes to be used as filter.")
    without_operations: Optional[List[StrictStr]] = Field(default=None, description="List of Operation Status documents don't have to be used as filter.")
    upload_to_elastic: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["conversion_settings", "target_settings", "document_hashes", "without_operations", "upload_to_elastic"]

    @field_validator('without_operations')
    def without_operations_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['PENDING', 'FAILURE', 'SUCCESS']):
                raise ValueError("each list item must be one of ('PENDING', 'FAILURE', 'SUCCESS')")
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
        """Create an instance of ConvertDocumentsRequestBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of conversion_settings
        if self.conversion_settings:
            _dict['conversion_settings'] = self.conversion_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of target_settings
        if self.target_settings:
            _dict['target_settings'] = self.target_settings.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConvertDocumentsRequestBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "conversion_settings": PartialDirectConversionParameters.from_dict(obj["conversion_settings"]) if obj.get("conversion_settings") is not None else None,
            "target_settings": TargetConversionParameters.from_dict(obj["target_settings"]) if obj.get("target_settings") is not None else None,
            "document_hashes": obj.get("document_hashes"),
            "without_operations": obj.get("without_operations"),
            "upload_to_elastic": obj.get("upload_to_elastic")
        })
        return _obj


