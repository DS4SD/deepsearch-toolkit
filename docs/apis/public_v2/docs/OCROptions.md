# OCROptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**do_ocr** | **bool** |  | [optional] [default to True]
**kind** | **str** |  | [optional] [default to 'easyocr']

## Example

```python
from deepsearch.cps.apis.public_v2.models.ocr_options import OCROptions

# TODO update the JSON string below
json = "{}"
# create an instance of OCROptions from a JSON string
ocr_options_instance = OCROptions.from_json(json)
# print the JSON string representation of the object
print(OCROptions.to_json())

# convert the object into a dict
ocr_options_dict = ocr_options_instance.to_dict()
# create an instance of OCROptions from a dict
ocr_options_form_dict = ocr_options.from_dict(ocr_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


