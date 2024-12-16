# ConvertDocumentsRequestBodyTargetSettings

Specify the target settings to use.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_raw_pages** | [**AddRawPages**](AddRawPages.md) |  | [optional] 
**add_annotations** | [**AddAnnotations**](AddAnnotations.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.convert_documents_request_body_target_settings import ConvertDocumentsRequestBodyTargetSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertDocumentsRequestBodyTargetSettings from a JSON string
convert_documents_request_body_target_settings_instance = ConvertDocumentsRequestBodyTargetSettings.from_json(json)
# print the JSON string representation of the object
print(ConvertDocumentsRequestBodyTargetSettings.to_json())

# convert the object into a dict
convert_documents_request_body_target_settings_dict = convert_documents_request_body_target_settings_instance.to_dict()
# create an instance of ConvertDocumentsRequestBodyTargetSettings from a dict
convert_documents_request_body_target_settings_form_dict = convert_documents_request_body_target_settings.from_dict(convert_documents_request_body_target_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


