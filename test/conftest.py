import pytest

from deepsearch.cps.client.api import CpsApi


@pytest.fixture
def cps_api() -> CpsApi:
    return CpsApi.default_from_env()
