# ListProjectFlavours


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flavours** | [**List[BagFlavourFullData]**](BagFlavourFullData.md) |  | 
**proj_key** | **str** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.list_project_flavours import ListProjectFlavours

# TODO update the JSON string below
json = "{}"
# create an instance of ListProjectFlavours from a JSON string
list_project_flavours_instance = ListProjectFlavours.from_json(json)
# print the JSON string representation of the object
print(ListProjectFlavours.to_json())

# convert the object into a dict
list_project_flavours_dict = list_project_flavours_instance.to_dict()
# create an instance of ListProjectFlavours from a dict
list_project_flavours_form_dict = list_project_flavours.from_dict(list_project_flavours_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


