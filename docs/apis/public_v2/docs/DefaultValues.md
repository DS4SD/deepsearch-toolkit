# DefaultValues


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ccs_project** | [**CCSProject**](CCSProject.md) |  | 
**dataflow** | [**DataFlow**](DataFlow.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.default_values import DefaultValues

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultValues from a JSON string
default_values_instance = DefaultValues.from_json(json)
# print the JSON string representation of the object
print(DefaultValues.to_json())

# convert the object into a dict
default_values_dict = default_values_instance.to_dict()
# create an instance of DefaultValues from a dict
default_values_form_dict = default_values.from_dict(default_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


