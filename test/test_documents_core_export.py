import json
import os
from typing import Any

from deepsearch.documents.core.export import export_to_markdown, export_to_html

def test_export_to_markdown():
    doc: dict[str, Any] | None = None
    root = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(root, "inputs", "test_document.json")) as file_doc:
        doc = json.load(file_doc)
    assert doc
    assert isinstance(doc, dict)

    md = export_to_markdown(doc)
    assert md

    """
    with open(os.path.join(root, "inputs", "test_document.md"), "w") as fw:
        fw.write(md)
    """
    
    html = export_to_html(doc)
    assert html

    """
    with open(os.path.join(root, "inputs", "test_document.html"), "w") as fw:
        fw.write(html)
    """
    
