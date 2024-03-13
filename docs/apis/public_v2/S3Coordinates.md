# S3Coordinates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | 
**port** | **int** |  | 
**ssl** | **bool** |  | 
**verify_ssl** | **bool** |  | 
**access_key** | **str** |  | 
**secret_key** | **str** |  | 
**bucket** | **str** |  | 
**key_prefix** | **str** |  | [optional] 
**location** | **str** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.s3_coordinates import S3Coordinates

# TODO update the JSON string below
json = "{}"
# create an instance of S3Coordinates from a JSON string
s3_coordinates_instance = S3Coordinates.from_json(json)
# print the JSON string representation of the object
print(S3Coordinates.to_json())

# convert the object into a dict
s3_coordinates_dict = s3_coordinates_instance.to_dict()
# create an instance of S3Coordinates from a dict
s3_coordinates_form_dict = s3_coordinates.from_dict(s3_coordinates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


