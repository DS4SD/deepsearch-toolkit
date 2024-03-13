# ProjectScratchFiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**proj_key** | **str** |  | 
**user_key** | **str** |  | 
**filename** | **str** |  | 
**timestamp** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.project_scratch_files import ProjectScratchFiles

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectScratchFiles from a JSON string
project_scratch_files_instance = ProjectScratchFiles.from_json(json)
# print the JSON string representation of the object
print(ProjectScratchFiles.to_json())

# convert the object into a dict
project_scratch_files_dict = project_scratch_files_instance.to_dict()
# create an instance of ProjectScratchFiles from a dict
project_scratch_files_form_dict = project_scratch_files.from_dict(project_scratch_files_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


