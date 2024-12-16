# Wait

Optionally block this method call for a few seconds to wait for the result instead of polling through multiple calls.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from deepsearch.cps.apis.public_v2.models.wait import Wait

# TODO update the JSON string below
json = "{}"
# create an instance of Wait from a JSON string
wait_instance = Wait.from_json(json)
# print the JSON string representation of the object
print(Wait.to_json())

# convert the object into a dict
wait_dict = wait_instance.to_dict()
# create an instance of Wait from a dict
wait_form_dict = wait.from_dict(wait_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


