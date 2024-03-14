# ProjectScratchFilesPaginated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**List[ProjectScratchFiles]**](ProjectScratchFiles.md) |  | 
**count** | **int** |  | 
**page** | **int** |  | 
**items_per_page** | **int** |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.project_scratch_files_paginated import ProjectScratchFilesPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectScratchFilesPaginated from a JSON string
project_scratch_files_paginated_instance = ProjectScratchFilesPaginated.from_json(json)
# print the JSON string representation of the object
print(ProjectScratchFilesPaginated.to_json())

# convert the object into a dict
project_scratch_files_paginated_dict = project_scratch_files_paginated_instance.to_dict()
# create an instance of ProjectScratchFilesPaginated from a dict
project_scratch_files_paginated_form_dict = project_scratch_files_paginated.from_dict(project_scratch_files_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


