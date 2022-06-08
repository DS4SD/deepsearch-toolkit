# deepsearch.cps.apis.user.SettingsApi

All URIs are relative to *http://localhost/api/cps/user/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**global_permissions**](SettingsApi.md#global_permissions) | **GET** /permissions | 


# **global_permissions**
> dict(str, bool) global_permissions()



Get the global permissions for users.

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import deepsearch.cps.apis.user
from deepsearch.cps.apis.user.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/cps/user/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = deepsearch.cps.apis.user.Configuration(
    host = "http://localhost/api/cps/user/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = deepsearch.cps.apis.user.Configuration(
    host = "http://localhost/api/cps/user/v1",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with deepsearch.cps.apis.user.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deepsearch.cps.apis.user.SettingsApi(api_client)
    
    try:
        api_response = api_instance.global_permissions()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SettingsApi->global_permissions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, bool)**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

