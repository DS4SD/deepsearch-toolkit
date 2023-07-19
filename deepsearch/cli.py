import logging
from pathlib import Path
from typing import List

from deepsearch import DeepSearchConfig
from deepsearch.artifacts.cli.main import app as artifacts_app
from deepsearch.core.cli.main import app
from deepsearch.core.cli.plugins import get_cli_groups
from deepsearch.core.util.config_paths import config_file_path
from deepsearch.cps.cli.main import app as cps_app
from deepsearch.documents.cli.main import app as documents_app
from deepsearch.query.cli.main import app as query_app

# TODO review if unwanted information is being logged


def setup_logger():
    # Setting up root logger
    config_file = config_file_path()

    if not config_file.exists():
        raise RuntimeError(
            f"Config file {config_file} does not exist. Please configure your default authentication with `$ deepsearch login`"
        )
    config = DeepSearchConfig.parse_file(config_file)

    p = Path(config.log_configuration.target_file)
    if not p.parent.is_dir():
        p.parent.mkdir(parents=True)

    handlers: List[logging.Handler] = [
        logging.FileHandler(p),
    ]
    if config.log_configuration.write_to_console:
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

app.add_typer(cps_app, name="cps", help="Interact with DeepSearch CPS component")
logger.info("Cps module initialized")
app.add_typer(query_app, name="query", help="Interact with DeepSearch Query component")
logger.info("Query module initialized")
app.add_typer(
    documents_app,
    name="documents",
    help="Interact with DeepSearch Document Conversion component",
)
logger.info("Documents module initialized")
app.add_typer(artifacts_app, name="artifacts", help="Manage artifacts")
logger.info("Artifacts module initialized")

for group in get_cli_groups():
    app.add_typer(group)
logger.info("Root module finished initialization")

if __name__ == "__main__":
    app()
