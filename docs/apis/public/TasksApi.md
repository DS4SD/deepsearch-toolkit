# deepsearch.cps.apis.public.TasksApi

All URIs are relative to *http://localhost/api/cps/public/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_project_task**](TasksApi.md#abort_project_task) | **POST** /project/{proj_key}/tasks/{task_id}/actions/abort | 
[**get_project_celery_task**](TasksApi.md#get_project_celery_task) | **GET** /project/{proj_key}/celery_tasks/{task_id} | 
[**get_project_task**](TasksApi.md#get_project_task) | **GET** /project/{proj_key}/tasks/{task_id} | 
[**list_failure_celery_tasks**](TasksApi.md#list_failure_celery_tasks) | **GET** /system/celery_tasks/failure | 
[**list_project_tasks**](TasksApi.md#list_project_tasks) | **GET** /project/{proj_key}/tasks | 
[**list_system_celery_tasks**](TasksApi.md#list_system_celery_tasks) | **GET** /system/celery_tasks/status | 


# **abort_project_task**
> abort_project_task(proj_key, task_id)



Abort a task.

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
    api_instance = deepsearch.cps.apis.public.TasksApi(api_client)
    proj_key = 'proj_key_example' # str | 
task_id = 'task_id_example' # str | 

    try:
        api_instance.abort_project_task(proj_key, task_id)
    except ApiException as e:
        print("Exception when calling TasksApi->abort_project_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **task_id** | **str**|  | 

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
**204** | Task aborted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_celery_task**
> CeleryTaskPromise get_project_celery_task(proj_key, task_id)



Get a celery task for a project.

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
    api_instance = deepsearch.cps.apis.public.TasksApi(api_client)
    proj_key = 'proj_key_example' # str | 
task_id = 'task_id_example' # str | 

    try:
        api_response = api_instance.get_project_celery_task(proj_key, task_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->get_project_celery_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **task_id** | **str**|  | 

### Return type

[**CeleryTaskPromise**](CeleryTaskPromise.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task |  -  |
**404** | Task not found. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_task**
> ProjectTask get_project_task(proj_key, task_id)



Get a task for a project.

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

# Configure API key authorization: KGAuth
configuration = deepsearch.cps.apis.public.Configuration(
    host = "http://localhost/api/cps/public/v1",
    api_key = {
        'X-CPS-KG-Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CPS-KG-Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with deepsearch.cps.apis.public.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deepsearch.cps.apis.public.TasksApi(api_client)
    proj_key = 'proj_key_example' # str | 
task_id = 'task_id_example' # str | 

    try:
        api_response = api_instance.get_project_task(proj_key, task_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->get_project_task: %s\n" % e)
```

* Api Key Authentication (KGAuth):
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

# Configure API key authorization: KGAuth
configuration = deepsearch.cps.apis.public.Configuration(
    host = "http://localhost/api/cps/public/v1",
    api_key = {
        'X-CPS-KG-Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CPS-KG-Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with deepsearch.cps.apis.public.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deepsearch.cps.apis.public.TasksApi(api_client)
    proj_key = 'proj_key_example' # str | 
task_id = 'task_id_example' # str | 

    try:
        api_response = api_instance.get_project_task(proj_key, task_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->get_project_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **task_id** | **str**|  | 

### Return type

[**ProjectTask**](ProjectTask.md)

### Authorization

[Bearer](../README.md#Bearer), [KGAuth](../README.md#KGAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task |  -  |
**404** | Task not found. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_failure_celery_tasks**
> list[CeleryTask] list_failure_celery_tasks(proj_key, task_id)



Get celery tasks that failed.

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
    api_instance = deepsearch.cps.apis.public.TasksApi(api_client)
    proj_key = 'proj_key_example' # str | 
task_id = 'task_id_example' # str | 

    try:
        api_response = api_instance.list_failure_celery_tasks(proj_key, task_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->list_failure_celery_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **task_id** | **str**|  | 

### Return type

[**list[CeleryTask]**](CeleryTask.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Celery tasks |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_tasks**
> list[ProjectTask] list_project_tasks(proj_key, task_type=task_type, limit=limit, skip=skip, sort_by=sort_by, sort_order=sort_order)



List tasks for a project.

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
    api_instance = deepsearch.cps.apis.public.TasksApi(api_client)
    proj_key = 'proj_key_example' # str | 
task_type = 'task_type_example' # str |  (optional)
limit = 50 # int |  (optional) (default to 50)
skip = 0 # int |  (optional) (default to 0)
sort_by = 'sort_by_example' # str |  (optional)
sort_order = 'asc' # str |  (optional) (default to 'asc')

    try:
        api_response = api_instance.list_project_tasks(proj_key, task_type=task_type, limit=limit, skip=skip, sort_by=sort_by, sort_order=sort_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->list_project_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **task_type** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **skip** | **int**|  | [optional] [default to 0]
 **sort_by** | **str**|  | [optional] 
 **sort_order** | **str**|  | [optional] [default to &#39;asc&#39;]

### Return type

[**list[ProjectTask]**](ProjectTask.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of tasks. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_system_celery_tasks**
> list[CeleryTask1] list_system_celery_tasks(proj_key=proj_key, project_task_id=project_task_id, started_since=started_since, task_status=task_status, limit=limit)



Get the status of Celery tasks.

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
    api_instance = deepsearch.cps.apis.public.TasksApi(api_client)
    proj_key = 'proj_key_example' # str |  (optional)
project_task_id = 'project_task_id_example' # str |  (optional)
started_since = 3.4 # float | If set, return the tasks created at or after this timestamp. Otherwise, return the tasks created up to 60 minutes of the system's date, if `project_task_id` is not set. (optional)
task_status = 3.4 # float |  (optional)
limit = 50 # int |  (optional) (default to 50)

    try:
        api_response = api_instance.list_system_celery_tasks(proj_key=proj_key, project_task_id=project_task_id, started_since=started_since, task_status=task_status, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->list_system_celery_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | [optional] 
 **project_task_id** | **str**|  | [optional] 
 **started_since** | **float**| If set, return the tasks created at or after this timestamp. Otherwise, return the tasks created up to 60 minutes of the system&#39;s date, if &#x60;project_task_id&#x60; is not set. | [optional] 
 **task_status** | **float**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]

### Return type

[**list[CeleryTask1]**](CeleryTask1.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Celery tasks |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

