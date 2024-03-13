# ElasticIndexSearchQueryOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **List[str]** |  | [optional] 
**from_** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**query** | **object** |  | [optional] 
**aggs** | **object** |  | [optional] 
**sort** | **List[object]** |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.elastic_index_search_query_options import ElasticIndexSearchQueryOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ElasticIndexSearchQueryOptions from a JSON string
elastic_index_search_query_options_instance = ElasticIndexSearchQueryOptions.from_json(json)
# print the JSON string representation of the object
print(ElasticIndexSearchQueryOptions.to_json())

# convert the object into a dict
elastic_index_search_query_options_dict = elastic_index_search_query_options_instance.to_dict()
# create an instance of ElasticIndexSearchQueryOptions from a dict
elastic_index_search_query_options_form_dict = elastic_index_search_query_options.from_dict(elastic_index_search_query_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


