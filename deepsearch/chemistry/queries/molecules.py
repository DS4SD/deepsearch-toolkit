from enum import Enum
from typing import List, Union

from pydantic.v1 import BaseModel

from deepsearch.cps.client.queries import Query

from ..resources import ChemVecDbResource, KnowledgeDbResource


class MolQueryType(str, Enum):
    SIMILARITY = "similarity"
    SUBSTRUCTURE = "substructure"


class MolQueryLang(str, Enum):
    SMILES = "smiles"
    SMARTS = "smarts"


class MolIdType(str, Enum):
    SMILES = "smiles"
    SMARTS = "smarts"
    INCHI = "inchi"
    INCHIKEY = "inchikey"


class MolId(BaseModel):
    type: MolIdType
    value: str


CHEMVECDB_COLLECTIONS = {
    MolQueryType.SIMILARITY: "patcid_tanimoto",
    MolQueryType.SUBSTRUCTURE: "patcid_substructure",
}


def MoleculeQuery(
    query: str,
    query_type: MolQueryType,
    query_lang: MolQueryLang = MolQueryLang.SMILES,
    num_items: int = 10,
) -> Query:
    """
    Use the vector database in Deep Search for querying molecules
    by substructure or similarity.
    The result is contained in the `molecules` output of the response.
    """

    mol_query = Query()
    vec_search_task = mol_query.add(
        "ChemVec",
        task_id="vec_search",
        parameters={
            "query_type": query_type,
            "query_lang": query_lang,
            "coll_name": CHEMVECDB_COLLECTIONS[query_type],
            "query": query,
            "topk": num_items,
        },
        coordinates=ChemVecDbResource(),
    )

    projection_task = mol_query.add(
        "Projection",
        task_id="projection",
        parameters={
            "projections": {
                "nodes": {"field_path": ["$$map", "id"]},
            }
        },
        inputs={"nodes": vec_search_task.output("compounds")},
    )

    lookup_task = mol_query.add(
        "DbSubject",
        task_id="db_lookup",
        parameters={
            "identifiers": {
                "persistent_identifiers": {"#Input": {"db_lookup": "nodes"}}
            },
            "limit": num_items,
        },
        inputs={"nodes": projection_task.output("nodes")},
        coordinates=KnowledgeDbResource(),
    )

    lookup_task.output("subjects").output_as("molecules")

    return mol_query


def MoleculesInPatentsQuery(
    patents: Union[str, List[str]],
    num_items: int = 10,
    partial_lookup: bool = False,
) -> Query:
    """
    List all molecules contained in a list of patents.
    The result is contained in the `molecules` output of the response.
    """

    if isinstance(patents, str):
        patents = [patents]

    mol_query = Query()
    lookup_task = mol_query.add(
        "DbSubject",
        task_id="db_lookup",
        parameters={
            "references": {
                "identifiers": [
                    {
                        "type": "patentid",
                        "value": v,
                    }
                    for v in patents
                ]
            },
            "partial_references": partial_lookup,
            "limit": num_items,
        },
        coordinates=KnowledgeDbResource(),
    )

    lookup_task.output("subjects").output_as("molecules")

    return mol_query


def PatentsWithMoleculesQuery(
    molecules: List[MolId],
    num_items: int = 10,
) -> Query:
    """
    List all patents containing any of the input molecules.
    The result is contained in the `patents` output of the response.
    """

    doc_query = Query()
    lookup_task = doc_query.add(
        "DbDocument",
        task_id="db_lookup",
        parameters={
            "subjects": {
                "identifiers": [
                    {
                        "type": item.type.value,
                        "value": item.value,
                    }
                    for item in molecules
                ]
            },
            "limit": num_items,
        },
        coordinates=KnowledgeDbResource(),
    )

    lookup_task.output("documents").output_as("patents")

    return doc_query
