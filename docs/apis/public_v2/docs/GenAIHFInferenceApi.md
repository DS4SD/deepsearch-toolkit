# GenAIHFInferenceApi

GenAI integration for Inference API settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | [optional] [default to 'hf_api']
**config** | [**GenAIHFInferenceApiConfig**](GenAIHFInferenceApiConfig.md) |  | 
**proj_params** | [**GenAIAWSBedrockProjParams**](GenAIAWSBedrockProjParams.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.gen_aihf_inference_api import GenAIHFInferenceApi

# TODO update the JSON string below
json = "{}"
# create an instance of GenAIHFInferenceApi from a JSON string
gen_aihf_inference_api_instance = GenAIHFInferenceApi.from_json(json)
# print the JSON string representation of the object
print(GenAIHFInferenceApi.to_json())

# convert the object into a dict
gen_aihf_inference_api_dict = gen_aihf_inference_api_instance.to_dict()
# create an instance of GenAIHFInferenceApi from a dict
gen_aihf_inference_api_form_dict = gen_aihf_inference_api.from_dict(gen_aihf_inference_api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


