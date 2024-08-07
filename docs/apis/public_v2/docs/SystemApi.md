# deepsearch.cps.apis.public_v2.SystemApi

All URIs are relative to */api/cps/public/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_system_information**](SystemApi.md#get_system_information) | **GET** /system/info | Get System Information
[**get_system_modules_configuration**](SystemApi.md#get_system_modules_configuration) | **GET** /system/modules/configuration | Get System Modules Configuration
[**get_system_modules_tasks**](SystemApi.md#get_system_modules_tasks) | **GET** /system/modules/tasks | Get System Modules Tasks
[**list_packages**](SystemApi.md#list_packages) | **GET** /system/packages | List Packages
[**list_system_knowledge_graphs**](SystemApi.md#list_system_knowledge_graphs) | **GET** /system/kgs | List System Knowledge Graphs
[**system_get_all_dcs_admin**](SystemApi.md#system_get_all_dcs_admin) | **GET** /system/admin/get_all_dcs | System Get All Dcs Admin
[**system_get_all_kgs_admin**](SystemApi.md#system_get_all_kgs_admin) | **GET** /system/admin/get_all_kgs | System Get All Kgs Admin


# **get_system_information**
> SystemInfo get_system_information()

Get System Information

Get system info.

### Example


```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.system_info import SystemInfo
from deepsearch.cps.apis.public_v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/cps/public/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = deepsearch.cps.apis.public_v2.Configuration(
    host = "/api/cps/public/v2"
)


# Enter a context with an instance of the API client
with deepsearch.cps.apis.public_v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deepsearch.cps.apis.public_v2.SystemApi(api_client)

    try:
        # Get System Information
        api_response = api_instance.get_system_information()
        print("The response of SystemApi->get_system_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->get_system_information: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SystemInfo**](SystemInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_modules_configuration**
> ModulesConfig get_system_modules_configuration()

Get System Modules Configuration

Get modules configuration.

### Example


```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.modules_config import ModulesConfig
from deepsearch.cps.apis.public_v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/cps/public/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = deepsearch.cps.apis.public_v2.Configuration(
    host = "/api/cps/public/v2"
)


# Enter a context with an instance of the API client
with deepsearch.cps.apis.public_v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deepsearch.cps.apis.public_v2.SystemApi(api_client)

    try:
        # Get System Modules Configuration
        api_response = api_instance.get_system_modules_configuration()
        print("The response of SystemApi->get_system_modules_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->get_system_modules_configuration: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ModulesConfig**](ModulesConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_modules_tasks**
> object get_system_modules_tasks()

Get System Modules Tasks

Get modules configuration.

### Example


```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/cps/public/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = deepsearch.cps.apis.public_v2.Configuration(
    host = "/api/cps/public/v2"
)


# Enter a context with an instance of the API client
with deepsearch.cps.apis.public_v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deepsearch.cps.apis.public_v2.SystemApi(api_client)

    try:
        # Get System Modules Tasks
        api_response = api_instance.get_system_modules_tasks()
        print("The response of SystemApi->get_system_modules_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->get_system_modules_tasks: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_packages**
> List[CPSPackage] list_packages()

List Packages

Get packages available in this CPS installation for installing in a project.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.cps_package import CPSPackage
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
    api_instance = deepsearch.cps.apis.public_v2.SystemApi(api_client)

    try:
        # List Packages
        api_response = api_instance.list_packages()
        print("The response of SystemApi->list_packages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->list_packages: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CPSPackage]**](CPSPackage.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_system_knowledge_graphs**
> List[object] list_system_knowledge_graphs(proj_key=proj_key, term=term)

List System Knowledge Graphs

List all Knowledge Graphs in the system.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
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
    api_instance = deepsearch.cps.apis.public_v2.SystemApi(api_client)
    proj_key = 'proj_key_example' # str |  (optional)
    term = 'term_example' # str |  (optional)

    try:
        # List System Knowledge Graphs
        api_response = api_instance.list_system_knowledge_graphs(proj_key=proj_key, term=term)
        print("The response of SystemApi->list_system_knowledge_graphs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->list_system_knowledge_graphs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | [optional] 
 **term** | **str**|  | [optional] 

### Return type

**List[object]**

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

# **system_get_all_dcs_admin**
> List[str] system_get_all_dcs_admin()

System Get All Dcs Admin

Get all data catalogs (only dc_key) for admin use.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
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
    api_instance = deepsearch.cps.apis.public_v2.SystemApi(api_client)

    try:
        # System Get All Dcs Admin
        api_response = api_instance.system_get_all_dcs_admin()
        print("The response of SystemApi->system_get_all_dcs_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->system_get_all_dcs_admin: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_get_all_kgs_admin**
> List[object] system_get_all_kgs_admin()

System Get All Kgs Admin

Get all kgs (only bag_key) for admin use.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
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
    api_instance = deepsearch.cps.apis.public_v2.SystemApi(api_client)

    try:
        # System Get All Kgs Admin
        api_response = api_instance.system_get_all_kgs_admin()
        print("The response of SystemApi->system_get_all_kgs_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->system_get_all_kgs_admin: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

