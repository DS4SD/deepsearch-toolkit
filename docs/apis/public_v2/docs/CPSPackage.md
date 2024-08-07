# CPSPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**package_id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.cps_package import CPSPackage

# TODO update the JSON string below
json = "{}"
# create an instance of CPSPackage from a JSON string
cps_package_instance = CPSPackage.from_json(json)
# print the JSON string representation of the object
print(CPSPackage.to_json())

# convert the object into a dict
cps_package_dict = cps_package_instance.to_dict()
# create an instance of CPSPackage from a dict
cps_package_form_dict = cps_package.from_dict(cps_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


