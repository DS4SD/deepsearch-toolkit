from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel

from deepsearch.cps.client.components.queries import RunQueryResult


class ChunkRef(BaseModel):
    doc_hash: str
    main_path: str  # the anchor path among the contributing group
    path_group: List[str]  # the doc paths contributing to the encoding source


class SearchResultItem(ChunkRef):
    chunk: str
    source_is_text: bool


class RAGGroundingInfo(BaseModel):
    retr_items: Optional[List[SearchResultItem]] = None
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
    search_result_items: Optional[List[SearchResultItem]] = None

    @classmethod
    def from_api_output(cls, data: RunQueryResult, raise_on_error=True):
        answers: List[RAGAnswerItem] = []
        try:
            retrieval_part = data.outputs["retrieval"]
            if retrieval_part is not None:
                search_result_items = retrieval_part["items"]
                if raise_on_error and len(search_result_items) == 0:
                    raise NoSearchResultsError()
            else:
                search_result_items = None
            for answer_item in data.outputs["answers"]:
                if raise_on_error and (gen_err := answer_item.get("gen_err")):
                    raise GenerationError(gen_err)
                retr_idxs = answer_item["grounding_info"]["retr_idxs"]
                answers.append(
                    RAGAnswerItem(
                        answer=answer_item["answer"],
                        grounding=RAGGroundingInfo(
                            retr_items=(
                                [
                                    SearchResultItem.model_validate(
                                        search_result_items[i]
                                    )
                                    for i in retr_idxs
                                ]
                                if retr_idxs is not None and retrieval_part is not None
                                else None
                            ),
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
