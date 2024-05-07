# GenAIWatsonx

GenAI integration for watsonx settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | [optional] [default to 'watsonx']
**config** | [**GenAIWatsonxConfig**](GenAIWatsonxConfig.md) |  | 
**proj_params** | [**GenAIPartialParams**](GenAIPartialParams.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.gen_ai_watsonx import GenAIWatsonx

# TODO update the JSON string below
json = "{}"
# create an instance of GenAIWatsonx from a JSON string
gen_ai_watsonx_instance = GenAIWatsonx.from_json(json)
# print the JSON string representation of the object
print(GenAIWatsonx.to_json())

# convert the object into a dict
gen_ai_watsonx_dict = gen_ai_watsonx_instance.to_dict()
# create an instance of GenAIWatsonx from a dict
gen_ai_watsonx_form_dict = gen_ai_watsonx.from_dict(gen_ai_watsonx_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


