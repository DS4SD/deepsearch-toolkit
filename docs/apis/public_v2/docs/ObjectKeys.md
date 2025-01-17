# ObjectKeys

List of s3 object keys to retrieve from bucket to be converted and uploaded to the data index.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from deepsearch.cps.apis.public_v2.models.object_keys import ObjectKeys

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectKeys from a JSON string
object_keys_instance = ObjectKeys.from_json(json)
# print the JSON string representation of the object
print(ObjectKeys.to_json())

# convert the object into a dict
object_keys_dict = object_keys_instance.to_dict()
# create an instance of ObjectKeys from a dict
object_keys_form_dict = object_keys.from_dict(object_keys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


