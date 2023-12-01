from typing import Optional

import typer
from rich.console import Console
from rich.table import Table
from typing_extensions import Annotated

from deepsearch.core.cli.profile_utils import (
    MSG_NO_PROFILE_SELECTED,
    MSG_NO_PROFILES_DEFINED,
)
from deepsearch.core.cli.utils import cli_handler
from deepsearch.core.client.settings import ProfileSettings
from deepsearch.core.client.settings_manager import SettingsManager

app = typer.Typer(no_args_is_help=True)

console = Console()
err_console = Console(stderr=True)


@app.command(
    name="config",
    help=f"Add or update a profile.",
)
@cli_handler()
def add_profile(
    host: str = typer.Option(prompt=True),
    username: str = typer.Option(prompt=True),
    api_key: str = typer.Option(prompt=True, hide_input=True),
    verify_ssl: bool = typer.Option(default=True),
    profile_name: str = typer.Option(
        default="",
        help="If not set, the active profile will be updated or, if no profile available, a new profile with a predetermined name will be created.",
    ),
    activate_profile: bool = typer.Option(default=True),
):
    settings_mgr = SettingsManager()
    prfl_name = (
        profile_name if profile_name else settings_mgr.get_profile_name_suggestion()
    )

    profile_settings = ProfileSettings(
        host=host,
        username=username,
        api_key=api_key,  # type: ignore[arg-type]
        verify_ssl=verify_ssl,
    )

    settings_mgr.save_settings(
        profile_settgs=profile_settings,
        profile_name=prfl_name,
        activate_profile=activate_profile,
    )


@app.command(
    name="list",
    help=f"List all profiles.",
)
@cli_handler()
def list_profiles() -> None:
    table = Table(
        "active",
        "profile",
    )
    settings_mgr = SettingsManager()
    profiles = settings_mgr.get_all_profile_settings()
    active_profile = settings_mgr.get_active_profile()

    if len(profiles) > 0:
        for k in profiles:
            mark = "*" if k == active_profile else " "
            table.add_row(
                mark,
                k,
            )
        console.print(table)

        if active_profile is None:
            console.print(MSG_NO_PROFILE_SELECTED)
    else:
        console.print(MSG_NO_PROFILES_DEFINED)


@app.command(
    name="show",
    help=f"Display a profile.",
)
@cli_handler()
def show_profile(
    profile_name: Annotated[
        Optional[str],
        typer.Argument(
            help="If not set, the active profile will be displayed.",
        ),
    ] = None
) -> None:
    table = Table(
        "profile",
        "config",
    )
    settings_mgr = SettingsManager()
    prfl_name = profile_name or settings_mgr.get_active_profile()
    profile = settings_mgr.get_profile_settings(profile_name=prfl_name)

    table.add_row(
        prfl_name,
        repr(profile.dict()),
    )
    console.print(table)


@app.command(
    name="use",
    help=f"Activate a profile.",
    no_args_is_help=True,
)
@cli_handler()
def set_default_profile(
    profile_name: str,
) -> None:
    settings_mgr = SettingsManager()
    settings_mgr.activate_profile(profile_name=profile_name)


@app.command(
    name="remove",
    help=f"Remove a profile.",
    no_args_is_help=True,
)
@cli_handler()
def remove_profile(
    profile_name: str,
) -> None:
    settings_mgr = SettingsManager()
    settings_mgr.remove_profile(profile_name=profile_name)
