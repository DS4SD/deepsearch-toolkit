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


class Workflow(Task):
    def __init__(
        self,
        *,
        id: str,
        builder: WorkflowBuilder,
        inputs: TaskInputs,
        coordinates: TaskCoordinates,
    ) -> None:
        super().__init__(
            id=id,
            kind="Workflow",
            parameters={},
            inputs=inputs,
            coordinates=coordinates,
        )

        self._builder = builder

    def build(self) -> dict:
        self.parameters = {"workflow": self._builder.build()}
        return super().build()

    def output(self, name: Union[str, WorkflowTask]) -> Output:
        if isinstance(name, str):
            task = self._builder.task_at(int(name))
        else:
            task = name

        task.set_as_output()

        return super().output(str(self._builder.index(task)))
