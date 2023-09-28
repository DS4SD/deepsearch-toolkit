from typing import Any, Dict, List, Optional, Union

from deepsearch.cps.client.components.elastic import ElasticSearchQuery
from deepsearch.cps.client.components.projects import Project, QAGenAIResource
from deepsearch.cps.client.queries import Query, TaskCoordinates


def Wf(wf_query: Dict[str, Any], kg: TaskCoordinates) -> Query:
    query = Query()
    wf = query.add(
        "Workflow", parameters={"workflow": wf_query["template"]}, coordinates=kg
    )

    for k, spec in wf_query.get("outputs", {}).items():
        wf.output(k).output_as(spec["name"])

    return query


def Fts(search_query: str, collection_name: str, kg: TaskCoordinates) -> Query:
    query = Query()
    task = query.add(
        "FullTextSearch",
        parameters={"text": search_query, "collection": collection_name},
        coordinates=kg,
    )
    task.output("documents").output_as("fts")

    return query


def DataQuery(
    search_query: ElasticSearchQuery,
    *,
    source: Optional[List[str]] = None,
    aggregations: Optional[dict] = None,
    highlight: Optional[dict] = None,
    sort: Optional[List[Dict[str, Any]]] = None,
    limit: int = 20,
    search_after: Optional[List[str]] = None,
    coordinates: TaskCoordinates,
) -> Query:

    if isinstance(search_query, str):
        search_query = {"query_string": {"query": search_query}}

    if sort is None:
        sort = [{"file-info.document-hash": "asc"}]

    payload = {
        "elastic_query": search_query,
        "limit": limit,
        "sort": sort,
    }

    if source is not None:
        payload["source"] = source

    if aggregations is not None:
        payload["aggregations"] = aggregations

    if highlight is not None:
        payload["highlight"] = highlight

    if search_after is not None:
        payload["search_after"] = search_after

    query = Query()

    task = query.add("ElasticQuery", parameters=payload, coordinates=coordinates)
    task.output("items").output_as("data_outputs")
    task.output("total").output_as("data_count")
    task.output("aggregations").output_as("data_aggs")

    query.paginated_task = task

    return query


def DocumentQuestionQuery(
    question: str,
    *,
    document_hash: str,
    project: Union[str, Project],
) -> Query:

    proj_key = project.key if isinstance(project, Project) else project

    query = Query()
    task = query.add(
        "QA",
        parameters={
            "doc_id": document_hash,
            "question": question,
        },
        coordinates=QAGenAIResource(proj_key=proj_key),
    )
    task.output("answer").output_as("answer")
    task.output("contexts").output_as("contexts")
    task.output("provenance").output_as("provenance")

    return query
