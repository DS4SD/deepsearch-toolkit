# FlavoursDefaultQuota


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | 
**name** | **str** |  | 
**default_quota** | **int** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.flavours_default_quota import FlavoursDefaultQuota

# TODO update the JSON string below
json = "{}"
# create an instance of FlavoursDefaultQuota from a JSON string
flavours_default_quota_instance = FlavoursDefaultQuota.from_json(json)
# print the JSON string representation of the object
print(FlavoursDefaultQuota.to_json())

# convert the object into a dict
flavours_default_quota_dict = flavours_default_quota_instance.to_dict()
# create an instance of FlavoursDefaultQuota from a dict
flavours_default_quota_form_dict = flavours_default_quota.from_dict(flavours_default_quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


