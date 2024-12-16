# TableStructureOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**do_table_structure** | **bool** |  | [optional] [default to True]
**table_structure_mode** | [**TableFormerMode**](TableFormerMode.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.table_structure_options import TableStructureOptions

# TODO update the JSON string below
json = "{}"
# create an instance of TableStructureOptions from a JSON string
table_structure_options_instance = TableStructureOptions.from_json(json)
# print the JSON string representation of the object
print(TableStructureOptions.to_json())

# convert the object into a dict
table_structure_options_dict = table_structure_options_instance.to_dict()
# create an instance of TableStructureOptions from a dict
table_structure_options_form_dict = table_structure_options.from_dict(table_structure_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


