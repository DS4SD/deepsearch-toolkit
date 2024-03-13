# ProjectSourceDataIndex


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index_key** | **str** |  | 
**query_options** | [**ElasticIndexSearchQueryOptions**](ElasticIndexSearchQueryOptions.md) |  | 
**proj_key** | **str** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.project_source_data_index import ProjectSourceDataIndex

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSourceDataIndex from a JSON string
project_source_data_index_instance = ProjectSourceDataIndex.from_json(json)
# print the JSON string representation of the object
print(ProjectSourceDataIndex.to_json())

# convert the object into a dict
project_source_data_index_dict = project_source_data_index_instance.to_dict()
# create an instance of ProjectSourceDataIndex from a dict
project_source_data_index_form_dict = project_source_data_index.from_dict(project_source_data_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


