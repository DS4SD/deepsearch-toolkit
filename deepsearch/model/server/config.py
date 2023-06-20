from pydantic import BaseSettings


class Settings(BaseSettings):
    # API
    api_key: str
