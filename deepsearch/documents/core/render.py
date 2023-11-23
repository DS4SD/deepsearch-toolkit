from typing import Any, Dict


def get_figure_svg(document: Dict[str, Any], figure: Dict[str, Any]):
    """
    Generates a SVG which crops the figure from the image of the document page.
    """
    page_no = figure["prov"][0]["page"]
    doc_page_dims = next(
        (p for p in document["page-dimensions"] if p["page"] == page_no), None
    )
    if doc_page_dims is None:
        return ""

    s3_page_image = next(
        (p for p in document["_s3_data"]["pdf-images"] if p["page"] == page_no), None
    )
    if s3_page_image is None:
        return ""

    [pw, ph] = doc_page_dims["width"], doc_page_dims["height"]
    [x1, y1, x2, y2] = figure["prov"][0]["bbox"]

    page_url = s3_page_image["url"]

    svg = f"""
    <svg viewBox="{x1} {ph - y2} {x2 - x1} {y2 - y1}">
        <image width={pw} height={ph} href="{page_url}" /> 
    </svg>
    """
    return svg


def get_page_svg_with_item(document: Dict[str, Any], item: Dict[str, Any]):
    """
    Generates a SVG which overlays the bounding-box of the item with the image of the page.
    """
    page_no = item["prov"][0]["page"]
    doc_page_dims = next(
        (p for p in document["page-dimensions"] if p["page"] == page_no), None
    )
    if doc_page_dims is None:
        return ""

    s3_page_image = next(
        (p for p in document["_s3_data"]["pdf-images"] if p["page"] == page_no), None
    )
    if s3_page_image is None:
        return ""

    [pw, ph] = doc_page_dims["width"], doc_page_dims["height"]
    [x1, y1, x2, y2] = item["prov"][0]["bbox"]

    page_url = s3_page_image["url"]

    svg = f"""
    <svg viewBox="0 0 {pw} {ph}">
        <image width={pw} height={ph} href="{page_url}" /> 
        <rect x="{x1}" y="{ph - y2}" width="{x2 - x1}" height="{y2 - y1}" style="stroke-width:0.03;stroke:rgb(0,0,255);fill-opacity:0" />
    </svg>
    """
    return svg
