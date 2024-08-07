# ResponseGetProjectIntegrationConfigGenai


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **object** |  | [optional] 
**config** | [**GenAIAWSBedrockConfig**](GenAIAWSBedrockConfig.md) |  | 
**proj_params** | [**GenAIPartialParams**](GenAIPartialParams.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.response_get_project_integration_config_genai import ResponseGetProjectIntegrationConfigGenai

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetProjectIntegrationConfigGenai from a JSON string
response_get_project_integration_config_genai_instance = ResponseGetProjectIntegrationConfigGenai.from_json(json)
# print the JSON string representation of the object
print(ResponseGetProjectIntegrationConfigGenai.to_json())

# convert the object into a dict
response_get_project_integration_config_genai_dict = response_get_project_integration_config_genai_instance.to_dict()
# create an instance of ResponseGetProjectIntegrationConfigGenai from a dict
response_get_project_integration_config_genai_form_dict = response_get_project_integration_config_genai.from_dict(response_get_project_integration_config_genai_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


