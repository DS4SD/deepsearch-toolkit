from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List, Literal, Optional

WorkflowTaskType = Literal["INPUT", "OUTPUT", "INPUT/OUTPUT", "AUXILIARY"]


@dataclass
class WorkflowTaskOperation:
    type: str
    parameters: Dict[str, Any]
    outputs: Optional[Dict[str, Any]] = field(default=None)


class WorkflowTask:
    operation: WorkflowTaskOperation
    in_edges: List[int]
    out_edges: List[int]
    type: WorkflowTaskType

    def __init__(
        self,
        operation: WorkflowTaskOperation,
        in_edges: List[int],
        type: WorkflowTaskType,
    ) -> None:
        self.operation = operation
        self.type = type
        self.in_edges = in_edges
        self.out_edges: List[int] = []

    def set_as_output(self) -> None:
        """Set this task to provide an output."""

        if self.type == "AUXILIARY":
            self.type = "OUTPUT"

        if self.type == "INPUT":
            self.type = "INPUT/OUTPUT"

    def build(self) -> dict:
        operation = asdict(self.operation)

        if operation["parameters"] is None:
            del operation["parameters"]

        if operation["outputs"] is None:
            del operation["outputs"]

        return {
            "edges": {
                "in": self.in_edges,
                "out": self.out_edges,
            },
            "operation": operation,
            "type": self.type,
        }


class WorkflowBuilder:
    def __init__(self) -> None:
        self._tasks: List[WorkflowTask] = []

    def add(
        self,
        operation: WorkflowTaskOperation,
        *,
        type: WorkflowTaskType = "AUXILIARY",
        inputs: Optional[List[WorkflowTask]] = None,
    ) -> WorkflowTask:
        if inputs is None:
            inputs = []

        t = WorkflowTask(operation, [self.index(t) for t in inputs], type)

        t.out_edges.append(len(self._tasks))

        self._tasks.append(t)

        return t

    def task_at(self, index: int) -> WorkflowTask:
        return self._tasks[index]

    def index(self, task: WorkflowTask) -> int:
        return self._tasks.index(task)

    def build(self) -> List[dict]:
        return [t.build() for t in self._tasks]
