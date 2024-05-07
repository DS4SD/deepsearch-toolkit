# UploadJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** |  | 
**num_docs** | **int** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.upload_job import UploadJob

# TODO update the JSON string below
json = "{}"
# create an instance of UploadJob from a JSON string
upload_job_instance = UploadJob.from_json(json)
# print the JSON string representation of the object
print(UploadJob.to_json())

# convert the object into a dict
upload_job_dict = upload_job_instance.to_dict()
# create an instance of UploadJob from a dict
upload_job_form_dict = upload_job.from_dict(upload_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


