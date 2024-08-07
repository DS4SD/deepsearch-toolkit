# HttpSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**headers** | **object** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.http_source import HttpSource

# TODO update the JSON string below
json = "{}"
# create an instance of HttpSource from a JSON string
http_source_instance = HttpSource.from_json(json)
# print the JSON string representation of the object
print(HttpSource.to_json())

# convert the object into a dict
http_source_dict = http_source_instance.to_dict()
# create an instance of HttpSource from a dict
http_source_form_dict = http_source.from_dict(http_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


