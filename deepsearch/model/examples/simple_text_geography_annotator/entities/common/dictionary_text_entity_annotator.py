import logging

logger = logging.getLogger("cps-nlp")
import json
import re
from dataclasses import dataclass
from typing import List, Optional

from .base_text_entity_annotator import BaseTextEntityAnnotator


@dataclass
class Config:
    dictionary_filename: str


class DictionaryTextEntityAnnotator(BaseTextEntityAnnotator):
    def __init__(self, config: Config):
        self.config = config
        self._initialized = False

    def initialize(self):
        if self._initialized:
            return

        ## In this example annotator, we load dictionaries.
        ## Here you might load AI models instead.
        logger.info("reading from %s", self.config.dictionary_filename)
        with open(self.config.dictionary_filename) as f:
            dictionary = json.load(f)
            logger.info("loaded %s", len(dictionary))
            self._exprs = self._compile_dictionary(dictionary)
            logger.info("compiled expr")

        self._initialized = True

    ## Dictionary compilation.
    ## If you use AI models instead of dictionaries, no similar function is needed.
    def _compile_dictionary(self, dictionary):
        logger.info("compiling dictionary")

        # delimiters used to avoid partial matches
        starts_with = "(^|\s|'|\"|\(|\{|\[|\,|\.|\!|\?|\:|\;)"
        ends_with = "($|\s|'|\"|\)|\}|\]|\,|\.|\!|\?|\:|\;)"
        try:
            tmp = []
            for item in dictionary:
                tmp.append(re.escape(item))

            # The regex is split into multiple expressions if we exceed 4096 characters.
            # This is needed to avoid length limits of regex.
            exprs = []
            MAX_LEN = 48
            local = []
            for texpr in tmp:

                if len("|".join(local)) > 4096:

                    expr_str = starts_with + "(" + "|".join(local) + ")" + ends_with
                    expr = re.compile(expr_str)
                    exprs.append(expr)

                    local = []

                if len(texpr) < MAX_LEN:
                    local.append(texpr)
                else:
                    logger.warning(
                        "name of entity '%s' is longer than %s chars", texpr, MAX_LEN
                    )

            if len(local) > 0:
                expr_str = starts_with + "(" + "|".join(local) + ")" + ends_with
                expr = re.compile(expr_str)
                exprs.append(expr)
        except BaseException as e:
            logger.exception("Could not compile the dictionary")
            raise RuntimeError("Could not compile the dictionary")
        return exprs

    def annotate_entities_text(self, text: str) -> list:
        self.initialize()

        ## Annotate one text string with the desired entities.
        ## Output: List of entities in CPS format, i.e., dicts with keys type, match, original, range.

        logger.debug("------ Starting 'annotate_entities_text' -------")
        matches = []

        # Run all expressions created for this entity_name
        for expr in self._exprs:
            for match in re.finditer(expr, text):
                beg = match.group(1)
                end = match.group(3)
                orig = match.group(2)

                tmp = {
                    "type": self.key(),
                    "match": orig,
                    "original": orig,
                    "range": [match.start() + len(beg), match.end() - len(end)],
                }
                matches.append(tmp)

        return matches
