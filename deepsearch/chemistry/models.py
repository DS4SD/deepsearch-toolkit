from typing import Optional

from pydantic import BaseModel


class ChemistryModel(BaseModel, extra="allow"):
    id: int
    """Transient identifier for short term use."""

    persistent_id: str
    """Identifier for long term (storage) use."""


class ChemistryDocument(ChemistryModel):
    application_id: Optional[str]
    """Identifier under which a patent application has been filed."""

    publication_id: Optional[str]
    """Identifier under which a patent has been published."""

    title: str
    """(Readable) title of the document."""


class ChemistryCompound(ChemistryModel):
    smiles: str
    """SMILES representation of compound structure."""

    display_name: str
    """User friendly representation of compound."""

    inchi: str
    """InChI representation of compound structure."""

    inchikey: str
    """Hashed form of InChI."""

    sum_formula: str
    """Sum formula of compound. For example 'C6 O2 H5'"""
