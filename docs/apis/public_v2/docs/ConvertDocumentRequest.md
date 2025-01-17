# ConvertDocumentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_source** | [**ConvertDocumentRequestHttpSource**](ConvertDocumentRequestHttpSource.md) |  | [optional] 
**file_source** | [**ConvertDocumentRequestFileSource**](ConvertDocumentRequestFileSource.md) |  | [optional] 
**settings** | [**ConvertDocumentRequestSettings**](ConvertDocumentRequestSettings.md) |  | [optional] 
**image_urls** | [**ConvertDocumentRequestImageUrls**](ConvertDocumentRequestImageUrls.md) |  | [optional] 
**truncate_pages** | [**TruncatePages**](TruncatePages.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.convert_document_request import ConvertDocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertDocumentRequest from a JSON string
convert_document_request_instance = ConvertDocumentRequest.from_json(json)
# print the JSON string representation of the object
print(ConvertDocumentRequest.to_json())

# convert the object into a dict
convert_document_request_dict = convert_document_request_instance.to_dict()
# create an instance of ConvertDocumentRequest from a dict
convert_document_request_form_dict = convert_document_request.from_dict(convert_document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


