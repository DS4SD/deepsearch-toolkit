# FlavoursQuota


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | 
**name** | **str** |  | 
**quota** | **int** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.flavours_quota import FlavoursQuota

# TODO update the JSON string below
json = "{}"
# create an instance of FlavoursQuota from a JSON string
flavours_quota_instance = FlavoursQuota.from_json(json)
# print the JSON string representation of the object
print(FlavoursQuota.to_json())

# convert the object into a dict
flavours_quota_dict = flavours_quota_instance.to_dict()
# create an instance of FlavoursQuota from a dict
flavours_quota_form_dict = flavours_quota.from_dict(flavours_quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


