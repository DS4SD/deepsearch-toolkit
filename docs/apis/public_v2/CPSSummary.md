# CPSSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avail_cpu_slots** | **int** |  | 
**avail_mem_slots** | **int** |  | 
**avail_slots** | **int** |  | 
**name** | **str** |  | 
**num_nodes** | **int** |  | 
**number_kgs** | **int** |  | 
**running_kgs** | **int** |  | 
**workers_pool** | **str** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.cps_summary import CPSSummary

# TODO update the JSON string below
json = "{}"
# create an instance of CPSSummary from a JSON string
cps_summary_instance = CPSSummary.from_json(json)
# print the JSON string representation of the object
print(CPSSummary.to_json())

# convert the object into a dict
cps_summary_dict = cps_summary_instance.to_dict()
# create an instance of CPSSummary from a dict
cps_summary_form_dict = cps_summary.from_dict(cps_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


