# CollectionMetadataSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**license** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.collection_metadata_settings import CollectionMetadataSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionMetadataSettings from a JSON string
collection_metadata_settings_instance = CollectionMetadataSettings.from_json(json)
# print the JSON string representation of the object
print(CollectionMetadataSettings.to_json())

# convert the object into a dict
collection_metadata_settings_dict = collection_metadata_settings_instance.to_dict()
# create an instance of CollectionMetadataSettings from a dict
collection_metadata_settings_form_dict = collection_metadata_settings.from_dict(collection_metadata_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


