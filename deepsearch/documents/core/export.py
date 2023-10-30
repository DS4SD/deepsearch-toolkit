from typing import Any, Dict

from tabulate import tabulate


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


def export_to_markdown(document: Dict[str, Any]) -> str:
    """ """

    markdown_text = ""
    prev_text = ""
    has_title = False

    for item in document["main-text"]:

        item = _resolve_item(item, document)

        if item == None:
            continue

        item_type = item["type"]

        if (
            item_type in ("title", "subtitle-level-1", "paragraph", "caption")
            and "text" in item
        ):

            text = item["text"]

            # Ignore repeated text
            if prev_text == text:
                continue
            else:
                prev_text = text

            # The first match of a title type
            if item_type == "title" and (not has_title):
                markdown_text += f"# {text}\n\n"
                has_title = True

            # Secondary titles
            elif item_type in ("title", "subtitle-level-1") or (
                has_title and item_type == "title"
            ):
                markdown_text += f"## {text}\n\n"

            # Normal text
            else:
                markdown_text += f"{text}\n\n"

        elif item_type in ("table"):

            table = []
            for row in item["data"]:

                tmp = []
                for col in row:
                    tmp.append(col.get("text", ""))
                table.append(tmp)

            if len(table) > 1 and len(table[0]) > 0:

                markdown_text += tabulate(
                    table[1:], headers=table[0], tablefmt="github"
                )
                markdown_text += "\n\n"

    return markdown_text
