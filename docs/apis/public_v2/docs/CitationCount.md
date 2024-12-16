# CitationCount

Total number of citations that this document has received (number of documents in whose bibliography this document appears).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from deepsearch.cps.apis.public_v2.models.citation_count import CitationCount

# TODO update the JSON string below
json = "{}"
# create an instance of CitationCount from a JSON string
citation_count_instance = CitationCount.from_json(json)
# print the JSON string representation of the object
print(CitationCount.to_json())

# convert the object into a dict
citation_count_dict = citation_count_instance.to_dict()
# create an instance of CitationCount from a dict
citation_count_form_dict = citation_count.from_dict(citation_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


