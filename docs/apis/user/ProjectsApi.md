# deepsearch.cps.apis.user.ProjectsApi

All URIs are relative to *http://localhost/api/cps/user/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user**](ProjectsApi.md#add_user) | **POST** /projects/{proj_key}/users | 
[**create**](ProjectsApi.md#create) | **POST** /projects | 
[**delete**](ProjectsApi.md#delete) | **DELETE** /projects/{proj_key} | 
[**details**](ProjectsApi.md#details) | **GET** /projects/{proj_key} | 
[**edit_user**](ProjectsApi.md#edit_user) | **PUT** /projects/{proj_key}/users | 
[**get_delete_confirmation_token**](ProjectsApi.md#get_delete_confirmation_token) | **GET** /projects/{proj_key}/delete | 
[**get_project_token**](ProjectsApi.md#get_project_token) | **GET** /projects/{proj_key}/token | 
[**is_authorized**](ProjectsApi.md#is_authorized) | **GET** /projects/{proj_key}/is_authorized | 
[**list_audits_in_project**](ProjectsApi.md#list_audits_in_project) | **GET** /projects/{proj_key}/audits | 
[**list_projects**](ProjectsApi.md#list_projects) | **GET** /projects | 
[**list_users**](ProjectsApi.md#list_users) | **GET** /projects/{proj_key}/users | 
[**remove_user**](ProjectsApi.md#remove_user) | **DELETE** /projects/{proj_key}/users/{username} | 


# **add_user**
> SuccessMessage add_user(proj_key, data)



Assign a new user to a project

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
    api_instance = deepsearch.cps.apis.user.ProjectsApi(api_client)
    proj_key = 'proj_key_example' # str | The project key
data = deepsearch.cps.apis.user.ProjectUserAssignment() # ProjectUserAssignment | 

    try:
        api_response = api_instance.add_user(proj_key, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->add_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key | 
 **data** | [**ProjectUserAssignment**](ProjectUserAssignment.md)|  | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User assigned to project. |  -  |
**400** | Invalid new_user_type. |  -  |
**403** | The user that&#39;s performing this operation does not have permission to assign the user. |  -  |
**404** | User that&#39;s going to be assigned doesn&#39;t exist, or the project doesn&#39;t exist. |  -  |
**409** | Reassigning the user would leave the project in an invalid state. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> Project create(data)



Create a new project

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
    api_instance = deepsearch.cps.apis.user.ProjectsApi(api_client)
    data = deepsearch.cps.apis.user.CreateProjectRequestBody() # CreateProjectRequestBody | 

    try:
        api_response = api_instance.create(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**CreateProjectRequestBody**](CreateProjectRequestBody.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New project details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(proj_key, confirmation_token)



Delete a project.

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
    api_instance = deepsearch.cps.apis.user.ProjectsApi(api_client)
    proj_key = 'proj_key_example' # str | The project key
confirmation_token = 'confirmation_token_example' # str | The delete confirmation token

    try:
        api_instance.delete(proj_key, confirmation_token)
    except ApiException as e:
        print("Exception when calling ProjectsApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key | 
 **confirmation_token** | **str**| The delete confirmation token | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Project deleted successfully. |  -  |
**403** | The user that is executing this operation is not an owner of the project. |  -  |
**404** | Project not found. |  -  |
**409** | User not assigned to project. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **details**
> Project details(proj_key)



Returns the details of the project

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
    api_instance = deepsearch.cps.apis.user.ProjectsApi(api_client)
    proj_key = 'proj_key_example' # str | The project key

    try:
        api_response = api_instance.details(proj_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key | 

### Return type

[**Project**](Project.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized. |  -  |
**404** | Project does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_user**
> SuccessMessage edit_user(proj_key, data)



Assign a new user to a project

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
    api_instance = deepsearch.cps.apis.user.ProjectsApi(api_client)
    proj_key = 'proj_key_example' # str | The project key
data = deepsearch.cps.apis.user.ProjectUserAssignment() # ProjectUserAssignment | 

    try:
        api_response = api_instance.edit_user(proj_key, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->edit_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key | 
 **data** | [**ProjectUserAssignment**](ProjectUserAssignment.md)|  | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User assigned to project. |  -  |
**400** | Invalid new_user_type. |  -  |
**403** | The user that&#39;s performing this operation does not have permission to assign the user. |  -  |
**404** | User that&#39;s going to be assigned doesn&#39;t exist, or the project doesn&#39;t exist. |  -  |
**409** | Reassigning the user would leave the project in an invalid state. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delete_confirmation_token**
> TokenResponse get_delete_confirmation_token(proj_key)



Get a delete confirmation token for the provided project.

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
    api_instance = deepsearch.cps.apis.user.ProjectsApi(api_client)
    proj_key = 'proj_key_example' # str | The project key

    try:
        api_response = api_instance.get_delete_confirmation_token(proj_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_delete_confirmation_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key | 

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Confirmation token. |  -  |
**403** | The user that is executing this operation is not an owner of the project. |  -  |
**404** | Project not found. |  -  |
**409** | User not assigned to project. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_token**
> AccessToken get_project_token(proj_key)



Request a token granting access to the current project

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
    api_instance = deepsearch.cps.apis.user.ProjectsApi(api_client)
    proj_key = 'proj_key_example' # str | The project key

    try:
        api_response = api_instance.get_project_token(proj_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_project_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key | 

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized. |  -  |
**404** | Project does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_authorized**
> SuccessMessage is_authorized(proj_key, role=role)



Provide user-key and project-key to coordinates a project

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
    api_instance = deepsearch.cps.apis.user.ProjectsApi(api_client)
    proj_key = 'proj_key_example' # str | The project key
role = 'role_example' # str | The specific role to probe (optional)

    try:
        api_response = api_instance.is_authorized(proj_key, role=role)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->is_authorized: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key | 
 **role** | **str**| The specific role to probe | [optional] 

### Return type

[**SuccessMessage**](SuccessMessage.md)

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
**404** | Project does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_audits_in_project**
> InlineResponse200 list_audits_in_project(proj_key, user_key=user_key, type_=type_, search_term=search_term, before=before, after=after, limit=limit)



List audits related to the project

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
    api_instance = deepsearch.cps.apis.user.ProjectsApi(api_client)
    proj_key = 'proj_key_example' # str | The project key
user_key = 'user_key_example' # str |  (optional)
type_ = 'type__example' # str |  (optional)
search_term = 'search_term_example' # str |  (optional)
before = 'before_example' # str |  (optional)
after = 'after_example' # str |  (optional)
limit = 50 # int |  (optional) (default to 50)

    try:
        api_response = api_instance.list_audits_in_project(proj_key, user_key=user_key, type_=type_, search_term=search_term, before=before, after=after, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->list_audits_in_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key | 
 **user_key** | **str**|  | [optional] 
 **type_** | **str**|  | [optional] 
 **search_term** | **str**|  | [optional] 
 **before** | **str**|  | [optional] 
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized. |  -  |
**404** | Project does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_projects**
> list[Project] list_projects(role=role, include_collaborators=include_collaborators)



List all projects assigned to a user

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
    api_instance = deepsearch.cps.apis.user.ProjectsApi(api_client)
    role = 'role_example' # str | filter for the user role (optional)
include_collaborators = True # bool |  (optional) (default to True)

    try:
        api_response = api_instance.list_projects(role=role, include_collaborators=include_collaborators)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->list_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| filter for the user role | [optional] 
 **include_collaborators** | **bool**|  | [optional] [default to True]

### Return type

[**list[Project]**](Project.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Project does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> dict(str, list[UserDetails]) list_users(proj_key)



List all users belonging to a project

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
    api_instance = deepsearch.cps.apis.user.ProjectsApi(api_client)
    proj_key = 'proj_key_example' # str | The project key

    try:
        api_response = api_instance.list_users(proj_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->list_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key | 

### Return type

**dict(str, list[UserDetails])**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized. |  -  |
**404** | User does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user**
> remove_user(proj_key, username)



Delete an user from a project.

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
    api_instance = deepsearch.cps.apis.user.ProjectsApi(api_client)
    proj_key = 'proj_key_example' # str | The project key
username = 'username_example' # str | The username for the user

    try:
        api_instance.remove_user(proj_key, username)
    except ApiException as e:
        print("Exception when calling ProjectsApi->remove_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key | 
 **username** | **str**| The username for the user | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | User deleted from project successfully. |  -  |
**403** | The user that is executing this operation is not an owner of the project. |  -  |
**404** | Project or user not found. |  -  |
**409** | User not assigned to project, or the project only has one owner left. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

