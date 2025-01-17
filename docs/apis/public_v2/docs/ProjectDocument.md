# ProjectDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_hash** | **str** |  | 
**filename** | [**Filename**](Filename.md) |  | [optional] 
**file_uri** | [**FileUri**](FileUri.md) |  | [optional] 
**ref_uri** | [**RefUri**](RefUri.md) |  | [optional] 
**number_pages** | [**NumberPages**](NumberPages.md) |  | [optional] 
**status** | [**Status**](Status.md) |  | [optional] 

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


