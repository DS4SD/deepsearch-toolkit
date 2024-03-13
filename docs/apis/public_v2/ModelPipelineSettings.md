# ModelPipelineSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusters** | [**List[ModelPipelineSettingsClustersInner]**](ModelPipelineSettingsClustersInner.md) |  | 
**page** | [**List[ModelPipelineSettingsClustersInner]**](ModelPipelineSettingsClustersInner.md) |  | 
**tables** | [**List[ModelPipelineSettingsClustersInner]**](ModelPipelineSettingsClustersInner.md) |  | 
**normalization** | [**List[ModelPipelineSettingsClustersInner]**](ModelPipelineSettingsClustersInner.md) |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.model_pipeline_settings import ModelPipelineSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ModelPipelineSettings from a JSON string
model_pipeline_settings_instance = ModelPipelineSettings.from_json(json)
# print the JSON string representation of the object
print(ModelPipelineSettings.to_json())

# convert the object into a dict
model_pipeline_settings_dict = model_pipeline_settings_instance.to_dict()
# create an instance of ModelPipelineSettings from a dict
model_pipeline_settings_form_dict = model_pipeline_settings.from_dict(model_pipeline_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


