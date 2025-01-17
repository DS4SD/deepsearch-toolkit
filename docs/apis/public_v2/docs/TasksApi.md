# deepsearch.cps.apis.public_v2.TasksApi

All URIs are relative to */api/cps/public/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_project_task**](TasksApi.md#abort_project_task) | **POST** /project/{proj_key}/tasks/{task_id}/actions/abort | Abort Project Task
[**get_project_celery_task**](TasksApi.md#get_project_celery_task) | **GET** /project/{proj_key}/celery_tasks/{task_id} | Get Project Celery Task
[**get_project_task**](TasksApi.md#get_project_task) | **GET** /project/{proj_key}/tasks/{task_id} | Get Project Task
[**list_project_tasks**](TasksApi.md#list_project_tasks) | **GET** /project/{proj_key}/tasks | List Project Tasks


# **abort_project_task**
> abort_project_task(task_id, proj_key)

Abort Project Task

Abort a task.

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
    api_instance = deepsearch.cps.apis.public_v2.TasksApi(api_client)
    task_id = 'task_id_example' # str | 
    proj_key = 'proj_key_example' # str | 

    try:
        # Abort Project Task
        api_instance.abort_project_task(task_id, proj_key)
    except Exception as e:
        print("Exception when calling TasksApi->abort_project_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 
 **proj_key** | **str**|  | 

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
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_celery_task**
> TaskResult get_project_celery_task(task_id, proj_key, wait=wait)

Get Project Celery Task

Get a celery task for a project.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.task_result import TaskResult
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
    api_instance = deepsearch.cps.apis.public_v2.TasksApi(api_client)
    task_id = 'task_id_example' # str | 
    proj_key = 'proj_key_example' # str | 
    wait = deepsearch.cps.apis.public_v2.Wait1() # Wait1 | Optionally block this method call for a few seconds to wait for the result instead of polling through multiple calls. (optional)

    try:
        # Get Project Celery Task
        api_response = api_instance.get_project_celery_task(task_id, proj_key, wait=wait)
        print("The response of TasksApi->get_project_celery_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_project_celery_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 
 **proj_key** | **str**|  | 
 **wait** | [**Wait1**](.md)| Optionally block this method call for a few seconds to wait for the result instead of polling through multiple calls. | [optional] 

### Return type

[**TaskResult**](TaskResult.md)

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

# **get_project_task**
> TaskContext get_project_task(task_id, proj_key)

Get Project Task

Get a task for a project.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.task_context import TaskContext
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
    api_instance = deepsearch.cps.apis.public_v2.TasksApi(api_client)
    task_id = 'task_id_example' # str | 
    proj_key = 'proj_key_example' # str | 

    try:
        # Get Project Task
        api_response = api_instance.get_project_task(task_id, proj_key)
        print("The response of TasksApi->get_project_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_project_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 
 **proj_key** | **str**|  | 

### Return type

[**TaskContext**](TaskContext.md)

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

# **list_project_tasks**
> List[TaskContext] list_project_tasks(proj_key, task_type=task_type, skip=skip, limit=limit, sort_by=sort_by, sort_order=sort_order)

List Project Tasks

List tasks for a project.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.task_context import TaskContext
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
    api_instance = deepsearch.cps.apis.public_v2.TasksApi(api_client)
    proj_key = 'proj_key_example' # str | 
    task_type = deepsearch.cps.apis.public_v2.TaskType() # TaskType |  (optional)
    skip = 0 # int |  (optional) (default to 0)
    limit = 50 # int |  (optional) (default to 50)
    sort_by = '_id' # str |  (optional) (default to '_id')
    sort_order = 'desc' # str |  (optional) (default to 'desc')

    try:
        # List Project Tasks
        api_response = api_instance.list_project_tasks(proj_key, task_type=task_type, skip=skip, limit=limit, sort_by=sort_by, sort_order=sort_order)
        print("The response of TasksApi->list_project_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->list_project_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **task_type** | [**TaskType**](.md)|  | [optional] 
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 50]
 **sort_by** | **str**|  | [optional] [default to &#39;_id&#39;]
 **sort_order** | **str**|  | [optional] [default to &#39;desc&#39;]

### Return type

[**List[TaskContext]**](TaskContext.md)

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

