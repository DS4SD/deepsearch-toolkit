# GenAICPDConfig

Config for CPD watsonx

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**genai_api** | **str** |  | 
**genai_project_id** | **str** |  | 
**genai_cpd_url** | **str** |  | 
**genai_cpd_verify_tls** | **bool** |  | [optional] [default to True]
**genai_cpd_username** | **str** |  | 
**genai_cpd_password** | [**GenaiCpdPassword**](GenaiCpdPassword.md) |  | [optional] 
**genai_cpd_api_key** | [**GenaiCpdApiKey**](GenaiCpdApiKey.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.gen_aicpd_config import GenAICPDConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GenAICPDConfig from a JSON string
gen_aicpd_config_instance = GenAICPDConfig.from_json(json)
# print the JSON string representation of the object
print(GenAICPDConfig.to_json())

# convert the object into a dict
gen_aicpd_config_dict = gen_aicpd_config_instance.to_dict()
# create an instance of GenAICPDConfig from a dict
gen_aicpd_config_form_dict = gen_aicpd_config.from_dict(gen_aicpd_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


