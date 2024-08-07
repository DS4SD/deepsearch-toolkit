# GenAIHFInferenceApiConfig

Config for HF Inference API

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**genai_hf_api_key** | **str** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.gen_aihf_inference_api_config import GenAIHFInferenceApiConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GenAIHFInferenceApiConfig from a JSON string
gen_aihf_inference_api_config_instance = GenAIHFInferenceApiConfig.from_json(json)
# print the JSON string representation of the object
print(GenAIHFInferenceApiConfig.to_json())

# convert the object into a dict
gen_aihf_inference_api_config_dict = gen_aihf_inference_api_config_instance.to_dict()
# create an instance of GenAIHFInferenceApiConfig from a dict
gen_aihf_inference_api_config_form_dict = gen_aihf_inference_api_config.from_dict(gen_aihf_inference_api_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


