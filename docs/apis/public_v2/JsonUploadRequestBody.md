# JsonUploadRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_url** | **str** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.json_upload_request_body import JsonUploadRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of JsonUploadRequestBody from a JSON string
json_upload_request_body_instance = JsonUploadRequestBody.from_json(json)
# print the JSON string representation of the object
print(JsonUploadRequestBody.to_json())

# convert the object into a dict
json_upload_request_body_dict = json_upload_request_body_instance.to_dict()
# create an instance of JsonUploadRequestBody from a dict
json_upload_request_body_form_dict = json_upload_request_body.from_dict(json_upload_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


