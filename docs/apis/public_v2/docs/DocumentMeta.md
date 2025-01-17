# DocumentMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | [**Filename**](Filename.md) |  | [optional] 
**description** | [**DocumentMetaDescription**](DocumentMetaDescription.md) |  | [optional] 
**identifiers** | [**Identifiers**](Identifiers.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.document_meta import DocumentMeta

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentMeta from a JSON string
document_meta_instance = DocumentMeta.from_json(json)
# print the JSON string representation of the object
print(DocumentMeta.to_json())

# convert the object into a dict
document_meta_dict = document_meta_instance.to_dict()
# create an instance of DocumentMeta from a dict
document_meta_form_dict = document_meta.from_dict(document_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


