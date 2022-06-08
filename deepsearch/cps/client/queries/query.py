from typing import Any, Dict, List, Optional, TypeVar, Union, overload

from deepsearch.cps.client.queries.task import Task, TaskCoordinates, TaskInputs

TTask = TypeVar("TTask", bound=Task)


class Query:
    def __init__(self) -> None:
        self.tasks: List[Task] = []
        self.variables: Dict[str, Any] = {}
        self.paginated_task: Optional[Task] = None

    @overload
    def add(self, kind_or_task: TTask) -> TTask:
        ...

    @overload
    def add(
        self,
        kind_or_task: str,
        *,
        task_id: Optional[str] = None,
        parameters: Optional[Dict[str, Any]] = None,
        inputs: Optional[TaskInputs] = None,
        coordinates: Optional[TaskCoordinates] = None,
    ) -> Task:
        ...

    def add(
        self,
        kind_or_task: Union[str, Task],
        *,
        task_id: Optional[str] = None,
        parameters: Optional[Dict[str, Any]] = None,
        inputs: Optional[TaskInputs] = None,
        coordinates: Optional[TaskCoordinates] = None,
    ) -> Task:

        if isinstance(kind_or_task, Task):
            task = kind_or_task
        else:
            task = self._build_task(
                kind_or_task,
                task_id=task_id,
                parameters=parameters,
                inputs=inputs,
                coordinates=coordinates,
            )

        if not task.id:
            task.id = f"{len(self.tasks)}_{task.kind}"

        self.tasks.append(task)

        return task

    def _build_task(
        self,
        kind: str,
        *,
        task_id: Optional[str] = None,
        parameters: Optional[Dict[str, Any]] = None,
        inputs: Optional[TaskInputs] = None,
        coordinates: Optional[TaskCoordinates] = None,
    ):
        if inputs is None:
            inputs = {}

        if parameters is None:
            parameters = {}

        if coordinates is None:
            coordinates = {}

        if task_id is None:
            task_id = f"{len(self.tasks)}_{kind}"

        return Task(
            id=task_id,
            kind=kind,
            parameters=parameters,
            inputs=inputs,
            coordinates=coordinates,
        )

    def to_flow(self) -> Dict[str, Any]:
        flow: Dict[str, Any] = {
            "version": "1",
            "tasks": [],
            "outputs": {},
        }

        for task in self.tasks:
            flow["tasks"].append(task.build())

            for output_id, output in task._outputs.items():
                if output.flow_output_name is not None:
                    if output.flow_output_name in flow["outputs"]:
                        raise ValueError(
                            f"Output {output.flow_output_name!r} is already assigned: {flow['outputs'][output.flow_output_name]!r}"
                        )

                    flow["outputs"][output.flow_output_name] = {
                        "task_id": output.task_id,
                        "output_id": output_id,
                        "name": output.flow_output_description,
                    }

        return flow

    @classmethod
    def parse(cls, value: dict) -> "Query":
        raise NotImplementedError
