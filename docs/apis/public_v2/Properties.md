# Properties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**Dict[str, Properties]**](Properties.md) |  | 
**type** | **object** |  | 
**enabled** | **object** |  | [optional] 
**ignore_above** | **object** |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.properties import Properties

# TODO update the JSON string below
json = "{}"
# create an instance of Properties from a JSON string
properties_instance = Properties.from_json(json)
# print the JSON string representation of the object
print(Properties.to_json())

# convert the object into a dict
properties_dict = properties_instance.to_dict()
# create an instance of Properties from a dict
properties_form_dict = properties.from_dict(properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


