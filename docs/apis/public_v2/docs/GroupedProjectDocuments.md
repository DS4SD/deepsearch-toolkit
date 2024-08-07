# GroupedProjectDocuments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documents** | [**List[ProjectDocument]**](ProjectDocument.md) |  | 
**upload_date** | [**UploadDate**](UploadDate.md) |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.grouped_project_documents import GroupedProjectDocuments

# TODO update the JSON string below
json = "{}"
# create an instance of GroupedProjectDocuments from a JSON string
grouped_project_documents_instance = GroupedProjectDocuments.from_json(json)
# print the JSON string representation of the object
print(GroupedProjectDocuments.to_json())

# convert the object into a dict
grouped_project_documents_dict = grouped_project_documents_instance.to_dict()
# create an instance of GroupedProjectDocuments from a dict
grouped_project_documents_form_dict = grouped_project_documents.from_dict(grouped_project_documents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


