import logging
from pathlib import Path
from typing import List

from deepsearch.core.client.settings_manager import settings_mgr


def setup_logger():
    # Setting up root logger
    log_target_file, log_to_console = settings_mgr.get_logging_conf()

    p = Path(log_target_file)
    if not p.parent.is_dir():
        p.parent.mkdir(parents=True)

    p = p.joinpath("deepsearch.log")

    handlers: List[logging.Handler] = [
        logging.FileHandler(p),
    ]
    if log_to_console:
        handlers.append(logging.StreamHandler())
    formatter = logging.Formatter(
        "%(asctime)s %(name)s — %(levelname)s — %(module)s:%(funcName)s:%(lineno)d — %(message)s"
    )
    logger = logging.getLogger("root")
    [h.setFormatter(formatter) for h in handlers]  # type: ignore
    [logger.addHandler(h) for h in handlers]  # type: ignore
    [e.setLevel(logging.DEBUG) for e in (logger, *handlers)]  # type: ignore

    return logger


logger = setup_logger()

from deepsearch.artifacts.cli.main import app as artifacts_app
from deepsearch.core.cli.main import app
from deepsearch.core.cli.plugins import get_cli_groups
from deepsearch.cps.cli.main import app as cps_app
from deepsearch.documents.cli.main import app as documents_app
from deepsearch.query.cli.main import app as query_app

app.add_typer(cps_app, name="cps", help="Interact with DeepSearch CPS component")
app.add_typer(query_app, name="query", help="Interact with DeepSearch Query component")
app.add_typer(
    documents_app,
    name="documents",
    help="Interact with DeepSearch Document Conversion component",
)
app.add_typer(artifacts_app, name="artifacts", help="Manage artifacts")

for group in get_cli_groups():
    app.add_typer(group)
logger.info("Root module finished initialization")

if __name__ == "__main__":
    app()
