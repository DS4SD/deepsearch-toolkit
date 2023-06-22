from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    api_key: SecretStr

    class Config:
        env_prefix = "DS_MODEL_"
