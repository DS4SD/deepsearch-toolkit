from typing import Any, Dict, List, Literal, Optional, Union

from pydantic.v1 import BaseModel, Field, validate_arguments
from typing_extensions import Annotated

from deepsearch.cps.client.components.documents import (
    DataSource,
    PrivateDataCollectionSource,
    PrivateDataDocumentSource,
)
from deepsearch.cps.client.components.elastic import ElasticSearchQuery
from deepsearch.cps.client.components.projects import (
    Project,
    SemanticBackendPublicResource,
    SemanticBackendResource,
)
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


class _APISemanticRetrievalParameters(BaseModel):
    doc_id: Optional[str] = None
    question: str
    retr_k: int = 10
    use_reranker: bool = False
    hybrid_search_text_weight: ConstrainedWeight = 0.1


class _APISemanticRagParameters(_APISemanticRetrievalParameters):
    model_id: Optional[str] = None
    prompt_template: Optional[str] = None
    gen_params: Optional[Dict[str, Any]] = None
    gen_ctx_extr_method: Literal["window", "page"] = "window"
    gen_ctx_window_size: int = 5000
    gen_ctx_window_lead_weight: float = 0.5
    return_prompt: bool = False
    gen_timeout: Optional[float] = None


@validate_arguments
def RAGQuery(
    question: str,
    *,
    project: Union[str, Project],
    data_source: DataSource,
    retr_k: int = 10,
    rerank: bool = False,
    text_weight: ConstrainedWeight = 0.1,
    model_id: Optional[str] = None,
    prompt_template: Optional[str] = None,
    gen_params: Optional[Dict[str, Any]] = None,
    gen_ctx_extr_method: Literal["window", "page"] = "window",
    gen_ctx_window_size: int = 5000,
    gen_ctx_window_lead_weight: float = 0.5,
    return_prompt: bool = False,
    gen_timeout: Optional[float] = None,
) -> Query:
    """Create a RAG query

    Args:
        question (str): the natural-language query
        project (Union[str, Project]): project to use
        data_source (DataSource): the data source to query
        retr_k (int, optional): num of items to retrieve; defaults to 10
        rerank (bool, optional): whether to rerank retrieval results; defaults to False
        text_weight (ConstrainedWeight, optional): lexical weight for hybrid search; allowed values: {0.0, 0.1, 0.2, ..., 1.0}; defaults to 0.1
        model_id (str, optional): the LLM to use for generation; defaults to None, i.e. determined by system
        prompt_template (str, optional): the prompt template to use; defaults to None, i.e. determined by system
        gen_params (dict, optional): the generation params to send to the Gen AI platforms; defaults to None, i.e. determined by system
        gen_ctx_extr_method (Literal["window", "page"], optional): method for gen context extraction from document; defaults to "window"
        gen_ctx_window_size (int, optional): (relevant only if gen_ctx_extr_method=="window") max chars to use for extracted gen context (actual extraction quantized on doc item level); defaults to 5000
        gen_ctx_window_lead_weight (float, optional): (relevant only if gen_ctx_extr_method=="window") weight of leading text for distributing remaining window size after extracting the `main_path`; defaults to 0.5 (centered around `main_path`)
        return_prompt (bool, optional): whether to return the instantiated prompt; defaults to False
        gen_timeout (float, optional): timeout for LLM generation; defaults to None, i.e. determined by system
    """

    proj_key = project.key if isinstance(project, Project) else project
    index_key = data_source.source.index_key

    if isinstance(
        data_source, (PrivateDataDocumentSource, PrivateDataCollectionSource)
    ):
        coords = SemanticBackendResource(proj_key=proj_key, index_key=index_key)
    else:
        coords = SemanticBackendPublicResource(
            proj_key=proj_key,
            index_key=index_key,
            elastic_id=data_source.source.elastic_id,
        )

    params = _APISemanticRagParameters(
        doc_id=(
            None
            if isinstance(data_source, PrivateDataCollectionSource)
            else data_source.document_hash
        ),
        question=question,
        retr_k=retr_k,
        use_reranker=rerank,
        hybrid_search_text_weight=text_weight,
        model_id=model_id,
        prompt_template=prompt_template,
        gen_params=gen_params,
        gen_ctx_extr_method=gen_ctx_extr_method,
        gen_ctx_window_size=gen_ctx_window_size,
        gen_ctx_window_lead_weight=gen_ctx_window_lead_weight,
        return_prompt=return_prompt,
        gen_timeout=gen_timeout,
    )

    query = Query()
    task = query.add(
        task_id="QA",
        kind_or_task="SemanticRag",
        parameters=params.dict(),
        coordinates=coords,
    )
    task.output("answers").output_as("answers")
    task.output("retrieval").output_as("retrieval")

    return query


@validate_arguments
def SemanticQuery(
    question: str,
    *,
    project: Union[str, Project],
    data_source: DataSource,
    retr_k: int = 10,
    rerank: bool = False,
    text_weight: ConstrainedWeight = 0.1,
) -> Query:
    """Create a semantic retrieval query

    Args:
        question (str): the natural-language query
        document_hash (str): hash of target document
        project (Union[str, Project]): project to use
        data_source (DataSource): the data source to query
        retr_k (int, optional): num of items to retrieve; defaults to 10
        rerank (bool, optional): whether to rerank retrieval results; defaults to False
        text_weight (ConstrainedWeight, optional): lexical weight for hybrid search; allowed values: {0.0, 0.1, 0.2, ..., 1.0}; defaults to 0.1
    """

    proj_key = project.key if isinstance(project, Project) else project
    index_key = data_source.source.index_key

    if isinstance(
        data_source, (PrivateDataDocumentSource, PrivateDataCollectionSource)
    ):
        coords = SemanticBackendResource(proj_key=proj_key, index_key=index_key)
    else:
        coords = SemanticBackendPublicResource(
            proj_key=proj_key,
            index_key=index_key,
            elastic_id=data_source.source.elastic_id,
        )

    params = _APISemanticRetrievalParameters(
        doc_id=(
            None
            if isinstance(data_source, PrivateDataCollectionSource)
            else data_source.document_hash
        ),
        question=question,
        retr_k=retr_k,
        use_reranker=rerank,
        hybrid_search_text_weight=text_weight,
    )

    query = Query()
    task = query.add(
        task_id="QA",
        kind_or_task="SemanticRetrieval",
        parameters=params.dict(),
        coordinates=coords,
    )
    task.output("items").output_as("items")

    return query
