from pydantic import SecretStr

from deepsearch.core.client.settings import DSSettings, SubPrefix


class ModelAppSettings(DSSettings):
    class Config:
        env_prefix = DSSettings.build_prefix(sub_prefix=SubPrefix.MODEL_APP)

    api_key: SecretStr
    host: str = "127.0.0.1"
    port: int = 8000
