# PartialDirectConversionParameters

Specify conversion settings (OCR, Assemble, ML Models) directly.  Fields left null are set to platform defaults.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'direct']
**ocr** | [**PartialDirectConversionParametersOcr**](PartialDirectConversionParametersOcr.md) |  | [optional] 
**assemble** | [**PartialDirectConversionParametersAssemble**](PartialDirectConversionParametersAssemble.md) |  | [optional] 
**metadata** | [**PartialDirectConversionParametersMetadata**](PartialDirectConversionParametersMetadata.md) |  | [optional] 
**page_labels** | [**PageLabels**](PageLabels.md) |  | [optional] 
**model_pipeline** | [**PartialDirectConversionParametersModelPipeline**](PartialDirectConversionParametersModelPipeline.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.partial_direct_conversion_parameters import PartialDirectConversionParameters

# TODO update the JSON string below
json = "{}"
# create an instance of PartialDirectConversionParameters from a JSON string
partial_direct_conversion_parameters_instance = PartialDirectConversionParameters.from_json(json)
# print the JSON string representation of the object
print(PartialDirectConversionParameters.to_json())

# convert the object into a dict
partial_direct_conversion_parameters_dict = partial_direct_conversion_parameters_instance.to_dict()
# create an instance of PartialDirectConversionParameters from a dict
partial_direct_conversion_parameters_form_dict = partial_direct_conversion_parameters.from_dict(partial_direct_conversion_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


