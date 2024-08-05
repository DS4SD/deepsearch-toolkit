# ConvertUploadDocumentsRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_url** | **List[str]** | List of File&#39;s URL to be converted and uploaded to the data index. | [optional] 
**internal_file_url** | [**List[InternalUrl]**](InternalUrl.md) | List of Internal File&#39;s URLs to be converted and uploaded to the data index. | [optional] 
**s3_source** | [**S3DocumentSource**](S3DocumentSource.md) | Coordinates to object store to get files to convert. Can specify which files with object keys. | [optional] 
**upload_to_elastic** | **bool** |  | [optional] 
**conversion_settings** | [**PartialDirectConversionParameters**](PartialDirectConversionParameters.md) | Specify the conversion settings to use. | [optional] 
**target_settings** | [**TargetConversionParameters**](TargetConversionParameters.md) | Specify the target settings to use. | [optional] 

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


