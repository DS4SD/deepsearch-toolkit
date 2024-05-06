# ResponseUploadJobs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_jobs** | [**List[UploadJob]**](UploadJob.md) |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.response_upload_jobs import ResponseUploadJobs

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseUploadJobs from a JSON string
response_upload_jobs_instance = ResponseUploadJobs.from_json(json)
# print the JSON string representation of the object
print(ResponseUploadJobs.to_json())

# convert the object into a dict
response_upload_jobs_dict = response_upload_jobs_instance.to_dict()
# create an instance of ResponseUploadJobs from a dict
response_upload_jobs_form_dict = response_upload_jobs.from_dict(response_upload_jobs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


