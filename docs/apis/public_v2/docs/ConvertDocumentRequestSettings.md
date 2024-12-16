# ConvertDocumentRequestSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ocr** | [**OCROptions**](OCROptions.md) |  | [optional] 
**table_structure** | [**TableStructureOptions**](TableStructureOptions.md) |  | [optional] 
**generate_page_images** | **object** |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.convert_document_request_settings import ConvertDocumentRequestSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertDocumentRequestSettings from a JSON string
convert_document_request_settings_instance = ConvertDocumentRequestSettings.from_json(json)
# print the JSON string representation of the object
print(ConvertDocumentRequestSettings.to_json())

# convert the object into a dict
convert_document_request_settings_dict = convert_document_request_settings_instance.to_dict()
# create an instance of ConvertDocumentRequestSettings from a dict
convert_document_request_settings_form_dict = convert_document_request_settings.from_dict(convert_document_request_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


