# CcsTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | 
**ccs_project_key** | **str** |  | 
**ccs_collection_name** | **str** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.ccs_task import CcsTask

# TODO update the JSON string below
json = "{}"
# create an instance of CcsTask from a JSON string
ccs_task_instance = CcsTask.from_json(json)
# print the JSON string representation of the object
print(CcsTask.to_json())

# convert the object into a dict
ccs_task_dict = ccs_task_instance.to_dict()
# create an instance of CcsTask from a dict
ccs_task_form_dict = ccs_task.from_dict(ccs_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


