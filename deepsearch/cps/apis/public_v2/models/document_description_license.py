# coding: utf-8

"""
    Deep Search (DS) API

    API for Deep Search.  **WARNING**: This API is subject to change without warning!

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, Optional
from deepsearch.cps.apis.public_v2.models.description_license import DescriptionLicense
from typing import Union, Any, List, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field

DOCUMENTDESCRIPTIONLICENSE_ANY_OF_SCHEMAS = ["DescriptionLicense", "object"]

class DocumentDescriptionLicense(BaseModel):
    """
    DocumentDescriptionLicense
    """

    # data type: DescriptionLicense
    anyof_schema_1_validator: Optional[DescriptionLicense] = None
    # data type: object
    anyof_schema_2_validator: Optional[Any] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[DescriptionLicense, object]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: List[str] = Field(default=Literal["DescriptionLicense", "object"])

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        instance = DocumentDescriptionLicense.model_construct()
        error_messages = []
        # validate data type: DescriptionLicense
        if not isinstance(v, DescriptionLicense):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DescriptionLicense`")
        else:
            return v

        # validate data type: object
        try:
            instance.anyof_schema_2_validator = v
            return v
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in DocumentDescriptionLicense with anyOf schemas: DescriptionLicense, object. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[DescriptionLicense] = None
        try:
            instance.actual_instance = DescriptionLicense.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # deserialize data into object
        try:
            # validation
            instance.anyof_schema_2_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.anyof_schema_2_validator
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into DocumentDescriptionLicense with anyOf schemas: DescriptionLicense, object. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], DescriptionLicense, object]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


