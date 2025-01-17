# PartialDirectConversionParametersOcr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **object** |  | [optional] 
**backend** | [**Backend**](Backend.md) |  | [optional] 
**backend_settings** | [**BackendSettings**](BackendSettings.md) |  | [optional] 
**merge_mode** | [**MergeMode**](MergeMode.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.partial_direct_conversion_parameters_ocr import PartialDirectConversionParametersOcr

# TODO update the JSON string below
json = "{}"
# create an instance of PartialDirectConversionParametersOcr from a JSON string
partial_direct_conversion_parameters_ocr_instance = PartialDirectConversionParametersOcr.from_json(json)
# print the JSON string representation of the object
print(PartialDirectConversionParametersOcr.to_json())

# convert the object into a dict
partial_direct_conversion_parameters_ocr_dict = partial_direct_conversion_parameters_ocr_instance.to_dict()
# create an instance of PartialDirectConversionParametersOcr from a dict
partial_direct_conversion_parameters_ocr_form_dict = partial_direct_conversion_parameters_ocr.from_dict(partial_direct_conversion_parameters_ocr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


