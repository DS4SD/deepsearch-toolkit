from __future__ import annotations

from typing import List, Optional

from pydantic.v1 import BaseModel, root_validator

from deepsearch.cps.client.components.queries import RunQueryResult


class SearchResultItem(BaseModel):
    doc_hash: str
    chunk: str
    main_path: str
    path_group: List[str]
    source_is_text: bool


class RAGGroundingInfo(BaseModel):
    retr_items: List[SearchResultItem]
    gen_ctx_paths: List[str]


class RAGAnswerItem(BaseModel):
    answer: str
    grounding: RAGGroundingInfo
    prompt: Optional[str] = None


class SemanticError(Exception):
    pass


class GenerationError(SemanticError):
    def __init__(self, msg="", *args, **kwargs):
        err_msg = "There was an error during generation"
        if msg:
            err_msg += f": {msg}"
        super().__init__(err_msg, *args, **kwargs)


class NoSearchResultsError(SemanticError):
    def __init__(self, msg="Search returned no results", *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class RAGResult(BaseModel):
    answers: List[RAGAnswerItem]
    search_result_items: List[SearchResultItem]

    @classmethod
    def from_api_output(cls, data: RunQueryResult, raise_on_error=True):
        answers: List[RAGAnswerItem] = []
        try:
            search_result_items = data.outputs["retrieval"]["items"]
            if raise_on_error and len(search_result_items) == 0:
                raise NoSearchResultsError()
            for answer_item in data.outputs["answers"]:
                if raise_on_error and (gen_err := answer_item.get("gen_err")):
                    raise GenerationError(gen_err)
                answers.append(
                    RAGAnswerItem(
                        answer=answer_item["answer"],
                        grounding=RAGGroundingInfo(
                            retr_items=[
                                SearchResultItem.parse_obj(search_result_items[i])
                                for i in answer_item["grounding_info"]["retr_idxs"]
                            ],
                            gen_ctx_paths=answer_item["grounding_info"][
                                "gen_ctx_paths"
                            ],
                        ),
                        prompt=answer_item["prompt"],
                    ),
                )
        except KeyError:
            raise ValueError("Unexpected input format.")
        return RAGResult(
            answers=answers,
            search_result_items=search_result_items,
        )


class SearchResult(BaseModel):
    search_result_items: List[SearchResultItem]

    @classmethod
    def from_api_output(cls, data: RunQueryResult, raise_on_error=True):
        try:
            search_result_items = data.outputs["items"]
            if raise_on_error and len(search_result_items) == 0:
                raise NoSearchResultsError()
        except KeyError:
            raise ValueError("Unexpected input format.")
        return SearchResult(
            search_result_items=search_result_items,
        )
