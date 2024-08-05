# GenAIParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_id** | **str** |  | 
**prompt_template** | **str** |  | 
**params** | **object** |  | 
**timeout** | **float** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.gen_ai_params import GenAIParams

# TODO update the JSON string below
json = "{}"
# create an instance of GenAIParams from a JSON string
gen_ai_params_instance = GenAIParams.from_json(json)
# print the JSON string representation of the object
print(GenAIParams.to_json())

# convert the object into a dict
gen_ai_params_dict = gen_ai_params_instance.to_dict()
# create an instance of GenAIParams from a dict
gen_ai_params_form_dict = gen_ai_params.from_dict(gen_ai_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


