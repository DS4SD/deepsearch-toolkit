from typing import Any, Dict, List

from pydantic.v1 import BaseModel


def _resolve_item(item, doc):
    """
    Return the resolved item in the document.
    If the item is referencing another part of the document, it will be retrieved.
    """

    # TODO: improve the function for handling proper json path (not only two segments)
    try:
        if "$ref" in item:
            parts = item["$ref"].split("/")
            citem = doc[parts[1]][int(parts[2])]
        elif "__ref" in item:
            parts = item["__ref"].split("/")
            citem = doc[parts[1]][int(parts[2])]
        else:
            citem = item

        return citem

    except KeyError:
        return None


class EntitiesLookup:
    class _MatchedEntry(BaseModel):
        index: int
        doc_path: str
        type: str
        content: Dict[str, Any]

    def __init__(self, document: Dict[str, Any]):
        self.document = document
        self._lookup: Dict[
            str, Dict[str, List[EntitiesLookup._MatchedEntry]]
        ] = {}  # {entity_type: {entity_instance: [reference, ...]}}
        self._build()

    def _build(self):
        """
        Build the internal lookup structure for entities in a document.
        """
        for ix, item in enumerate(self.document["main-text"]):
            item = _resolve_item(item, self.document)
            if not "entities" in item:
                continue

            me = EntitiesLookup._MatchedEntry(
                index=ix,
                doc_path=f"main-text.{ix}",
                type=item["type"],
                content=item,
            )

            for entity_type, entities in item["entities"].items():
                if not entity_type in self._lookup:
                    self._lookup[entity_type] = {}

                for entity in entities:
                    matches = {entity["match"], entity["original"]}
                    for match in matches:
                        if not match in self._lookup[entity_type]:
                            self._lookup[entity_type][match] = []

                        self._lookup[entity_type][match].append(me)

    def get(self, *, entity_type: str, entity: str) -> List[_MatchedEntry]:
        """
        Lookup where a given entity is mentioned in a document.
        """
        return self._lookup.get(entity_type, {}).get(entity, [])
