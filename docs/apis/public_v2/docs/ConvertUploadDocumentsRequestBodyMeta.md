# ConvertUploadDocumentsRequestBodyMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | [**Filename**](Filename.md) |  | [optional] 
**description** | [**DocumentMetaDescription**](DocumentMetaDescription.md) |  | [optional] 
**identifiers** | [**Identifiers**](Identifiers.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.convert_upload_documents_request_body_meta import ConvertUploadDocumentsRequestBodyMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertUploadDocumentsRequestBodyMeta from a JSON string
convert_upload_documents_request_body_meta_instance = ConvertUploadDocumentsRequestBodyMeta.from_json(json)
# print the JSON string representation of the object
print(ConvertUploadDocumentsRequestBodyMeta.to_json())

# convert the object into a dict
convert_upload_documents_request_body_meta_dict = convert_upload_documents_request_body_meta_instance.to_dict()
# create an instance of ConvertUploadDocumentsRequestBodyMeta from a dict
convert_upload_documents_request_body_meta_form_dict = convert_upload_documents_request_body_meta.from_dict(convert_upload_documents_request_body_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


