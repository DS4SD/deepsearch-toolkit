# Publication

Publication details of a journal or venue.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiers** | [**Identifiers1**](Identifiers1.md) |  | [optional] 
**name** | **str** | Name of the publication. | 
**alternate_names** | [**AlternateNames**](AlternateNames.md) |  | [optional] 
**type** | [**Type1**](Type1.md) |  | [optional] 
**pages** | [**Pages**](Pages.md) |  | [optional] 
**issue** | [**Issue**](Issue.md) |  | [optional] 
**volume** | [**Volume**](Volume.md) |  | [optional] 
**url** | [**Url**](Url.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.publication import Publication

# TODO update the JSON string below
json = "{}"
# create an instance of Publication from a JSON string
publication_instance = Publication.from_json(json)
# print the JSON string representation of the object
print(Publication.to_json())

# convert the object into a dict
publication_dict = publication_instance.to_dict()
# create an instance of Publication from a dict
publication_form_dict = publication.from_dict(publication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


