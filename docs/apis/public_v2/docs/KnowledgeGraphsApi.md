# deepsearch.cps.apis.public_v2.KnowledgeGraphsApi

All URIs are relative to */api/cps/public/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backend_list_project_kgs**](KnowledgeGraphsApi.md#backend_list_project_kgs) | **GET** /backend/project/{proj_key}/bags | Backend List Project Kgs
[**create_project_knowledge_graph**](KnowledgeGraphsApi.md#create_project_knowledge_graph) | **POST** /backend/project/{proj_key}/bags | Create Project Knowledge Graph
[**list_public_knowledge_graphs**](KnowledgeGraphsApi.md#list_public_knowledge_graphs) | **GET** /project/public/bags | List Public Knowledge Graphs
[**update_project_knowledge_graph_metadata**](KnowledgeGraphsApi.md#update_project_knowledge_graph_metadata) | **PATCH** /backend/project/{proj_key}/bags/{bag_key} | Update Project Knowledge Graph Metadata


# **backend_list_project_kgs**
> List[object] backend_list_project_kgs(proj_key, term=term)

Backend List Project Kgs

List all bags in the project, backend-aware

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
    api_instance = deepsearch.cps.apis.public_v2.KnowledgeGraphsApi(api_client)
    proj_key = 'proj_key_example' # str | 
    term = None # object |  (optional)

    try:
        # Backend List Project Kgs
        api_response = api_instance.backend_list_project_kgs(proj_key, term=term)
        print("The response of KnowledgeGraphsApi->backend_list_project_kgs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeGraphsApi->backend_list_project_kgs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **term** | [**object**](.md)|  | [optional] 

### Return type

**List[object]**

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

# **create_project_knowledge_graph**
> object create_project_knowledge_graph(proj_key, body)

Create Project Knowledge Graph

Create new BAG, backend-aware

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
    api_instance = deepsearch.cps.apis.public_v2.KnowledgeGraphsApi(api_client)
    proj_key = 'proj_key_example' # str | 
    body = None # object | 

    try:
        # Create Project Knowledge Graph
        api_response = api_instance.create_project_knowledge_graph(proj_key, body)
        print("The response of KnowledgeGraphsApi->create_project_knowledge_graph:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeGraphsApi->create_project_knowledge_graph: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **body** | **object**|  | 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_public_knowledge_graphs**
> List[object] list_public_knowledge_graphs(term=term)

List Public Knowledge Graphs

List all public BAGs

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
    api_instance = deepsearch.cps.apis.public_v2.KnowledgeGraphsApi(api_client)
    term = None # object |  (optional)

    try:
        # List Public Knowledge Graphs
        api_response = api_instance.list_public_knowledge_graphs(term=term)
        print("The response of KnowledgeGraphsApi->list_public_knowledge_graphs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeGraphsApi->list_public_knowledge_graphs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | [**object**](.md)|  | [optional] 

### Return type

**List[object]**

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

# **update_project_knowledge_graph_metadata**
> object update_project_knowledge_graph_metadata(bag_key, proj_key, body)

Update Project Knowledge Graph Metadata

Update the metadata of a Knowledge graph

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
    api_instance = deepsearch.cps.apis.public_v2.KnowledgeGraphsApi(api_client)
    bag_key = None # object | 
    proj_key = 'proj_key_example' # str | 
    body = None # object | 

    try:
        # Update Project Knowledge Graph Metadata
        api_response = api_instance.update_project_knowledge_graph_metadata(bag_key, proj_key, body)
        print("The response of KnowledgeGraphsApi->update_project_knowledge_graph_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeGraphsApi->update_project_knowledge_graph_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bag_key** | [**object**](.md)|  | 
 **proj_key** | **str**|  | 
 **body** | **object**|  | 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

