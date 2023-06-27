# deepsearch.cps.apis.user.AdminApi

All URIs are relative to *http://localhost/api/cps/user/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_add_user**](AdminApi.md#admin_add_user) | **POST** /admin/projects/{proj_key}/users | 
[**admin_list_users**](AdminApi.md#admin_list_users) | **GET** /admin/projects/{proj_key}/users | 
[**admin_remove_user**](AdminApi.md#admin_remove_user) | **DELETE** /admin/projects/{proj_key}/users/{username} | 
[**confirm_user**](AdminApi.md#confirm_user) | **POST** /admin/users/{user_key}/confirmation | 
[**create_project**](AdminApi.md#create_project) | **POST** /admin/projects | 
[**list_all_projects**](AdminApi.md#list_all_projects) | **GET** /admin/projects/all | 
[**list_audits**](AdminApi.md#list_audits) | **GET** /admin/audits | 
[**list_pending_users**](AdminApi.md#list_pending_users) | **GET** /admin/users/pending | 


# **admin_add_user**
> SuccessMessage admin_add_user(proj_key, data)



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
    api_instance = deepsearch.cps.apis.user.AdminApi(api_client)
    proj_key = 'proj_key_example' # str | The project key
data = deepsearch.cps.apis.user.ProjectUserAssignment() # ProjectUserAssignment | 

    try:
        api_response = api_instance.admin_add_user(proj_key, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminApi->admin_add_user: %s\n" % e)
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

# **admin_list_users**
> dict(str, list[UserDetails]) admin_list_users(proj_key, page=page, items_per_page=items_per_page)



List all users belonging to a cps project

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
    api_instance = deepsearch.cps.apis.user.AdminApi(api_client)
    proj_key = 'proj_key_example' # str | The project key
page = 56 # int | page of the result list (optional)
items_per_page = 2 # int | items on one page of the result list (optional) (default to 2)

    try:
        api_response = api_instance.admin_list_users(proj_key, page=page, items_per_page=items_per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminApi->admin_list_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key | 
 **page** | **int**| page of the result list | [optional] 
 **items_per_page** | **int**| items on one page of the result list | [optional] [default to 2]

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

# **admin_remove_user**
> admin_remove_user(proj_key, username)



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
    api_instance = deepsearch.cps.apis.user.AdminApi(api_client)
    proj_key = 'proj_key_example' # str | The project key
username = 'username_example' # str | The username for the user

    try:
        api_instance.admin_remove_user(proj_key, username)
    except ApiException as e:
        print("Exception when calling AdminApi->admin_remove_user: %s\n" % e)
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

# **confirm_user**
> confirm_user(user_key)



Confirm a pending user.

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
    api_instance = deepsearch.cps.apis.user.AdminApi(api_client)
    user_key = 'user_key_example' # str | 

    try:
        api_instance.confirm_user(user_key)
    except ApiException as e:
        print("Exception when calling AdminApi->confirm_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_key** | **str**|  | 

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
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> Project create_project(data)



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
    api_instance = deepsearch.cps.apis.user.AdminApi(api_client)
    data = deepsearch.cps.apis.user.CreateProjectRequestBody() # CreateProjectRequestBody | 

    try:
        api_response = api_instance.create_project(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminApi->create_project: %s\n" % e)
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

# **list_all_projects**
> list[Project] list_all_projects()



List all projects

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
    api_instance = deepsearch.cps.apis.user.AdminApi(api_client)
    
    try:
        api_response = api_instance.list_all_projects()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminApi->list_all_projects: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **list_audits**
> InlineResponse200 list_audits(user_key=user_key, type_=type_, search_term=search_term, before=before, after=after, limit=limit)



List audits globally

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
    api_instance = deepsearch.cps.apis.user.AdminApi(api_client)
    user_key = 'user_key_example' # str |  (optional)
type_ = 'type__example' # str |  (optional)
search_term = 'search_term_example' # str |  (optional)
before = 'before_example' # str |  (optional)
after = 'after_example' # str |  (optional)
limit = 50 # int |  (optional) (default to 50)

    try:
        api_response = api_instance.list_audits(user_key=user_key, type_=type_, search_term=search_term, before=before, after=after, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminApi->list_audits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **list_pending_users**
> list[UserDetails] list_pending_users(term=term)



List pending user requests.

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
    api_instance = deepsearch.cps.apis.user.AdminApi(api_client)
    term = 'term_example' # str |  (optional)

    try:
        api_response = api_instance.list_pending_users(term=term)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminApi->list_pending_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**|  | [optional] 

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
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

