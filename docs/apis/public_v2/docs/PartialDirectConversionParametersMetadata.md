# PartialDirectConversionParametersMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | [**Description**](Description.md) |  | [optional] 
**display_name** | [**DisplayName**](DisplayName.md) |  | [optional] 
**license** | [**License**](License.md) |  | [optional] 
**source** | [**Source1**](Source1.md) |  | [optional] 
**version** | [**Version1**](Version1.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.partial_direct_conversion_parameters_metadata import PartialDirectConversionParametersMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of PartialDirectConversionParametersMetadata from a JSON string
partial_direct_conversion_parameters_metadata_instance = PartialDirectConversionParametersMetadata.from_json(json)
# print the JSON string representation of the object
print(PartialDirectConversionParametersMetadata.to_json())

# convert the object into a dict
partial_direct_conversion_parameters_metadata_dict = partial_direct_conversion_parameters_metadata_instance.to_dict()
# create an instance of PartialDirectConversionParametersMetadata from a dict
partial_direct_conversion_parameters_metadata_form_dict = partial_direct_conversion_parameters_metadata.from_dict(partial_direct_conversion_parameters_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


