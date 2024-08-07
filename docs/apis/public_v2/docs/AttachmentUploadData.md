# AttachmentUploadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachment_path** | **str** |  | 
**upload_data** | **str** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.attachment_upload_data import AttachmentUploadData

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentUploadData from a JSON string
attachment_upload_data_instance = AttachmentUploadData.from_json(json)
# print the JSON string representation of the object
print(AttachmentUploadData.to_json())

# convert the object into a dict
attachment_upload_data_dict = attachment_upload_data_instance.to_dict()
# create an instance of AttachmentUploadData from a dict
attachment_upload_data_form_dict = attachment_upload_data.from_dict(attachment_upload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


