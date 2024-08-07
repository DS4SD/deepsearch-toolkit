# DirectModelConfig

Direct configuration of a model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**config** | **object** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.direct_model_config import DirectModelConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DirectModelConfig from a JSON string
direct_model_config_instance = DirectModelConfig.from_json(json)
# print the JSON string representation of the object
print(DirectModelConfig.to_json())

# convert the object into a dict
direct_model_config_dict = direct_model_config_instance.to_dict()
# create an instance of DirectModelConfig from a dict
direct_model_config_form_dict = direct_model_config.from_dict(direct_model_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


