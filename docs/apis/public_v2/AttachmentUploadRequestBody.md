# AttachmentUploadRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachment_path** | **str** |  | 
**attachment_key** | **str** |  | [optional] [default to 'usr_attachments']

## Example

```python
from deepsearch.cps.apis.public_v2.models.attachment_upload_request_body import AttachmentUploadRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentUploadRequestBody from a JSON string
attachment_upload_request_body_instance = AttachmentUploadRequestBody.from_json(json)
# print the JSON string representation of the object
print(AttachmentUploadRequestBody.to_json())

# convert the object into a dict
attachment_upload_request_body_dict = attachment_upload_request_body_instance.to_dict()
# create an instance of AttachmentUploadRequestBody from a dict
attachment_upload_request_body_form_dict = attachment_upload_request_body.from_dict(attachment_upload_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


