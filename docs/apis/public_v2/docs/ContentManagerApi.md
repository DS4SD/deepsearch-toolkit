# deepsearch.cps.apis.public_v2.ContentManagerApi

All URIs are relative to */api/cps/public/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_project_data_index_document_metadata**](ContentManagerApi.md#add_project_data_index_document_metadata) | **POST** /project/{proj_key}/data_indices/{index_key}/documents/{document_hash}/metadata | Add Project Data Index Document Metadata
[**get_all_project_data_index_documents**](ContentManagerApi.md#get_all_project_data_index_documents) | **GET** /project/{proj_key}/data_indices/{index_key}/documents/ | Get All Project Data Index Documents
[**get_project_agents**](ContentManagerApi.md#get_project_agents) | **GET** /project/{proj_key}/data_indices/documents/agents | Get Project Agents
[**get_project_conversion_statistics**](ContentManagerApi.md#get_project_conversion_statistics) | **GET** /project/{proj_key}/data_indices/{index_key}/documents/statistics | Get Project Conversion Statistics
[**get_project_data_index_document_artifacts**](ContentManagerApi.md#get_project_data_index_document_artifacts) | **GET** /project/{proj_key}/data_indices/{index_key}/documents/{document_hash}/artifacts | Get Project Data Index Document Artifacts
[**get_project_data_index_document_events**](ContentManagerApi.md#get_project_data_index_document_events) | **GET** /project/{proj_key}/data_indices/{index_key}/documents/{document_hash}/doc_events | Get Project Data Index Document Events
[**get_project_data_index_document_markdown**](ContentManagerApi.md#get_project_data_index_document_markdown) | **GET** /project/{proj_key}/data_indices/{index_key}/documents/{document_hash}/Markdown | Get Project Data Index Document Markdown
[**get_project_data_index_document_metadata**](ContentManagerApi.md#get_project_data_index_document_metadata) | **GET** /project/{proj_key}/data_indices/{index_key}/documents/{document_hash}/metadata | Get Project Data Index Document Metadata
[**get_project_data_index_documents**](ContentManagerApi.md#get_project_data_index_documents) | **GET** /project/{proj_key}/data_indices/{index_key}/documents/agent/{agent_name} | Get Project Data Index Documents
[**get_project_data_index_grouped_documents**](ContentManagerApi.md#get_project_data_index_grouped_documents) | **GET** /project/{proj_key}/data_indices/{index_key}/documents/agent/{agent_name}/grouped | Get Project Data Index Grouped Documents
[**get_project_data_index_json_document**](ContentManagerApi.md#get_project_data_index_json_document) | **GET** /project/{proj_key}/data_indices/{index_key}/documents/{document_hash}/JSON | Get Project Data Index Json Document
[**get_project_data_index_pdf_document**](ContentManagerApi.md#get_project_data_index_pdf_document) | **GET** /project/{proj_key}/data_indices/{index_key}/documents/{document_hash}/PDF | Get Project Data Index Pdf Document
[**get_project_documents_by_transaction**](ContentManagerApi.md#get_project_documents_by_transaction) | **GET** /project/{proj_key}/data_indices/{index_key}/documents/transactions/{transaction_id} | Get Project Documents By Transaction
[**get_project_index_upload_jobs**](ContentManagerApi.md#get_project_index_upload_jobs) | **GET** /project/{proj_key}/data_indices/{index_key}/documents/upload_jobs | Get Project Index Upload Jobs


# **add_project_data_index_document_metadata**
> add_project_data_index_document_metadata(index_key, document_hash, proj_key, document_meta)

Add Project Data Index Document Metadata

Insert project document metadata.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.document_meta import DocumentMeta
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
    api_instance = deepsearch.cps.apis.public_v2.ContentManagerApi(api_client)
    index_key = 'index_key_example' # str | 
    document_hash = 'document_hash_example' # str | 
    proj_key = 'proj_key_example' # str | 
    document_meta = deepsearch.cps.apis.public_v2.DocumentMeta() # DocumentMeta | 

    try:
        # Add Project Data Index Document Metadata
        api_instance.add_project_data_index_document_metadata(index_key, document_hash, proj_key, document_meta)
    except Exception as e:
        print("Exception when calling ContentManagerApi->add_project_data_index_document_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_key** | **str**|  | 
 **document_hash** | **str**|  | 
 **proj_key** | **str**|  | 
 **document_meta** | [**DocumentMeta**](DocumentMeta.md)|  | 

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
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_project_data_index_documents**
> ProjectDocuments get_all_project_data_index_documents(index_key, proj_key, page=page, page_size=page_size)

Get All Project Data Index Documents

Get all project documents

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.project_documents import ProjectDocuments
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
    api_instance = deepsearch.cps.apis.public_v2.ContentManagerApi(api_client)
    index_key = 'index_key_example' # str | 
    proj_key = 'proj_key_example' # str | 
    page = 1 # int |  (optional) (default to 1)
    page_size = 25 # int |  (optional) (default to 25)

    try:
        # Get All Project Data Index Documents
        api_response = api_instance.get_all_project_data_index_documents(index_key, proj_key, page=page, page_size=page_size)
        print("The response of ContentManagerApi->get_all_project_data_index_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentManagerApi->get_all_project_data_index_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_key** | **str**|  | 
 **proj_key** | **str**|  | 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 25]

### Return type

[**ProjectDocuments**](ProjectDocuments.md)

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

# **get_project_agents**
> ProjectAgents get_project_agents(proj_key)

Get Project Agents

Get project agents.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.project_agents import ProjectAgents
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
    api_instance = deepsearch.cps.apis.public_v2.ContentManagerApi(api_client)
    proj_key = 'proj_key_example' # str | 

    try:
        # Get Project Agents
        api_response = api_instance.get_project_agents(proj_key)
        print("The response of ContentManagerApi->get_project_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentManagerApi->get_project_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 

### Return type

[**ProjectAgents**](ProjectAgents.md)

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

# **get_project_conversion_statistics**
> DocumentStatistics get_project_conversion_statistics(index_key, proj_key)

Get Project Conversion Statistics

Get project conversion statistics.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.document_statistics import DocumentStatistics
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
    api_instance = deepsearch.cps.apis.public_v2.ContentManagerApi(api_client)
    index_key = 'index_key_example' # str | 
    proj_key = 'proj_key_example' # str | 

    try:
        # Get Project Conversion Statistics
        api_response = api_instance.get_project_conversion_statistics(index_key, proj_key)
        print("The response of ContentManagerApi->get_project_conversion_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentManagerApi->get_project_conversion_statistics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_key** | **str**|  | 
 **proj_key** | **str**|  | 

### Return type

[**DocumentStatistics**](DocumentStatistics.md)

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

# **get_project_data_index_document_artifacts**
> ResponseDocumentArtifacts get_project_data_index_document_artifacts(index_key, document_hash, proj_key)

Get Project Data Index Document Artifacts

Get project document artifacts.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.response_document_artifacts import ResponseDocumentArtifacts
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
    api_instance = deepsearch.cps.apis.public_v2.ContentManagerApi(api_client)
    index_key = 'index_key_example' # str | 
    document_hash = 'document_hash_example' # str | 
    proj_key = 'proj_key_example' # str | 

    try:
        # Get Project Data Index Document Artifacts
        api_response = api_instance.get_project_data_index_document_artifacts(index_key, document_hash, proj_key)
        print("The response of ContentManagerApi->get_project_data_index_document_artifacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentManagerApi->get_project_data_index_document_artifacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_key** | **str**|  | 
 **document_hash** | **str**|  | 
 **proj_key** | **str**|  | 

### Return type

[**ResponseDocumentArtifacts**](ResponseDocumentArtifacts.md)

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

# **get_project_data_index_document_events**
> object get_project_data_index_document_events(index_key, document_hash, proj_key, agent_name=agent_name, status=status)

Get Project Data Index Document Events

Get events of a project document.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.status_filter import StatusFilter
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
    api_instance = deepsearch.cps.apis.public_v2.ContentManagerApi(api_client)
    index_key = 'index_key_example' # str | 
    document_hash = 'document_hash_example' # str | 
    proj_key = 'proj_key_example' # str | 
    agent_name = deepsearch.cps.apis.public_v2.AgentName() # AgentName |  (optional)
    status = deepsearch.cps.apis.public_v2.StatusFilter() # StatusFilter |  (optional)

    try:
        # Get Project Data Index Document Events
        api_response = api_instance.get_project_data_index_document_events(index_key, document_hash, proj_key, agent_name=agent_name, status=status)
        print("The response of ContentManagerApi->get_project_data_index_document_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentManagerApi->get_project_data_index_document_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_key** | **str**|  | 
 **document_hash** | **str**|  | 
 **proj_key** | **str**|  | 
 **agent_name** | [**AgentName**](.md)|  | [optional] 
 **status** | [**StatusFilter**](.md)|  | [optional] 

### Return type

**object**

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

# **get_project_data_index_document_markdown**
> ProjectDocumentURL get_project_data_index_document_markdown(index_key, document_hash, proj_key)

Get Project Data Index Document Markdown

Get project document Markdown.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.project_document_url import ProjectDocumentURL
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
    api_instance = deepsearch.cps.apis.public_v2.ContentManagerApi(api_client)
    index_key = 'index_key_example' # str | 
    document_hash = 'document_hash_example' # str | 
    proj_key = 'proj_key_example' # str | 

    try:
        # Get Project Data Index Document Markdown
        api_response = api_instance.get_project_data_index_document_markdown(index_key, document_hash, proj_key)
        print("The response of ContentManagerApi->get_project_data_index_document_markdown:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentManagerApi->get_project_data_index_document_markdown: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_key** | **str**|  | 
 **document_hash** | **str**|  | 
 **proj_key** | **str**|  | 

### Return type

[**ProjectDocumentURL**](ProjectDocumentURL.md)

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

# **get_project_data_index_document_metadata**
> ProjectDocument get_project_data_index_document_metadata(index_key, document_hash, proj_key)

Get Project Data Index Document Metadata

Get project document metadata.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.project_document import ProjectDocument
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
    api_instance = deepsearch.cps.apis.public_v2.ContentManagerApi(api_client)
    index_key = 'index_key_example' # str | 
    document_hash = 'document_hash_example' # str | 
    proj_key = 'proj_key_example' # str | 

    try:
        # Get Project Data Index Document Metadata
        api_response = api_instance.get_project_data_index_document_metadata(index_key, document_hash, proj_key)
        print("The response of ContentManagerApi->get_project_data_index_document_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentManagerApi->get_project_data_index_document_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_key** | **str**|  | 
 **document_hash** | **str**|  | 
 **proj_key** | **str**|  | 

### Return type

[**ProjectDocument**](ProjectDocument.md)

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

# **get_project_data_index_documents**
> ProjectDocuments get_project_data_index_documents(index_key, agent_name, proj_key, status=status, page=page, page_size=page_size)

Get Project Data Index Documents

Get project documents, can be filter by status.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.project_documents import ProjectDocuments
from deepsearch.cps.apis.public_v2.models.status_filter import StatusFilter
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
    api_instance = deepsearch.cps.apis.public_v2.ContentManagerApi(api_client)
    index_key = 'index_key_example' # str | 
    agent_name = 'agent_name_example' # str | 
    proj_key = 'proj_key_example' # str | 
    status = deepsearch.cps.apis.public_v2.StatusFilter() # StatusFilter |  (optional)
    page = 1 # int |  (optional) (default to 1)
    page_size = 25 # int |  (optional) (default to 25)

    try:
        # Get Project Data Index Documents
        api_response = api_instance.get_project_data_index_documents(index_key, agent_name, proj_key, status=status, page=page, page_size=page_size)
        print("The response of ContentManagerApi->get_project_data_index_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentManagerApi->get_project_data_index_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_key** | **str**|  | 
 **agent_name** | **str**|  | 
 **proj_key** | **str**|  | 
 **status** | [**StatusFilter**](.md)|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 25]

### Return type

[**ProjectDocuments**](ProjectDocuments.md)

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

# **get_project_data_index_grouped_documents**
> ResponseGroupedDocuments get_project_data_index_grouped_documents(index_key, agent_name, proj_key, status=status, page=page, page_size=page_size)

Get Project Data Index Grouped Documents

Get project documents grouped by upload.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.response_grouped_documents import ResponseGroupedDocuments
from deepsearch.cps.apis.public_v2.models.status_filter import StatusFilter
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
    api_instance = deepsearch.cps.apis.public_v2.ContentManagerApi(api_client)
    index_key = 'index_key_example' # str | 
    agent_name = 'agent_name_example' # str | 
    proj_key = 'proj_key_example' # str | 
    status = deepsearch.cps.apis.public_v2.StatusFilter() # StatusFilter |  (optional)
    page = 1 # int |  (optional) (default to 1)
    page_size = 25 # int |  (optional) (default to 25)

    try:
        # Get Project Data Index Grouped Documents
        api_response = api_instance.get_project_data_index_grouped_documents(index_key, agent_name, proj_key, status=status, page=page, page_size=page_size)
        print("The response of ContentManagerApi->get_project_data_index_grouped_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentManagerApi->get_project_data_index_grouped_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_key** | **str**|  | 
 **agent_name** | **str**|  | 
 **proj_key** | **str**|  | 
 **status** | [**StatusFilter**](.md)|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 25]

### Return type

[**ResponseGroupedDocuments**](ResponseGroupedDocuments.md)

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

# **get_project_data_index_json_document**
> object get_project_data_index_json_document(index_key, document_hash, proj_key)

Get Project Data Index Json Document

Get project JSON document.

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
    api_instance = deepsearch.cps.apis.public_v2.ContentManagerApi(api_client)
    index_key = 'index_key_example' # str | 
    document_hash = 'document_hash_example' # str | 
    proj_key = 'proj_key_example' # str | 

    try:
        # Get Project Data Index Json Document
        api_response = api_instance.get_project_data_index_json_document(index_key, document_hash, proj_key)
        print("The response of ContentManagerApi->get_project_data_index_json_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentManagerApi->get_project_data_index_json_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_key** | **str**|  | 
 **document_hash** | **str**|  | 
 **proj_key** | **str**|  | 

### Return type

**object**

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

# **get_project_data_index_pdf_document**
> ProjectDocumentURL get_project_data_index_pdf_document(index_key, document_hash, proj_key)

Get Project Data Index Pdf Document

Get project PDF document.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.project_document_url import ProjectDocumentURL
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
    api_instance = deepsearch.cps.apis.public_v2.ContentManagerApi(api_client)
    index_key = 'index_key_example' # str | 
    document_hash = 'document_hash_example' # str | 
    proj_key = 'proj_key_example' # str | 

    try:
        # Get Project Data Index Pdf Document
        api_response = api_instance.get_project_data_index_pdf_document(index_key, document_hash, proj_key)
        print("The response of ContentManagerApi->get_project_data_index_pdf_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentManagerApi->get_project_data_index_pdf_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_key** | **str**|  | 
 **document_hash** | **str**|  | 
 **proj_key** | **str**|  | 

### Return type

[**ProjectDocumentURL**](ProjectDocumentURL.md)

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

# **get_project_documents_by_transaction**
> ProjectDocuments get_project_documents_by_transaction(index_key, transaction_id, proj_key)

Get Project Documents By Transaction

Get project documents by transaction ID.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.project_documents import ProjectDocuments
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
    api_instance = deepsearch.cps.apis.public_v2.ContentManagerApi(api_client)
    index_key = 'index_key_example' # str | 
    transaction_id = 'transaction_id_example' # str | 
    proj_key = 'proj_key_example' # str | 

    try:
        # Get Project Documents By Transaction
        api_response = api_instance.get_project_documents_by_transaction(index_key, transaction_id, proj_key)
        print("The response of ContentManagerApi->get_project_documents_by_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentManagerApi->get_project_documents_by_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_key** | **str**|  | 
 **transaction_id** | **str**|  | 
 **proj_key** | **str**|  | 

### Return type

[**ProjectDocuments**](ProjectDocuments.md)

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

# **get_project_index_upload_jobs**
> ResponseUploadJobs get_project_index_upload_jobs(index_key, proj_key)

Get Project Index Upload Jobs

Get project upload jobs.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.response_upload_jobs import ResponseUploadJobs
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
    api_instance = deepsearch.cps.apis.public_v2.ContentManagerApi(api_client)
    index_key = 'index_key_example' # str | 
    proj_key = 'proj_key_example' # str | 

    try:
        # Get Project Index Upload Jobs
        api_response = api_instance.get_project_index_upload_jobs(index_key, proj_key)
        print("The response of ContentManagerApi->get_project_index_upload_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentManagerApi->get_project_index_upload_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_key** | **str**|  | 
 **proj_key** | **str**|  | 

### Return type

[**ResponseUploadJobs**](ResponseUploadJobs.md)

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

