# SemanticIngestReqParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip_ingested_docs** | **bool** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.semantic_ingest_req_params import SemanticIngestReqParams

# TODO update the JSON string below
json = "{}"
# create an instance of SemanticIngestReqParams from a JSON string
semantic_ingest_req_params_instance = SemanticIngestReqParams.from_json(json)
# print the JSON string representation of the object
print(SemanticIngestReqParams.to_json())

# convert the object into a dict
semantic_ingest_req_params_dict = semantic_ingest_req_params_instance.to_dict()
# create an instance of SemanticIngestReqParams from a dict
semantic_ingest_req_params_form_dict = semantic_ingest_req_params.from_dict(semantic_ingest_req_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


