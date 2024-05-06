# ProjectAgents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agents** | [**List[ProjectAgent]**](ProjectAgent.md) |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.project_agents import ProjectAgents

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectAgents from a JSON string
project_agents_instance = ProjectAgents.from_json(json)
# print the JSON string representation of the object
print(ProjectAgents.to_json())

# convert the object into a dict
project_agents_dict = project_agents_instance.to_dict()
# create an instance of ProjectAgents from a dict
project_agents_form_dict = project_agents.from_dict(project_agents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


