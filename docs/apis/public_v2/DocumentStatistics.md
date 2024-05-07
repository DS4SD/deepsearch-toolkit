# DocumentStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_documents** | **int** |  | 
**documents_pending** | **int** |  | 
**documents_failed** | **int** |  | 
**documents_converted** | **int** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.document_statistics import DocumentStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentStatistics from a JSON string
document_statistics_instance = DocumentStatistics.from_json(json)
# print the JSON string representation of the object
print(DocumentStatistics.to_json())

# convert the object into a dict
document_statistics_dict = document_statistics_instance.to_dict()
# create an instance of DocumentStatistics from a dict
document_statistics_form_dict = document_statistics.from_dict(document_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


