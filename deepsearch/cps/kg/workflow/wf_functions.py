import requests

import deepsearch.cps.apis.kg.query
from deepsearch.cps.apis.kg.query.configuration import Configuration

from . import workflow


def validate(wf: workflow.Workflow, config: Configuration):
    """
    Validate the workflow DAG
    :param workflow: Workflow object
    :type workflow: Workflow
    :param config: Knowledge Graph API Configuration
    :type config: Configuration
    """
    operations = wf.get_operations()

    try:
        result = requests.post(
            f"{config.host}/query/validateWorkflow",
            json=operations,
            headers=config.api_key,
            verify=config.verify_ssl,
        )

        result.raise_for_status()

        return True
    except:
        try:
            data = result.json()
            if data.get("message"):
                raise RuntimeError(data["message"])
            else:
                raise RuntimeError("Error in validation request")

        except ValueError as e:
            raise RuntimeError("Error in validation request")


def run(wf: workflow.Workflow, config: Configuration):
    """
    Run the workflow against the given KG
    :param workflow: Workflow object
    :type workflow: Workflow
    :param config: Knowledge Graph API Configuration
    :type config: Configuration
    :returns workflow results
    """
    operations = wf.get_operations()

    with deepsearch.cps.apis.kg.query.ApiClient(config) as api_client:
        api_instance = deepsearch.cps.apis.kg.query.QueryApi(api_client)
        results = api_instance.query_run_workflow(operations)
        return results
