# ElasticIndexPropertyObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**enabled** | [**Enabled**](Enabled.md) |  | [optional] 
**ignore_above** | [**IgnoreAbove**](IgnoreAbove.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.elastic_index_property_object import ElasticIndexPropertyObject

# TODO update the JSON string below
json = "{}"
# create an instance of ElasticIndexPropertyObject from a JSON string
elastic_index_property_object_instance = ElasticIndexPropertyObject.from_json(json)
# print the JSON string representation of the object
print(ElasticIndexPropertyObject.to_json())

# convert the object into a dict
elastic_index_property_object_dict = elastic_index_property_object_instance.to_dict()
# create an instance of ElasticIndexPropertyObject from a dict
elastic_index_property_object_form_dict = elastic_index_property_object.from_dict(elastic_index_property_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


