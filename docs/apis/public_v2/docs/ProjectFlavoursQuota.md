# ProjectFlavoursQuota


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**proj_key** | **str** |  | 
**quotas** | [**List[FlavoursQuota]**](FlavoursQuota.md) |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.project_flavours_quota import ProjectFlavoursQuota

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectFlavoursQuota from a JSON string
project_flavours_quota_instance = ProjectFlavoursQuota.from_json(json)
# print the JSON string representation of the object
print(ProjectFlavoursQuota.to_json())

# convert the object into a dict
project_flavours_quota_dict = project_flavours_quota_instance.to_dict()
# create an instance of ProjectFlavoursQuota from a dict
project_flavours_quota_form_dict = project_flavours_quota.from_dict(project_flavours_quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


