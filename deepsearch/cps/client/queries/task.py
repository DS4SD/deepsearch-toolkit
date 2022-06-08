from typing import (
    Any,
    Dict,
    Optional,
    Protocol,
    Tuple,
    TypeVar,
    Union,
    overload,
    runtime_checkable,
)


@runtime_checkable
class Resource(Protocol):
    """Models which implement this Protocol can be passed as coordinates to tasks"""

    def to_resource(self) -> Dict[str, Any]:
        ...


class Output:
    def __init__(self, *, task_id: str, output_id: str) -> None:
        self.task_id = task_id
        self.output_id = output_id

        self.flow_output_name: Optional[str] = None
        self.flow_output_description: Optional[str] = None

    def output_as(self, name: str, description: Optional[str] = None) -> None:
        self.flow_output_name = name
        self.flow_output_description = description


class Value:
    def __init__(self, value: Any) -> None:
        self.value = value


InputValue = Union[Output, Value]

TaskInputs = Dict[str, InputValue]
TaskCoordinates = Union[
    Dict[str, Any], Resource, Tuple[Union[Dict[str, Any], Resource], ...]
]

TOutputs = TypeVar("TOutputs", covariant=True)


class TaskWithWellKnownOutputs(Protocol[TOutputs]):
    @property
    def outputs(self) -> TOutputs:
        ...


class Task:
    def __init__(
        self,
        *,
        id: str,
        kind: str,
        parameters: Dict[str, Any],
        inputs: TaskInputs,
        coordinates: TaskCoordinates,
    ) -> None:
        self.id = id
        self.kind = kind
        self.parameters = parameters
        self.inputs = inputs
        self.coordinates = coordinates
        self._outputs: Dict[str, Output] = {}

    def output(self, name: str) -> Output:
        if name not in self._outputs:
            self._outputs[name] = Output(task_id=self.id, output_id=name)

        return self._outputs[name]

    def build(self) -> Dict[str, Any]:
        result = {
            "id": self.id,
            "kind": self.kind,
            "inputs": self._build_inputs(),
            "parameters": self.parameters,
        }

        # Top-level resources that are used as coordinates
        # need to be put top-level, instead of the coordinates.
        if isinstance(self.coordinates, Resource):
            result.update(self._build_coordinates())
        else:
            result["coordinates"] = self._build_coordinates()

        return result

    def _build_inputs(self) -> Dict[str, Any]:
        inputs = {}

        for input_name, input in self.inputs.items():
            if isinstance(input, Output):
                inputs[input_name] = {
                    "task_id": input.task_id,
                    "output_id": input.output_id,
                }
            elif isinstance(input, Value):
                inputs[input_name] = {"literal": input.value}
            else:
                raise ValueError(f"Unknown input: {input_name}={input!r}")

        return inputs

    def _build_coordinates(self) -> Dict[str, Any]:
        @overload
        def _build(value: Dict[str, Any]) -> Dict[str, Any]:
            ...

        @overload
        def _build(value: TaskCoordinates) -> Dict[str, Any]:
            ...

        def _build(value: Any) -> Any:
            if isinstance(value, tuple):
                result = {}

                for item in value:
                    result.update(_build(item))

                return result

            if isinstance(value, list):
                return [_build(v) for v in value]

            if isinstance(value, dict):
                return {k: _build(v) for k, v in value.items()}

            if isinstance(value, Resource):
                return {"@resource": value.to_resource()}

            return value

        return _build(self.coordinates)

    @classmethod
    def parse(cls, value: dict) -> "Task":
        raise NotImplementedError
