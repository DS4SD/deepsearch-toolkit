# deepsearch.cps.apis.public.KnowledgeGraphsApi

All URIs are relative to *http://localhost/api/cps/public/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assemble_project_knowledge_graph_data_flow**](KnowledgeGraphsApi.md#assemble_project_knowledge_graph_data_flow) | **POST** /project/{proj_key}/bags/{bag_key}/tasks/assemble_dataflow | 
[**backend_assemble_project_kg_data_flow**](KnowledgeGraphsApi.md#backend_assemble_project_kg_data_flow) | **POST** /backend/project/{proj_key}/bags/{bag_key}/tasks/assemble_dataflow | 
[**backend_create_project_kg**](KnowledgeGraphsApi.md#backend_create_project_kg) | **POST** /backend/project/{proj_key}/bags | 
[**backend_create_project_kg_snapshot_from_data_flow_assembly**](KnowledgeGraphsApi.md#backend_create_project_kg_snapshot_from_data_flow_assembly) | **POST** /backend/project/{proj_key}/bags/{bag_key}/tasks/assemble_dataflow/latest/snapshots | 
[**backend_get_project_kg_status**](KnowledgeGraphsApi.md#backend_get_project_kg_status) | **GET** /backend/project/{proj_key}/bags/{bag_key}/status | 
[**backend_list_project_kgs**](KnowledgeGraphsApi.md#backend_list_project_kgs) | **GET** /backend/project/{proj_key}/bags | 
[**backend_update_project_kg_metadata**](KnowledgeGraphsApi.md#backend_update_project_kg_metadata) | **PATCH** /backend/project/{proj_key}/bags/{bag_key} | 
[**create_project_knowledge_graph**](KnowledgeGraphsApi.md#create_project_knowledge_graph) | **POST** /project/{proj_key}/bags | 
[**create_project_knowledge_graph_authentication_token**](KnowledgeGraphsApi.md#create_project_knowledge_graph_authentication_token) | **GET** /project/{proj_key}/bags/{bag_key}/auth_token | 
[**create_project_knowledge_graph_backup**](KnowledgeGraphsApi.md#create_project_knowledge_graph_backup) | **POST** /project/{proj_key}/bags/{bag_key}/tasks/backup | 
[**create_project_knowledge_graph_delete_token**](KnowledgeGraphsApi.md#create_project_knowledge_graph_delete_token) | **POST** /project/{proj_key}/bags/{bag_key}/delete_token | 
[**create_project_knowledge_graph_snapshot**](KnowledgeGraphsApi.md#create_project_knowledge_graph_snapshot) | **POST** /project/{proj_key}/bags/{bag_key}/snapshots | 
[**create_project_knowledge_graph_snapshot_from_data_flow_assembly**](KnowledgeGraphsApi.md#create_project_knowledge_graph_snapshot_from_data_flow_assembly) | **POST** /project/{proj_key}/bags/{bag_key}/tasks/assemble_dataflow/latest/snapshots | 
[**delete_project_knowledge_graph**](KnowledgeGraphsApi.md#delete_project_knowledge_graph) | **DELETE** /project/{proj_key}/bags/{bag_key} | 
[**delete_project_knowledge_graph_snapshot**](KnowledgeGraphsApi.md#delete_project_knowledge_graph_snapshot) | **DELETE** /project/{proj_key}/bags/{bag_key}/snapshots/{execution_id} | 
[**download_project_knowledge_graph**](KnowledgeGraphsApi.md#download_project_knowledge_graph) | **POST** /project/{proj_key}/bags/{bag_key}/tasks/export | 
[**get_project_knowledge_graph_authentication_callback**](KnowledgeGraphsApi.md#get_project_knowledge_graph_authentication_callback) | **GET** /project/{proj_key}/bags/{bag_key}/auth_callback | 
[**get_project_knowledge_graph_status**](KnowledgeGraphsApi.md#get_project_knowledge_graph_status) | **GET** /project/{proj_key}/bags/{bag_key}/status | 
[**get_project_knowledge_graph_usage_stats**](KnowledgeGraphsApi.md#get_project_knowledge_graph_usage_stats) | **GET** /project/{proj_key}/bags/{bag_key}/usage_stats | 
[**list_project_knowledge_graph_assemble_tasks**](KnowledgeGraphsApi.md#list_project_knowledge_graph_assemble_tasks) | **GET** /project/{proj_key}/bags/{bag_key}/tasks/assemble_dataflow | 
[**list_project_knowledge_graph_load_tasks**](KnowledgeGraphsApi.md#list_project_knowledge_graph_load_tasks) | **GET** /project/{proj_key}/bags/{bag_key}/tasks/load_dataflow | 
[**list_project_knowledge_graph_snapshots**](KnowledgeGraphsApi.md#list_project_knowledge_graph_snapshots) | **GET** /project/{proj_key}/bags/{bag_key}/snapshots | 
[**list_project_knowledge_graphs**](KnowledgeGraphsApi.md#list_project_knowledge_graphs) | **GET** /project/{proj_key}/bags | 
[**list_public_knowledge_graphs**](KnowledgeGraphsApi.md#list_public_knowledge_graphs) | **GET** /project/public/bags | 
[**load_project_knowledge_graph_data_flow**](KnowledgeGraphsApi.md#load_project_knowledge_graph_data_flow) | **POST** /project/{proj_key}/bags/{bag_key}/tasks/load_dataflow | 
[**load_project_knowledge_graph_snapshot**](KnowledgeGraphsApi.md#load_project_knowledge_graph_snapshot) | **POST** /project/{proj_key}/bags/{bag_key}/snapshots/{execution_id}/actions/load | 
[**recreate_project_knowledge_graph_deployment**](KnowledgeGraphsApi.md#recreate_project_knowledge_graph_deployment) | **POST** /project/{proj_key}/bags/{bag_key}/tasks/recreate_deployment | 
[**restore_project_knowledge_graph_backup**](KnowledgeGraphsApi.md#restore_project_knowledge_graph_backup) | **POST** /project/{proj_key}/bags/{bag_key}/tasks/restore | 
[**resume_project_knowledge_graph**](KnowledgeGraphsApi.md#resume_project_knowledge_graph) | **POST** /project/{proj_key}/bags/{bag_key}/tasks/resume | 
[**suspend_project_knowledge_graph**](KnowledgeGraphsApi.md#suspend_project_knowledge_graph) | **POST** /project/{proj_key}/bags/{bag_key}/tasks/suspend | 
[**update_project_knowledge_graph_metadata**](KnowledgeGraphsApi.md#update_project_knowledge_graph_metadata) | **PATCH** /project/{proj_key}/bags/{bag_key} | 
[**upgrade_project_knowledge_graph_deployment**](KnowledgeGraphsApi.md#upgrade_project_knowledge_graph_deployment) | **POST** /project/{proj_key}/bags/{bag_key}/tasks/upgrade | 


# **assemble_project_knowledge_graph_data_flow**
> ProjectTask assemble_project_knowledge_graph_data_flow(proj_key, bag_key, options)



Assemble a data flow on a Knowledge Graph

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
    api_instance = deepsearch.cps.apis.public.KnowledgeGraphsApi(api_client)
    proj_key = 'proj_key_example' # str | 
bag_key = 'bag_key_example' # str | 
options = deepsearch.cps.apis.public.AssembleDataFlowIntoKnowledgeGraphOptions1() # AssembleDataFlowIntoKnowledgeGraphOptions1 | 

    try:
        api_response = api_instance.assemble_project_knowledge_graph_data_flow(proj_key, bag_key, options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KnowledgeGraphsApi->assemble_project_knowledge_graph_data_flow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **bag_key** | **str**|  | 
 **options** | [**AssembleDataFlowIntoKnowledgeGraphOptions1**](AssembleDataFlowIntoKnowledgeGraphOptions1.md)|  | 

### Return type

[**ProjectTask**](ProjectTask.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task started. |  -  |
**400** | Invalid dataflow. |  -  |
**404** | Data flow template doesn&#39;t exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backend_assemble_project_kg_data_flow**
> ProjectTask backend_assemble_project_kg_data_flow(proj_key, bag_key, options)



Assemble a data flow on a Knowledge Graph, backend-aware

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
    api_instance = deepsearch.cps.apis.public.KnowledgeGraphsApi(api_client)
    proj_key = 'proj_key_example' # str | 
bag_key = 'bag_key_example' # str | 
options = deepsearch.cps.apis.public.AssembleDataFlowIntoKnowledgeGraphOptions() # AssembleDataFlowIntoKnowledgeGraphOptions | 

    try:
        api_response = api_instance.backend_assemble_project_kg_data_flow(proj_key, bag_key, options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KnowledgeGraphsApi->backend_assemble_project_kg_data_flow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **bag_key** | **str**|  | 
 **options** | [**AssembleDataFlowIntoKnowledgeGraphOptions**](AssembleDataFlowIntoKnowledgeGraphOptions.md)|  | 

### Return type

[**ProjectTask**](ProjectTask.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task started. |  -  |
**400** | Invalid dataflow. |  -  |
**404** | Data flow template doesn&#39;t exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backend_create_project_kg**
> BagBackendAware backend_create_project_kg(proj_key, data)



Create new BAG, backend-aware

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
    api_instance = deepsearch.cps.apis.public.KnowledgeGraphsApi(api_client)
    proj_key = 'proj_key_example' # str | 
data = deepsearch.cps.apis.public.CreateKnowledgeGraphOptions() # CreateKnowledgeGraphOptions | 

    try:
        api_response = api_instance.backend_create_project_kg(proj_key, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KnowledgeGraphsApi->backend_create_project_kg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **data** | [**CreateKnowledgeGraphOptions**](CreateKnowledgeGraphOptions.md)|  | 

### Return type

[**BagBackendAware**](BagBackendAware.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Invalid parameters. |  -  |
**403** | Create knowledge graphs is disabled. |  -  |
**409** | Cannot create BAG because one already exists with that name. |  -  |
**500** | Error occured on the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backend_create_project_kg_snapshot_from_data_flow_assembly**
> ProjectTask backend_create_project_kg_snapshot_from_data_flow_assembly(proj_key, bag_key, body)



Create a snapshot of a Knowledge Graph from the last data flow assembly task, backend-aware

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
    api_instance = deepsearch.cps.apis.public.KnowledgeGraphsApi(api_client)
    proj_key = 'proj_key_example' # str | 
bag_key = 'bag_key_example' # str | 
body = deepsearch.cps.apis.public.InlineObject() # InlineObject | 

    try:
        api_response = api_instance.backend_create_project_kg_snapshot_from_data_flow_assembly(proj_key, bag_key, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KnowledgeGraphsApi->backend_create_project_kg_snapshot_from_data_flow_assembly: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **bag_key** | **str**|  | 
 **body** | [**InlineObject**](InlineObject.md)|  | 

### Return type

[**ProjectTask**](ProjectTask.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task started. |  -  |
**404** | KG/BAG/Data Flow Assembly not found. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backend_get_project_kg_status**
> BagStatusBackendAware backend_get_project_kg_status(proj_key, bag_key, details=details)



Get the status of a Knowledge Graph, backend-aware

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
    api_instance = deepsearch.cps.apis.public.KnowledgeGraphsApi(api_client)
    proj_key = 'proj_key_example' # str | 
bag_key = 'bag_key_example' # str | 
details = False # bool |  (optional) (default to False)

    try:
        api_response = api_instance.backend_get_project_kg_status(proj_key, bag_key, details=details)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KnowledgeGraphsApi->backend_get_project_kg_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **bag_key** | **str**|  | 
 **details** | **bool**|  | [optional] [default to False]

### Return type

[**BagStatusBackendAware**](BagStatusBackendAware.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Knowledge Graph status. |  -  |
**404** | BAG not found. |  -  |
**500** | Error occured on the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backend_list_project_kgs**
> list[BagBackendAware] backend_list_project_kgs(proj_key, term=term)



List all bags in the project, backend-aware

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
    api_instance = deepsearch.cps.apis.public.KnowledgeGraphsApi(api_client)
    proj_key = 'proj_key_example' # str | 
term = 'term_example' # str |  (optional)

    try:
        api_response = api_instance.backend_list_project_kgs(proj_key, term=term)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KnowledgeGraphsApi->backend_list_project_kgs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **term** | **str**|  | [optional] 

### Return type

[**list[BagBackendAware]**](BagBackendAware.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Error occured on the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backend_update_project_kg_metadata**
> BagBackendAware backend_update_project_kg_metadata(proj_key, bag_key, data)



Update the metadata of a Knowledge graph, backend-aware

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
    api_instance = deepsearch.cps.apis.public.KnowledgeGraphsApi(api_client)
    proj_key = 'proj_key_example' # str | 
bag_key = 'bag_key_example' # str | 
data = deepsearch.cps.apis.public.PatchKnowledgeGraphOptions() # PatchKnowledgeGraphOptions | 

    try:
        api_response = api_instance.backend_update_project_kg_metadata(proj_key, bag_key, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KnowledgeGraphsApi->backend_update_project_kg_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **bag_key** | **str**|  | 
 **data** | [**PatchKnowledgeGraphOptions**](PatchKnowledgeGraphOptions.md)|  | 

### Return type

[**BagBackendAware**](BagBackendAware.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Knowledge graph metadata updated. |  -  |
**404** | Knowledge graph not found |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_knowledge_graph**
> Bag create_project_knowledge_graph(proj_key, data)



Create new BAG

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
    api_instance = deepsearch.cps.apis.public.KnowledgeGraphsApi(api_client)
    proj_key = 'proj_key_example' # str | 
data = deepsearch.cps.apis.public.CreateKnowledgeGraphOptions1() # CreateKnowledgeGraphOptions1 | 

    try:
        api_response = api_instance.create_project_knowledge_graph(proj_key, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KnowledgeGraphsApi->create_project_knowledge_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **data** | [**CreateKnowledgeGraphOptions1**](CreateKnowledgeGraphOptions1.md)|  | 

### Return type

[**Bag**](Bag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Invalid parameters. |  -  |
**403** | Create knowledge graphs is disabled. |  -  |
**409** | Cannot create BAG because one already exists with that name. |  -  |
**500** | Error occured on the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_knowledge_graph_authentication_token**
> TokenResponse create_project_knowledge_graph_authentication_token(proj_key, bag_key)



Get a token used to authenticate in the Erlenmeyer / KG APIs of a BAG.

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
    api_instance = deepsearch.cps.apis.public.KnowledgeGraphsApi(api_client)
    proj_key = 'proj_key_example' # str | 
bag_key = 'bag_key_example' # str | 

    try:
        api_response = api_instance.create_project_knowledge_graph_authentication_token(proj_key, bag_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KnowledgeGraphsApi->create_project_knowledge_graph_authentication_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **bag_key** | **str**|  | 

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
**200** | BAG auth token. |  -  |
**404** | BAG not found. |  -  |
**500** | Error occured on the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_knowledge_graph_backup**
> Task create_project_knowledge_graph_backup(proj_key, bag_key, options)



Back up a Knowledge Graph

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
    api_instance = deepsearch.cps.apis.public.KnowledgeGraphsApi(api_client)
    proj_key = 'proj_key_example' # str | 
bag_key = 'bag_key_example' # str | 
options = deepsearch.cps.apis.public.BackupKnowledgeGraphOptions() # BackupKnowledgeGraphOptions | 

    try:
        api_response = api_instance.create_project_knowledge_graph_backup(proj_key, bag_key, options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KnowledgeGraphsApi->create_project_knowledge_graph_backup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **bag_key** | **str**|  | 
 **options** | [**BackupKnowledgeGraphOptions**](BackupKnowledgeGraphOptions.md)|  | 

### Return type

[**Task**](Task.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Invalid parameters. |  -  |
**404** | KG/BAG not found. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_knowledge_graph_delete_token**
> TokenResponse create_project_knowledge_graph_delete_token(proj_key, bag_key)



Get a token used to confirm the deletion of a BAG.

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
    api_instance = deepsearch.cps.apis.public.KnowledgeGraphsApi(api_client)
    proj_key = 'proj_key_example' # str | 
bag_key = 'bag_key_example' # str | 

    try:
        api_response = api_instance.create_project_knowledge_graph_delete_token(proj_key, bag_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KnowledgeGraphsApi->create_project_knowledge_graph_delete_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **bag_key** | **str**|  | 

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
**200** | BAG deletion token. |  -  |
**404** | BAG not found. |  -  |
**500** | Error occured on the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_knowledge_graph_snapshot**
> ProjectTask create_project_knowledge_graph_snapshot(proj_key, bag_key, body)



Create a snapshot of a Knowledge Graph, with its current state.

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
    api_instance = deepsearch.cps.apis.public.KnowledgeGraphsApi(api_client)
    proj_key = 'proj_key_example' # str | 
bag_key = 'bag_key_example' # str | 
body = deepsearch.cps.apis.public.KnowledgeGraphSnapshotOptions() # KnowledgeGraphSnapshotOptions | 

    try:
        api_response = api_instance.create_project_knowledge_graph_snapshot(proj_key, bag_key, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KnowledgeGraphsApi->create_project_knowledge_graph_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **bag_key** | **str**|  | 
 **body** | [**KnowledgeGraphSnapshotOptions**](KnowledgeGraphSnapshotOptions.md)|  | 

### Return type

[**ProjectTask**](ProjectTask.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task started. |  -  |
**403** | Feature is disabled on this instance. |  -  |
**404** | KG/BAG not found. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_knowledge_graph_snapshot_from_data_flow_assembly**
> ProjectTask create_project_knowledge_graph_snapshot_from_data_flow_assembly(proj_key, bag_key, body)



Create a snapshot of a Knowledge Graph from the last data flow assembly task.

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
    api_instance = deepsearch.cps.apis.public.KnowledgeGraphsApi(api_client)
    proj_key = 'proj_key_example' # str | 
bag_key = 'bag_key_example' # str | 
body = deepsearch.cps.apis.public.InlineObject2() # InlineObject2 | 

    try:
        api_response = api_instance.create_project_knowledge_graph_snapshot_from_data_flow_assembly(proj_key, bag_key, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KnowledgeGraphsApi->create_project_knowledge_graph_snapshot_from_data_flow_assembly: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **bag_key** | **str**|  | 
 **body** | [**InlineObject2**](InlineObject2.md)|  | 

### Return type

[**ProjectTask**](ProjectTask.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task started. |  -  |
**404** | KG/BAG/Data Flow Assembly not found. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_knowledge_graph**
> delete_project_knowledge_graph(proj_key, bag_key, confirmation_token)



Delete a BAG

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
    api_instance = deepsearch.cps.apis.public.KnowledgeGraphsApi(api_client)
    proj_key = 'proj_key_example' # str | 
bag_key = 'bag_key_example' # str | 
confirmation_token = 'confirmation_token_example' # str | 

    try:
        api_instance.delete_project_knowledge_graph(proj_key, bag_key, confirmation_token)
    except ApiException as e:
        print("Exception when calling KnowledgeGraphsApi->delete_project_knowledge_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **bag_key** | **str**|  | 
 **confirmation_token** | **str**|  | 

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
**204** | BAG deleted. |  -  |
**404** | BAG not found. |  -  |
**500** | Error occured on the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_knowledge_graph_snapshot**
> delete_project_knowledge_graph_snapshot(proj_key, bag_key, execution_id)



Delete a snapshot resulting from an assembled data flow. The execution log itself is not deleted.

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
    api_instance = deepsearch.cps.apis.public.KnowledgeGraphsApi(api_client)
    proj_key = 'proj_key_example' # str | 
bag_key = 'bag_key_example' # str | 
execution_id = 'execution_id_example' # str | 

    try:
        api_instance.delete_project_knowledge_graph_snapshot(proj_key, bag_key, execution_id)
    except ApiException as e:
        print("Exception when calling KnowledgeGraphsApi->delete_project_knowledge_graph_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **bag_key** | **str**|  | 
 **execution_id** | **str**|  | 

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
**204** | OK |  -  |
**400** | Invalid parameters. |  -  |
**404** | KG/BAG/Snapshot not found. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_project_knowledge_graph**
> Task download_project_knowledge_graph(proj_key, bag_key)



Download a Knowledge Graph

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
    api_instance = deepsearch.cps.apis.public.KnowledgeGraphsApi(api_client)
    proj_key = 'proj_key_example' # str | 
bag_key = 'bag_key_example' # str | 

    try:
        api_response = api_instance.download_project_knowledge_graph(proj_key, bag_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KnowledgeGraphsApi->download_project_knowledge_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **bag_key** | **str**|  | 

### Return type

[**Task**](Task.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Invalid parameters. |  -  |
**404** | KG/BAG not found. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_knowledge_graph_authentication_callback**
> KnowledgeGraphAuthenticationCallback get_project_knowledge_graph_authentication_callback(proj_key, bag_key, bag_token)



Final step of redirection for authentication on a BAG.

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
    api_instance = deepsearch.cps.apis.public.KnowledgeGraphsApi(api_client)
    proj_key = 'proj_key_example' # str | 
bag_key = 'bag_key_example' # str | 
bag_token = 'bag_token_example' # str | 

    try:
        api_response = api_instance.get_project_knowledge_graph_authentication_callback(proj_key, bag_key, bag_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KnowledgeGraphsApi->get_project_knowledge_graph_authentication_callback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **bag_key** | **str**|  | 
 **bag_token** | **str**|  | 

### Return type

[**KnowledgeGraphAuthenticationCallback**](KnowledgeGraphAuthenticationCallback.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BAG auth redirect URL. |  -  |
**401** | Unauthorized. |  -  |
**404** | BAG not found. |  -  |
**500** | Error occured on the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_knowledge_graph_status**
> BagStatus get_project_knowledge_graph_status(proj_key, bag_key, details=details)



Get the status of a Knowledge Graph

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
    api_instance = deepsearch.cps.apis.public.KnowledgeGraphsApi(api_client)
    proj_key = 'proj_key_example' # str | 
bag_key = 'bag_key_example' # str | 
details = False # bool |  (optional) (default to False)

    try:
        api_response = api_instance.get_project_knowledge_graph_status(proj_key, bag_key, details=details)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KnowledgeGraphsApi->get_project_knowledge_graph_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **bag_key** | **str**|  | 
 **details** | **bool**|  | [optional] [default to False]

### Return type

[**BagStatus**](BagStatus.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Knowledge Graph status. |  -  |
**404** | BAG not found. |  -  |
**500** | Error occured on the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_knowledge_graph_usage_stats**
> UsageStats get_project_knowledge_graph_usage_stats(proj_key, bag_key)



Get the usage stats of a Knowledge Graph

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
    api_instance = deepsearch.cps.apis.public.KnowledgeGraphsApi(api_client)
    proj_key = 'proj_key_example' # str | 
bag_key = 'bag_key_example' # str | 

    try:
        api_response = api_instance.get_project_knowledge_graph_usage_stats(proj_key, bag_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KnowledgeGraphsApi->get_project_knowledge_graph_usage_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **bag_key** | **str**|  | 

### Return type

[**UsageStats**](UsageStats.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Knowledge Graph usage stats. |  -  |
**404** | BAG not found. |  -  |
**500** | Error occured on the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_knowledge_graph_assemble_tasks**
> list[DataFlowAssembleIntoKnowledgeGraphTask] list_project_knowledge_graph_assemble_tasks(proj_key, bag_key, limit=limit, skip=skip)



List assemble tasks for a Knowledge Graph.

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
    api_instance = deepsearch.cps.apis.public.KnowledgeGraphsApi(api_client)
    proj_key = 'proj_key_example' # str | 
bag_key = 'bag_key_example' # str | 
limit = 50 # int |  (optional) (default to 50)
skip = 0 # int |  (optional) (default to 0)

    try:
        api_response = api_instance.list_project_knowledge_graph_assemble_tasks(proj_key, bag_key, limit=limit, skip=skip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KnowledgeGraphsApi->list_project_knowledge_graph_assemble_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **bag_key** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 50]
 **skip** | **int**|  | [optional] [default to 0]

### Return type

[**list[DataFlowAssembleIntoKnowledgeGraphTask]**](DataFlowAssembleIntoKnowledgeGraphTask.md)

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

# **list_project_knowledge_graph_load_tasks**
> list[DataFlowLoadIntoKnowledgeGraphTask] list_project_knowledge_graph_load_tasks(proj_key, bag_key, limit=limit, skip=skip)



List load tasks for a Knowledge Graph

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
    api_instance = deepsearch.cps.apis.public.KnowledgeGraphsApi(api_client)
    proj_key = 'proj_key_example' # str | 
bag_key = 'bag_key_example' # str | 
limit = 50 # int |  (optional) (default to 50)
skip = 0 # int |  (optional) (default to 0)

    try:
        api_response = api_instance.list_project_knowledge_graph_load_tasks(proj_key, bag_key, limit=limit, skip=skip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KnowledgeGraphsApi->list_project_knowledge_graph_load_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **bag_key** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 50]
 **skip** | **int**|  | [optional] [default to 0]

### Return type

[**list[DataFlowLoadIntoKnowledgeGraphTask]**](DataFlowLoadIntoKnowledgeGraphTask.md)

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

# **list_project_knowledge_graph_snapshots**
> list[KgSnapshot] list_project_knowledge_graph_snapshots(proj_key, bag_key)



List snapshots for a knowledge graph from assembled data flows.

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
    api_instance = deepsearch.cps.apis.public.KnowledgeGraphsApi(api_client)
    proj_key = 'proj_key_example' # str | 
bag_key = 'bag_key_example' # str | 

    try:
        api_response = api_instance.list_project_knowledge_graph_snapshots(proj_key, bag_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KnowledgeGraphsApi->list_project_knowledge_graph_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **bag_key** | **str**|  | 

### Return type

[**list[KgSnapshot]**](KgSnapshot.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Snapshots |  -  |
**404** | KG/BAG not found. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_knowledge_graphs**
> list[Bag] list_project_knowledge_graphs(proj_key, term=term)



List all bags in the project

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
    api_instance = deepsearch.cps.apis.public.KnowledgeGraphsApi(api_client)
    proj_key = 'proj_key_example' # str | 
term = 'term_example' # str |  (optional)

    try:
        api_response = api_instance.list_project_knowledge_graphs(proj_key, term=term)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KnowledgeGraphsApi->list_project_knowledge_graphs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **term** | **str**|  | [optional] 

### Return type

[**list[Bag]**](Bag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Error occured on the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_public_knowledge_graphs**
> list[Bag] list_public_knowledge_graphs(term=term)



List all public BAGs

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
    api_instance = deepsearch.cps.apis.public.KnowledgeGraphsApi(api_client)
    term = 'term_example' # str |  (optional)

    try:
        api_response = api_instance.list_public_knowledge_graphs(term=term)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KnowledgeGraphsApi->list_public_knowledge_graphs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**|  | [optional] 

### Return type

[**list[Bag]**](Bag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Error occured on the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_project_knowledge_graph_data_flow**
> ProjectTask load_project_knowledge_graph_data_flow(proj_key, bag_key, options)



Load a data flow onto a Knowledge Graph.

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
    api_instance = deepsearch.cps.apis.public.KnowledgeGraphsApi(api_client)
    proj_key = 'proj_key_example' # str | 
bag_key = 'bag_key_example' # str | 
options = deepsearch.cps.apis.public.LoadDataFlowIntoKnowledgeGraphOptions() # LoadDataFlowIntoKnowledgeGraphOptions | 

    try:
        api_response = api_instance.load_project_knowledge_graph_data_flow(proj_key, bag_key, options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KnowledgeGraphsApi->load_project_knowledge_graph_data_flow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **bag_key** | **str**|  | 
 **options** | [**LoadDataFlowIntoKnowledgeGraphOptions**](LoadDataFlowIntoKnowledgeGraphOptions.md)|  | 

### Return type

[**ProjectTask**](ProjectTask.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task started. |  -  |
**400** | Invalid dataflow. |  -  |
**404** | Data flow template doesn&#39;t exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_project_knowledge_graph_snapshot**
> Task load_project_knowledge_graph_snapshot(proj_key, bag_key, execution_id)



Load a snapshot resulting from an assembled data flow

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
    api_instance = deepsearch.cps.apis.public.KnowledgeGraphsApi(api_client)
    proj_key = 'proj_key_example' # str | 
bag_key = 'bag_key_example' # str | 
execution_id = 'execution_id_example' # str | 

    try:
        api_response = api_instance.load_project_knowledge_graph_snapshot(proj_key, bag_key, execution_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KnowledgeGraphsApi->load_project_knowledge_graph_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **bag_key** | **str**|  | 
 **execution_id** | **str**|  | 

### Return type

[**Task**](Task.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Snapshot is being loaded. |  -  |
**400** | Invalid parameters. |  -  |
**403** | Feature is disabled on this instance. |  -  |
**404** | KG/BAG/Snapshot not found. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recreate_project_knowledge_graph_deployment**
> recreate_project_knowledge_graph_deployment(proj_key, bag_key, body)



(Re)create the deployment for a Knowledge Graph

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
    api_instance = deepsearch.cps.apis.public.KnowledgeGraphsApi(api_client)
    proj_key = 'proj_key_example' # str | 
bag_key = 'bag_key_example' # str | 
body = deepsearch.cps.apis.public.KnowledgeGraphDeploymentRecreationOptions() # KnowledgeGraphDeploymentRecreationOptions | 

    try:
        api_instance.recreate_project_knowledge_graph_deployment(proj_key, bag_key, body)
    except ApiException as e:
        print("Exception when calling KnowledgeGraphsApi->recreate_project_knowledge_graph_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **bag_key** | **str**|  | 
 **body** | [**KnowledgeGraphDeploymentRecreationOptions**](KnowledgeGraphDeploymentRecreationOptions.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deployment upgrading. |  -  |
**404** | Knowledge Graph doesn&#39;t exist. |  -  |
**409** | Refused to recreate the deployment since it already exists and the &#x60;force&#x60; flag is not &#x60;true&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_project_knowledge_graph_backup**
> Task restore_project_knowledge_graph_backup(proj_key, bag_key, options)



Restore a back up of a Knowledge Graph

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
    api_instance = deepsearch.cps.apis.public.KnowledgeGraphsApi(api_client)
    proj_key = 'proj_key_example' # str | 
bag_key = 'bag_key_example' # str | 
options = deepsearch.cps.apis.public.RestoreKnowledgeGraphBackupOptions() # RestoreKnowledgeGraphBackupOptions | 

    try:
        api_response = api_instance.restore_project_knowledge_graph_backup(proj_key, bag_key, options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KnowledgeGraphsApi->restore_project_knowledge_graph_backup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **bag_key** | **str**|  | 
 **options** | [**RestoreKnowledgeGraphBackupOptions**](RestoreKnowledgeGraphBackupOptions.md)|  | 

### Return type

[**Task**](Task.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Invalid parameters. |  -  |
**404** | KG/BAG not found. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_project_knowledge_graph**
> ProjectTask resume_project_knowledge_graph(proj_key, bag_key, body)



Resume a Knowledge Graph

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
    api_instance = deepsearch.cps.apis.public.KnowledgeGraphsApi(api_client)
    proj_key = 'proj_key_example' # str | 
bag_key = 'bag_key_example' # str | 
body = deepsearch.cps.apis.public.ResumeKnowledgeGraphOptions() # ResumeKnowledgeGraphOptions | 

    try:
        api_response = api_instance.resume_project_knowledge_graph(proj_key, bag_key, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KnowledgeGraphsApi->resume_project_knowledge_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **bag_key** | **str**|  | 
 **body** | [**ResumeKnowledgeGraphOptions**](ResumeKnowledgeGraphOptions.md)|  | 

### Return type

[**ProjectTask**](ProjectTask.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task started. |  -  |
**403** | Feature is disabled on this instance. |  -  |
**404** | Knowledge Graph doesn&#39;t exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend_project_knowledge_graph**
> ProjectTask suspend_project_knowledge_graph(proj_key, bag_key, options)



Suspend a Knowledge Graph

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
    api_instance = deepsearch.cps.apis.public.KnowledgeGraphsApi(api_client)
    proj_key = 'proj_key_example' # str | 
bag_key = 'bag_key_example' # str | 
options = deepsearch.cps.apis.public.SuspendKnowledgeGraphOptions() # SuspendKnowledgeGraphOptions | 

    try:
        api_response = api_instance.suspend_project_knowledge_graph(proj_key, bag_key, options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KnowledgeGraphsApi->suspend_project_knowledge_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **bag_key** | **str**|  | 
 **options** | [**SuspendKnowledgeGraphOptions**](SuspendKnowledgeGraphOptions.md)|  | 

### Return type

[**ProjectTask**](ProjectTask.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task started. |  -  |
**404** | Knowledge Graph doesn&#39;t exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_knowledge_graph_metadata**
> Bag update_project_knowledge_graph_metadata(proj_key, bag_key, data)



Update the metadata of a Knowledge graph

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
    api_instance = deepsearch.cps.apis.public.KnowledgeGraphsApi(api_client)
    proj_key = 'proj_key_example' # str | 
bag_key = 'bag_key_example' # str | 
data = deepsearch.cps.apis.public.PatchKnowledgeGraphOptions1() # PatchKnowledgeGraphOptions1 | 

    try:
        api_response = api_instance.update_project_knowledge_graph_metadata(proj_key, bag_key, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling KnowledgeGraphsApi->update_project_knowledge_graph_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **bag_key** | **str**|  | 
 **data** | [**PatchKnowledgeGraphOptions1**](PatchKnowledgeGraphOptions1.md)|  | 

### Return type

[**Bag**](Bag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Knowledge graph metadata updated. |  -  |
**404** | Knowledge graph not found |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upgrade_project_knowledge_graph_deployment**
> upgrade_project_knowledge_graph_deployment(proj_key, bag_key, body)



Upgrade the deployment chart of a Knowledge Graph

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
    api_instance = deepsearch.cps.apis.public.KnowledgeGraphsApi(api_client)
    proj_key = 'proj_key_example' # str | 
bag_key = 'bag_key_example' # str | 
body = deepsearch.cps.apis.public.KnowledgeGraphChartUpgradeOptions() # KnowledgeGraphChartUpgradeOptions | 

    try:
        api_instance.upgrade_project_knowledge_graph_deployment(proj_key, bag_key, body)
    except ApiException as e:
        print("Exception when calling KnowledgeGraphsApi->upgrade_project_knowledge_graph_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **bag_key** | **str**|  | 
 **body** | [**KnowledgeGraphChartUpgradeOptions**](KnowledgeGraphChartUpgradeOptions.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Chart upgrading. |  -  |
**404** | Knowledge Graph doesn&#39;t exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

