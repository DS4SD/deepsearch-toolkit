# ConvertDocumentsSourcesS3Source

Coordinates to object store to get files to convert. Can specify which files with object keys.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinates** | [**S3Coordinates**](S3Coordinates.md) |  | 
**object_keys** | [**ObjectKeys**](ObjectKeys.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.convert_documents_sources_s3_source import ConvertDocumentsSourcesS3Source

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertDocumentsSourcesS3Source from a JSON string
convert_documents_sources_s3_source_instance = ConvertDocumentsSourcesS3Source.from_json(json)
# print the JSON string representation of the object
print(ConvertDocumentsSourcesS3Source.to_json())

# convert the object into a dict
convert_documents_sources_s3_source_dict = convert_documents_sources_s3_source_instance.to_dict()
# create an instance of ConvertDocumentsSourcesS3Source from a dict
convert_documents_sources_s3_source_form_dict = convert_documents_sources_s3_source.from_dict(convert_documents_sources_s3_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


