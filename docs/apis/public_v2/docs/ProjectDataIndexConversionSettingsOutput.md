# ProjectDataIndexConversionSettingsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ocr** | [**OCROptions**](OCROptions.md) |  | [optional] 
**table_structure** | [**TableStructureOptions**](TableStructureOptions.md) |  | [optional] 
**generate_page_images** | **bool** |  | [optional] [default to True]

## Example

```python
from deepsearch.cps.apis.public_v2.models.project_data_index_conversion_settings_output import ProjectDataIndexConversionSettingsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDataIndexConversionSettingsOutput from a JSON string
project_data_index_conversion_settings_output_instance = ProjectDataIndexConversionSettingsOutput.from_json(json)
# print the JSON string representation of the object
print(ProjectDataIndexConversionSettingsOutput.to_json())

# convert the object into a dict
project_data_index_conversion_settings_output_dict = project_data_index_conversion_settings_output_instance.to_dict()
# create an instance of ProjectDataIndexConversionSettingsOutput from a dict
project_data_index_conversion_settings_output_form_dict = project_data_index_conversion_settings_output.from_dict(project_data_index_conversion_settings_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


