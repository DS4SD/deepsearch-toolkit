# ConvertDocumentsSources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_url** | [**FileUrl**](FileUrl.md) |  | [optional] 
**http_source** | [**HttpSource**](HttpSource.md) |  | [optional] 
**s3_source** | [**ConvertDocumentsSourcesS3Source**](ConvertDocumentsSourcesS3Source.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.convert_documents_sources import ConvertDocumentsSources

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertDocumentsSources from a JSON string
convert_documents_sources_instance = ConvertDocumentsSources.from_json(json)
# print the JSON string representation of the object
print(ConvertDocumentsSources.to_json())

# convert the object into a dict
convert_documents_sources_dict = convert_documents_sources_instance.to_dict()
# create an instance of ConvertDocumentsSources from a dict
convert_documents_sources_form_dict = convert_documents_sources.from_dict(convert_documents_sources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


