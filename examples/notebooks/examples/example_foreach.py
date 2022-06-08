import json
from dataclasses import asdict

from deepsearch.core.client import (
    DeepSearchBearerTokenAuth,
    DeepSearchConfig,
    DeepSearchKeyAuth,
)
from deepsearch.cps.client.api import CpsApi, CpsApiClient
from deepsearch.cps.client.builders.wf_builder import (
    WorkflowBuilder,
    WorkflowTaskOperation,
)
from deepsearch.cps.client.queries import Query
from deepsearch.cps.client.queries.query_tasks import ForEach, Workflow

# Token auth
# auth = CpsApiAuth(bearer_token="TOKEN")

# Api key auth
auth = DeepSearchKeyAuth(
    username="EMAIL",
    api_key="API KEY",
)


config = DeepSearchConfig(
    host="https://cps.foc-deepsearch.zurich.ibm.com", # IBM internal system
    auth=auth,
    verify_ssl=False,
)

client = CpsApiClient(config)
api = CpsApi(client)


kg = api.knowledge_graphs.get(
    "49beb4bb6d706b6282032cd743d03c4a3fbc64e1",
    "720047c8cd473e20f4b298acc924dd7cb78fbd92",
)
# kg = api.knowledge_graphs.get(
#     "617ffb14b1ec92fcd5985b3643d2d992508a9f10",
#     "5b8ab8392d964049c18ec9c0e1ec92362c7f3c4b",
# )

if kg is None:
    raise Exception("No such kg")

topo = kg.get_topology()

query = Query()


builder = WorkflowBuilder()

input_task = builder.add(
    WorkflowTaskOperation(
        type="SEARCH",
        parameters={
            "names": ["pag"],
            "type": "equal",
        },
    ),
    type="INPUT",
)
filter_category_task = builder.add(
    WorkflowTaskOperation(
        type="FILTER",
        parameters={
            "categories": ["material-class"],
            "filter-type": "categories",
        },
    ),
    inputs=[input_task],
)
mat_class_to_material = builder.add(
    WorkflowTaskOperation(
        type="EDGE-TRAVERSAL",
        parameters={
            "edges": [
                {
                    "index": builder.index(filter_category_task),
                    "name": "material-to-material-class",
                }
            ]
        },
    ),
    inputs=[filter_category_task],
)
material_to_experiment = builder.add(
    WorkflowTaskOperation(
        type="EDGE-TRAVERSAL",
        parameters={
            "edges": [
                {
                    "index": builder.index(mat_class_to_material),
                    "name": "experiment-to-material",
                }
            ]
        },
        outputs={"nodes": {"type": "NODE_LIST", "parameters": {"limit": 10}}},
    ),
    inputs=[mat_class_to_material],
)

wf = query.add(Workflow(id="", builder=builder, inputs={}, coordinates=kg))

wf.output(mat_class_to_material).output_as("pag_materials")
wf.output(material_to_experiment).output_as("pag_experiments")

projection = query.add(
    "Projection",
    inputs={"nodes": wf.output(material_to_experiment)},
    parameters={"projections": {"nodes": {"field_path": ["nodes"]}}},
)

# Do a For-Each...
wf_for_each = query.add(
    ForEach(id="", query=Query(), items=projection.output("nodes")),
)

wf_body = wf_for_each.query.add(
    "Workflow",
    parameters={
        "workflow": [
            {
                "edges": {"in": [], "out": [0]},
                "operation": {
                    "parameters": {
                        "ids": [{"#ForEach": {wf_for_each.id: "CurrentElement"}}]
                    },
                    "type": "SEARCH",
                },
                "type": "INPUT",
            },
            {
                "edges": {"in": [0], "out": [1]},
                "operation": {
                    "parameters": {
                        "edges": [{"index": 0, "name": "experiment-to-material"}]
                    },
                    "type": "EDGE-TRAVERSAL",
                },
                "type": "AUXILIARY",
            },
            {
                "edges": {"in": [1], "out": [2]},
                "operation": {
                    "parameters": {
                        "edges": [
                            {
                                "index": 1,
                                "name": "material-identifiers-to-identifier-type",
                            },
                            {"index": 1, "name": "material-to-identifiers"},
                        ]
                    },
                    "type": "EDGE-TRAVERSAL",
                },
                "type": "AUXILIARY",
            },
            {
                "edges": {"in": [], "out": [3]},
                "operation": {
                    "parameters": {"names": ["smiles"], "type": "equal"},
                    "type": "SEARCH",
                },
                "type": "INPUT",
            },
            {
                "edges": {"in": [3], "out": [4]},
                "operation": {
                    "parameters": {
                        "categories": ["identifier-type"],
                        "filter-type": "categories",
                    },
                    "type": "FILTER",
                },
                "type": "AUXILIARY",
            },
            {
                "edges": {"in": [4], "out": [5]},
                "operation": {
                    "parameters": {
                        "edges": [
                            {
                                "index": 4,
                                "name": "material-identifiers-to-identifier-type",
                            }
                        ]
                    },
                    "type": "EDGE-TRAVERSAL",
                },
                "type": "AUXILIARY",
            },
            {
                "edges": {"in": [2, 5], "out": [6]},
                "operation": {"parameters": {}, "type": "AND"},
                "type": "OUTPUT",
            },
            {
                "edges": {"in": [1], "out": [7]},
                "operation": {
                    "parameters": {
                        "edges": [
                            {"index": 1, "name": "material-to-material-via-names"}
                        ]
                    },
                    "type": "EDGE-TRAVERSAL",
                },
                "type": "AUXILIARY",
            },
            {
                "edges": {"in": [9, 5], "out": [8]},
                "operation": {"parameters": {}, "type": "AND"},
                "type": "OUTPUT",
            },
            {
                "edges": {"in": [7], "out": [9]},
                "operation": {
                    "parameters": {
                        "edges": [{"index": 7, "name": "experiment-to-material"}]
                    },
                    "type": "EDGE-TRAVERSAL",
                },
                "type": "AUXILIARY",
            },
            {
                "edges": {"in": [6, 8], "out": [10]},
                "operation": {"parameters": {}, "type": "OR"},
                "type": "OUTPUT",
            },
        ]
    },
    coordinates=kg,
)

wf_body.output("6").output_as("smiles direct match")
wf_body.output("8").output_as("smiles indirect match")
wf_body.output("10").output_as("smiles")

wf_for_each.outputs.result.output_as("for_each_node")

print(json.dumps(query.to_flow(), indent=2))

result = api.queries.run(query)

print(json.dumps(asdict(result), indent=2))
