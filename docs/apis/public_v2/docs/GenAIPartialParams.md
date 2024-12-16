# GenAIPartialParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_id** | [**ModelId**](ModelId.md) |  | [optional] 
**prompt_template** | [**PromptTemplate**](PromptTemplate.md) |  | [optional] 
**params** | [**Params**](Params.md) |  | [optional] 
**timeout** | [**Timeout**](Timeout.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.gen_ai_partial_params import GenAIPartialParams

# TODO update the JSON string below
json = "{}"
# create an instance of GenAIPartialParams from a JSON string
gen_ai_partial_params_instance = GenAIPartialParams.from_json(json)
# print the JSON string representation of the object
print(GenAIPartialParams.to_json())

# convert the object into a dict
gen_ai_partial_params_dict = gen_ai_partial_params_instance.to_dict()
# create an instance of GenAIPartialParams from a dict
gen_ai_partial_params_form_dict = gen_ai_partial_params.from_dict(gen_ai_partial_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


