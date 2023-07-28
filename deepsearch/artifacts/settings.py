import os
from enum import Enum

from deepsearch.core.client.settings import CFG_ROOT_PATH, DSSettings, SubPrefix

FALLBACK_INDEX_PATH = os.getcwd()
FALLBACK_CACHE_PATH = str(CFG_ROOT_PATH / "artifact_cache")
FALLBACK_META_FILENAME = "meta.info"
FALLBACK_META_URL_FIELD = "static_url"


class ArtifactSettings(DSSettings):
    class Config:
        env_prefix = DSSettings.build_prefix(sub_prefix=SubPrefix.ARTIFACT)

    class HitStrategy(str, Enum):
        RAISE = "raise"
        PASS = "pass"
        OVERWRITE = "overwrite"

    index_path: str = FALLBACK_INDEX_PATH
    cache_path: str = FALLBACK_CACHE_PATH
    meta_filename: str = FALLBACK_META_FILENAME
    meta_url_field: str = FALLBACK_META_URL_FIELD
    hit_strategy: HitStrategy = HitStrategy.OVERWRITE
    unpack_archives: bool = True
    progress_bar: bool = False
