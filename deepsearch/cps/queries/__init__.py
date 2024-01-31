from typing import Any, Dict, List, Optional, Union

from pydantic.v1 import Field, validate_arguments
from typing_extensions import Annotated

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


ConstrainedWeight = Annotated[
    float, Field(strict=True, ge=0.0, le=1.0, multiple_of=0.1)
]


def CorpusRAGQuery(
    question: str,
    *,
    project: Union[str, Project],
    index_key: str,
    retr_k: int = 10,
    rerank: bool = False,
    text_weight: ConstrainedWeight = 0.1,
) -> Query:
    """Create a RAG query against a collection

    Args:
        question (str): the natural-language query
        project (Union[str, Project]): project to use
        index_key (str): index key of target private collection (must already be semantically indexed)
        retr_k (int, optional): num of items to retrieve; defaults to 10
        rerank (bool, optional): whether to rerank retrieval results; defaults to False
        text_weight (ConstrainedWeight, optional): lexical weight for hybrid search; allowed values: {0.0, 0.1, 0.2, ..., 1.0}; defaults to 0.1
    """

    return _create_rag_query(
        question=question,
        project=project,
        index_key=index_key,
        retr_k=retr_k,
        rerank=rerank,
        text_weight=text_weight,
    )


def DocumentRAGQuery(
    question: str,
    *,
    document_hash: str,
    project: Union[str, Project],
    index_key: Optional[str] = None,
    retr_k: int = 10,
    rerank: bool = False,
    text_weight: ConstrainedWeight = 0.1,
) -> Query:
    """Create a RAG query against a specific document

    Args:
        question (str): the natural-language query
        document_hash (str): hash of target document
        project (Union[str, Project]): project to use
        index_key (str, optional): index key of target private collection (must already be semantically indexed) in case doc within one; defaults to None (doc must already be semantically indexed)
        retr_k (int, optional): num of items to retrieve; defaults to 10
        rerank (bool, optional): whether to rerank retrieval results; defaults to False
        text_weight (ConstrainedWeight, optional): lexical weight for hybrid search; allowed values: {0.0, 0.1, 0.2, ..., 1.0}; defaults to 0.1
    """

    return _create_rag_query(
        question=question,
        document_hash=document_hash,
        project=project,
        index_key=index_key,
        retr_k=retr_k,
        rerank=rerank,
        text_weight=text_weight,
    )


@validate_arguments
def _create_rag_query(
    question: str,
    *,
    document_hash: Optional[str] = None,
    project: Union[str, Project],
    index_key: Optional[str],
    retr_k: int,
    rerank: bool,
    text_weight: ConstrainedWeight,
) -> Query:
    proj_key = project.key if isinstance(project, Project) else project
    idx_key = index_key or "__project__"

    query = Query()

    q_params = {
        "question": question,
        "retr_k": retr_k,
        "use_reranker": rerank,
        "hybrid_search_text_weight": text_weight,
    }
    if document_hash:
        q_params["doc_id"] = document_hash
    task = query.add(
        task_id="QA",
        kind_or_task="SemanticRag",
        parameters=q_params,
        coordinates=SemanticBackendResource(proj_key=proj_key, index_key=idx_key),
    )
    task.output("answers").output_as("answers")
    task.output("retrieval").output_as("retrieval")

    return query


def CorpusSemanticQuery(
    question: str,
    *,
    project: Union[str, Project],
    index_key: str,
    retr_k: int = 10,
    rerank: bool = False,
    text_weight: ConstrainedWeight = 0.1,
) -> Query:
    """Create a semantic retrieval query against a collection

    Args:
        question (str): the natural-language query
        project (Union[str, Project]): project to use
        index_key (str): index key of target private collection (must already be semantically indexed)
        retr_k (int, optional): num of items to retrieve; defaults to 10
        rerank (bool, optional): whether to rerank retrieval results; defaults to False
        text_weight (ConstrainedWeight, optional): lexical weight for hybrid search; allowed values: {0.0, 0.1, 0.2, ..., 1.0}; defaults to 0.1
    """

    return _create_semantic_query(
        question=question,
        project=project,
        index_key=index_key,
        retr_k=retr_k,
        rerank=rerank,
        text_weight=text_weight,
    )


def DocumentSemanticQuery(
    question: str,
    *,
    document_hash: str,
    project: Union[str, Project],
    index_key: Optional[str] = None,
    retr_k: int = 10,
    rerank: bool = False,
    text_weight: ConstrainedWeight = 0.1,
) -> Query:
    """Create a semantic retrieval query against a specific document

    Args:
        question (str): the natural-language query
        document_hash (str): hash of target document
        project (Union[str, Project]): project to use
        index_key (str, optional): index key of target private collection (must already be semantically indexed) in case doc within one; defaults to None (doc must already be semantically indexed)
        retr_k (int, optional): num of items to retrieve; defaults to 10
        rerank (bool, optional): whether to rerank retrieval results; defaults to False
        text_weight (ConstrainedWeight, optional): lexical weight for hybrid search; allowed values: {0.0, 0.1, 0.2, ..., 1.0}; defaults to 0.1
    """

    return _create_semantic_query(
        question=question,
        document_hash=document_hash,
        project=project,
        index_key=index_key,
        retr_k=retr_k,
        rerank=rerank,
        text_weight=text_weight,
    )


@validate_arguments
def _create_semantic_query(
    question: str,
    *,
    document_hash: Optional[str] = None,
    project: Union[str, Project],
    index_key: Optional[str],
    retr_k: int,
    rerank: bool,
    text_weight: ConstrainedWeight,
) -> Query:
    proj_key = project.key if isinstance(project, Project) else project
    idx_key = index_key or "__project__"

    query = Query()

    q_params = {
        "question": question,
        "retr_k": retr_k,
        "use_reranker": rerank,
        "hybrid_search_text_weight": text_weight,
    }
    if document_hash:
        q_params["doc_id"] = document_hash
    task = query.add(
        task_id="QA",
        kind_or_task="SemanticRetrieval",
        parameters=q_params,
        coordinates=SemanticBackendResource(proj_key=proj_key, index_key=idx_key),
    )
    task.output("items").output_as("items")

    return query
