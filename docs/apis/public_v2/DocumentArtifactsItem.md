# DocumentArtifactsItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mime** | **str** |  | 
**path** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.document_artifacts_item import DocumentArtifactsItem

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentArtifactsItem from a JSON string
document_artifacts_item_instance = DocumentArtifactsItem.from_json(json)
# print the JSON string representation of the object
print(DocumentArtifactsItem.to_json())

# convert the object into a dict
document_artifacts_item_dict = document_artifacts_item_instance.to_dict()
# create an instance of DocumentArtifactsItem from a dict
document_artifacts_item_form_dict = document_artifacts_item.from_dict(document_artifacts_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


