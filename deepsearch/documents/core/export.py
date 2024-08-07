import html
import logging
import warnings
from typing import Any, Dict

from docling_core.types import Document as DsDocument

_log = logging.getLogger(__name__)


class JsonToHTML:
    def __init__(self):
        return

    def template(self):

        template = """<!DOCTYPE html>

        <html>

        <head>
        <meta charset="UTF-8" />
        <title>TITLE</title>

        <style>
        ul            {   border: 2px solid red; }
        li            {   border: 1px solid blue; }
        section       {   border: 1px dashed green; }
        span.title    {   background-color: yellow; }
        span.number   {   background-color: aquamarine; }
        .footnote     {   font-size: 70%; }
        sup, sub      {   background-color: coral; }
        table         { border-collapse: collapse; margin-top: 50px; }
        table, td, th { border: 1px solid black; padding: 8px; text-align: left; }
        tr:hover      { background-color:#f5f5f5 }
        </style>

        <labeler-meta>
        PAGES-BBOX
        PAGES-SOURCES
        </labeler-meta>

        </head>

        <body>
        <h1>TITLE</h1>

        BODY
        </body>

        </html>
        """

        pages_bbox = ""
        if self.pages is not None:
            for page in self.pages:
                pages_bbox += '<bbox page="{page}" x="0" y="0" width="{width}" height="{height}" />\n'.format(
                    **page
                )

        pages_sources = ""
        if self.page_hashes is not None:
            for page in self.page_hashes:
                pages_sources += '<source page="{page}" model="{model}" page-hash="{hash}" />\n'.format(
                    **page
                )

        template = template.replace("PAGES-BBOX", pages_bbox).replace(
            "PAGES-SOURCES", pages_sources
        )

        return template

    def get_title(self, data):

        title = ""

        if "description" in data:
            if "title" in data["description"]:
                return data["description"]["title"]

        return title

    def get_page(self, item):

        if "page" in item:
            return 'page="{}"'.format(item["page"])
        else:
            return ""

    def get_style(self, item):

        style = "font-family:Times-Roman; color: rgb(0, 0, 0);"
        if "font" in item:
            style = (
                "font-family:"
                + (item["font"].split("+"))[-1]
                + "; color: rgb(0, 0, 0);"
            )

        return style

    def get_refs(self, ref):
        splits = ref.split("/")
        if len(splits) == 0 or splits[0] != "#":
            _log.error("Can only interpret internal references")
            return {}

        obj = self.data
        splits = splits[1:]
        while len(splits):
            if isinstance(obj, list):
                ix = int(splits[0])

                if ix < len(obj):
                    obj = obj[ix]
                else:
                    _log.error("Element {} not found. %s", splits)

            elif isinstance(obj, dict):
                if splits[0].isdigit() and int(splits[0]) in obj:
                    ix = int(splits[0])
                else:
                    ix = splits[0]

                if ix in obj:
                    obj = obj[ix]
                else:
                    _log.error("Element {} not found. %s", splits)

            splits = splits[1:]
        return obj

    def get_tablecell_span(self, cell, ix):
        span = set([s[ix] for s in cell["spans"]])
        if len(span) == 0:
            return 1, None, None
        return len(span), min(span), max(span)

    def make_bbox_dict(self, page, bbox_rect):
        bbox = {}
        bbox["page"] = "{:d}".format(page)
        if bbox_rect is None:
            return bbox

        x0, y0, x1, y1 = [float(v) for v in bbox_rect]
        width = x1 - x0
        height = y1 - y0
        if self.pages is not None:
            page_dimensions = [p for p in self.pages if p["page"] == page][0]
            y0 = page_dimensions["height"] - height - y0
            y1 = page_dimensions["height"] + height - y1
        bbox["x"] = str(x0)
        bbox["y"] = str(y0)
        bbox["width"] = str(width)
        bbox["height"] = str(height)
        return bbox

    def make_bbox(self, page, bbox_rect):
        bbox_dict = self.make_bbox_dict(page, bbox_rect)
        bbox = " ".join(['{}="{}"'.format(k, v) for k, v in bbox_dict.items()])
        return bbox

    def split_item_in_boxes(self, item):
        boxes = []
        dirty_text = item["text"]
        if not "prov" in item:
            boxes.append(["", self.clean(dirty_text)])
            _log.warning("Element missing prov")
        else:
            for box in item["prov"]:
                if not "span" in box:
                    _log.warning("Element missing span")
                    box["span"] = [0, len(item["text"])]

            spans_size = max(box["span"][1] for box in item["prov"])
            shift = abs(len(dirty_text) - spans_size)
            for box in item["prov"]:
                start = max(0, box["span"][0] - shift)
                end = max(0, box["span"][1] - shift)
                if box["span"][1] == spans_size:
                    end = len(dirty_text)
                boxes.append(
                    [
                        self.make_bbox(box["page"], box["bbox"]),
                        self.clean(dirty_text[start:end]),
                    ]
                )
        return boxes

    def get_body_new(self, data):

        body = ""

        subtitle_l1 = False
        subtitle_l2 = False
        subtitle_l3 = False
        subtitle_l4 = False
        subtitle_l5 = False
        subtitle_l6 = False

        enumeration = False
        subenumeration = False
        subsubenumeration = False

        opened_list = False

        # loop though content
        for item in data["main-text"]:

            # if this is a reference, get it
            if "$ref" in item:
                item = self.get_refs(item["$ref"])
            if "__ref" in item:
                item = self.get_refs(item["__ref"])

            page = self.get_page(item)
            style = self.get_style(item)

            if item["type"] == "subtitle-level-1" or item["type"] == "subtitle":

                if opened_list:
                    body += "</ul>\n"
                    opened_list = False

                if subtitle_l6:
                    body += "</section>\n"
                    subtitle_l6 = False

                if subtitle_l5:
                    body += "</section>\n"
                    subtitle_l5 = False

                if subtitle_l4:
                    body += "</section>\n"
                    subtitle_l4 = False

                if subtitle_l3:
                    body += "</section>\n"
                    subtitle_l3 = False

                if subtitle_l2:
                    body += "</section>\n"
                    subtitle_l2 = False

                if subtitle_l1:
                    body += "</section>\n"

                subtitle_l1 = True

                body += "<section>\n"

                body += '<h2><span class="title" info="subtitle_l1" {page}><span style="{style}">'.format(
                    page=page, style=style
                )
                for bbox, text in self.split_item_in_boxes(item):
                    body += "<bbox {bbox}>{text}</bbox>\n".format(bbox=bbox, text=text)
                body += "</span></span></h2>\n"

            elif item["type"] == "subtitle-level-2" or item["type"] == "subsubtitle":

                if opened_list:
                    body += "</ul>\n"
                    opened_list = False

                if subtitle_l6:
                    body += "</section>\n"
                    subtitle_l6 = False

                if subtitle_l5:
                    body += "</section>\n"
                    subtitle_l5 = False

                if subtitle_l4:
                    body += "</section>\n"
                    subtitle_l4 = False

                if subtitle_l3:
                    body += "</section>\n"
                    subtitle_l3 = False

                if subtitle_l2:
                    body += "</section>\n"

                subtitle_l2 = True

                body += "<section>\n"

                body += '<p><span class="title" info="subtitle_l2" {page}><span style="{style}">\n'.format(
                    page=page, style=style
                )
                for bbox, text in self.split_item_in_boxes(item):
                    body += "<bbox {bbox}>{text}</bbox>\n".format(bbox=bbox, text=text)
                body += "</span></span></p>\n"

            elif item["type"] == "subtitle-level-3" or item["type"] == "subsubsubtitle":

                if opened_list:
                    body += "</ul>\n"
                    opened_list = False

                if subtitle_l6:
                    body += "</section>\n"
                    subtitle_l6 = False

                if subtitle_l5:
                    body += "</section>\n"
                    subtitle_l5 = False

                if subtitle_l4:
                    body += "</section>\n"
                    subtitle_l4 = False

                if subtitle_l3:
                    body += "</section>\n"

                subtitle_l3 = True

                body += "<section>\n"

                body += '<p><span class="title" info="subtitle_l3" {page}><span style="{style}">\n'.format(
                    page=page, style=style
                )
                for bbox, text in self.split_item_in_boxes(item):
                    body += "<bbox {bbox}>{text}</bbox>\n".format(bbox=bbox, text=text)
                body += "</span></span></p>\n"

            elif item["type"] == "subtitle-level-4":

                if opened_list:
                    body += "</ul>\n"
                    opened_list = False

                if subtitle_l6:
                    body += "</section>\n"
                    subtitle_l6 = False

                if subtitle_l5:
                    body += "</section>\n"
                    subtitle_l5 = False

                if subtitle_l4:
                    body += "</section>\n"

                subtitle_l4 = True

                body += "<section>\n"

                body += '<p><span class="title" info="subtitle_l4" {page}><span style="{style}">\n'.format(
                    page=page, style=style
                )
                for bbox, text in self.split_item_in_boxes(item):
                    body += "<bbox {bbox}>{text}</bbox>\n".format(bbox=bbox, text=text)
                body += "</span></span></p>\n"

            elif item["type"] == "subtitle-level-5":

                if opened_list:
                    body += "</ul>\n"
                    opened_list = False

                if subtitle_l6:
                    body += "</section>\n"
                    subtitle_l6 = False

                if subtitle_l5:
                    body += "</section>\n"

                subtitle_l5 = True

                body += "<section>\n"

                body += '<p><span class="title" info="subtitle_l5" {page}><span style="{style}">\n'.format(
                    page=page, style=style
                )
                for bbox, text in self.split_item_in_boxes(item):
                    body += "<bbox {bbox}>{text}</bbox>\n".format(bbox=bbox, text=text)
                body += "</span></span></p>\n"

            elif item["type"] == "subtitle-level-6":

                if opened_list:
                    body += "</ul>\n"
                    opened_list = False

                if subtitle_l6:
                    body += "</section>\n"

                subtitle_l6 = True

                body += "<section>\n"

                body += '<p><span class="title" info="subtitle_l5" {page}><span style="{style}">\n'.format(
                    page=page, style=style
                )
                for bbox, text in self.split_item_in_boxes(item):
                    body += "<bbox {bbox}>{text}</bbox>\n".format(bbox=bbox, text=text)
                body += "</span></span></p>\n"

            elif item["type"] in ["paragraph"]:

                if (
                    "name" in item
                    and item["name"].startswith("list-item")
                    and opened_list
                ):

                    body += (
                        '<li><span info="paragraph" style="{style}" {page}>\n'.format(
                            page=page, style=style
                        )
                    )
                    for bbox, text in self.split_item_in_boxes(item):
                        body += "<bbox {bbox}>{text}</bbox>\n".format(
                            bbox=bbox, text=text
                        )
                    body += "</span></li>\n"

                elif "name" in item and item["name"].startswith("list-item"):

                    body += "<ul>\n"
                    opened_list = True

                    body += (
                        '<li><span info="paragraph" style="{style}" {page}>\n'.format(
                            page=page, style=style
                        )
                    )
                    for bbox, text in self.split_item_in_boxes(item):
                        body += "<bbox {bbox}>{text}</bbox>\n".format(
                            bbox=bbox, text=text
                        )
                    body += "</span></li>\n"

                else:
                    if opened_list:
                        body += "</ul>\n"
                        opened_list = False

                    body += (
                        '<p><span info="paragraph" style="{style}" {page}>\n'.format(
                            page=page, style=style
                        )
                    )
                    for bbox, text in self.split_item_in_boxes(item):
                        body += "<bbox {bbox}>{text}</bbox>\n".format(
                            bbox=bbox, text=text
                        )
                    body += "</span></p>\n"

            elif item["type"] == "caption":

                if opened_list:
                    body += "</ul>\n"
                    opened_list = False

                body += '<p><span info="caption" style="{style}" {page}>\n'.format(
                    page=page, style=style
                )
                for bbox, text in self.split_item_in_boxes(item):
                    body += "<bbox {bbox}>{text}</bbox>\n".format(bbox=bbox, text=text)
                body += "</span></p>\n"

            elif item["type"] == "footnote":

                if opened_list:
                    body += "</ul>\n"
                    opened_list = False

                body += '<p class="footnote" style="{style}" {page}>\n'.format(
                    page=page, style=style
                )
                for bbox, text in self.split_item_in_boxes(item):
                    body += "<bbox {bbox}>{text}</bbox>\n".format(bbox=bbox, text=text)
                body += "</p>\n"

            elif item["type"] == "page-footer":

                if opened_list:
                    body += "</ul>\n"
                    opened_list = False

                body += '<p class="page-footer" style="{style}" {page}>\n'.format(
                    page=page, style=style
                )
                for bbox, text in self.split_item_in_boxes(item):
                    body += "<bbox {bbox}>{text}</bbox>\n".format(bbox=bbox, text=text)
                body += "</p>\n"

            elif item["type"] == "page-header":

                if opened_list:
                    body += "</ul>\n"
                    opened_list = False

                body += '<p class="page-header" style="{style}" {page}>\n'.format(
                    page=page, style=style
                )
                for bbox, text in self.split_item_in_boxes(item):
                    body += "<bbox {bbox}>{text}</bbox>\n".format(bbox=bbox, text=text)
                body += "</p>\n"

            # elif(item["type"].startswith("list-item-level-")):
            #
            #     body += self.write_enum(item)
            #
            # elif(item["type"]=="enumeration"):
            #
            #     body += self.write_enum(item)

            elif item["type"] == "table":

                if opened_list:
                    body += "</ul>\n"
                    opened_list = False

                body += self.write_table(item)

            ## By defualt dump everything containing text
            elif "text" in item:

                if opened_list:
                    body += "</ul>\n"
                    opened_list = False

                body += '<p><span info="{type}" style="{style}" {page}>\n'.format(
                    page=page, style=style, type=item["type"]
                )
                for bbox, text in self.split_item_in_boxes(item):
                    body += "<bbox {bbox}>{text}</bbox>\n".format(bbox=bbox, text=text)
                body += "</span></p>\n"

            else:
                _log.debug("ignoring")

        if subtitle_l6:
            body += "</section>\n"

        if subtitle_l5:
            body += "</section>\n"

        if subtitle_l4:
            body += "</section>\n"

        if subtitle_l3:
            body += "</section>\n"

        if subtitle_l2:
            body += "</section>\n"

        if subtitle_l1:
            body += "</section>\n"

        return body

    def enum_has_ids(self, enums):

        has_ids = True
        for item in enums:
            if (not ("identifier" in item and item["identifier"] != "?")) and (
                not "data" in item
            ):
                has_ids = False

        return has_ids

    def write_enum(self, item):

        body = ""

        page = self.get_page(item)
        style = self.get_style(item)

        if self.enum_has_ids(item["data"]):
            body += '<ul style="list-style-type: none;" ' + page + ">\n"
        else:
            body += "<ul " + page + ">\n"

        open_enumitem = False
        open_identifier = False

        for enumitem_id, enumitem in enumerate(item["data"]):

            if "text" in enumitem:
                local_identifier = (
                    "identifier" in enumitem and enumitem["identifier"] != "?"
                )

                if not (open_enumitem and open_identifier and not local_identifier):
                    if open_enumitem:
                        body += "</li>\n"
                        open_identifier = False
                    open_enumitem = True

                    body += '<li><span style="' + style + '">\n'
                    if local_identifier:
                        open_identifier = True

                if "item-bbox" in enumitem:
                    item_bbox = self.make_bbox(
                        enumitem["prov"][0]["page"], enumitem["identifier-bbox"]
                    )
                elif len(enumitem["prov"]) > 0:
                    item_bbox = self.make_bbox(
                        enumitem["prov"][0]["page"], enumitem["prov"][0]["bbox"]
                    )
                else:
                    item_bbox = ""

                for bid, (bbox, text) in enumerate(self.split_item_in_boxes(enumitem)):

                    body += "<bbox {bbox}>".format(bbox=bbox)
                    if bid == 0 and local_identifier:
                        if "prov" in enumitem and "identifier-bbox" in enumitem:
                            identif_bbox = self.make_bbox(
                                enumitem["prov"][0]["page"], enumitem["identifier-bbox"]
                            )
                        else:
                            identif_bbox = ""

                        identif_text = self.clean(enumitem["identifier"])
                        body += '<span class="number"><bbox {bbox}>{text}</bbox></span>'.format(
                            bbox=identif_bbox, text=identif_text
                        )

                    this_item_bbox = item_bbox if bid == 0 else bbox
                    body += "<span><bbox {bbox}>{text}</bbox></span>".format(
                        text=text, bbox=this_item_bbox
                    )

                    body += "</bbox>\n"

                body += "</span>\n"

            elif "data" in enumitem:

                body += self.write_enum(enumitem)

            # Evaluate internal references
            if "refs" in enumitem and len(enumitem["refs"]) > 0:

                for refitem_id, refitem in enumerate(enumitem["refs"]):
                    if "$ref" in refitem:
                        refitem = self.get_refs(refitem["$ref"])

                    if len(refitem) == 0:
                        continue

                    if refitem["type"] == "table":

                        body += self.write_table(refitem)

                    elif "text" in refitem:

                        refpage = self.get_page(refitem)
                        refstyle = self.get_style(refitem)

                        body += (
                            '<p><span info="{type}" style="{style}" {page}>\n'.format(
                                type=refitem["type"], page=refpage, style=refstyle
                            )
                        )
                        for bbox, text in self.split_item_in_boxes(refitem):
                            body += "<bbox {bbox}>{text}</bbox>\n".format(
                                bbox=bbox, text=text
                            )
                        body += "</span></p>\n"

        if open_enumitem:
            body += "</li>\n"

        body += "</ul>\n"

        return body

    def write_table_simple(self, item):
        if "data" in item:
            data = item["data"]
        else:
            return ""

        body = "\n\n"

        page = self.get_page(item)

        body += "<table " + page + ">"
        for row in data:
            body += "  <tr>\n"
            for cell in row:
                body += "    <td>"
                body += self.clean(cell)
                body += "</td>\n"
            body += "</tr>\n"

        body += "</table>\n\n\n"
        return body

    def write_table(self, item):
        table = item
        body = "\n\n"

        if not "prov" in table:
            return self.write_table_simple(item)

        if not "data" in table:
            return ""

        page = self.get_page(item)
        page_no = table["prov"][0]["page"]

        nrows = table["#-rows"]
        ncols = table["#-cols"]

        table_model = ""
        if "model" in item:
            table_model = 'source="{}"'.format(item["model"])

        try:
            if "bounding-box" in table and "min" in table["bounding-box"]:
                table_bbox = self.make_bbox_dict(page_no, table["bounding-box"]["min"])
            else:
                table_bbox = self.make_bbox_dict(page_no, table["prov"][0]["bbox"])
        except:
            _log.warning("Missing table bbox")
            table_bbox = {}

        table_maximum_bbox = {}
        if "bounding-box" in table and "max" in table["bounding-box"]:
            table_maximum_bbox = self.make_bbox_dict(
                page_no, table["bounding-box"]["max"]
            )
        else:
            table_maximum_bbox = table_bbox

        table_min_bbox_str = " ".join(
            [
                (
                    'data-min-{}="{}"'.format(k, v)
                    if k != "page"
                    else 'data-{}="{}"'.format(k, v)
                )
                for k, v in table_bbox.items()
            ]
        )
        table_max_bbox_str = " ".join(
            [
                'data-max-{}="{}"'.format(k, v)
                for k, v in table_maximum_bbox.items()
                if k != "page"
            ]
        )
        body += "<table {} {}>\n".format(table_min_bbox_str, table_max_bbox_str)
        for i in range(nrows):
            body += "  <tr>\n"
            for j in range(ncols):
                cell = table["data"][i][j]

                rowspan, rowstart, rowend = self.get_tablecell_span(cell, 0)
                colspan, colstart, colend = self.get_tablecell_span(cell, 1)

                if rowstart is not None and rowstart != i:
                    continue
                if colstart is not None and colstart != j:
                    continue

                if rowstart is None:
                    rowstart = i
                if colstart is None:
                    colstart = j

                content = self.clean(cell["text"])
                if content == "":
                    content = "&nbsp;"
                bbox = (
                    self.make_bbox(page_no, cell["bbox"])
                    if cell["bbox"] is not None
                    else None
                )

                scope = ""
                label = cell["type"]
                label_class = "body"
                if label in ["row_header", "row_multi_header", "row_title"]:
                    label_class = "header"
                    scope = 'scope="row"'
                elif label in ["col_header", "col_multi_header"]:
                    label_class = "header"
                    scope = 'scope="col"'

                celltag = "th" if label_class == "header" else "td"
                style = 'class="label-{}"'.format(label_class)

                if not bbox and content == "&nbsp;":
                    cell_html_content = content
                else:
                    cell_html_content = (
                        "<span><bbox {bbox}>{content}</bbox></span>".format(
                            bbox=bbox, content=content
                        )
                    )

                body += '    <{celltag} {scope} rowstart="{rowstart}" colstart="{colstart}" rowspan="{rowspan}" colspan="{colspan}" label-class="{label_class}" label="{label}" {style}>{content}</{celltag}>\n'.format(
                    celltag=celltag,
                    scope=scope,
                    rowstart=rowstart + 1,
                    colstart=colstart + 1,
                    rowspan=rowspan,
                    colspan=colspan,
                    content=cell_html_content,
                    label_class=label_class,
                    label=label,
                    style=style,
                )

            body += "  </tr>\n"

        body += "</table>\n\n\n"

        return body

    def clean(self, data, escape=True):

        data = data.replace("$_{", "")
        data = data.replace("$^{", "")
        data = data.replace("}$", "")
        if escape:
            data = html.escape(data)
        return data

    def execute(self, data):

        self.data = data
        self.pages = data["page-dimensions"] if "page-dimensions" in data else None
        self.page_hashes = (
            data["file-info"]["page-hashes"]
            if "page-hashes" in data["file-info"]
            else None
        )

        result = self.template()

        title = self.get_title(data)
        body = self.get_body_new(data)

        result = result.replace("TITLE", title)
        result = result.replace("BODY", body)

        result = self.clean(result, escape=False)

        return result


def export_to_html(document: Dict[str, Any]) -> str:

    html_generator = JsonToHTML()
    return html_generator.execute(document)


def export_to_markdown(document: Dict[str, Any]) -> str:
    """ """

    warnings.warn(
        "export_to_markdown() is deprecated and will be removed in a future version. Use the docling_core package instead.",
        DeprecationWarning,
    )

    d: DsDocument = DsDocument.model_validate(document)
    return d.export_to_markdown()
