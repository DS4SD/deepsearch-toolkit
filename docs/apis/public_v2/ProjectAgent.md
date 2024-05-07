# ProjectAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_info** | **object** |  | 
**agent_name** | **str** |  | 
**version** | **str** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.project_agent import ProjectAgent

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectAgent from a JSON string
project_agent_instance = ProjectAgent.from_json(json)
# print the JSON string representation of the object
print(ProjectAgent.to_json())

# convert the object into a dict
project_agent_dict = project_agent_instance.to_dict()
# create an instance of ProjectAgent from a dict
project_agent_form_dict = project_agent.from_dict(project_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


