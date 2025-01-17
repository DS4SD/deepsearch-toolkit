# ProjectDataIndexConversionSettingsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ocr** | [**OCROptions**](OCROptions.md) |  | [optional] 
**table_structure** | [**TableStructureOptions**](TableStructureOptions.md) |  | [optional] 
**generate_page_images** | **bool** |  | [optional] [default to True]

## Example

```python
from deepsearch.cps.apis.public_v2.models.project_data_index_conversion_settings_input import ProjectDataIndexConversionSettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDataIndexConversionSettingsInput from a JSON string
project_data_index_conversion_settings_input_instance = ProjectDataIndexConversionSettingsInput.from_json(json)
# print the JSON string representation of the object
print(ProjectDataIndexConversionSettingsInput.to_json())

# convert the object into a dict
project_data_index_conversion_settings_input_dict = project_data_index_conversion_settings_input_instance.to_dict()
# create an instance of ProjectDataIndexConversionSettingsInput from a dict
project_data_index_conversion_settings_input_form_dict = project_data_index_conversion_settings_input.from_dict(project_data_index_conversion_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


