# Affiliation

Affiliation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**id** | [**Id**](Id.md) |  | [optional] 
**source** | [**Source**](Source.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.affiliation import Affiliation

# TODO update the JSON string below
json = "{}"
# create an instance of Affiliation from a JSON string
affiliation_instance = Affiliation.from_json(json)
# print the JSON string representation of the object
print(Affiliation.to_json())

# convert the object into a dict
affiliation_dict = affiliation_instance.to_dict()
# create an instance of Affiliation from a dict
affiliation_form_dict = affiliation.from_dict(affiliation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


