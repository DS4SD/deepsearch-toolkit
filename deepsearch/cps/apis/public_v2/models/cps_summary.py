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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class CPSSummary(BaseModel):
    """
    CPSSummary
    """ # noqa: E501
    avail_cpu_slots: StrictInt = Field(alias="availCpuSlots")
    avail_mem_slots: StrictInt = Field(alias="availMemSlots")
    avail_slots: StrictInt = Field(alias="availSlots")
    name: StrictStr
    num_nodes: StrictInt = Field(alias="numNodes")
    number_kgs: StrictInt = Field(alias="numberKgs")
    running_kgs: StrictInt = Field(alias="runningKgs")
    workers_pool: StrictStr = Field(alias="workersPool")
    __properties: ClassVar[List[str]] = ["availCpuSlots", "availMemSlots", "availSlots", "name", "numNodes", "numberKgs", "runningKgs", "workersPool"]

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
        """Create an instance of CPSSummary from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CPSSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "availCpuSlots": obj.get("availCpuSlots"),
            "availMemSlots": obj.get("availMemSlots"),
            "availSlots": obj.get("availSlots"),
            "name": obj.get("name"),
            "numNodes": obj.get("numNodes"),
            "numberKgs": obj.get("numberKgs"),
            "runningKgs": obj.get("runningKgs"),
            "workersPool": obj.get("workersPool")
        })
        return _obj


