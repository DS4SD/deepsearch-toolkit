import json
from typing import Any, Dict, List, Optional, Sequence, Union

from .MultiLinkedList import MultiLinkedList, Node


class Workflow:
    def __init__(self, starting_node=None):
        self._operations = MultiLinkedList(starting_node)

    def __add__(self, workflow):
        if isinstance(workflow, Workflow):
            return self.sum(workflow)
        else:
            raise TypeError(
                f"Invalid object type {type(workflow).__name__} should be Workflow."
            )

    def __and__(self, workflow):
        if isinstance(workflow, Workflow):
            return self.intersect(workflow)
        else:
            raise TypeError(
                f"Invalid object type {type(workflow).__name__} should be Workflow."
            )

    def __or__(self, workflow):
        if isinstance(workflow, Workflow):
            return self.combine(workflow)
        else:
            raise TypeError(
                f"Invalid object type {type(workflow).__name__} should be Workflow."
            )

    def __mul__(self, workflow):
        if isinstance(workflow, Workflow):
            return self.multiply(workflow)
        else:
            raise TypeError(
                f"Invalid object type {type(workflow).__name__} should be Workflow."
            )

    def as_output(self, limit: Optional[int] = None):
        """
        Set node type as output
        :param limit: Response limit
        :type limit: int
        """
        last_op = self._operations.tail.data
        if last_op["type"] == "INPUT":
            last_op["type"] = "INPUT/OUTPUT"
        elif last_op["type"] == "AUXILIARY":
            last_op["type"] = "OUTPUT"

        if limit is not None:
            last_op["parameters"]["limit"] = limit

        self._operations.tail.data = last_op
        return self

    def search_nodes_containing(self, *args: List[str], include: List["Workflow"] = []):
        """
        Search nodes that contain the args
        :param `*args`: the search arguments
        :type `*args`: List[str]
        :param include: Include nodes in operation
        :type include: List['Workflow']
        """
        operation = {
            "type": "SEARCH",
            "parameters": {"type": "contains", "names": args},
        }
        self._add_with_requirements(operation, include)
        return self

    def search_nodes_equal(self, *args: List[str], include: List["Workflow"] = []):
        """
        Search nodes that equal the args
        :param `*args`: the search arguments
        :type `*args`: List[str]
        :param include: Include nodes in operation
        :type include: List['Workflow']
        """
        operation = {"type": "SEARCH", "parameters": {"type": "equal", "names": args}}
        self._add_with_requirements(operation, include)
        return self

    def search_nodes_by_db_id_pair(
        self, *args: List[Dict[str, str]], include: List["Workflow"] = []
    ):
        """
        Search nodes that contain the db\id pair
        :param `*args`: the db\id pairs in format {"_db": "db value", "_id": "id value"}
        :type `*args`: List[str]
        :param include: Include nodes in operation
        :type include: List['Workflow']
        """
        operation = {"type": "SEARCH", "parameters": {"ids": args}}
        self._add_with_requirements(operation, include)
        return self

    def search_nodes_by_index(
        self,
        indices: List[str] = [],
        weights: List[float] = [],
        include: List["Workflow"] = [],
    ):
        """
        Search nodes by index
        :param indices: the indices to search
        :type indices: str
        :param weights: the weight to search
        :type weights: float
        :param include: Include nodes in operation
        :type include: List['Workflow']
        """
        operation = {
            "type": "SEARCH",
            "parameters": {"indices": indices, "weights": weights},
        }
        self._add_with_requirements(operation, include)
        return self

    def search_nodes_by_regex(self, *args: List[str], include: List["Workflow"] = []):
        """
        Search nodes by regex that match args
        :param `*args`: the search arguments
        :type `*args`: List[str]
        :param include: Include nodes in operation
        :type include: List['Workflow']
        """
        operation = {"type": "SEARCH", "parameters": {"type": "regex", "names": args}}
        self._add_with_requirements(operation, include)
        return self

    def search_nodes_by_approximation(
        self, *args: List[str], tolerance: float = 0.8, include: List["Workflow"] = []
    ):
        """
        Search nodes where the arguments are approximate
        :param `*args`: the search arguments
        :type `*args`: List[str]
        :param tolerance: the tolerance
        :type tolerance: float
        :param include: Include nodes in operation
        :type include: List['Workflow']
        """
        operation = {
            "type": "SEARCH",
            "parameters": {"type": "approximate", "names": args, "epsilon": tolerance},
        }
        self._add_with_requirements(operation, include)
        return self

    def search_nodes_in_category(
        self, *categories: List[str], include: List["Workflow"] = []
    ):
        """
        Search nodes in categories
        :param categories: the categories to search
        :type categories: List[str]
        :param include: Include nodes in operation
        :type include: List['Workflow']
        """
        operation = {"type": "SEARCH", "parameters": {"categories": categories}}
        self._add_with_requirements(operation, include)
        return self

    def set_to_field_value(self, field_name: str = "", include: List["Workflow"] = []):
        """
        Set node to field value
        :param field_name: The field name
        :type field_name: str
        :param include: Include nodes in operation
        :type include: List['Workflow']
        """
        operation = {
            "type": "SET_TO_FIELDVALUE",
            "parameters": {"fieldname": field_name},
        }
        self._add_with_requirements(operation, include)
        return self

    def filter(
        self,
        filter_type: str = "cut-off",
        field_operation: str = "==",
        field_value: str = "",
        include: List["Workflow"] = [],
    ):
        """
        Filter values
        :param filter_type: Filter type. Possible values "cut-off", "field-value"
        :type filter_type: str
        :param field_operation: The field operation to use if filter type is "field-value". Possible values "<", "==", ">"
        :type field_operation: str
        :param field_value: The field value to filter by
        :type field_value: str
        :param include: Include nodes in operation
        :type include: List['Workflow']
        """
        existing_filter_type = ("cut-off", "field-value")
        existing_field_operations = ("<", "==", ">")
        if filter_type in existing_filter_type:
            parameters = {"filter-type": filter_type}
            if filter_type == "field-value":
                if field_operation in existing_field_operations:
                    parameters["field-operation"] = field_operation
                    parameters["field-value"] = field_value
                else:
                    raise ValueError(
                        "field_operation must be of type {field_operations}.".format(
                            field_operations=" or ".join(existing_field_operations)
                        )
                    )

            operation = {"type": "FILTER", "parameters": parameters}
            self._add_with_requirements(operation, include)
            return self
        else:
            raise ValueError(
                "filter_type must be of type {field_operations}.".format(
                    field_operations=" or ".join(existing_filter_type)
                )
            )

    def filter_categories(self, *categories: List[str], include: List["Workflow"] = []):
        """
        Filter node type by category
        :param categories: the categories to filter
        :type categories: List[str]
        :param include: Include nodes in operation
        :type include: List['Workflow']
        """
        parameters: Dict[str, Any] = {"filter-type": "categories"}
        parameters["categories"] = categories
        operation = {"type": "FILTER", "parameters": parameters}
        self._add_with_requirements(operation, include)
        return self

    def edge_traversal(self, edges: List[str] = [], include: List["Workflow"] = []):
        """
        Traverse edges
        :param edges: The edges to traverse
        :type edges: List[str]
        :param include: Include nodes in operation
        :type include: List['Workflow']
        """
        input_key = self._operations.tail.id
        operation = {
            "type": "EDGE-TRAVERSAL",
            "parameters": {
                "edges": [{"name": name, "index": input_key} for name in edges]
            },
        }
        self._add_with_requirements(operation, include, replace_index=True)
        return self

    def pearson_traversal(self, edges: List[str] = [], include: List["Workflow"] = []):
        """
        Traverse edges using pearson traversal
        :param edges: The edges to traverse
        :type edges: List[str]
        :param include: Include nodes in operation
        :type include: List['Workflow']
        """
        input_key = self._operations.tail.id
        operation = {
            "type": "PEARSON-TRAVERSAL",
            "parameters": {
                "edges": [{"name": name, "index": input_key} for name in edges]
            },
        }
        self._add_with_requirements(operation, include, replace_index=True)
        return self

    def normalize(
        self, normalize_type: str = "RENORMALIZE_L2", include: List["Workflow"] = []
    ):
        """
        Normalize result
        :param normalize_type: Normalize type to use. Possible values "RENORMALIZE_L1", "RENORMALIZE_L2", "RENORMALIZE_LINF"
        :type normalize_type: str
        :param include: Include nodes in operation
        :type include: List['Workflow']
        """
        normalize_types = ("RENORMALIZE_L1", "RENORMALIZE_L2", "RENORMALIZE_LINF")

        if normalize_type in normalize_types:
            operation = {"parameters": {}, "type": normalize_type}
            self._add_with_requirements(operation, include)
            return self
        else:
            raise ValueError(
                "filter_type must be of type {normalize_types}.".format(
                    normalize_types=" or ".join(normalize_types)
                )
            )

    def scalar_function(
        self, scalar_function: str = "abs", include: List["Workflow"] = []
    ):
        """
        Run result through scalar function
        :param scalar_function: Scalar function to use. Possible values "uniform", "abs", "inv", "sigmoid", "softmax"
        :type scalar_function: str
        :param include: Include nodes in operation
        :type include: List['Workflow']
        """
        scalar_function_types = ("uniform", "abs", "inv", "sigmoid", "softmax")
        if scalar_function in scalar_function_types:
            operation = {
                "type": "SCALAR_FUNCTION",
                "parameters": {"scalar-function": scalar_function},
            }
            self._add_with_requirements(operation, include)
            return self
        else:
            raise ValueError(
                "filter_type must be of type {scalar_function_types}.".format(
                    scalar_function_types=" or ".join(scalar_function_types)
                )
            )

    def matrix_function(
        self, matrix_function: str = "abs", include: List["Workflow"] = []
    ):
        """
        Run result through matrix function
        :param matrix_function: Scalar function to use. Possible values "e^A", "cosh", "sinh"
        :type matrix_function: str
        :param include: Include nodes in operation
        :type include: List['Workflow']
        """
        matrix_function_types = ("e^A", "cosh", "sinh")
        if matrix_function in matrix_function_types:
            operation = {
                "type": "MATRIX_FUNCTION",
                "parameters": {"function": matrix_function, "edges": []},
            }
            self._add_with_requirements(operation, include)
            return self
        else:
            raise ValueError(
                "filter_type must be of type {matrix_function_types}.".format(
                    matrix_function_types=" or ".join(matrix_function_types)
                )
            )

    def intersect(self, *workflows: List["Workflow"]):
        """
        Intersect result
        :param `*workflows`: Nodes to intersect
        :type `*workflows`: List['Workflow']
        """
        operation = {"parameters": {}, "type": "AND"}
        self._add_with_requirements(operation, workflows)
        return self

    def combine(self, *workflows: List["Workflow"]):
        """
        Combine result
        :param `*workflows`: Nodes to combine
        :type `*workflows`: List['Workflow']
        """
        operation = {"parameters": {}, "type": "OR"}
        self._add_with_requirements(operation, workflows)
        return self

    def sum(self, *workflows: List["Workflow"]):
        """
        Sum result
        :param `*workflows`: Nodes to sum
        :type `*workflows`: List['Workflow']
        """
        operation = {"parameters": {}, "type": "SUM"}
        self._add_with_requirements(operation, workflows)
        return self

    def multiply(self, *workflows: List["Workflow"]):
        """
        Multiply result
        :param `*workflows`: Nodes to multiply
        :type `*workflows`: List['Workflow']
        """
        operation = {"parameters": {}, "type": "MULT"}
        self._add_with_requirements(operation, workflows)
        return self

    def negate(self, *workflows: List["Workflow"]):
        """
        Negate result
        :param `*workflows`: Nodes to negate
        :type `*workflows`: List['Workflow']
        """
        operation = {"parameters": {}, "type": "NOT"}
        self._add_with_requirements(operation, workflows)
        return self

    def to_json(self, indent=2) -> str:
        """
        Return workflow as json string
        :param indent: result indentation
        :type indent: int
        """
        return json.dumps(self.get_operations(), indent=indent)

    def get_operations(self):
        """
        Return workflow operations
        """
        self.as_output()  # mark type to output
        result = []
        flatten_list = self._operations.flatten_list()
        op_edge_map = {
            key: edge_count for edge_count, key in enumerate(flatten_list.keys())
        }
        for op_key, op in flatten_list.items():
            if not op:
                continue
            edge_in = []
            if op["requirements"]:
                edge_in = [op_edge_map[dep_op] for dep_op in op["requirements"]]
            if op["replace_index"]:
                new_edges = [
                    {"name": edge["name"], "index": op_edge_map[edge["index"]]}
                    for edge in _get_edges(op)
                ]
                op = _set_edges(op, new_edges)

            edge_in.sort()
            edge_out = [op_edge_map[op_key]]
            processed_op = {
                "edges": {"in": edge_in, "out": edge_out},
                "operation": op["operation"],
                "type": op["type"],
            }
            result.append(processed_op)

        return result

    def _add_with_requirements(
        self, operation, workflows=[], replace_index: bool = False
    ):
        if self._operations.tail:
            requirements = [self._operations.tail.id]
        else:
            requirements = []

        if workflows:
            for workflow in workflows:
                self._operations.append_child(workflow._operations.head)
                requirements.append(workflow._operations.tail.id)
        self._add_operation(operation, requirements, replace_index)

    def _add_operation(
        self, operation: dict, requirements: List[str] = [], replace_index: bool = False
    ):
        if not self._operations.head:
            op_type = "INPUT"
        else:
            op_type = "AUXILIARY"

        self._operations.append(
            {
                "operation": operation,
                "type": op_type,
                "requirements": requirements,
                "replace_index": replace_index,
            }
        )

    def split(self, times: int = 1):
        """
        Add children to node
        :param times: Number of children to add
        :type times: int
        :returns node childs
        """
        result = []
        if not self._operations.tail.child:
            self._operations.tail.child = []

        for index in range(times - 1):
            new_node = Node(None, self._operations.tail.id)
            self._operations.tail.child.append(new_node)
            result.append(Workflow(new_node))

        return (self, *result)


def _get_edges(op):
    return op["operation"]["parameters"]["edges"]


def _set_edges(op, new_edges):
    op["operation"]["parameters"]["edges"] = new_edges
    return op
