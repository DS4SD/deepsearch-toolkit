# ElasticInstanceDataIndex


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index_key** | **str** |  | 
**query_options** | [**ElasticIndexSearchQueryOptions**](ElasticIndexSearchQueryOptions.md) |  | 
**elastic_id** | **str** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.elastic_instance_data_index import ElasticInstanceDataIndex

# TODO update the JSON string below
json = "{}"
# create an instance of ElasticInstanceDataIndex from a JSON string
elastic_instance_data_index_instance = ElasticInstanceDataIndex.from_json(json)
# print the JSON string representation of the object
print(ElasticInstanceDataIndex.to_json())

# convert the object into a dict
elastic_instance_data_index_dict = elastic_instance_data_index_instance.to_dict()
# create an instance of ElasticInstanceDataIndex from a dict
elastic_instance_data_index_form_dict = elastic_instance_data_index.from_dict(elastic_instance_data_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


