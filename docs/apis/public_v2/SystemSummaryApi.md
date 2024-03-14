# deepsearch.cps.apis.public_v2.SystemSummaryApi

All URIs are relative to */api/cps/public/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_get_cps_summary**](SystemSummaryApi.md#system_get_cps_summary) | **GET** /system/admin/summary | System Get Cps Summary
[**system_get_dc_storage_summary_async**](SystemSummaryApi.md#system_get_dc_storage_summary_async) | **GET** /system/admin/dc_storage_summary/{dc_key} | System Get Dc Storage Summary Async
[**system_get_kg_storage_summary_async**](SystemSummaryApi.md#system_get_kg_storage_summary_async) | **GET** /system/admin/kg_storage_summary/{kg_key} | System Get Kg Storage Summary Async


# **system_get_cps_summary**
> List[CPSSummary] system_get_cps_summary()

System Get Cps Summary

Get cps summary data.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.cps_summary import CPSSummary
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
    api_instance = deepsearch.cps.apis.public_v2.SystemSummaryApi(api_client)

    try:
        # System Get Cps Summary
        api_response = api_instance.system_get_cps_summary()
        print("The response of SystemSummaryApi->system_get_cps_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSummaryApi->system_get_cps_summary: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CPSSummary]**](CPSSummary.md)

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

# **system_get_dc_storage_summary_async**
> StorageSummaryTask system_get_dc_storage_summary_async(dc_key)

System Get Dc Storage Summary Async

Get data catalog storage summary.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.storage_summary_task import StorageSummaryTask
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
    api_instance = deepsearch.cps.apis.public_v2.SystemSummaryApi(api_client)
    dc_key = 'dc_key_example' # str | 

    try:
        # System Get Dc Storage Summary Async
        api_response = api_instance.system_get_dc_storage_summary_async(dc_key)
        print("The response of SystemSummaryApi->system_get_dc_storage_summary_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSummaryApi->system_get_dc_storage_summary_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dc_key** | **str**|  | 

### Return type

[**StorageSummaryTask**](StorageSummaryTask.md)

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

# **system_get_kg_storage_summary_async**
> StorageSummaryTask system_get_kg_storage_summary_async(kg_key)

System Get Kg Storage Summary Async

Get knowledge graph storage summary.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.storage_summary_task import StorageSummaryTask
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
    api_instance = deepsearch.cps.apis.public_v2.SystemSummaryApi(api_client)
    kg_key = 'kg_key_example' # str | 

    try:
        # System Get Kg Storage Summary Async
        api_response = api_instance.system_get_kg_storage_summary_async(kg_key)
        print("The response of SystemSummaryApi->system_get_kg_storage_summary_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemSummaryApi->system_get_kg_storage_summary_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kg_key** | **str**|  | 

### Return type

[**StorageSummaryTask**](StorageSummaryTask.md)

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

