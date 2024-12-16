# DescriptionLicense

Licence in document description.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**Code**](Code.md) |  | [optional] 
**text** | [**Text**](Text.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.description_license import DescriptionLicense

# TODO update the JSON string below
json = "{}"
# create an instance of DescriptionLicense from a JSON string
description_license_instance = DescriptionLicense.from_json(json)
# print the JSON string representation of the object
print(DescriptionLicense.to_json())

# convert the object into a dict
description_license_dict = description_license_instance.to_dict()
# create an instance of DescriptionLicense from a dict
description_license_form_dict = description_license.from_dict(description_license_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


