# TemporaryUploadFileResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**upload** | [**TemporaryUrlFields**](TemporaryUrlFields.md) |  | 
**download** | [**TemporaryUrl**](TemporaryUrl.md) |  | 
**metadata** | [**TemporaryUrl**](TemporaryUrl.md) |  | 
**upload_private** | [**TemporaryUrlFields**](TemporaryUrlFields.md) |  | 
**download_private** | [**TemporaryUrl**](TemporaryUrl.md) |  | 
**metadata_private** | [**TemporaryUrl**](TemporaryUrl.md) |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.temporary_upload_file_result import TemporaryUploadFileResult

# TODO update the JSON string below
json = "{}"
# create an instance of TemporaryUploadFileResult from a JSON string
temporary_upload_file_result_instance = TemporaryUploadFileResult.from_json(json)
# print the JSON string representation of the object
print(TemporaryUploadFileResult.to_json())

# convert the object into a dict
temporary_upload_file_result_dict = temporary_upload_file_result_instance.to_dict()
# create an instance of TemporaryUploadFileResult from a dict
temporary_upload_file_result_form_dict = temporary_upload_file_result.from_dict(temporary_upload_file_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


