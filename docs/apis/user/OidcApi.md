# deepsearch.cps.apis.user.OidcApi

All URIs are relative to *http://localhost/api/cps/user/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate**](OidcApi.md#authenticate) | **GET** /oidc/authenticate | 
[**create_tokens**](OidcApi.md#create_tokens) | **POST** /oidc/token | 
[**register_user**](OidcApi.md#register_user) | **POST** /oidc/register_user | 
[**token**](OidcApi.md#token) | **GET** /oidc/token | 


# **authenticate**
> authenticate()



Redirect to the OIDC authenticate endpoint.

### Example

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


# Enter a context with an instance of the API client
with deepsearch.cps.apis.user.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = deepsearch.cps.apis.user.OidcApi(api_client)
    
    try:
        api_instance.authenticate()
    except ApiException as e:
        print("Exception when calling OidcApi->authenticate: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Redirect to the OIDC authenticate endpoint |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tokens**
> OidcTokenResponse create_tokens(body=body)



Retrieve the user access and identity tokens using either the code or the refresh_token.

### Example

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


# Enter a context with an instance of the API client
with deepsearch.cps.apis.user.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = deepsearch.cps.apis.user.OidcApi(api_client)
    body = deepsearch.cps.apis.user.CreateTokensRequestBody() # CreateTokensRequestBody |  (optional)

    try:
        api_response = api_instance.create_tokens(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OidcApi->create_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTokensRequestBody**](CreateTokensRequestBody.md)|  | [optional] 

### Return type

[**OidcTokenResponse**](OidcTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_user**
> UserDetails register_user(data)



Register a new user, provided a valid access_token and id_token from the oidc provider.

### Example

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


# Enter a context with an instance of the API client
with deepsearch.cps.apis.user.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = deepsearch.cps.apis.user.OidcApi(api_client)
    data = deepsearch.cps.apis.user.RegisterUserRequestBody() # RegisterUserRequestBody | 

    try:
        api_response = api_instance.register_user(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OidcApi->register_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**RegisterUserRequestBody**](RegisterUserRequestBody.md)|  | 

### Return type

[**UserDetails**](UserDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token**
> OidcTokenResponse token(code=code, refresh_token=refresh_token)



Retrieve the user access and identity tokens using either the code or the refresh_token.

### Example

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


# Enter a context with an instance of the API client
with deepsearch.cps.apis.user.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = deepsearch.cps.apis.user.OidcApi(api_client)
    code = 'code_example' # str | The oidc code response (optional)
refresh_token = 'refresh_token_example' # str | The oidc code response (optional)

    try:
        api_response = api_instance.token(code=code, refresh_token=refresh_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OidcApi->token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The oidc code response | [optional] 
 **refresh_token** | **str**| The oidc code response | [optional] 

### Return type

[**OidcTokenResponse**](OidcTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

