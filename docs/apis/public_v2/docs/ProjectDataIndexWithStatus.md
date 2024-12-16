# ProjectDataIndexWithStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**Source3**](Source3.md) |  | 
**name** | **str** |  | 
**documents** | **int** |  | 
**health** | **str** |  | 
**status** | **str** |  | 
**creation_date** | **str** |  | 
**metadata** | [**ProjectDataIndexWithStatusMetadata**](ProjectDataIndexWithStatusMetadata.md) |  | [optional] 
**description** | **str** |  | 
**schema_key** | [**SchemaKey**](SchemaKey.md) |  | [optional] 
**type** | **str** |  | 
**view_of** | [**ViewOf1**](ViewOf1.md) |  | [optional] 
**record_properties** | [**RecordProperties**](RecordProperties.md) |  | [optional] 
**provenance** | [**Provenance**](Provenance.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.project_data_index_with_status import ProjectDataIndexWithStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDataIndexWithStatus from a JSON string
project_data_index_with_status_instance = ProjectDataIndexWithStatus.from_json(json)
# print the JSON string representation of the object
print(ProjectDataIndexWithStatus.to_json())

# convert the object into a dict
project_data_index_with_status_dict = project_data_index_with_status_instance.to_dict()
# create an instance of ProjectDataIndexWithStatus from a dict
project_data_index_with_status_form_dict = project_data_index_with_status.from_dict(project_data_index_with_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


