# OcrSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] [default to False]
**backend** | **str** |  | [optional] 
**backend_settings** | **object** |  | [optional] 
**merge_mode** | **str** |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.ocr_settings import OcrSettings

# TODO update the JSON string below
json = "{}"
# create an instance of OcrSettings from a JSON string
ocr_settings_instance = OcrSettings.from_json(json)
# print the JSON string representation of the object
print(OcrSettings.to_json())

# convert the object into a dict
ocr_settings_dict = ocr_settings_instance.to_dict()
# create an instance of OcrSettings from a dict
ocr_settings_form_dict = ocr_settings.from_dict(ocr_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


