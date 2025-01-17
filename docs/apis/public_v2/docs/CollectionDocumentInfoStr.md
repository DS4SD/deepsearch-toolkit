# CollectionDocumentInfoStr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**Name**](Name.md) |  | [optional] 
**type** | **object** | The collection type. | 
**version** | [**Version**](Version.md) |  | [optional] 
**alias** | [**Alias**](Alias.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.collection_document_info_str import CollectionDocumentInfoStr

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionDocumentInfoStr from a JSON string
collection_document_info_str_instance = CollectionDocumentInfoStr.from_json(json)
# print the JSON string representation of the object
print(CollectionDocumentInfoStr.to_json())

# convert the object into a dict
collection_document_info_str_dict = collection_document_info_str_instance.to_dict()
# create an instance of CollectionDocumentInfoStr from a dict
collection_document_info_str_form_dict = collection_document_info_str.from_dict(collection_document_info_str_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


