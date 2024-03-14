# BagFlavourFullData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backend** | **str** |  | 
**config** | **object** |  | 
**default_quota** | **int** |  | [optional] [default to 0]
**description** | **str** |  | 
**display_name** | **str** |  | 
**is_from_deployment** | **bool** |  | [optional] [default to True]
**name** | **str** |  | 
**order** | **int** |  | [optional] [default to 0]
**project_specific** | **bool** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.bag_flavour_full_data import BagFlavourFullData

# TODO update the JSON string below
json = "{}"
# create an instance of BagFlavourFullData from a JSON string
bag_flavour_full_data_instance = BagFlavourFullData.from_json(json)
# print the JSON string representation of the object
print(BagFlavourFullData.to_json())

# convert the object into a dict
bag_flavour_full_data_dict = bag_flavour_full_data_instance.to_dict()
# create an instance of BagFlavourFullData from a dict
bag_flavour_full_data_form_dict = bag_flavour_full_data.from_dict(bag_flavour_full_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


