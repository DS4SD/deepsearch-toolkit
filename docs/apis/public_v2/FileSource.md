# FileSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base64_string** | **str** |  | 
**filename** | **str** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.file_source import FileSource

# TODO update the JSON string below
json = "{}"
# create an instance of FileSource from a JSON string
file_source_instance = FileSource.from_json(json)
# print the JSON string representation of the object
print(FileSource.to_json())

# convert the object into a dict
file_source_dict = file_source_instance.to_dict()
# create an instance of FileSource from a dict
file_source_form_dict = file_source.from_dict(file_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


