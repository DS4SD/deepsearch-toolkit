from typing import Union

from platformdirs import user_log_dir
from pydantic import BaseModel


class DeepSearchBearerTokenAuth(BaseModel):
    bearer_token: str


class DeepSearchKeyAuth(BaseModel):
    username: str
    api_key: str


DeepSearchAuth = Union[DeepSearchBearerTokenAuth, DeepSearchKeyAuth]


class DeepSearchLogConfig(BaseModel):
    target_file: str = user_log_dir("DeepSearch", "IBM")
    write_to_console: bool = False


class DeepSearchConfig(BaseModel):
    host: str
    auth: DeepSearchAuth
    verify_ssl: bool = True
    log_configuration: DeepSearchLogConfig
