# ModelPipelineSettingsClustersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_config_key** | **object** |  | 
**proj_key** | **object** |  | 
**name** | **object** |  | [optional] 
**description** | **object** |  | [optional] 
**type** | **object** |  | 
**config** | **object** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.model_pipeline_settings_clusters_inner import ModelPipelineSettingsClustersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ModelPipelineSettingsClustersInner from a JSON string
model_pipeline_settings_clusters_inner_instance = ModelPipelineSettingsClustersInner.from_json(json)
# print the JSON string representation of the object
print(ModelPipelineSettingsClustersInner.to_json())

# convert the object into a dict
model_pipeline_settings_clusters_inner_dict = model_pipeline_settings_clusters_inner_instance.to_dict()
# create an instance of ModelPipelineSettingsClustersInner from a dict
model_pipeline_settings_clusters_inner_form_dict = model_pipeline_settings_clusters_inner.from_dict(model_pipeline_settings_clusters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


