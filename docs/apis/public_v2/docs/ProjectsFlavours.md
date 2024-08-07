# ProjectsFlavours


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**proj_key** | **str** |  | 
**name** | **str** |  | 
**flavours** | [**List[Flavour]**](Flavour.md) |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.projects_flavours import ProjectsFlavours

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsFlavours from a JSON string
projects_flavours_instance = ProjectsFlavours.from_json(json)
# print the JSON string representation of the object
print(ProjectsFlavours.to_json())

# convert the object into a dict
projects_flavours_dict = projects_flavours_instance.to_dict()
# create an instance of ProjectsFlavours from a dict
projects_flavours_form_dict = projects_flavours.from_dict(projects_flavours_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


