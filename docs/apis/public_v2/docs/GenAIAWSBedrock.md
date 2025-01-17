# GenAIAWSBedrock

GenAI integration for AWS Bedrock settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | [optional] [default to 'aws_bedrock']
**config** | [**GenAIAWSBedrockConfig**](GenAIAWSBedrockConfig.md) |  | 
**proj_params** | [**GenAIAWSBedrockProjParams**](GenAIAWSBedrockProjParams.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.gen_aiaws_bedrock import GenAIAWSBedrock

# TODO update the JSON string below
json = "{}"
# create an instance of GenAIAWSBedrock from a JSON string
gen_aiaws_bedrock_instance = GenAIAWSBedrock.from_json(json)
# print the JSON string representation of the object
print(GenAIAWSBedrock.to_json())

# convert the object into a dict
gen_aiaws_bedrock_dict = gen_aiaws_bedrock_instance.to_dict()
# create an instance of GenAIAWSBedrock from a dict
gen_aiaws_bedrock_form_dict = gen_aiaws_bedrock.from_dict(gen_aiaws_bedrock_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


