# ElasticIndexSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index_key** | **str** |  | 
**elastic_id** | **str** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.elastic_index_source import ElasticIndexSource

# TODO update the JSON string below
json = "{}"
# create an instance of ElasticIndexSource from a JSON string
elastic_index_source_instance = ElasticIndexSource.from_json(json)
# print the JSON string representation of the object
print(ElasticIndexSource.to_json())

# convert the object into a dict
elastic_index_source_dict = elastic_index_source_instance.to_dict()
# create an instance of ElasticIndexSource from a dict
elastic_index_source_form_dict = elastic_index_source.from_dict(elastic_index_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


