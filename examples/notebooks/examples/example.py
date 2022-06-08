import json

from deepsearch.core.client import DeepSearchBearerTokenAuth, DeepSearchConfig
from deepsearch.cps.client.api import CpsApi, CpsApiClient
from deepsearch.cps.client.builders.wf_builder import (
    WorkflowBuilder,
    WorkflowTaskOperation,
)
from deepsearch.cps.client.queries import Query
from deepsearch.cps.client.queries.query_tasks import Workflow

token = "eyJhbGciOiJS..."

config = DeepSearchConfig(
    host="https://cps.foc-deepsearch.zurich.ibm.com", # IBM internal system
    auth=DeepSearchBearerTokenAuth(bearer_token=token),
    verify_ssl=False,
)

client = CpsApiClient(config)
api = CpsApi(client)


kg = api.knowledge_graphs.get(
    "617ffb14b1ec92fcd5985b3643d2d992508a9f10",
    "5b8ab8392d964049c18ec9c0e1ec92362c7f3c4b",
)

if kg is None:
    raise Exception("No such kg")

topo = kg.get_topology()

query = Query()

# fts = query.add(
#     "FullTextSearch",
#     parameters={"text": "hello", "collection": "test"},
#     coordinates=kg,
# )

# fts.output("documents").output_as("documents")

# proj = query.add(
#     "Projection",
#     inputs={"items": fts.output("documents")},
#     parameters={"projections": {"items": {"field_path": ["$$map", "_hash"]}}},
# )

builder = WorkflowBuilder()

# [] -> [1]
search_paragraphs = builder.add(
    WorkflowTaskOperation(
        type="SEARCH",
        parameters={"categories": ["paragraphs"]},
        # outputs={},
    ),
    type="INPUT",
)

# [1] -> [2]
traverse_paragraphs_to_material = builder.add(
    WorkflowTaskOperation(
        type="EDGE-TRAVERSAL",
        parameters={
            "edges": [
                {
                    "index": builder.index(search_paragraphs),
                    "name": "paragraphs-to-material",
                }
            ]
        },
        outputs={
            "nodes": {"type": "NODE_LIST", "parameters": {"limit": 50}},
            "weight": {
                "type": "STATISTICS",
                "parameters": {
                    "source": "weights",
                    "do-histogram": True,
                    "#-of-histogram-bins": 16,
                },
            },
        },
    ),
    type="OUTPUT",
    inputs=[search_paragraphs],
)

# [2] -> [0]
traverse_material_via_names = builder.add(
    WorkflowTaskOperation(
        type="EDGE-TRAVERSAL",
        parameters={
            "edges": [
                {
                    "index": builder.index(traverse_paragraphs_to_material),
                    "name": "material-to-material-via-names",
                }
            ]
        },
        outputs={
            "nodes": {"type": "NODE_LIST", "parameters": {"limit": 50}},
            "weight": {
                "type": "STATISTICS",
                "parameters": {
                    "source": "weights",
                    "do-histogram": True,
                    "#-of-histogram-bins": 16,
                },
            },
        },
    ),
    type="OUTPUT",
    inputs=[traverse_paragraphs_to_material],
)

# [] -> [3]
search_databases = builder.add(
    WorkflowTaskOperation(
        type="SEARCH",
        parameters={"categories": ["databases"]},
        outputs={},
    ),
    type="INPUT",
)

# [3] -> [4]
traverse_databases_to_material = builder.add(
    WorkflowTaskOperation(
        type="EDGE-TRAVERSAL",
        parameters={
            "edges": [
                {
                    "index": builder.index(search_databases),
                    "name": "databases-to-material",
                }
            ]
        },
        outputs={
            "nodes": {"type": "NODE_LIST", "parameters": {"limit": 50}},
            "weight": {
                "type": "STATISTICS",
                "parameters": {
                    "source": "weights",
                    "do-histogram": True,
                    "#-of-histogram-bins": 16,
                },
            },
        },
    ),
    type="OUTPUT",
    inputs=[search_databases],
)

# [2, 4] -> [5]
and_materials = builder.add(
    WorkflowTaskOperation(
        type="AND",
        parameters={},
        outputs={
            "nodes": {"type": "NODE_LIST", "parameters": {"limit": 50}},
            "weight": {
                "type": "STATISTICS",
                "parameters": {
                    "source": "weights",
                    "do-histogram": True,
                    "#-of-histogram-bins": 16,
                },
            },
        },
    ),
    inputs=[traverse_paragraphs_to_material, traverse_databases_to_material],
    type="OUTPUT",
)

# [0, 4] -> [6]
and_materials_from_paragraphs = builder.add(
    WorkflowTaskOperation(
        type="AND",
        parameters={},
        outputs={
            "nodes": {"type": "NODE_LIST", "parameters": {"limit": 50}},
            "weight": {
                "type": "STATISTICS",
                "parameters": {
                    "source": "weights",
                    "do-histogram": True,
                    "#-of-histogram-bins": 16,
                },
            },
        },
    ),
    type="OUTPUT",
    inputs=[traverse_material_via_names, traverse_databases_to_material],
)

# [4] -> [7]
traverse_material_via_names_again = builder.add(
    WorkflowTaskOperation(
        parameters={"edges": [{"index": 4, "name": "material-to-material-via-names"}]},
        type="EDGE-TRAVERSAL",
        outputs={
            "nodes": {"type": "NODE_LIST", "parameters": {"limit": 50}},
            "weight": {
                "type": "STATISTICS",
                "parameters": {
                    "source": "weights",
                    "do-histogram": True,
                    "#-of-histogram-bins": 16,
                },
            },
        },
    ),
    type="OUTPUT",
    inputs=[traverse_databases_to_material],
)

# [7, 2] -> [8]

builder.add(
    WorkflowTaskOperation(
        parameters={},
        type="AND",
        outputs={
            "nodes": {"type": "NODE_LIST", "parameters": {"limit": 50}},
            "weight": {
                "type": "STATISTICS",
                "parameters": {
                    "source": "weights",
                    "do-histogram": True,
                    "#-of-histogram-bins": 16,
                },
            },
        },
    ),
    type="OUTPUT",
    inputs=[traverse_material_via_names_again, traverse_paragraphs_to_material],
)

wf = query.add(Workflow(id="", builder=builder, coordinates=kg, inputs={}))

wf.output(traverse_material_via_names_again).output_as("searched_documents")

print(json.dumps(query.to_flow(), indent=2))

result = api.queries.run(query)

print(json.dumps(result, indent=2))
