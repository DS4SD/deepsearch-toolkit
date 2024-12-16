# Author

Author.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**id** | [**Id**](Id.md) |  | [optional] 
**source** | [**Source**](Source.md) |  | [optional] 
**affiliations** | [**Affiliations**](Affiliations.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.author import Author

# TODO update the JSON string below
json = "{}"
# create an instance of Author from a JSON string
author_instance = Author.from_json(json)
# print the JSON string representation of the object
print(Author.to_json())

# convert the object into a dict
author_dict = author_instance.to_dict()
# create an instance of Author from a dict
author_form_dict = author.from_dict(author_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


