# SystemInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notifications** | **List[object]** |  | 
**default_project** | **object** |  | 
**deployment** | [**Deployment**](Deployment.md) |  | 
**toolkit** | **object** |  | 
**allow_non_admins_to_make_resources_public** | **bool** |  | 
**api** | **object** |  | 
**genai_defaults** | [**Dict[str, GenAIParams]**](GenAIParams.md) |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.system_info import SystemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SystemInfo from a JSON string
system_info_instance = SystemInfo.from_json(json)
# print the JSON string representation of the object
print(SystemInfo.to_json())

# convert the object into a dict
system_info_dict = system_info_instance.to_dict()
# create an instance of SystemInfo from a dict
system_info_form_dict = system_info.from_dict(system_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


