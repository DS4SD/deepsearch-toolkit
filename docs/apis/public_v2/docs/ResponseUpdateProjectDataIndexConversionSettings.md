# ResponseUpdateProjectDataIndexConversionSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ocr** | [**OCROptions**](OCROptions.md) |  | [optional] 
**table_structure** | [**TableStructureOptions**](TableStructureOptions.md) |  | [optional] 
**generate_page_images** | **object** |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.response_update_project_data_index_conversion_settings import ResponseUpdateProjectDataIndexConversionSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseUpdateProjectDataIndexConversionSettings from a JSON string
response_update_project_data_index_conversion_settings_instance = ResponseUpdateProjectDataIndexConversionSettings.from_json(json)
# print the JSON string representation of the object
print(ResponseUpdateProjectDataIndexConversionSettings.to_json())

# convert the object into a dict
response_update_project_data_index_conversion_settings_dict = response_update_project_data_index_conversion_settings_instance.to_dict()
# create an instance of ResponseUpdateProjectDataIndexConversionSettings from a dict
response_update_project_data_index_conversion_settings_form_dict = response_update_project_data_index_conversion_settings.from_dict(response_update_project_data_index_conversion_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


