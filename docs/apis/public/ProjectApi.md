# deepsearch.cps.apis.public.ProjectApi

All URIs are relative to *http://localhost/api/cps/public/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_project_default_values**](ProjectApi.md#get_project_default_values) | **GET** /project/{proj_key}/default_values | 
[**provision_project_packages**](ProjectApi.md#provision_project_packages) | **POST** /project/{proj_key}/packages | 
[**update_project_default_values**](ProjectApi.md#update_project_default_values) | **POST** /project/{proj_key}/default_values | 


# **get_project_default_values**
> ProjectDefaultValues get_project_default_values(proj_key)



List project's default values

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
    api_instance = deepsearch.cps.apis.public.ProjectApi(api_client)
    proj_key = 'proj_key_example' # str | 

    try:
        api_response = api_instance.get_project_default_values(proj_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->get_project_default_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 

### Return type

[**ProjectDefaultValues**](ProjectDefaultValues.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Error occured on the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **provision_project_packages**
> Task provision_project_packages(proj_key, body=body)



Install packages on a project

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
    api_instance = deepsearch.cps.apis.public.ProjectApi(api_client)
    proj_key = 'proj_key_example' # str | 
body = deepsearch.cps.apis.public.ProjectPackageInstalationManifest() # ProjectPackageInstalationManifest |  (optional)

    try:
        api_response = api_instance.provision_project_packages(proj_key, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->provision_project_packages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **body** | [**ProjectPackageInstalationManifest**](ProjectPackageInstalationManifest.md)|  | [optional] 

### Return type

[**Task**](Task.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task started. It can be found in the tasks endpoint for the project. |  -  |
**404** | Package not found. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_default_values**
> update_project_default_values(proj_key, default_values)



List project's default values

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
    api_instance = deepsearch.cps.apis.public.ProjectApi(api_client)
    proj_key = 'proj_key_example' # str | 
default_values = deepsearch.cps.apis.public.ProjectDefaultValues() # ProjectDefaultValues | 

    try:
        api_instance.update_project_default_values(proj_key, default_values)
    except ApiException as e:
        print("Exception when calling ProjectApi->update_project_default_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **default_values** | [**ProjectDefaultValues**](ProjectDefaultValues.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Error occured on the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

