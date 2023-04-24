from ..entities.cities_annotator import CitiesAnnotator  # type: ignore
from ..entities.countries_annotator import CountriesAnnotator  # type: ignore
from .common.multi_entities_relationship_annotator import (
    Config,
    MultiEntitiesRelationshipAnnotator,
)


class CitiesToCountriesAnnotator(MultiEntitiesRelationshipAnnotator):
    def __init__(self):
        super().__init__(
            Config(entities=[CitiesAnnotator().key(), CountriesAnnotator().key()])
        )
