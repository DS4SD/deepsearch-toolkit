# DocumentArtifacts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_meta_json** | [**DocumentArtifactsItem**](DocumentArtifactsItem.md) |  | [optional] 
**document_pdf** | [**DocumentArtifactsItem**](DocumentArtifactsItem.md) |  | [optional] 
**document_json** | [**DocumentArtifactsItem**](DocumentArtifactsItem.md) |  | [optional] 
**document_glm_json** | [**DocumentArtifactsItem**](DocumentArtifactsItem.md) |  | [optional] 
**document_md** | [**DocumentArtifactsItem**](DocumentArtifactsItem.md) |  | [optional] 
**page_pdfs** | [**List[DocumentArtifactsPageItem]**](DocumentArtifactsPageItem.md) |  | [optional] [default to []]
**page_images** | [**List[DocumentArtifactsPageItem]**](DocumentArtifactsPageItem.md) |  | [optional] [default to []]

## Example

```python
from deepsearch.cps.apis.public_v2.models.document_artifacts import DocumentArtifacts

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentArtifacts from a JSON string
document_artifacts_instance = DocumentArtifacts.from_json(json)
# print the JSON string representation of the object
print(DocumentArtifacts.to_json())

# convert the object into a dict
document_artifacts_dict = document_artifacts_instance.to_dict()
# create an instance of DocumentArtifacts from a dict
document_artifacts_form_dict = document_artifacts.from_dict(document_artifacts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


