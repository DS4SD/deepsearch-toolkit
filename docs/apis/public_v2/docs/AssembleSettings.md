# AssembleSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | [**AssembleMode**](AssembleMode.md) |  | 
**include_incomplete_documents** | **bool** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.assemble_settings import AssembleSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AssembleSettings from a JSON string
assemble_settings_instance = AssembleSettings.from_json(json)
# print the JSON string representation of the object
print(AssembleSettings.to_json())

# convert the object into a dict
assemble_settings_dict = assemble_settings_instance.to_dict()
# create an instance of AssembleSettings from a dict
assemble_settings_form_dict = assemble_settings.from_dict(assemble_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


