from ..entities.cities_annotator import CitiesAnnotator  # type: ignore
from ..entities.provincies_annotator import ProvinciesAnnotator  # type: ignore
from .common.multi_entities_relationship_annotator import (
    Config,
    MultiEntitiesRelationshipAnnotator,
)


class CitiesToProvinciesAnnotator(MultiEntitiesRelationshipAnnotator):
    def __init__(self):
        super().__init__(
            Config(entities=[CitiesAnnotator().key(), ProvinciesAnnotator().key()])
        )
