# ConversionSettings

Specify the conversion settings to use.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ocr** | [**PartialDirectConversionParametersOcr**](PartialDirectConversionParametersOcr.md) |  | [optional] 
**table_structure** | [**TableStructureOptions**](TableStructureOptions.md) |  | [optional] 
**generate_page_images** | **object** |  | [optional] 
**type** | **object** |  | [optional] 
**assemble** | [**PartialDirectConversionParametersAssemble**](PartialDirectConversionParametersAssemble.md) |  | [optional] 
**metadata** | [**PartialDirectConversionParametersMetadata**](PartialDirectConversionParametersMetadata.md) |  | [optional] 
**page_labels** | [**PageLabels**](PageLabels.md) |  | [optional] 
**model_pipeline** | [**PartialDirectConversionParametersModelPipeline**](PartialDirectConversionParametersModelPipeline.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.conversion_settings import ConversionSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ConversionSettings from a JSON string
conversion_settings_instance = ConversionSettings.from_json(json)
# print the JSON string representation of the object
print(ConversionSettings.to_json())

# convert the object into a dict
conversion_settings_dict = conversion_settings_instance.to_dict()
# create an instance of ConversionSettings from a dict
conversion_settings_form_dict = conversion_settings.from_dict(conversion_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


