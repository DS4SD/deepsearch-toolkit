# Acquisition

Information on how the data was obtained.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The method to obtain the data. | 
**var_date** | [**ModelDate**](ModelDate.md) |  | [optional] 
**link** | [**Link**](Link.md) |  | [optional] 
**size** | [**Size**](Size.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.acquisition import Acquisition

# TODO update the JSON string below
json = "{}"
# create an instance of Acquisition from a JSON string
acquisition_instance = Acquisition.from_json(json)
# print the JSON string representation of the object
print(Acquisition.to_json())

# convert the object into a dict
acquisition_dict = acquisition_instance.to_dict()
# create an instance of Acquisition from a dict
acquisition_form_dict = acquisition.from_dict(acquisition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


