from typing import Optional

import typer
from typing_extensions import Annotated

from deepsearch.artifacts.artifact_manager import ArtifactManager
from deepsearch.artifacts.settings import (
    FALLBACK_CACHE_PATH,
    FALLBACK_INDEX_PATH,
    ArtifactSettings,
)
from deepsearch.core.cli.utils import cli_handler

index_app = typer.Typer(no_args_is_help=True, add_completion=False)
cache_app = typer.Typer(no_args_is_help=True, add_completion=False)

app = typer.Typer(no_args_is_help=True, add_completion=False)
app.add_typer(index_app, name="index", help="Manage artifact indices.")
app.add_typer(cache_app, name="cache", help="Manage artifact caches.")


def _get_unset_case_help(fallback=None) -> str:
    fallback_msg = "" if fallback is None else f' (fallback: "{fallback}")'
    return f"If not set, resolved from environment{fallback_msg}."


INDEX_OPTION = typer.Option(
    None,
    "--index",
    "-i",
    help=f"Artifact index path. {_get_unset_case_help(FALLBACK_INDEX_PATH)}",
)

CACHE_OPTION = typer.Option(
    None,
    "--cache",
    "-c",
    help=f"Artifact cache path. {_get_unset_case_help(FALLBACK_CACHE_PATH)}",
)

HIT_STRATEGY_OPTION = typer.Option(
    ArtifactSettings.HitStrategy.OVERWRITE,
    "--hit-strategy",
    "-s",
    help="Controls handling of case artifact being already in cache.",
)

UNPACK_OPTION = typer.Option(
    True,
    help="Controls archive unpacking.",
)

PROGRESS_BAR_OPTION = typer.Option(
    True,
    help="Controls progress bar display.",
)


def _create_settings(
    index_path: Optional[str] = None,
    cache_path: Optional[str] = None,
    hit_strategy: Optional[ArtifactSettings.HitStrategy] = None,
    unpack_archives: Optional[bool] = None,
    progress_bar: Optional[bool] = None,
) -> ArtifactSettings:
    settings = ArtifactSettings()
    if index_path is not None:
        settings.index_path = index_path
    if cache_path is not None:
        settings.cache_path = cache_path
    if hit_strategy is not None:
        settings.hit_strategy = hit_strategy
    if unpack_archives is not None:
        settings.unpack_archives = unpack_archives
    if progress_bar is not None:
        settings.progress_bar = progress_bar
    return settings


@index_app.command(name="list", help="List artifacts in index.")
@cli_handler()
def list_index(
    index_path: Annotated[
        Optional[str],
        typer.Argument(help=_get_unset_case_help(FALLBACK_INDEX_PATH)),
    ] = None
):
    artf_mgr = ArtifactManager(settings=_create_settings(index_path=index_path))
    artifacts = artf_mgr.get_artifacts_in_index()
    for artf in artifacts:
        typer.echo(artf)


@cache_app.command(name="list", help="List artifacts in cache.")
@cli_handler()
def list_cache(
    cache_path: Annotated[
        Optional[str],
        typer.Argument(help=_get_unset_case_help(FALLBACK_CACHE_PATH)),
    ] = None
):
    artf_mgr = ArtifactManager(settings=_create_settings(cache_path=cache_path))
    artifacts = artf_mgr.get_artifacts_in_cache()
    for artf in artifacts:
        typer.echo(artf)


@cache_app.command(name="locate", help="Show default cache path.")
@cli_handler()
def locate_cache():
    artf_mgr = ArtifactManager()
    path_str = str(artf_mgr.get_cache_path().resolve())
    typer.echo(path_str)


@app.command(
    name="locate", help="Show path of a cached artifact.", no_args_is_help=True
)
@cli_handler()
def locate_cached_artifact(
    artifact_name: str,
    cache: str = CACHE_OPTION,
):

    artf_mgr = ArtifactManager(settings=_create_settings(cache_path=cache))
    artf_path = artf_mgr.get_artifact_path_in_cache(artifact_name=artifact_name)
    artifact_path_str = str(artf_path.resolve())
    typer.echo(artifact_path_str)


@app.command(
    name="download", help="Download an artifact to cache.", no_args_is_help=True
)
@cli_handler()
def download(
    artifact_name: str,
    index: Optional[str] = INDEX_OPTION,
    cache: Optional[str] = CACHE_OPTION,
    hit_strategy: ArtifactSettings.HitStrategy = HIT_STRATEGY_OPTION,
    unpack: bool = UNPACK_OPTION,
    progress_bar: bool = PROGRESS_BAR_OPTION,
):
    artf_mgr = ArtifactManager(
        settings=_create_settings(
            index_path=index,
            cache_path=cache,
            hit_strategy=hit_strategy,
            unpack_archives=unpack,
            progress_bar=progress_bar,
        ),
    )
    artf_mgr.download_artifact_to_cache(artifact_name=artifact_name)


@index_app.command(name="download", help="Download all index artifacts to cache.")
@cli_handler()
def download_all(
    index: Annotated[
        Optional[str],
        typer.Argument(help=_get_unset_case_help(FALLBACK_INDEX_PATH)),
    ] = None,
    cache: Optional[str] = CACHE_OPTION,
    hit_strategy: ArtifactSettings.HitStrategy = HIT_STRATEGY_OPTION,
    unpack: bool = UNPACK_OPTION,
    progress_bar: bool = PROGRESS_BAR_OPTION,
):
    artf_mgr = ArtifactManager(
        settings=_create_settings(
            index_path=index,
            cache_path=cache,
            hit_strategy=hit_strategy,
            unpack_archives=unpack,
            progress_bar=progress_bar,
        ),
    )
    for artf_name in artf_mgr.get_artifacts_in_index():
        artf_mgr.download_artifact_to_cache(artifact_name=artf_name)
