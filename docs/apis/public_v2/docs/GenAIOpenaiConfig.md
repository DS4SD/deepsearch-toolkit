# GenAIOpenaiConfig

Config for OpenAI API

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**genai_openai_api_key** | **str** |  | 
**genai_openai_base_url** | **str** |  | 
**genai_openai_verify_tls** | **bool** |  | [optional] [default to True]

## Example

```python
from deepsearch.cps.apis.public_v2.models.gen_ai_openai_config import GenAIOpenaiConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GenAIOpenaiConfig from a JSON string
gen_ai_openai_config_instance = GenAIOpenaiConfig.from_json(json)
# print the JSON string representation of the object
print(GenAIOpenaiConfig.to_json())

# convert the object into a dict
gen_ai_openai_config_dict = gen_ai_openai_config_instance.to_dict()
# create an instance of GenAIOpenaiConfig from a dict
gen_ai_openai_config_form_dict = gen_ai_openai_config.from_dict(gen_ai_openai_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


