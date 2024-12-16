# GenAICPD

GenAI integration for watsonx settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | [optional] [default to 'cpd']
**config** | [**GenAICPDConfig**](GenAICPDConfig.md) |  | 
**proj_params** | [**GenAIAWSBedrockProjParams**](GenAIAWSBedrockProjParams.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.gen_aicpd import GenAICPD

# TODO update the JSON string below
json = "{}"
# create an instance of GenAICPD from a JSON string
gen_aicpd_instance = GenAICPD.from_json(json)
# print the JSON string representation of the object
print(GenAICPD.to_json())

# convert the object into a dict
gen_aicpd_dict = gen_aicpd_instance.to_dict()
# create an instance of GenAICPD from a dict
gen_aicpd_form_dict = gen_aicpd.from_dict(gen_aicpd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


