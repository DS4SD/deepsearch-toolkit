from copy import deepcopy

from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader

from deepsearch.model.server import settings

api_key = APIKeyHeader(name="Authorization")


def api_key_auth(header_api_key: str = Security(api_key)):
    request_api_key = header_api_key
    # If we run without auth
    if not settings.api_key:
        return

    header_api_key_arg = (
        request_api_key.replace("Bearer ", "")
        .replace("bearer ", "")
        .replace("Bearer: ", "")
        .replace("bearer: ", "")
        .strip()
    )
    # Otherwise check the apikey
    if header_api_key_arg != settings.api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API key"
        )
