# ModulesConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**df_template_variables** | **List[object]** |  | 
**linked_ccs_instances** | **List[object]** |  | 
**linked_elastic_instances** | **List[object]** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.modules_config import ModulesConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ModulesConfig from a JSON string
modules_config_instance = ModulesConfig.from_json(json)
# print the JSON string representation of the object
print(ModulesConfig.to_json())

# convert the object into a dict
modules_config_dict = modules_config_instance.to_dict()
# create an instance of ModulesConfig from a dict
modules_config_form_dict = modules_config.from_dict(modules_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


