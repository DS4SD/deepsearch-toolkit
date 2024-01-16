import json
import os
from typing import Any

from deepsearch.documents.core.export import export_to_markdown

def test_export_to_markdown():
    doc: dict[str, Any] | None = None
    root = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(root, "inputs", "export_to_markdown.json")) as file_doc:
        doc = json.load(file_doc)
    assert doc
    assert isinstance(doc, dict)

    md = export_to_markdown(doc)
    assert md
