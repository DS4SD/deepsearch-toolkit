from pydantic.v1 import BaseSettings, SecretStr


class Settings(BaseSettings):
    api_key: SecretStr

    class Config:
        env_prefix = "DS_MODEL_"
