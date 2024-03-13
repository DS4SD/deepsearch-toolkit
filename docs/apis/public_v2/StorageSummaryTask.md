# StorageSummaryTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dc_key** | **str** |  | [optional] 
**kg_key** | **str** |  | [optional] 
**kind** | **str** |  | 
**proj_key** | **str** |  | 
**task_id** | **str** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.storage_summary_task import StorageSummaryTask

# TODO update the JSON string below
json = "{}"
# create an instance of StorageSummaryTask from a JSON string
storage_summary_task_instance = StorageSummaryTask.from_json(json)
# print the JSON string representation of the object
print(StorageSummaryTask.to_json())

# convert the object into a dict
storage_summary_task_dict = storage_summary_task_instance.to_dict()
# create an instance of StorageSummaryTask from a dict
storage_summary_task_form_dict = storage_summary_task.from_dict(storage_summary_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


