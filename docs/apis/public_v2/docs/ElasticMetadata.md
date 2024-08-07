# ElasticMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | **List[str]** |  | [optional] 
**created** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**storage** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**domain** | **List[str]** |  | [optional] 
**classification** | **List[str]** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.elastic_metadata import ElasticMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ElasticMetadata from a JSON string
elastic_metadata_instance = ElasticMetadata.from_json(json)
# print the JSON string representation of the object
print(ElasticMetadata.to_json())

# convert the object into a dict
elastic_metadata_dict = elastic_metadata_instance.to_dict()
# create an instance of ElasticMetadata from a dict
elastic_metadata_form_dict = elastic_metadata.from_dict(elastic_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


