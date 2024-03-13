# CpsTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | 
**task_type** | **str** |  | 
**task_status** | **str** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.cps_task import CpsTask

# TODO update the JSON string below
json = "{}"
# create an instance of CpsTask from a JSON string
cps_task_instance = CpsTask.from_json(json)
# print the JSON string representation of the object
print(CpsTask.to_json())

# convert the object into a dict
cps_task_dict = cps_task_instance.to_dict()
# create an instance of CpsTask from a dict
cps_task_form_dict = cps_task.from_dict(cps_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


