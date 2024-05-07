# GenAIBAMConfig

Config for BAM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**genai_api** | **str** |  | 
**genai_key** | **str** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.gen_aibam_config import GenAIBAMConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GenAIBAMConfig from a JSON string
gen_aibam_config_instance = GenAIBAMConfig.from_json(json)
# print the JSON string representation of the object
print(GenAIBAMConfig.to_json())

# convert the object into a dict
gen_aibam_config_dict = gen_aibam_config_instance.to_dict()
# create an instance of GenAIBAMConfig from a dict
gen_aibam_config_form_dict = gen_aibam_config.from_dict(gen_aibam_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


