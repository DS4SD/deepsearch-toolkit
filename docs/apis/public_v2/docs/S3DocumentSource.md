# S3DocumentSource

Specifies documents to import from an S3 bucket

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinates** | [**S3Coordinates**](S3Coordinates.md) |  | 
**object_keys** | **List[str]** | List of s3 object keys to retrieve from bucket to be converted and uploaded to the data index. | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.s3_document_source import S3DocumentSource

# TODO update the JSON string below
json = "{}"
# create an instance of S3DocumentSource from a JSON string
s3_document_source_instance = S3DocumentSource.from_json(json)
# print the JSON string representation of the object
print(S3DocumentSource.to_json())

# convert the object into a dict
s3_document_source_dict = s3_document_source_instance.to_dict()
# create an instance of S3DocumentSource from a dict
s3_document_source_form_dict = s3_document_source.from_dict(s3_document_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


