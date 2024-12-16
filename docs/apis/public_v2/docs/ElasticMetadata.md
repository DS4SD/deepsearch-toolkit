# ElasticMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | [**Aliases**](Aliases.md) |  | [optional] 
**created** | [**Created**](Created.md) |  | [optional] 
**description** | [**Description**](Description.md) |  | [optional] 
**display_name** | [**DisplayName**](DisplayName.md) |  | [optional] 
**source** | [**Source1**](Source1.md) |  | [optional] 
**storage** | [**Storage**](Storage.md) |  | [optional] 
**version** | [**Version1**](Version1.md) |  | [optional] 
**type** | [**Type**](Type.md) |  | [optional] 
**domain** | [**Domain**](Domain.md) |  | [optional] 
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


