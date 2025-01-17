# TargetConversionParameters

Specify target settings (add_raw_pages, add_annotations).  Fields left null are set to platform defaults.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_raw_pages** | [**AddRawPages**](AddRawPages.md) |  | [optional] 
**add_annotations** | [**AddAnnotations**](AddAnnotations.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.target_conversion_parameters import TargetConversionParameters

# TODO update the JSON string below
json = "{}"
# create an instance of TargetConversionParameters from a JSON string
target_conversion_parameters_instance = TargetConversionParameters.from_json(json)
# print the JSON string representation of the object
print(TargetConversionParameters.to_json())

# convert the object into a dict
target_conversion_parameters_dict = target_conversion_parameters_instance.to_dict()
# create an instance of TargetConversionParameters from a dict
target_conversion_parameters_form_dict = target_conversion_parameters.from_dict(target_conversion_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


