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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from deepsearch.cps.apis.public_v2.models.model_pipeline_settings_clusters_inner import ModelPipelineSettingsClustersInner
from typing import Optional, Set
from typing_extensions import Self

class ModelPipelineSettings(BaseModel):
    """
    ModelPipelineSettings
    """ # noqa: E501
    clusters: List[ModelPipelineSettingsClustersInner]
    page: List[ModelPipelineSettingsClustersInner]
    tables: List[ModelPipelineSettingsClustersInner]
    normalization: List[ModelPipelineSettingsClustersInner]
    __properties: ClassVar[List[str]] = ["clusters", "page", "tables", "normalization"]

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
        """Create an instance of ModelPipelineSettings from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in clusters (list)
        _items = []
        if self.clusters:
            for _item in self.clusters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['clusters'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in page (list)
        _items = []
        if self.page:
            for _item in self.page:
                if _item:
                    _items.append(_item.to_dict())
            _dict['page'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in tables (list)
        _items = []
        if self.tables:
            for _item in self.tables:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tables'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in normalization (list)
        _items = []
        if self.normalization:
            for _item in self.normalization:
                if _item:
                    _items.append(_item.to_dict())
            _dict['normalization'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ModelPipelineSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clusters": [ModelPipelineSettingsClustersInner.from_dict(_item) for _item in obj["clusters"]] if obj.get("clusters") is not None else None,
            "page": [ModelPipelineSettingsClustersInner.from_dict(_item) for _item in obj["page"]] if obj.get("page") is not None else None,
            "tables": [ModelPipelineSettingsClustersInner.from_dict(_item) for _item in obj["tables"]] if obj.get("tables") is not None else None,
            "normalization": [ModelPipelineSettingsClustersInner.from_dict(_item) for _item in obj["normalization"]] if obj.get("normalization") is not None else None
        })
        return _obj


