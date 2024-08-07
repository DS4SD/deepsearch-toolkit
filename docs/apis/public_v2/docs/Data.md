# Data


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** |  | 
**description** | **object** |  | [optional] 
**view_of** | [**ViewOf**](ViewOf.md) |  | 
**schema_key** | **object** |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.data import Data

# TODO update the JSON string below
json = "{}"
# create an instance of Data from a JSON string
data_instance = Data.from_json(json)
# print the JSON string representation of the object
print(Data.to_json())

# convert the object into a dict
data_dict = data_instance.to_dict()
# create an instance of Data from a dict
data_form_dict = data.from_dict(data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


