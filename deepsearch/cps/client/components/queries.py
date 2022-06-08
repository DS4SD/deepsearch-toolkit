from __future__ import annotations

import json
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, Iterable, Optional, Union

from requests.models import HTTPError

from deepsearch.cps.client.queries import Query

if TYPE_CHECKING:
    from deepsearch.cps.client import CpsApi


class CpsApiQueries:
    def __init__(self, api: CpsApi) -> None:
        self.api = api

    def run(self, query: Union[Query, dict]) -> RunQueryResult:
        if isinstance(query, Query):
            query_flow = query.to_flow()
            variables = query.variables
        else:
            query_flow = query
            variables = {}

        response = self.api.client.session.post(
            f"{self.api.client.config.host}/api/orchestrator/api/v1/query/run",
            json={"query": {"template": query_flow, "variables": variables}},
            headers={
                "X-Authorization": self.api.client.session.headers["Authorization"],
            },
        )

        try:
            response.raise_for_status()
        except HTTPError:
            if response.status_code in (400, 500):
                try:
                    err = response.json()
                    raise RunQueryError(**err) from None
                except json.decoder.JSONDecodeError:
                    raise Exception(response.text) from None
            raise

        contents = response.json()
        result: dict = contents["result"]

        return RunQueryResult(
            outputs=result["outputs"],
            next_pages=result.get("next_pages", {}),
            timings=RunQueryResult.QueryTimings(
                overall=result["timings"]["overall"],
                tasks={
                    k: RunQueryResult.QueryTimings.TaskTimings(**v)
                    for k, v in result["timings"]["tasks"].items()
                },
            ),
        )

    def run_paginated_query(
        self,
        query: Query,
        max_page_count: Optional[int] = None,
    ) -> Iterable[RunQueryResult]:
        if query.paginated_task is None:
            raise ValueError("No paginated task set, set one on 'query.paginated_task'")

        page_count = 0
        task = query.paginated_task
        result = None

        while True:
            if max_page_count is not None and page_count == max_page_count:
                break

            if result is not None:
                if task.id not in result.next_pages:
                    yield result
                    break

                # Update the parameters to point to the next page.
                task.parameters.update(result.next_pages[task.id])

            result = self.run(query)

            page_count += 1

            yield result


@dataclass
class RunQueryResult:
    outputs: Dict[str, Any]
    next_pages: Dict[str, Any]

    @dataclass
    class QueryTimings:
        overall: float

        @dataclass
        class TaskTimings:
            overall: float
            details: Any

        tasks: Dict[str, TaskTimings]

    timings: QueryTimings


class RunQueryError(Exception):
    task_id: Optional[str]
    message: str
    error_type: str
    detail: Optional[dict]

    def __init__(
        self, task_id: Optional[str], message: str, error_type: str, detail: dict
    ) -> None:
        super().__init__(message)

        self.task_id = task_id
        self.message = message
        self.error_type = error_type
        self.detail = detail

    def __str__(self) -> str:
        full_err_parts = [
            f"- Error Type: {self.error_type!r}",
        ]

        if self.detail:
            full_err_parts.append(f"- Detail: {self.detail!r}")

        if self.task_id:
            full_err_parts.append(f"- Task ID: {self.task_id!r}")

        full_err = "\n".join(full_err_parts)

        return f"{self.message}. Full error:\n{full_err}"
