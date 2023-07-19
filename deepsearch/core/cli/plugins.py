import logging
from typing import List

logger = logging.getLogger("root.core.plugins")

import pluggy
import typer

deepsearch_cli_hookspec = pluggy.HookspecMarker("deepsearch_cli")
deepsearch_cli_hookimpl = pluggy.HookimplMarker("deepsearch_cli")

logger.info("Plugins module initialized")


class DeepsearchCliPlugin:
    @deepsearch_cli_hookspec
    def deepsearch_cli_add_group(self) -> typer.Typer:
        """
        Add a deepsearch CLI command group.

        :return: A typer.Typer instance with a name set.
        """
        logger.error("Feature not implemented")
        raise NotImplementedError


def get_cli_plugin_manager():
    logger.info("getting cli plugin manager")
    manager = pluggy.PluginManager("deepsearch_cli")

    manager.add_hookspecs(DeepsearchCliPlugin)
    manager.load_setuptools_entrypoints("deepsearch", "cli")

    return manager


def get_cli_groups() -> List[typer.Typer]:
    manager = get_cli_plugin_manager()

    apps: List[typer.Typer] = manager.hook.deepsearch_cli_add_group()  # type: ignore

    for app in apps:
        if not app.info.name:
            logger.error(f"All registered apps must have names, but {app} doesn't")
            raise ValueError(f"All registered apps must have names, but {app} doesn't")

    return apps
