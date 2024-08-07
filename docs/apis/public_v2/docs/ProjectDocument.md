# ProjectDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_hash** | **str** |  | 
**filename** | **str** |  | 
**file_uri** | **str** |  | [optional] 
**ref_uri** | **str** |  | [optional] 
**number_pages** | **int** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.project_document import ProjectDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDocument from a JSON string
project_document_instance = ProjectDocument.from_json(json)
# print the JSON string representation of the object
print(ProjectDocument.to_json())

# convert the object into a dict
project_document_dict = project_document_instance.to_dict()
# create an instance of ProjectDocument from a dict
project_document_form_dict = project_document.from_dict(project_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


