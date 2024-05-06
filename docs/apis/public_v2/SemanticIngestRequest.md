# SemanticIngestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**Source1**](Source1.md) |  | 
**parameters** | [**SemanticIngestReqParams**](SemanticIngestReqParams.md) |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.semantic_ingest_request import SemanticIngestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SemanticIngestRequest from a JSON string
semantic_ingest_request_instance = SemanticIngestRequest.from_json(json)
# print the JSON string representation of the object
print(SemanticIngestRequest.to_json())

# convert the object into a dict
semantic_ingest_request_dict = semantic_ingest_request_instance.to_dict()
# create an instance of SemanticIngestRequest from a dict
semantic_ingest_request_form_dict = semantic_ingest_request.from_dict(semantic_ingest_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


