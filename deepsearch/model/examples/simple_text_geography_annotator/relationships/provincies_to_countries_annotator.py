from ..entities.countries_annotator import CountriesAnnotator  # type: ignore
from ..entities.provincies_annotator import ProvinciesAnnotator  # type: ignore
from .common.multi_entities_relationship_annotator import (
    Config,
    MultiEntitiesRelationshipAnnotator,
)


class ProvinciesToCountriesAnnotator(MultiEntitiesRelationshipAnnotator):
    def __init__(self):
        super().__init__(
            Config(entities=[ProvinciesAnnotator().key(), CountriesAnnotator().key()])
        )
