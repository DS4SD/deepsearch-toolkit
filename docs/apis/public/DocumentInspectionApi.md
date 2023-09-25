# deepsearch.cps.apis.public.DocumentInspectionApi

All URIs are relative to *http://localhost/api/cps/public/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**annotate_document**](DocumentInspectionApi.md#annotate_document) | **POST** /project/{proj_key}/annotate/document | 
[**delete_document_annotation_result**](DocumentInspectionApi.md#delete_document_annotation_result) | **DELETE** /project/{proj_key}/annotate/document/results/{document_hash} | 
[**get_annotate_document_result**](DocumentInspectionApi.md#get_annotate_document_result) | **GET** /project/{proj_key}/annotate/document/tasks/{task_id} | 
[**ingest_documentqa**](DocumentInspectionApi.md#ingest_documentqa) | **POST** /project/{proj_key}/ingest/documentqa | 
[**list_project_inspection_report**](DocumentInspectionApi.md#list_project_inspection_report) | **GET** /project/{proj_key}/annotate/inspection_report | 
[**report_inspected_document**](DocumentInspectionApi.md#report_inspected_document) | **POST** /project/{proj_key}/annotate/document/report | 


# **annotate_document**
> Task annotate_document(proj_key, body)



Run an annotator on a document

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
    api_instance = deepsearch.cps.apis.public.DocumentInspectionApi(api_client)
    proj_key = 'proj_key_example' # str | 
body = deepsearch.cps.apis.public.AnnotateDocumentRequest() # AnnotateDocumentRequest | 

    try:
        api_response = api_instance.annotate_document(proj_key, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentInspectionApi->annotate_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **body** | [**AnnotateDocumentRequest**](AnnotateDocumentRequest.md)|  | 

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
**200** | OK |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document_annotation_result**
> delete_document_annotation_result(proj_key, document_hash)



Delete annotation results for a document

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
    api_instance = deepsearch.cps.apis.public.DocumentInspectionApi(api_client)
    proj_key = 'proj_key_example' # str | 
document_hash = 'document_hash_example' # str | 

    try:
        api_instance.delete_document_annotation_result(proj_key, document_hash)
    except ApiException as e:
        print("Exception when calling DocumentInspectionApi->delete_document_annotation_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **document_hash** | **str**|  | 

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
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_annotate_document_result**
> InlineResponse2002 get_annotate_document_result(proj_key, task_id, wait=wait)



Get the result of a previous document annotation

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
    api_instance = deepsearch.cps.apis.public.DocumentInspectionApi(api_client)
    proj_key = 'proj_key_example' # str | 
task_id = 'task_id_example' # str | 
wait = 3.4 # float | Allow the response to be delayed for a few seconds to wait for the result, instead of doing client-side polling. (optional)

    try:
        api_response = api_instance.get_annotate_document_result(proj_key, task_id, wait=wait)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentInspectionApi->get_annotate_document_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **task_id** | **str**|  | 
 **wait** | **float**| Allow the response to be delayed for a few seconds to wait for the result, instead of doing client-side polling. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ingest_documentqa**
> Task ingest_documentqa(proj_key, body)



Ingest a document for QA

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
    api_instance = deepsearch.cps.apis.public.DocumentInspectionApi(api_client)
    proj_key = 'proj_key_example' # str | 
body = deepsearch.cps.apis.public.IngestDocumentQARequest() # IngestDocumentQARequest | 

    try:
        api_response = api_instance.ingest_documentqa(proj_key, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentInspectionApi->ingest_documentqa: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **body** | [**IngestDocumentQARequest**](IngestDocumentQARequest.md)|  | 

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
**200** | OK |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_inspection_report**
> list[InspectionReport] list_project_inspection_report(proj_key, page=page, items_per_page=items_per_page, search_string=search_string, begin_date=begin_date, end_date=end_date)



Get paginated list of inspection reports for a project

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
    api_instance = deepsearch.cps.apis.public.DocumentInspectionApi(api_client)
    proj_key = 'proj_key_example' # str | 
page = 56 # int | page of the result list (optional)
items_per_page = 20 # int | items on one page of the result list (optional) (default to 20)
search_string = 'search_string_example' # str | search keyword (optional)
begin_date = 56 # int | begin date of the search date interval (optional)
end_date = 56 # int | end date of the search date interval (optional)

    try:
        api_response = api_instance.list_project_inspection_report(proj_key, page=page, items_per_page=items_per_page, search_string=search_string, begin_date=begin_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentInspectionApi->list_project_inspection_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **page** | **int**| page of the result list | [optional] 
 **items_per_page** | **int**| items on one page of the result list | [optional] [default to 20]
 **search_string** | **str**| search keyword | [optional] 
 **begin_date** | **int**| begin date of the search date interval | [optional] 
 **end_date** | **int**| end date of the search date interval | [optional] 

### Return type

[**list[InspectionReport]**](InspectionReport.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reports |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_inspected_document**
> Task report_inspected_document(proj_key, body)



Submit a report on an inspected document

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
    api_instance = deepsearch.cps.apis.public.DocumentInspectionApi(api_client)
    proj_key = 'proj_key_example' # str | 
body = deepsearch.cps.apis.public.AnnotatedDocumentReport() # AnnotatedDocumentReport | 

    try:
        api_response = api_instance.report_inspected_document(proj_key, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentInspectionApi->report_inspected_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **body** | [**AnnotatedDocumentReport**](AnnotatedDocumentReport.md)|  | 

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
**200** | OK |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

