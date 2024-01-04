from typing import Any, Dict, List, Optional, Union

from deepsearch.cps.client.components.elastic import ElasticSearchQuery
from deepsearch.cps.client.components.projects import Project, SemanticBackendResource
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


def CorpusRAGQuery(
    question: str,
    *,
    project: Union[str, Project],
    index_key: str,
) -> Query:

    return _get_rag_query(
        question=question,
        project=project,
        index_key=index_key,
    )


def DocumentRAGQuery(
    question: str,
    *,
    document_hash: str,
    project: Union[str, Project],
    index_key: Optional[str] = None,  # set in case of private collection
) -> Query:

    return _get_rag_query(
        question=question,
        document_hash=document_hash,
        project=project,
        index_key=index_key,
    )


def _get_rag_query(
    question: str,
    *,
    document_hash: Optional[str] = None,
    project: Union[str, Project],
    index_key: Optional[str] = None,
) -> Query:
    proj_key = project.key if isinstance(project, Project) else project
    idx_key = index_key or "__project__"

    query = Query()
    q_params = {"question": question}
    if document_hash:
        q_params["doc_id"] = document_hash
    task = query.add(
        task_id="QA",
        kind_or_task="SemanticRag",
        parameters=q_params,
        coordinates=SemanticBackendResource(proj_key=proj_key, index_key=idx_key),
    )
    task.output("answer").output_as("answer")
    task.output("provenance").output_as("provenance")

    return query


def CorpusSemanticQuery(
    question: str,
    *,
    project: Union[str, Project],
    index_key: str,
) -> Query:

    return _get_semantic_query(
        question=question,
        project=project,
        index_key=index_key,
    )


def DocumentSemanticQuery(
    question: str,
    *,
    document_hash: str,
    project: Union[str, Project],
    index_key: Optional[str] = None,  # set in case of private collection
) -> Query:

    return _get_semantic_query(
        question=question,
        document_hash=document_hash,
        project=project,
        index_key=index_key,
    )


def _get_semantic_query(
    question: str,
    *,
    document_hash: Optional[str] = None,
    project: Union[str, Project],
    index_key: Optional[str] = None,
) -> Query:
    proj_key = project.key if isinstance(project, Project) else project
    idx_key = index_key or "__project__"

    query = Query()
    q_params = {"question": question}
    if document_hash:
        q_params["doc_id"] = document_hash
    task = query.add(
        task_id="QA",
        kind_or_task="SemanticRetrieval",
        parameters=q_params,
        coordinates=SemanticBackendResource(proj_key=proj_key, index_key=idx_key),
    )
    task.output("contexts").output_as("contexts")

    return query
