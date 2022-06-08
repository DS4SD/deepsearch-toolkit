from typing import Any, Dict
from urllib.parse import parse_qs, urlparse

from IPython.display import Javascript, display

CPS_IPYTHON_NOTEBOOK_URL = ""


def init() -> None:
    code = """
        IPython.notebook.kernel.execute("import deepsearch.cps.ipython; cps.ipython.CPS_IPYTHON_NOTEBOOK_URL = '" + window.location + "'");
    """
    display(Javascript(code))


def get_notebook_args() -> Dict[str, Any]:
    parsed = urlparse(CPS_IPYTHON_NOTEBOOK_URL)
    kwargs = parse_qs(parsed.query)
    result = {
        "proj_key": kwargs["proj_key"][0] if "proj_key" in kwargs else None,
        "bag_key": kwargs["bag_key"][0] if "bag_key" in kwargs else None,
    }
    return result
