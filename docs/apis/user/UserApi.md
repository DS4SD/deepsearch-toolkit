# deepsearch.cps.apis.user.UserApi

All URIs are relative to *http://localhost/api/cps/user/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_key_create**](UserApi.md#api_key_create) | **POST** /user/api_key | 


# **api_key_create**
> ApiKey api_key_create()



Create an API Key for your user

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
    api_instance = deepsearch.cps.apis.user.UserApi(api_client)
    
    try:
        api_response = api_instance.api_key_create()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->api_key_create: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

