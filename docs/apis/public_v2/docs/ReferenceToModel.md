# ReferenceToModel

Reference to a model configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_config_key** | **str** |  | 
**proj_key** | **str** |  | 
**name** | **str** |  | [optional] [default to '']
**description** | **str** |  | [optional] [default to '']

## Example

```python
from deepsearch.cps.apis.public_v2.models.reference_to_model import ReferenceToModel

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceToModel from a JSON string
reference_to_model_instance = ReferenceToModel.from_json(json)
# print the JSON string representation of the object
print(ReferenceToModel.to_json())

# convert the object into a dict
reference_to_model_dict = reference_to_model_instance.to_dict()
# create an instance of ReferenceToModel from a dict
reference_to_model_form_dict = reference_to_model.from_dict(reference_to_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


