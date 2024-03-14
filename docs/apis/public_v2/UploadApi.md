# deepsearch.cps.apis.public_v2.UploadApi

All URIs are relative to */api/cps/public/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_scratch_file**](UploadApi.md#create_project_scratch_file) | **POST** /project/{proj_key}/scratch/files/upload/{filename} | Create Project Scratch File
[**list_project_scratch_files**](UploadApi.md#list_project_scratch_files) | **GET** /project/{proj_key}/scratch/files | List Project Scratch Files
[**list_project_scratch_files_paginated**](UploadApi.md#list_project_scratch_files_paginated) | **GET** /project/{proj_key}/scratch/files_paginated | List Project Scratch Files Paginated


# **create_project_scratch_file**
> TemporaryUploadFileResult create_project_scratch_file(filename, proj_key)

Create Project Scratch File

Create file pointers for temporary storage.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.temporary_upload_file_result import TemporaryUploadFileResult
from deepsearch.cps.apis.public_v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/cps/public/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = deepsearch.cps.apis.public_v2.Configuration(
    host = "/api/cps/public/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with deepsearch.cps.apis.public_v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deepsearch.cps.apis.public_v2.UploadApi(api_client)
    filename = 'filename_example' # str | 
    proj_key = 'proj_key_example' # str | 

    try:
        # Create Project Scratch File
        api_response = api_instance.create_project_scratch_file(filename, proj_key)
        print("The response of UploadApi->create_project_scratch_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadApi->create_project_scratch_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**|  | 
 **proj_key** | **str**|  | 

### Return type

[**TemporaryUploadFileResult**](TemporaryUploadFileResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_scratch_files**
> List[ProjectScratchFiles] list_project_scratch_files(proj_key, scratch_ids=scratch_ids)

List Project Scratch Files

Get temporary files uploaded to a project.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.project_scratch_files import ProjectScratchFiles
from deepsearch.cps.apis.public_v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/cps/public/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = deepsearch.cps.apis.public_v2.Configuration(
    host = "/api/cps/public/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with deepsearch.cps.apis.public_v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deepsearch.cps.apis.public_v2.UploadApi(api_client)
    proj_key = 'proj_key_example' # str | 
    scratch_ids = 'scratch_ids_example' # str |  (optional)

    try:
        # List Project Scratch Files
        api_response = api_instance.list_project_scratch_files(proj_key, scratch_ids=scratch_ids)
        print("The response of UploadApi->list_project_scratch_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadApi->list_project_scratch_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **scratch_ids** | **str**|  | [optional] 

### Return type

[**List[ProjectScratchFiles]**](ProjectScratchFiles.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_scratch_files_paginated**
> ProjectScratchFilesPaginated list_project_scratch_files_paginated(proj_key, page=page, items_per_page=items_per_page, search_string=search_string, begin_date=begin_date, end_date=end_date)

List Project Scratch Files Paginated

Get paginated list of temporary files uploaded to a project.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.project_scratch_files_paginated import ProjectScratchFilesPaginated
from deepsearch.cps.apis.public_v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/cps/public/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = deepsearch.cps.apis.public_v2.Configuration(
    host = "/api/cps/public/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with deepsearch.cps.apis.public_v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deepsearch.cps.apis.public_v2.UploadApi(api_client)
    proj_key = 'proj_key_example' # str | 
    page = 56 # int |  (optional)
    items_per_page = 20 # int |  (optional) (default to 20)
    search_string = 'search_string_example' # str |  (optional)
    begin_date = 56 # int |  (optional)
    end_date = 56 # int |  (optional)

    try:
        # List Project Scratch Files Paginated
        api_response = api_instance.list_project_scratch_files_paginated(proj_key, page=page, items_per_page=items_per_page, search_string=search_string, begin_date=begin_date, end_date=end_date)
        print("The response of UploadApi->list_project_scratch_files_paginated:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadApi->list_project_scratch_files_paginated: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **page** | **int**|  | [optional] 
 **items_per_page** | **int**|  | [optional] [default to 20]
 **search_string** | **str**|  | [optional] 
 **begin_date** | **int**|  | [optional] 
 **end_date** | **int**|  | [optional] 

### Return type

[**ProjectScratchFilesPaginated**](ProjectScratchFilesPaginated.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

