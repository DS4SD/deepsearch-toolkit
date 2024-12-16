# TaskContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**proj_key** | **str** |  | 
**user_key** | **str** |  | 
**task_type** | **str** |  | 
**task_id** | **str** |  | 
**task_status** | **str** |  | 
**execution_mode** | **str** |  | 
**progress** | **float** |  | 
**meta** | **object** |  | 
**created_at** | **datetime** |  | 
**started_at** | [**StartedAt**](StartedAt.md) |  | [optional] 
**completed_at** | [**CompletedAt**](CompletedAt.md) |  | [optional] 
**start_count** | [**StartCount**](StartCount.md) |  | [optional] 
**error_reason** | [**ErrorReason**](ErrorReason.md) |  | [optional] 
**related_tasks** | [**RelatedTasks**](RelatedTasks.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.task_context import TaskContext

# TODO update the JSON string below
json = "{}"
# create an instance of TaskContext from a JSON string
task_context_instance = TaskContext.from_json(json)
# print the JSON string representation of the object
print(TaskContext.to_json())

# convert the object into a dict
task_context_dict = task_context_instance.to_dict()
# create an instance of TaskContext from a dict
task_context_form_dict = task_context.from_dict(task_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


