# SemanticIngestSourcePublicDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**elastic_id** | **str** |  | 
**index_key** | **str** |  | 
**document_hash** | **str** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.semantic_ingest_source_public_data_document import SemanticIngestSourcePublicDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SemanticIngestSourcePublicDataDocument from a JSON string
semantic_ingest_source_public_data_document_instance = SemanticIngestSourcePublicDataDocument.from_json(json)
# print the JSON string representation of the object
print(SemanticIngestSourcePublicDataDocument.to_json())

# convert the object into a dict
semantic_ingest_source_public_data_document_dict = semantic_ingest_source_public_data_document_instance.to_dict()
# create an instance of SemanticIngestSourcePublicDataDocument from a dict
semantic_ingest_source_public_data_document_form_dict = semantic_ingest_source_public_data_document.from_dict(semantic_ingest_source_public_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


