# GenAIWatsonxConfig

Config for watsonx

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**genai_api** | **str** |  | 
**genai_project_id** | **str** |  | 
**genai_key** | **str** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.gen_ai_watsonx_config import GenAIWatsonxConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GenAIWatsonxConfig from a JSON string
gen_ai_watsonx_config_instance = GenAIWatsonxConfig.from_json(json)
# print the JSON string representation of the object
print(GenAIWatsonxConfig.to_json())

# convert the object into a dict
gen_ai_watsonx_config_dict = gen_ai_watsonx_config_instance.to_dict()
# create an instance of GenAIWatsonxConfig from a dict
gen_ai_watsonx_config_form_dict = gen_ai_watsonx_config.from_dict(gen_ai_watsonx_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


