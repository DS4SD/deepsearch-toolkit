# deepsearch.cps.apis.public_v2.SystemQuotasApi

All URIs are relative to */api/cps/public/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_flavours_default_quotas**](SystemQuotasApi.md#get_flavours_default_quotas) | **GET** /system/admin/get_flavours_default_quota | Get Flavours Default Quotas
[**get_project_flavour_total_kgs**](SystemQuotasApi.md#get_project_flavour_total_kgs) | **GET** /system/admin/get_project_flavour_total_kgs/{proj_key}/{flavour_name} | Get Project Flavour Total Kgs
[**get_project_flavours_quota**](SystemQuotasApi.md#get_project_flavours_quota) | **GET** /system/admin/get_project_flavours_quota/{proj_key} | Get Project Flavours Quota
[**get_projects_flavours_quota**](SystemQuotasApi.md#get_projects_flavours_quota) | **GET** /system/admin/get_projects_flavours_quota | Get Projects Flavours Quota
[**save_flavours_default_quotas**](SystemQuotasApi.md#save_flavours_default_quotas) | **PUT** /system/admin/save_flavours_default_quota | Save Flavours Default Quotas
[**save_project_flavours_quota**](SystemQuotasApi.md#save_project_flavours_quota) | **PUT** /system/admin/save_project_flavours_quota | Save Project Flavours Quota


# **get_flavours_default_quotas**
> List[FlavoursDefaultQuota] get_flavours_default_quotas()

Get Flavours Default Quotas

Get flavours default values.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.flavours_default_quota import FlavoursDefaultQuota
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
    api_instance = deepsearch.cps.apis.public_v2.SystemQuotasApi(api_client)

    try:
        # Get Flavours Default Quotas
        api_response = api_instance.get_flavours_default_quotas()
        print("The response of SystemQuotasApi->get_flavours_default_quotas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemQuotasApi->get_flavours_default_quotas: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FlavoursDefaultQuota]**](FlavoursDefaultQuota.md)

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

# **get_project_flavour_total_kgs**
> ProjectFlavourTotalKgs get_project_flavour_total_kgs(flavour_name, proj_key)

Get Project Flavour Total Kgs

Gets kg total number by proj_key and flavour_key.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.project_flavour_total_kgs import ProjectFlavourTotalKgs
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
    api_instance = deepsearch.cps.apis.public_v2.SystemQuotasApi(api_client)
    flavour_name = 'flavour_name_example' # str | 
    proj_key = 'proj_key_example' # str | 

    try:
        # Get Project Flavour Total Kgs
        api_response = api_instance.get_project_flavour_total_kgs(flavour_name, proj_key)
        print("The response of SystemQuotasApi->get_project_flavour_total_kgs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemQuotasApi->get_project_flavour_total_kgs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flavour_name** | **str**|  | 
 **proj_key** | **str**|  | 

### Return type

[**ProjectFlavourTotalKgs**](ProjectFlavourTotalKgs.md)

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

# **get_project_flavours_quota**
> List[FlavoursQuota] get_project_flavours_quota(proj_key)

Get Project Flavours Quota

Get project flavours quota.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.flavours_quota import FlavoursQuota
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
    api_instance = deepsearch.cps.apis.public_v2.SystemQuotasApi(api_client)
    proj_key = 'proj_key_example' # str | 

    try:
        # Get Project Flavours Quota
        api_response = api_instance.get_project_flavours_quota(proj_key)
        print("The response of SystemQuotasApi->get_project_flavours_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemQuotasApi->get_project_flavours_quota: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 

### Return type

[**List[FlavoursQuota]**](FlavoursQuota.md)

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

# **get_projects_flavours_quota**
> List[ProjectFlavoursQuota] get_projects_flavours_quota()

Get Projects Flavours Quota

Get projects flavours quotas.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.project_flavours_quota import ProjectFlavoursQuota
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
    api_instance = deepsearch.cps.apis.public_v2.SystemQuotasApi(api_client)

    try:
        # Get Projects Flavours Quota
        api_response = api_instance.get_projects_flavours_quota()
        print("The response of SystemQuotasApi->get_projects_flavours_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemQuotasApi->get_projects_flavours_quota: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ProjectFlavoursQuota]**](ProjectFlavoursQuota.md)

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

# **save_flavours_default_quotas**
> List[FlavoursDefaultQuota] save_flavours_default_quotas(flavours_default_quota)

Save Flavours Default Quotas

Save flavours default quota.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.flavours_default_quota import FlavoursDefaultQuota
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
    api_instance = deepsearch.cps.apis.public_v2.SystemQuotasApi(api_client)
    flavours_default_quota = [deepsearch.cps.apis.public_v2.FlavoursDefaultQuota()] # List[FlavoursDefaultQuota] | 

    try:
        # Save Flavours Default Quotas
        api_response = api_instance.save_flavours_default_quotas(flavours_default_quota)
        print("The response of SystemQuotasApi->save_flavours_default_quotas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemQuotasApi->save_flavours_default_quotas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flavours_default_quota** | [**List[FlavoursDefaultQuota]**](FlavoursDefaultQuota.md)|  | 

### Return type

[**List[FlavoursDefaultQuota]**](FlavoursDefaultQuota.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_project_flavours_quota**
> object save_project_flavours_quota(project_flavours_quota)

Save Project Flavours Quota

Save project flavours quota.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.project_flavours_quota import ProjectFlavoursQuota
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
    api_instance = deepsearch.cps.apis.public_v2.SystemQuotasApi(api_client)
    project_flavours_quota = deepsearch.cps.apis.public_v2.ProjectFlavoursQuota() # ProjectFlavoursQuota | 

    try:
        # Save Project Flavours Quota
        api_response = api_instance.save_project_flavours_quota(project_flavours_quota)
        print("The response of SystemQuotasApi->save_project_flavours_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemQuotasApi->save_project_flavours_quota: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_flavours_quota** | [**ProjectFlavoursQuota**](ProjectFlavoursQuota.md)|  | 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

