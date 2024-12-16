# GenAIOpenai

GenAI integration for OpenAI API settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | [optional] [default to 'openai']
**config** | [**GenAIOpenaiConfig**](GenAIOpenaiConfig.md) |  | 
**proj_params** | [**GenAIAWSBedrockProjParams**](GenAIAWSBedrockProjParams.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.gen_ai_openai import GenAIOpenai

# TODO update the JSON string below
json = "{}"
# create an instance of GenAIOpenai from a JSON string
gen_ai_openai_instance = GenAIOpenai.from_json(json)
# print the JSON string representation of the object
print(GenAIOpenai.to_json())

# convert the object into a dict
gen_ai_openai_dict = gen_ai_openai_instance.to_dict()
# create an instance of GenAIOpenai from a dict
gen_ai_openai_form_dict = gen_ai_openai.from_dict(gen_ai_openai_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


