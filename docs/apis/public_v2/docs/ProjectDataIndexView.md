# ProjectDataIndexView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | [**Description**](Description.md) |  | [optional] 
**view_of** | [**ViewOf**](ViewOf.md) |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.project_data_index_view import ProjectDataIndexView

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDataIndexView from a JSON string
project_data_index_view_instance = ProjectDataIndexView.from_json(json)
# print the JSON string representation of the object
print(ProjectDataIndexView.to_json())

# convert the object into a dict
project_data_index_view_dict = project_data_index_view_instance.to_dict()
# create an instance of ProjectDataIndexView from a dict
project_data_index_view_form_dict = project_data_index_view.from_dict(project_data_index_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


