# UploadElasticRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_hashes** | **List[str]** | List of document hashes to be used as filter. | [optional] 
**with_operations** | **List[str]** | List of Operation Status documents don&#39;t have to be used as filter. | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.upload_elastic_request_body import UploadElasticRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of UploadElasticRequestBody from a JSON string
upload_elastic_request_body_instance = UploadElasticRequestBody.from_json(json)
# print the JSON string representation of the object
print(UploadElasticRequestBody.to_json())

# convert the object into a dict
upload_elastic_request_body_dict = upload_elastic_request_body_instance.to_dict()
# create an instance of UploadElasticRequestBody from a dict
upload_elastic_request_body_form_dict = upload_elastic_request_body.from_dict(upload_elastic_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


