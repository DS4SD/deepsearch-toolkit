# Log

Log entry to describe an ETL task on a document.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task** | [**Task**](Task.md) |  | [optional] 
**agent** | **object** | The Docling agent that performed the task, e.g., CCS or CXS. | 
**type** | **object** | A task category. | 
**comment** | [**Comment**](Comment.md) |  | [optional] 
**var_date** | **object** | A string representation of the task execution datetime in ISO 8601 format. | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.log import Log

# TODO update the JSON string below
json = "{}"
# create an instance of Log from a JSON string
log_instance = Log.from_json(json)
# print the JSON string representation of the object
print(Log.to_json())

# convert the object into a dict
log_dict = log_instance.to_dict()
# create an instance of Log from a dict
log_form_dict = log.from_dict(log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


