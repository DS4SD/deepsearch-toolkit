# DoclingCoreTypesBaseIdentifier

Unique identifier of a Docling data object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | A string representing a collection or database that contains this data object. | 
**value** | **str** | The identifier value of the data object within a collection or database. | 
**name** | **str** | A unique identifier of the data object across Docling, consisting of the concatenation of type and value in lower case, separated by hash (#). | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.docling_core_types_base_identifier import DoclingCoreTypesBaseIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of DoclingCoreTypesBaseIdentifier from a JSON string
docling_core_types_base_identifier_instance = DoclingCoreTypesBaseIdentifier.from_json(json)
# print the JSON string representation of the object
print(DoclingCoreTypesBaseIdentifier.to_json())

# convert the object into a dict
docling_core_types_base_identifier_dict = docling_core_types_base_identifier_instance.to_dict()
# create an instance of DoclingCoreTypesBaseIdentifier from a dict
docling_core_types_base_identifier_form_dict = docling_core_types_base_identifier.from_dict(docling_core_types_base_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


