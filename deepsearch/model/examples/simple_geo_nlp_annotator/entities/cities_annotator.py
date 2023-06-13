import os
from typing import Any, Optional

from .common.dictionary_text_entity_annotator import (
    Config,
    DictionaryTextEntityAnnotator,
)
from .common.utils import resources_dir


class CitiesAnnotator(DictionaryTextEntityAnnotator):
    def key(self) -> str:
        return "cities"

    def description(self) -> str:
        return "Names of cities"

    def __init__(self):
        super().__init__(
            Config(dictionary_filename=os.path.join(resources_dir, "cities.json"))
        )
