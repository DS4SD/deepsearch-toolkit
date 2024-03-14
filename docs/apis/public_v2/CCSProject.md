# CCSProject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**proj_key** | **str** |  | 
**collection_name** | **str** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.ccs_project import CCSProject

# TODO update the JSON string below
json = "{}"
# create an instance of CCSProject from a JSON string
ccs_project_instance = CCSProject.from_json(json)
# print the JSON string representation of the object
print(CCSProject.to_json())

# convert the object into a dict
ccs_project_dict = ccs_project_instance.to_dict()
# create an instance of CCSProject from a dict
ccs_project_form_dict = ccs_project.from_dict(ccs_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


