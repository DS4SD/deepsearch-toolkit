from typing import Union

from pydantic import BaseModel


class DeepSearchBearerTokenAuth(BaseModel):
    bearer_token: str


class DeepSearchKeyAuth(BaseModel):
    username: str
    api_key: str


DeepSearchAuth = Union[DeepSearchBearerTokenAuth, DeepSearchKeyAuth]


class DeepSearchConfig(BaseModel):
    host: str
    auth: DeepSearchAuth
    verify_ssl: bool = True
