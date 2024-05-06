# GenAIBAM

GenAI integration for BAM settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | [optional] [default to 'bam']
**config** | [**GenAIBAMConfig**](GenAIBAMConfig.md) |  | 
**proj_params** | [**GenAIPartialParams**](GenAIPartialParams.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.gen_aibam import GenAIBAM

# TODO update the JSON string below
json = "{}"
# create an instance of GenAIBAM from a JSON string
gen_aibam_instance = GenAIBAM.from_json(json)
# print the JSON string representation of the object
print(GenAIBAM.to_json())

# convert the object into a dict
gen_aibam_dict = gen_aibam_instance.to_dict()
# create an instance of GenAIBAM from a dict
gen_aibam_form_dict = gen_aibam.from_dict(gen_aibam_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


