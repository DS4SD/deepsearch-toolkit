# ConvertDocumentsRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversion_settings** | [**PartialDirectConversionParameters**](PartialDirectConversionParameters.md) | Specify the conversion settings to use. | [optional] 
**target_settings** | [**TargetConversionParameters**](TargetConversionParameters.md) | Specify the target settings to use. | [optional] 
**document_hashes** | **List[str]** | List of document hashes to be used as filter. | [optional] 
**without_operations** | **List[str]** | List of Operation Status documents don&#39;t have to be used as filter. | [optional] 
**upload_to_elastic** | **bool** |  | [optional] 

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


