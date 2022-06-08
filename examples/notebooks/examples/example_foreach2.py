import json
from dataclasses import asdict
from typing import Any, Dict

from deepsearch.core.client import (
    DeepSearchBearerTokenAuth,
    DeepSearchConfig,
    DeepSearchKeyAuth,
)
from deepsearch.cps.client.api import CpsApi, CpsApiClient
from deepsearch.cps.client.queries import Query
from deepsearch.cps.client.queries.query_tasks import ForEach

# Token auth
# auth = CpsApiAuth(bearer_token="TOKEN")

# Api key auth
auth = DeepSearchKeyAuth(
    username="dol@zurich.ibm.com",
    api_key="TOKEN",
)


config = DeepSearchConfig(
    host="https://cps.foc-deepsearch.zurich.ibm.com", # IBM internal system
    auth=auth,
    verify_ssl=False,
)

client = CpsApiClient(config)
api = CpsApi(client)


kg = api.knowledge_graphs.get(
    "f21574fe745fa0b8213cb08d0c4166513108158c",
    "80511ed4a524fe446dc102e704fd7577f2c2a26c",
)

if kg is None:
    raise Exception("No such kg")

topo = kg.get_topology()


query = Query()

## 1. Find conferences in time period
find_conf_wf_query: Dict[str, Any] = {
    "bag_key": "80511ed4a524fe446dc102e704fd7577f2c2a26c",
    "description": "",
    "name": "Conferences in time range",
    "outputs": {"1": {"name": "papers"}, "2": {"name": "conferences"}},
    "proj_key": "f21574fe745fa0b8213cb08d0c4166513108158c",
    "template": [
        {
            "edges": {"in": [], "out": [0]},
            "operation": {
                "parameters": {
                    "names": ["2020_1", "2020_2", "2020_3"],
                    "type": "equal",
                },
                "type": "SEARCH",
            },
            "type": "INPUT",
        },
        {
            "edges": {"in": [0], "out": [1]},
            "operation": {
                "parameters": {"edges": [{"index": 0, "name": "papers-to-year-month"}]},
                "type": "EDGE-TRAVERSAL",
                "outputs": {
                    "nodes": {"type": "NODE_LIST", "parameters": {"limit": 50}}
                },
            },
            "type": "OUTPUT",
        },
        {
            "edges": {"in": [1], "out": [2]},
            "operation": {
                "parameters": {
                    "edges": [{"index": 1, "name": "papers-to-conferences"}]
                },
                "type": "EDGE-TRAVERSAL",
                "outputs": {
                    "nodes": {"type": "NODE_LIST", "parameters": {"limit": -1}}
                },
            },
            "type": "OUTPUT",
        },
    ],
    "variables": {},
}

find_conf_wf = query.add(
    "Workflow", parameters={"workflow": find_conf_wf_query["template"]}, coordinates=kg
)

for k, spec in find_conf_wf_query.get("outputs", {}).items():
    find_conf_wf.output(k).output_as(spec["name"])


## 2. For each conference make stats

projection = query.add(
    "Projection",
    inputs={"nodes": find_conf_wf.output("conferences")},
    parameters={"projections": {"nodes": {"field_path": ["nodes"]}}},
)

wf_for_each = query.add(
    ForEach(id="", query=Query(), items=projection.output("nodes")),
)

conf_stats_wf_query: Dict[str, Any] = {
    "bag_key": "80511ed4a524fe446dc102e704fd7577f2c2a26c",
    "description": "",
    "name": "Conference stats",
    "outputs": {
        "1": {"name": "papers"},
        "2": {"name": "challenges"},
        "3": {"name": "researchers"},
    },
    "proj_key": "f21574fe745fa0b8213cb08d0c4166513108158c",
    "template": [
        {
            "edges": {"in": [], "out": [0]},
            "operation": {
                "parameters": {"ids": [wf_for_each.current_element()]},
                "type": "SEARCH",
            },
            "type": "INPUT",
        },
        {
            "edges": {"in": [0], "out": [1]},
            "operation": {
                "parameters": {
                    "edges": [{"index": 0, "name": "papers-to-conferences"}]
                },
                "type": "EDGE-TRAVERSAL",
                "outputs": {"nodes": {"type": "NODE_LIST", "parameters": {"limit": 0}}},
            },
            "type": "OUTPUT",
        },
        {
            "edges": {"in": [1], "out": [2]},
            "operation": {
                "parameters": {"edges": [{"index": 1, "name": "papers-to-challenges"}]},
                "type": "EDGE-TRAVERSAL",
                "outputs": {"nodes": {"type": "NODE_LIST", "parameters": {"limit": 0}}},
            },
            "type": "OUTPUT",
        },
        {
            "edges": {"in": [1], "out": [3]},
            "operation": {
                "parameters": {
                    "edges": [
                        {"index": 1, "name": "accomplishments-to-authors"},
                        {"index": 1, "name": "challenges-to-authors"},
                        {"index": 1, "name": "papers-to-authors"},
                        {"index": 1, "name": "recognition-to-authors"},
                    ]
                },
                "type": "EDGE-TRAVERSAL",
                "outputs": {"nodes": {"type": "NODE_LIST", "parameters": {"limit": 0}}},
            },
            "type": "OUTPUT",
        },
    ],
    "variables": {},
}

foreach_body = Query()
conf_stats_wf = wf_for_each.query.add(
    "Workflow", parameters={"workflow": conf_stats_wf_query["template"]}, coordinates=kg
)

for k, spec in conf_stats_wf_query.get("outputs", {}).items():
    conf_stats_wf.output(k).output_as(spec["name"])

wf_for_each.outputs.result.output_as("for_each_node")

print(json.dumps(query.to_flow(), indent=2))

result = api.queries.run(query)

print(json.dumps(asdict(result), indent=2))
