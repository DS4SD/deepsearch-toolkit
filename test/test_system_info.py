from deepsearch.cps.apis import public as sw_client
from deepsearch.cps.client.api import CpsApi


def test_system_info(cps_api: CpsApi):
    sw_api = sw_client.SystemApi(cps_api.client.swagger_client)
    infos = sw_api.get_system_information()

    print(infos)
