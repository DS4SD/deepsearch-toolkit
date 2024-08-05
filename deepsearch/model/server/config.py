from __future__ import annotations

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    api_key: SecretStr
    model_config = SettingsConfigDict(env_prefix="DS_MODEL_")
