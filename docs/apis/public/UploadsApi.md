# deepsearch.cps.apis.public.UploadsApi

All URIs are relative to *http://localhost/api/cps/public/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_scratch_file**](UploadsApi.md#create_project_scratch_file) | **POST** /project/{proj_key}/scratch/files/upload/{filename} | 
[**list_project_scratch_files**](UploadsApi.md#list_project_scratch_files) | **GET** /project/{proj_key}/scratch/files | 
[**list_project_scratch_files_paginated**](UploadsApi.md#list_project_scratch_files_paginated) | **GET** /project/{proj_key}/scratch/files_paginated | 
[**upload_project_scratch_file**](UploadsApi.md#upload_project_scratch_file) | **POST** /project/{proj_key}/scratch/files | 


# **create_project_scratch_file**
> TemporaryUploadFileResult create_project_scratch_file(proj_key, filename)



Create file pointers for temporary storage

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import deepsearch.cps.apis.public
from deepsearch.cps.apis.public.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/cps/public/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = deepsearch.cps.apis.public.Configuration(
    host = "http://localhost/api/cps/public/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = deepsearch.cps.apis.public.Configuration(
    host = "http://localhost/api/cps/public/v1",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with deepsearch.cps.apis.public.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deepsearch.cps.apis.public.UploadsApi(api_client)
    proj_key = 'proj_key_example' # str | 
filename = 'filename_example' # str | 

    try:
        api_response = api_instance.create_project_scratch_file(proj_key, filename)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UploadsApi->create_project_scratch_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **filename** | **str**|  | 

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
**201** | Temporary file details |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_scratch_files**
> list[UploadedFile] list_project_scratch_files(proj_key, scratch_ids=scratch_ids)



Get temporary files uploaded to a project

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import deepsearch.cps.apis.public
from deepsearch.cps.apis.public.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/cps/public/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = deepsearch.cps.apis.public.Configuration(
    host = "http://localhost/api/cps/public/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = deepsearch.cps.apis.public.Configuration(
    host = "http://localhost/api/cps/public/v1",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with deepsearch.cps.apis.public.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deepsearch.cps.apis.public.UploadsApi(api_client)
    proj_key = 'proj_key_example' # str | 
scratch_ids = 'scratch_ids_example' # str |  (optional)

    try:
        api_response = api_instance.list_project_scratch_files(proj_key, scratch_ids=scratch_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UploadsApi->list_project_scratch_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **scratch_ids** | **str**|  | [optional] 

### Return type

[**list[UploadedFile]**](UploadedFile.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Files |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_scratch_files_paginated**
> list[UploadedFile] list_project_scratch_files_paginated(proj_key, page=page, items_per_page=items_per_page, search_string=search_string, begin_date=begin_date, end_date=end_date)



Get paginated list of temporary files uploaded to a project

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import deepsearch.cps.apis.public
from deepsearch.cps.apis.public.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/cps/public/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = deepsearch.cps.apis.public.Configuration(
    host = "http://localhost/api/cps/public/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = deepsearch.cps.apis.public.Configuration(
    host = "http://localhost/api/cps/public/v1",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with deepsearch.cps.apis.public.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deepsearch.cps.apis.public.UploadsApi(api_client)
    proj_key = 'proj_key_example' # str | 
page = 56 # int | page of the result list (optional)
items_per_page = 20 # int | items on one page of the result list (optional) (default to 20)
search_string = 'search_string_example' # str | search keyword (optional)
begin_date = 56 # int | begin date of the search date interval (optional)
end_date = 56 # int | end date of the search date interval (optional)

    try:
        api_response = api_instance.list_project_scratch_files_paginated(proj_key, page=page, items_per_page=items_per_page, search_string=search_string, begin_date=begin_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UploadsApi->list_project_scratch_files_paginated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **page** | **int**| page of the result list | [optional] 
 **items_per_page** | **int**| items on one page of the result list | [optional] [default to 20]
 **search_string** | **str**| search keyword | [optional] 
 **begin_date** | **int**| begin date of the search date interval | [optional] 
 **end_date** | **int**| end date of the search date interval | [optional] 

### Return type

[**list[UploadedFile]**](UploadedFile.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Files |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_project_scratch_file**
> UploadedFileResult upload_project_scratch_file(proj_key, file)



Upload a file to temporary storage

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import deepsearch.cps.apis.public
from deepsearch.cps.apis.public.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/cps/public/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = deepsearch.cps.apis.public.Configuration(
    host = "http://localhost/api/cps/public/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = deepsearch.cps.apis.public.Configuration(
    host = "http://localhost/api/cps/public/v1",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with deepsearch.cps.apis.public.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deepsearch.cps.apis.public.UploadsApi(api_client)
    proj_key = 'proj_key_example' # str | 
file = '/path/to/file' # file | 

    try:
        api_response = api_instance.upload_project_scratch_file(proj_key, file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UploadsApi->upload_project_scratch_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **file** | **file**|  | 

### Return type

[**UploadedFileResult**](UploadedFileResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File uploaded |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

