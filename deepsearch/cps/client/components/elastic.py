from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Union

from pydantic.v1 import BaseModel

from deepsearch.cps.apis import public as sw_client
from deepsearch.cps.client.components.data_indices import (
    ElasticProjectDataCollectionSource,
)

if TYPE_CHECKING:
    from deepsearch.cps.client import CpsApi

# Either a raw string, or the entire Elastic query DSL
ElasticSearchQuery = Union[str, Dict[str, Any]]


class CpsApiElastic:
    api: CpsApi

    def __init__(self, api: CpsApi) -> None:
        self.api = api
        self.sw_api = sw_client.ElasticApi(self.api.client.swagger_client)

    def list(self, domain: str = "all") -> List[ElasticDataCollection]:
        response: list[
            sw_client.DataCollection
        ] = self.sw_api.list_indices_from_elastic_instance(
            index_type="all", index_domain=domain
        )

        return [ElasticDataCollection.parse_obj(item.to_dict()) for item in response]


class ElasticDataCollectionSource(BaseModel):
    elastic_id: str
    index_key: str

    def to_resource(self) -> Dict[str, Any]:
        return {
            "type": "elastic",
            "elastic_id": self.elastic_id,
            "index": self.index_key,
        }


class ElasticDataCollectionMetadata(BaseModel):
    description: str
    created: Union[datetime.datetime, str]
    domain: List[str]
    aliases: List[str]
    source: str
    type: str
    version: str


class ElasticDataCollection(BaseModel):

    source: Union[ElasticDataCollectionSource, ElasticProjectDataCollectionSource]
    name: str
    documents: int
    health: str
    status: str
    metadata: ElasticDataCollectionMetadata
