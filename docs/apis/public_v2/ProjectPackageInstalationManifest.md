# ProjectPackageInstalationManifest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**packages** | [**List[Package]**](Package.md) |  | 

## Example

```python
from deepsearch.cps.apis.public_v2.models.project_package_instalation_manifest import ProjectPackageInstalationManifest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectPackageInstalationManifest from a JSON string
project_package_instalation_manifest_instance = ProjectPackageInstalationManifest.from_json(json)
# print the JSON string representation of the object
print(ProjectPackageInstalationManifest.to_json())

# convert the object into a dict
project_package_instalation_manifest_dict = project_package_instalation_manifest_instance.to_dict()
# create an instance of ProjectPackageInstalationManifest from a dict
project_package_instalation_manifest_form_dict = project_package_instalation_manifest.from_dict(project_package_instalation_manifest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


