from deepsearch.model.server import settings
from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader

api_key = APIKeyHeader(name="Authorization")


def api_key_auth(header_api_key: str = Security(api_key)):
    # If we run without auth
    if not settings.api_key:
        return

    header_api_key = (
        header_api_key.replace("Bearer ", "")
        .replace("bearer ", "")
        .replace("Bearer: ", "")
        .replace("bearer: ", "")
        .strip()
    )
    # Otherwise check the apikey
    if header_api_key != settings.api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Forbidden"
        )