# DataIndexUploadFileSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**urls** | [**Urls**](Urls.md) |  | 
**conversion_settings** | [**PartialDirectConversionParameters**](PartialDirectConversionParameters.md) | Specify the conversion settings to use. | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.data_index_upload_file_source import DataIndexUploadFileSource

# TODO update the JSON string below
json = "{}"
# create an instance of DataIndexUploadFileSource from a JSON string
data_index_upload_file_source_instance = DataIndexUploadFileSource.from_json(json)
# print the JSON string representation of the object
print(DataIndexUploadFileSource.to_json())

# convert the object into a dict
data_index_upload_file_source_dict = data_index_upload_file_source_instance.to_dict()
# create an instance of DataIndexUploadFileSource from a dict
data_index_upload_file_source_form_dict = data_index_upload_file_source.from_dict(data_index_upload_file_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


