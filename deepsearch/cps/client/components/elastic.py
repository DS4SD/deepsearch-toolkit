from __future__ import annotations

import datetime
from collections import deque
from copy import deepcopy
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    Iterable,
    Iterator,
    List,
    Optional,
    Union,
)

from pydantic import BaseModel

from deepsearch.cps.apis import public as sw_client
from deepsearch.cps.apis.public.models.elastic_index_search_results import (
    ElasticIndexSearchResults,
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

    def search(
        self,
        instance_name: str,
        index_name: str,
        query: ElasticSearchQuery,
        *,
        source: Optional[List[str]] = None,
        aggregations: Optional[dict] = None,
        start_from: int = 0,
        sort: Optional[List[Dict[str, Any]]] = None,
        size: int = 5,
    ) -> ElasticSearchResult:

        if sort is None:
            sort = [{"file-info.document-hash": "asc"}]

        if isinstance(query, str):
            query = {"query_string": {"query": query}}

        params = {
            "query_options": {
                "from": start_from,
                "query": query,
                "size": size,
                "sort": sort,
            }
        }

        if source is not None:
            params["query_options"]["_source"] = source

        if aggregations is not None:
            params["query_options"]["aggs"] = aggregations

        def fetch_more(params):
            results: ElasticIndexSearchResults = self.sw_api.get_index_search_results(
                instance_name, index_name, params
            )

            return results

        results = fetch_more(params)

        return ElasticSearchResult(self, params, results, fetch_more)


class _PaginatedElasticSearchResult:
    def __init__(self, result: ElasticSearchResult, limit: Optional[int]) -> None:
        self._result = result

        self._items = deque(self._result.items)
        self._limit = result.total if limit is None else limit
        self._params = self._result.params
        self._search_after = [] if not self._items else self._items[-1]["sort"]
        self._yielded = 0
        self._fetch_more = self._result.fetch_more

    def __iter__(self) -> Iterator[dict]:
        return self

    def __next__(self) -> dict:
        if self._yielded >= self._limit:
            raise StopIteration

        if not self._items:
            # Repeat the query to fetch the next page
            params = deepcopy(self._params)

            params["query_options"]["search_after"] = self._search_after

            results = self._fetch_more(params)

            self._items = deque(results.items)

        if self._items:
            self._yielded += 1
            self._search_after = self._items[-1]["sort"]
            return self._items.popleft()

        raise StopIteration


class ElasticSearchResult:

    aggregations: Dict[str, Any]
    total: int
    items: List[dict]

    def __init__(
        self,
        elastic: CpsApiElastic,
        params: dict,
        results: ElasticIndexSearchResults,
        fetch_more: Callable[[dict], ElasticIndexSearchResults],
    ) -> None:
        self._elastic = elastic

        self.aggregations = results.aggregations
        self.total = int(results.total)
        self.items = results.items

        self.params = params
        self.fetch_more = fetch_more

    def paginated(self, *, limit: Optional[int] = 100) -> Iterable[dict]:
        return _PaginatedElasticSearchResult(self, limit)


class ElasticDataCollectionSource(BaseModel):
    elastic_id: str
    index_key: str

    def to_resource(self) -> Dict[str, Any]:
        return {
            "type": "elastic",
            "elastic_id": self.elastic_id,
            "index": self.index_key,
        }


class ElasticProjectDataCollectionSource(BaseModel):
    proj_key: str
    index_key: str

    def to_resource(self) -> Dict[str, Any]:
        return {"type": "elastic", "proj_key": self.proj_key, "index": self.index_key}


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
