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
from typing import Optional
from deepsearch.cps.apis.public_v2.models.elastic_index_property_object import ElasticIndexPropertyObject
from deepsearch.cps.apis.public_v2.models.elastic_index_property_primitive import ElasticIndexPropertyPrimitive
from typing import Union, Any, List, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field

PROPERTIES_ANY_OF_SCHEMAS = ["ElasticIndexPropertyObject", "ElasticIndexPropertyPrimitive"]

class Properties(BaseModel):
    """
    Properties
    """

    # data type: ElasticIndexPropertyPrimitive
    anyof_schema_1_validator: Optional[ElasticIndexPropertyPrimitive] = None
    # data type: ElasticIndexPropertyObject
    anyof_schema_2_validator: Optional[ElasticIndexPropertyObject] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[ElasticIndexPropertyObject, ElasticIndexPropertyPrimitive]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: List[str] = Field(default=Literal["ElasticIndexPropertyObject", "ElasticIndexPropertyPrimitive"])

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
        instance = Properties.model_construct()
        error_messages = []
        # validate data type: ElasticIndexPropertyPrimitive
        if not isinstance(v, ElasticIndexPropertyPrimitive):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ElasticIndexPropertyPrimitive`")
        else:
            return v

        # validate data type: ElasticIndexPropertyObject
        if not isinstance(v, ElasticIndexPropertyObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ElasticIndexPropertyObject`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in Properties with anyOf schemas: ElasticIndexPropertyObject, ElasticIndexPropertyPrimitive. Details: " + ", ".join(error_messages))
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
        # anyof_schema_1_validator: Optional[ElasticIndexPropertyPrimitive] = None
        try:
            instance.actual_instance = ElasticIndexPropertyPrimitive.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[ElasticIndexPropertyObject] = None
        try:
            instance.actual_instance = ElasticIndexPropertyObject.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into Properties with anyOf schemas: ElasticIndexPropertyObject, ElasticIndexPropertyPrimitive. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], ElasticIndexPropertyObject, ElasticIndexPropertyPrimitive]]:
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


