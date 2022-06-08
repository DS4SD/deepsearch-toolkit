# deepsearch.cps.apis.user.UsersApi

All URIs are relative to *http://localhost/api/cps/user/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_key_get**](UsersApi.md#api_key_get) | **GET** /user/api_key | 
[**get_access_token**](UsersApi.md#get_access_token) | **POST** /user/token | 
[**get_current_user_details**](UsersApi.md#get_current_user_details) | **GET** /user/current | 
[**impersonate_user_token**](UsersApi.md#impersonate_user_token) | **POST** /user/impersonate | 
[**search**](UsersApi.md#search) | **GET** /user/search | 
[**service_accounts_create**](UsersApi.md#service_accounts_create) | **POST** /user/service_accounts | 
[**service_accounts_list**](UsersApi.md#service_accounts_list) | **GET** /user/service_accounts | 


# **api_key_get**
> ApiKey api_key_get()



Show the API Key for your user

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
    api_instance = deepsearch.cps.apis.user.UsersApi(api_client)
    
    try:
        api_response = api_instance.api_key_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->api_key_get: %s\n" % e)
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

# **get_access_token**
> AccessToken get_access_token(options=options)



Request a user API token

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

# Configure HTTP basic authorization: UserAPIKey
configuration = deepsearch.cps.apis.user.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with deepsearch.cps.apis.user.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deepsearch.cps.apis.user.UsersApi(api_client)
    options = deepsearch.cps.apis.user.GetAccessTokenRequestBody() # GetAccessTokenRequestBody |  (optional)

    try:
        api_response = api_instance.get_access_token(options=options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->get_access_token: %s\n" % e)
```

* Basic Authentication (UserAPIKey):
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

# Configure HTTP basic authorization: UserAPIKey
configuration = deepsearch.cps.apis.user.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with deepsearch.cps.apis.user.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deepsearch.cps.apis.user.UsersApi(api_client)
    options = deepsearch.cps.apis.user.GetAccessTokenRequestBody() # GetAccessTokenRequestBody |  (optional)

    try:
        api_response = api_instance.get_access_token(options=options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->get_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**GetAccessTokenRequestBody**](GetAccessTokenRequestBody.md)|  | [optional] 

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

[Bearer](../README.md#Bearer), [UserAPIKey](../README.md#UserAPIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user_details**
> UserDetails get_current_user_details()



Gets the current user's details.

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
    api_instance = deepsearch.cps.apis.user.UsersApi(api_client)
    
    try:
        api_response = api_instance.get_current_user_details()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->get_current_user_details: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserDetails**](UserDetails.md)

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

# **impersonate_user_token**
> TokenResponse impersonate_user_token(body)



Request an impersonate user token.

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

# Configure HTTP basic authorization: UserAPIKey
configuration = deepsearch.cps.apis.user.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with deepsearch.cps.apis.user.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deepsearch.cps.apis.user.UsersApi(api_client)
    body = deepsearch.cps.apis.user.ImpersonateUserTokenRequestBody() # ImpersonateUserTokenRequestBody | 

    try:
        api_response = api_instance.impersonate_user_token(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->impersonate_user_token: %s\n" % e)
```

* Basic Authentication (UserAPIKey):
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

# Configure HTTP basic authorization: UserAPIKey
configuration = deepsearch.cps.apis.user.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with deepsearch.cps.apis.user.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deepsearch.cps.apis.user.UsersApi(api_client)
    body = deepsearch.cps.apis.user.ImpersonateUserTokenRequestBody() # ImpersonateUserTokenRequestBody | 

    try:
        api_response = api_instance.impersonate_user_token(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->impersonate_user_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImpersonateUserTokenRequestBody**](ImpersonateUserTokenRequestBody.md)|  | 

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

[Bearer](../README.md#Bearer), [UserAPIKey](../README.md#UserAPIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized. |  -  |
**403** | The user that&#39;s performing this operation does not have permission or the impersonate secret isn&#39;t valid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> list[UserDetails] search(term)



Search for users matching the email or name. Depending on the user's permissions, only owners and assignees from their projects may be shown.

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
    api_instance = deepsearch.cps.apis.user.UsersApi(api_client)
    term = 'term_example' # str | Search term

    try:
        api_response = api_instance.search(term)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**| Search term | 

### Return type

[**list[UserDetails]**](UserDetails.md)

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

# **service_accounts_create**
> ServiceAccount service_accounts_create()



Create a new service accounts for your user

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
    api_instance = deepsearch.cps.apis.user.UsersApi(api_client)
    
    try:
        api_response = api_instance.service_accounts_create()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->service_accounts_create: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ServiceAccount**](ServiceAccount.md)

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

# **service_accounts_list**
> list[ServiceAccount] service_accounts_list()



List all service accounts of your user

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
    api_instance = deepsearch.cps.apis.user.UsersApi(api_client)
    
    try:
        api_response = api_instance.service_accounts_list()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->service_accounts_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ServiceAccount]**](ServiceAccount.md)

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

