import requests
from IPython.display import IFrame, Markdown, display

from deepsearch.cps.apis.kg.query.configuration import Configuration
from deepsearch.cps.kg import workflow


def display_kg_topology(
    config: Configuration, width: int = 960, height: int = 600
) -> None:
    """
    Visualize the KG topology
    :param config: Knowledge Graph API Configuration
    :type config: Configuration
    :param width: IFrame width
    :type width: int
    :param height: IFrame height
    :type height: int
    """
    # Create iframe to view the topology
    auth_token = config.api_key["Authorization"]

    # url = f"{config.bag_url}/graphic/topology?auth_token={auth_token}"
    # display(IFrame(url, width=width, height=height))
    display(Markdown("No longer implemented."))


def display_workflow(
    wf: workflow.Workflow, config: Configuration, width: int = 800, height: int = 400
) -> None:
    """
    Visualize the workflow DAG
    :param config: Knowledge Graph API Configuration
    :type config: Configuration
    :param width: IFrame width
    :type width: int
    :param height: IFrame height
    :type height: int
    """

    display(Markdown("No longer implemented."))
    return

    workflow.validate(wf, config)

    operations = wf.get_operations()

    payload = {
        "name": "Search workflow",
        "description": "This is a temp workflow for searching",
        "template": operations,
        "variables": {},
    }

    # send temp workflow to api
    request = requests.post(
        f"{config.bag_api_base_url}/api/v1/temp/workflows",
        json=payload,
        headers=config.api_key,
        verify=config.verify_ssl,
    )

    result = request.json()

    # Create iframe to view workflow results
    wf_key = result["wf_key"]
    auth_token = config.api_key["Authorization"]

    url = f"{config.bag_url}/graphic/workflow/{wf_key}?auth_token={auth_token}"
    display(IFrame(url, width=width, height=height))
