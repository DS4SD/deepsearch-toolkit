# ConvertDocumentsRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_url** | **List[str]** | List of File&#39;s URL to be converted and uploaded to the data index. | [optional] 
**s3_source** | [**S3DocumentSource**](S3DocumentSource.md) | Coordinates to object store to get files to convert. Can specify which files with object keys. | [optional] 
**scratch_files_id** | **List[str]** | List of CCS&#39;s scratch files id to be converted and uploaded to the data index. | [optional] 
**conversion_settings** | [**PartialDirectConversionParameters**](PartialDirectConversionParameters.md) | Specify the conversion settings to use. | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.convert_documents_request_body import ConvertDocumentsRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertDocumentsRequestBody from a JSON string
convert_documents_request_body_instance = ConvertDocumentsRequestBody.from_json(json)
# print the JSON string representation of the object
print(ConvertDocumentsRequestBody.to_json())

# convert the object into a dict
convert_documents_request_body_dict = convert_documents_request_body_instance.to_dict()
# create an instance of ConvertDocumentsRequestBody from a dict
convert_documents_request_body_form_dict = convert_documents_request_body.from_dict(convert_documents_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


