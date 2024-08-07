# ResponseGroupedDocuments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grouped_documents** | [**List[GroupedProjectDocuments]**](GroupedProjectDocuments.md) |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.response_grouped_documents import ResponseGroupedDocuments

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGroupedDocuments from a JSON string
response_grouped_documents_instance = ResponseGroupedDocuments.from_json(json)
# print the JSON string representation of the object
print(ResponseGroupedDocuments.to_json())

# convert the object into a dict
response_grouped_documents_dict = response_grouped_documents_instance.to_dict()
# create an instance of ResponseGroupedDocuments from a dict
response_grouped_documents_form_dict = response_grouped_documents.from_dict(response_grouped_documents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


