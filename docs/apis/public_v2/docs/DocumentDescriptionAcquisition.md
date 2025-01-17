# DocumentDescriptionAcquisition

Information on how the document was obtained, for data governance purposes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | The method to obtain the data. | 
**var_date** | [**ModelDate**](ModelDate.md) |  | [optional] 
**link** | [**Link**](Link.md) |  | [optional] 
**size** | [**Size**](Size.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.document_description_acquisition import DocumentDescriptionAcquisition

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentDescriptionAcquisition from a JSON string
document_description_acquisition_instance = DocumentDescriptionAcquisition.from_json(json)
# print the JSON string representation of the object
print(DocumentDescriptionAcquisition.to_json())

# convert the object into a dict
document_description_acquisition_dict = document_description_acquisition_instance.to_dict()
# create an instance of DocumentDescriptionAcquisition from a dict
document_description_acquisition_form_dict = document_description_acquisition.from_dict(document_description_acquisition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


