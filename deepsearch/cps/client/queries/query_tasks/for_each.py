from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, Union

from deepsearch.cps.client.builders.wf_builder import WorkflowBuilder, WorkflowTask
from deepsearch.cps.client.queries.task import (
    InputValue,
    Output,
    Task,
    TaskCoordinates,
    TaskInputs,
    TaskWithWellKnownOutputs,
)

if TYPE_CHECKING:
    from deepsearch.cps.client.queries import Query


@dataclass
class ForEachOutputs:
    result: Output


class ForEach(Task, TaskWithWellKnownOutputs[ForEachOutputs]):
    def __init__(self, *, id: str, query: Query, items: InputValue) -> None:
        super().__init__(
            id=id,
            kind="ForEach",
            parameters={},
            inputs={"items": items},
            coordinates={},
        )

        self.query = query

    def build(self) -> dict:
        self.parameters = {"do": self.query.to_flow()}
        return super().build()

    def current_element(self) -> Dict[str, Any]:
        """Create a placeholder that will inject the current element into the template."""
        return {"#ForEach": {self.id: "CurrentElement"}}

    def current_index(self) -> Dict[str, Any]:
        """Create a placeholder that will inject the current index into the template."""
        return {"#ForEach": {self.id: "CurrentIndex"}}

    def output(self, name: str) -> Output:
        if name != "result":
            raise ValueError("A ForEach only has one output, with name 'result'")

        return super().output(name)

    @property
    def outputs(self) -> ForEachOutputs:
        return ForEachOutputs(result=self.output("result"))
