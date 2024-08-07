# GenAIAWSBedrockConfig

Config for AWS Bedrock

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**genai_aws_access_key** | **str** |  | 
**genai_aws_secret_key** | **str** |  | 
**genai_aws_region_name** | **str** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.gen_aiaws_bedrock_config import GenAIAWSBedrockConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GenAIAWSBedrockConfig from a JSON string
gen_aiaws_bedrock_config_instance = GenAIAWSBedrockConfig.from_json(json)
# print the JSON string representation of the object
print(GenAIAWSBedrockConfig.to_json())

# convert the object into a dict
gen_aiaws_bedrock_config_dict = gen_aiaws_bedrock_config_instance.to_dict()
# create an instance of GenAIAWSBedrockConfig from a dict
gen_aiaws_bedrock_config_form_dict = gen_aiaws_bedrock_config.from_dict(gen_aiaws_bedrock_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


