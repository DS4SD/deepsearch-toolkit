import typer

from deepsearch.artifacts.artifact_manager import (
    DFLT_ARTFCT_CACHE_DIR,
    DFLT_ARTFCT_INDEX_DIR,
    ArtifactManager,
)
from deepsearch.core.cli.utils import cli_handler

app = typer.Typer(no_args_is_help=True, add_completion=False)

INDEX_OPTION = typer.Option(
    None,
    "--index",
    "-i",
    help="Artifact index path (default set via env var DEEPSEARCH_ARTIFACT_INDEX, else current working dir).",
)

CACHE_OPTION = typer.Option(
    None,
    "--cache",
    "-c",
    help="Artifact cache path (default set via env var DEEPSEARCH_ARTIFACT_CACHE, else platform-specific).",
)

HIT_STRATEGY_OPTION = typer.Option(
    ArtifactManager.HitStrategy.OVERWRITE,
    "--hit-strategy",
    "-s",
    help="How to handle case of artifact being already in cache.",
)


@app.command(help="List artifacts in index")
@cli_handler()
def list_index(
    index: str = INDEX_OPTION,
):
    artf_mgr = ArtifactManager(index=index)
    artifacts = artf_mgr.get_artifacts_in_index()
    for artf in artifacts:
        typer.echo(artf)


@app.command(help="List artifacts in cache")
@cli_handler()
def list_cache(
    cache: str = CACHE_OPTION,
):
    artf_mgr = ArtifactManager(cache=cache)
    artifacts = artf_mgr.get_artifacts_in_cache()
    for artf in artifacts:
        typer.echo(artf)


@app.command(help="Show cache path")
@cli_handler()
def locate_default_cache():
    artf_mgr = ArtifactManager()
    path_str = str(artf_mgr.get_cache_path().resolve())
    typer.echo(path_str)


@app.command(help="Show path of a cached artifact")
@cli_handler()
def locate_cached_artifact(
    artifact_name: str,
    cache: str = CACHE_OPTION,
):
    artf_mgr = ArtifactManager(cache=cache)
    artf_path = artf_mgr.get_artifact_path_in_cache(artifact_name=artifact_name)
    artifact_path_str = str(artf_path.resolve())
    typer.echo(artifact_path_str)


@app.command(help="Download an artifact to cache")
@cli_handler()
def download(
    artifact_name: str,
    index: str = INDEX_OPTION,
    cache: str = CACHE_OPTION,
    hit_strategy: ArtifactManager.HitStrategy = HIT_STRATEGY_OPTION,
    unpack: bool = typer.Option(True),
    progress_bar: bool = typer.Option(True),
):
    artf_mgr = ArtifactManager(index=index, cache=cache)
    artf_mgr.download_artifact_to_cache(
        artifact_name=artifact_name,
        unpack_archives=unpack,
        hit_strategy=hit_strategy,
        with_progress_bar=progress_bar,
    )


@app.command(help="Download all artifacts to cache")
@cli_handler()
def download_all(
    index: str = INDEX_OPTION,
    cache: str = CACHE_OPTION,
    hit_strategy: ArtifactManager.HitStrategy = HIT_STRATEGY_OPTION,
    unpack: bool = typer.Option(True),
    progress_bar: bool = typer.Option(True),
):
    artf_mgr = ArtifactManager(index=index, cache=cache)
    for artf_name in artf_mgr.get_artifacts_in_index():
        artf_mgr.download_artifact_to_cache(
            artifact_name=artf_name,
            unpack_archives=unpack,
            hit_strategy=hit_strategy,
            with_progress_bar=progress_bar,
        )


if __name__ == "__main__":
    app()
