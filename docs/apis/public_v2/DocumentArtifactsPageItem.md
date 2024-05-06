# DocumentArtifactsPageItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mime** | **str** |  | 
**path** | **str** |  | 
**url** | **str** |  | 
**page** | **int** | Page number starting at 1. | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.document_artifacts_page_item import DocumentArtifactsPageItem

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentArtifactsPageItem from a JSON string
document_artifacts_page_item_instance = DocumentArtifactsPageItem.from_json(json)
# print the JSON string representation of the object
print(DocumentArtifactsPageItem.to_json())

# convert the object into a dict
document_artifacts_page_item_dict = document_artifacts_page_item_instance.to_dict()
# create an instance of DocumentArtifactsPageItem from a dict
document_artifacts_page_item_form_dict = document_artifacts_page_item.from_dict(document_artifacts_page_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


