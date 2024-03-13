# TemporaryUrlFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**fields** | **object** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.temporary_url_fields import TemporaryUrlFields

# TODO update the JSON string below
json = "{}"
# create an instance of TemporaryUrlFields from a JSON string
temporary_url_fields_instance = TemporaryUrlFields.from_json(json)
# print the JSON string representation of the object
print(TemporaryUrlFields.to_json())

# convert the object into a dict
temporary_url_fields_dict = temporary_url_fields_instance.to_dict()
# create an instance of TemporaryUrlFields from a dict
temporary_url_fields_form_dict = temporary_url_fields.from_dict(temporary_url_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


