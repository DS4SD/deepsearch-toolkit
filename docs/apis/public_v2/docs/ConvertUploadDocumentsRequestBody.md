# ConvertUploadDocumentsRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_url** | [**FileUrl**](FileUrl.md) |  | [optional] 
**http_source** | [**HttpSource**](HttpSource.md) |  | [optional] 
**s3_source** | [**ConvertDocumentsSourcesS3Source**](ConvertDocumentsSourcesS3Source.md) |  | [optional] 
**upload_to_elastic** | [**UploadToElastic**](UploadToElastic.md) |  | [optional] 
**meta** | [**ConvertUploadDocumentsRequestBodyMeta**](ConvertUploadDocumentsRequestBodyMeta.md) |  | [optional] 
**conversion_settings** | [**ConversionSettings**](ConversionSettings.md) |  | [optional] 
**target_settings** | [**ConvertDocumentsRequestBodyTargetSettings**](ConvertDocumentsRequestBodyTargetSettings.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.convert_upload_documents_request_body import ConvertUploadDocumentsRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertUploadDocumentsRequestBody from a JSON string
convert_upload_documents_request_body_instance = ConvertUploadDocumentsRequestBody.from_json(json)
# print the JSON string representation of the object
print(ConvertUploadDocumentsRequestBody.to_json())

# convert the object into a dict
convert_upload_documents_request_body_dict = convert_upload_documents_request_body_instance.to_dict()
# create an instance of ConvertUploadDocumentsRequestBody from a dict
convert_upload_documents_request_body_form_dict = convert_upload_documents_request_body.from_dict(convert_upload_documents_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


