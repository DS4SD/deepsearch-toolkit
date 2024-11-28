from abc import ABC
from typing import Any, Type, overload

from pydantic import BaseModel

from deepsearch.chemistry.models import ChemistryCompound, ChemistryDocument
from deepsearch.chemistry.resources import KnowledgeDbResource
from deepsearch.cps.client import api
from deepsearch.cps.client.queries.query import Query


class ChemistryQuery(BaseModel, ABC):
    _result_type: Type


class CompoundsQuery(ChemistryQuery):
    _result_type = ChemistryCompound


class DocumentsQuery(ChemistryQuery):
    _result_type = ChemistryDocument


class CompoundsByIds(CompoundsQuery):
    """Query compounds that have any of the given identifiers."""

    persistent_ids: list[str] = []


class CompoundsBySmiles(CompoundsQuery):
    """Query compounds that (exactly) match the given SMILES code."""

    structure: str


class CompoundsBySmarts(CompoundsQuery):
    """Query compounds that (exactly) match the given SMARTS code."""

    structure: str


class CompoundsBySimilarity(CompoundsQuery):
    """Query compounds that are similar to the given SMILES code."""

    structure: str
    threshold: float = 0.9


class CompoundsBySubstructure(CompoundsQuery):
    """Query compounds that contain a substructure with the given SMILES code."""

    structure: str


class CompoundsIn(CompoundsQuery):
    """Query compounds that occur in the given documents."""

    documents: DocumentsQuery


class DocumentsByIds(DocumentsQuery):
    """Query documents that have any of the given identifiers."""

    publication_ids: list[str] = []
    application_ids: list[str] = []
    persistent_ids: list[str] = []


class DocumentsHaving(DocumentsQuery):
    """Query documents that contain compounds matching the given query."""

    compounds: CompoundsQuery


@overload
def query_chemistry(
    api: api.CpsApi, query: CompoundsQuery, offset: int = 0, limit: int = 10
) -> list[ChemistryCompound]: ...


@overload
def query_chemistry(
    api: api.CpsApi, query: DocumentsQuery, offset: int = 0, limit: int = 10
) -> list[ChemistryDocument]: ...


def query_chemistry(
    api: api.CpsApi, query: ChemistryQuery, offset: int = 0, limit: int = 10
) -> list[Any]:
    """Perform a chemistry query on the knowledge base."""

    # Resolve knowledge lookup functions and arguments.
    function_names = {
        CompoundsByIds: "compounds",
        CompoundsBySmiles: "compounds_by_smiles",
        CompoundsBySmarts: "compounds_by_smarts",
        CompoundsBySimilarity: "compounds_by_similarity",
        CompoundsBySubstructure: "compounds_by_substructure",
        CompoundsIn: "compounds_in_documents",
        DocumentsByIds: "documents",
        DocumentsHaving: "documents_having_compounds",
    }

    query_parts: list[ChemistryQuery] = [query]

    if type(query) is CompoundsIn:
        query_parts.append(query.documents)
    elif type(query) is DocumentsHaving:
        query_parts.append(query.compounds)

    function_parts = [function_names[type(q)] for q in query_parts]
    arguments = query_parts[-1].model_dump()

    # Compose query task.
    query_tasks = Query()

    lookup = query_tasks.add(
        "KnowledgeLookup",
        task_id="lookup",
        parameters={
            "schema": "patcid",
            "function": function_parts,
            "arguments": arguments,
            "offset": offset,
            "limit": limit,
        },
        coordinates=KnowledgeDbResource(),
    )
    lookup.output("result").output_as("result")

    # Run task.
    response = api.queries.run(query_tasks)

    return [
        query_parts[0]._result_type.model_validate(item)
        for item in response.outputs["result"]
    ]
