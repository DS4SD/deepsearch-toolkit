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

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from deepsearch.cps.apis.public_v2.models.aliases import Aliases
from deepsearch.cps.apis.public_v2.models.created import Created
from deepsearch.cps.apis.public_v2.models.description import Description
from deepsearch.cps.apis.public_v2.models.display_name import DisplayName
from deepsearch.cps.apis.public_v2.models.domain import Domain
from deepsearch.cps.apis.public_v2.models.source1 import Source1
from deepsearch.cps.apis.public_v2.models.storage import Storage
from deepsearch.cps.apis.public_v2.models.type import Type
from deepsearch.cps.apis.public_v2.models.version1 import Version1
from typing import Optional, Set
from typing_extensions import Self

class ElasticMetadata(BaseModel):
    """
    ElasticMetadata
    """ # noqa: E501
    aliases: Optional[Aliases] = None
    created: Optional[Created] = None
    description: Optional[Description] = None
    display_name: Optional[DisplayName] = None
    source: Optional[Source1] = None
    storage: Optional[Storage] = None
    version: Optional[Version1] = None
    type: Optional[Type] = None
    domain: Optional[Domain] = None
    classification: List[StrictStr]
    __properties: ClassVar[List[str]] = ["aliases", "created", "description", "display_name", "source", "storage", "version", "type", "domain", "classification"]

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
        """Create an instance of ElasticMetadata from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of aliases
        if self.aliases:
            _dict['aliases'] = self.aliases.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created
        if self.created:
            _dict['created'] = self.created.to_dict()
        # override the default output from pydantic by calling `to_dict()` of description
        if self.description:
            _dict['description'] = self.description.to_dict()
        # override the default output from pydantic by calling `to_dict()` of display_name
        if self.display_name:
            _dict['display_name'] = self.display_name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of storage
        if self.storage:
            _dict['storage'] = self.storage.to_dict()
        # override the default output from pydantic by calling `to_dict()` of version
        if self.version:
            _dict['version'] = self.version.to_dict()
        # override the default output from pydantic by calling `to_dict()` of type
        if self.type:
            _dict['type'] = self.type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of domain
        if self.domain:
            _dict['domain'] = self.domain.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ElasticMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aliases": Aliases.from_dict(obj["aliases"]) if obj.get("aliases") is not None else None,
            "created": Created.from_dict(obj["created"]) if obj.get("created") is not None else None,
            "description": Description.from_dict(obj["description"]) if obj.get("description") is not None else None,
            "display_name": DisplayName.from_dict(obj["display_name"]) if obj.get("display_name") is not None else None,
            "source": Source1.from_dict(obj["source"]) if obj.get("source") is not None else None,
            "storage": Storage.from_dict(obj["storage"]) if obj.get("storage") is not None else None,
            "version": Version1.from_dict(obj["version"]) if obj.get("version") is not None else None,
            "type": Type.from_dict(obj["type"]) if obj.get("type") is not None else None,
            "domain": Domain.from_dict(obj["domain"]) if obj.get("domain") is not None else None,
            "classification": obj.get("classification")
        })
        return _obj


