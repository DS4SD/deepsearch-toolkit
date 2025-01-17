# DocumentDescriptionLicense


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**Code**](Code.md) |  | [optional] 
**text** | [**Text**](Text.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.document_description_license import DocumentDescriptionLicense

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentDescriptionLicense from a JSON string
document_description_license_instance = DocumentDescriptionLicense.from_json(json)
# print the JSON string representation of the object
print(DocumentDescriptionLicense.to_json())

# convert the object into a dict
document_description_license_dict = document_description_license_instance.to_dict()
# create an instance of DocumentDescriptionLicense from a dict
document_description_license_form_dict = document_description_license.from_dict(document_description_license_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


