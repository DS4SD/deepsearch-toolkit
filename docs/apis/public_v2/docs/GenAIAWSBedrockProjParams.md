# GenAIAWSBedrockProjParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_id** | [**ModelId**](ModelId.md) |  | [optional] 
**prompt_template** | [**PromptTemplate**](PromptTemplate.md) |  | [optional] 
**params** | [**Params**](Params.md) |  | [optional] 
**timeout** | [**Timeout**](Timeout.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.gen_aiaws_bedrock_proj_params import GenAIAWSBedrockProjParams

# TODO update the JSON string below
json = "{}"
# create an instance of GenAIAWSBedrockProjParams from a JSON string
gen_aiaws_bedrock_proj_params_instance = GenAIAWSBedrockProjParams.from_json(json)
# print the JSON string representation of the object
print(GenAIAWSBedrockProjParams.to_json())

# convert the object into a dict
gen_aiaws_bedrock_proj_params_dict = gen_aiaws_bedrock_proj_params_instance.to_dict()
# create an instance of GenAIAWSBedrockProjParams from a dict
gen_aiaws_bedrock_proj_params_form_dict = gen_aiaws_bedrock_proj_params.from_dict(gen_aiaws_bedrock_proj_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


