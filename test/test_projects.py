from deepsearch.cps.client.api import CpsApi


def test_project_listing(cps_api: CpsApi):
    projects = cps_api.projects.list()

    assert len(projects) > 0
