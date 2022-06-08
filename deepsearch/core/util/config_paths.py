import logging
import os
from pathlib import Path

import appdirs

_log = logging.getLogger(__name__)


CONFIG_FILE_NAME: str = "deepsearch_toolkit.json"
ENV_VAR_NAME = "DEEPSEARCH_TOOLKIT_CONFIG_FILE"


def config_dir() -> Path:
    """Get the path to the configuration directory"""

    p = Path(appdirs.user_config_dir("DeepSearch", "IBM"))

    if not p.is_dir():
        p.mkdir(parents=True)

    return p


def default_config_file_path() -> Path:
    """Get the path to the configuration file"""

    return config_dir() / CONFIG_FILE_NAME


def config_file_path() -> Path:
    """
    Get the actual path to the configuration file.

    This takes into account the following paths (from most to least relevant):

    - The file pointed to by `$DEEPSEARCH_TOOLKIT_CONFIG_FILE`
    - The file `$PWD/deepsearch_toolkit.json`, if it exists
    - The result of `default_config_file_path()`, which is os-dependent
    """

    if ENV_VAR_NAME in os.environ:
        _log.debug("Forwarding environment variable %r", ENV_VAR_NAME)
        return Path(os.environ[ENV_VAR_NAME])

    in_current_dir = Path(CONFIG_FILE_NAME)

    if in_current_dir.is_file():
        _log.debug(
            "Found config file %r in current working directory", CONFIG_FILE_NAME
        )
        return in_current_dir

    _log.debug("Returning default config file path")

    return default_config_file_path()
