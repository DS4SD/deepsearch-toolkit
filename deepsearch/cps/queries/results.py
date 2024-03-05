from __future__ import annotations

from typing import List

from pydantic.v1 import BaseModel, root_validator

from deepsearch.cps.client.components.queries import RunQueryResult


class SearchResultItem(BaseModel):
    doc_hash: str
    path_in_doc: str
    passage: str
    source_is_text: bool

    @root_validator(pre=True)
    def patch_pos(cls, values):
        path_in_doc = values.get("path_in_doc")
        pos_in_doc = values.get("pos_in_doc")
        if pos_in_doc is not None and isinstance(pos_in_doc, int) and not path_in_doc:
            values["path_in_doc"] = f"main-text.{pos_in_doc}"
        return values


class RAGGroundingInfo(BaseModel):
    items: List[SearchResultItem]


class RAGAnswerItem(BaseModel):
    answer: str
    grounding: RAGGroundingInfo


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
                            items=[
                                SearchResultItem.parse_obj(search_result_items[i])
                                for i in answer_item["grounding_retr_idxs"]
                            ]
                        ),
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
