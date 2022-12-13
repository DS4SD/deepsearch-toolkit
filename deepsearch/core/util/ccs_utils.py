from deepsearch import CpsApi
from deepsearch.cps.apis import public as sw_client


def get_ccs_project_key(api: CpsApi, cps_proj_key: str):
    """
    Given a cps project key, returns ccs project key and collection name.
    """
    sw_api = sw_client.ProjectApi(api.client.swagger_client)
    request_ccs_project_key = sw_api.get_project_default_values(proj_key=cps_proj_key)
    ccs_proj_key = request_ccs_project_key.ccs_project.proj_key
    collection_name = request_ccs_project_key.ccs_project.collection_name
    return (ccs_proj_key, collection_name)
