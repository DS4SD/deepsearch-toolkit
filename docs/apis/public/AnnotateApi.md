# deepsearch.cps.apis.public.AnnotateApi

All URIs are relative to *http://localhost/api/cps/public/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_project_object_annotations**](AnnotateApi.md#generate_project_object_annotations) | **POST** /project/{proj_key}/object_annotations | 
[**generate_project_object_annotations_async**](AnnotateApi.md#generate_project_object_annotations_async) | **POST** /project/{proj_key}/object_annotations_async | 
[**get_cached_annotator_metadata**](AnnotateApi.md#get_cached_annotator_metadata) | **POST** /project/{proj_key}/annotator/metadata | 
[**get_project_annotator_supported_annotations**](AnnotateApi.md#get_project_annotator_supported_annotations) | **POST** /project/{proj_key}/annotate/supported_annotations | 
[**list_project_inspection_report**](AnnotateApi.md#list_project_inspection_report) | **GET** /project/{proj_key}/annotate/inspection_report | 


# **generate_project_object_annotations**
> AnnotatedObject1 generate_project_object_annotations(proj_key, options)



Run an annotator on an object, using resources from the project. *DEPRECATED*, please use generate_project_object_annotations_async instead. 

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
    api_instance = deepsearch.cps.apis.public.AnnotateApi(api_client)
    proj_key = 'proj_key_example' # str | 
options = deepsearch.cps.apis.public.AnnotateObjectOptions() # AnnotateObjectOptions | 

    try:
        api_response = api_instance.generate_project_object_annotations(proj_key, options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnnotateApi->generate_project_object_annotations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **options** | [**AnnotateObjectOptions**](AnnotateObjectOptions.md)|  | 

### Return type

[**AnnotatedObject1**](AnnotatedObject1.md)

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

# **generate_project_object_annotations_async**
> Task generate_project_object_annotations_async(proj_key, options)



Run an annotator on an object, using resources from the project.

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
    api_instance = deepsearch.cps.apis.public.AnnotateApi(api_client)
    proj_key = 'proj_key_example' # str | 
options = deepsearch.cps.apis.public.AnnotateObjectOptions1() # AnnotateObjectOptions1 | 

    try:
        api_response = api_instance.generate_project_object_annotations_async(proj_key, options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnnotateApi->generate_project_object_annotations_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **options** | [**AnnotateObjectOptions1**](AnnotateObjectOptions1.md)|  | 

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

# **get_cached_annotator_metadata**
> AnnotatorMetadata get_cached_annotator_metadata(proj_key, options)



Get annotator's metadata

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
    api_instance = deepsearch.cps.apis.public.AnnotateApi(api_client)
    proj_key = 'proj_key_example' # str | 
options = None # object | 

    try:
        api_response = api_instance.get_cached_annotator_metadata(proj_key, options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnnotateApi->get_cached_annotator_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **options** | **object**|  | 

### Return type

[**AnnotatorMetadata**](AnnotatorMetadata.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_annotator_supported_annotations**
> SupportedAnnotatorAnnotations get_project_annotator_supported_annotations(proj_key, options)



Get supported annotations for an annotator

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
    api_instance = deepsearch.cps.apis.public.AnnotateApi(api_client)
    proj_key = 'proj_key_example' # str | 
options = None # object | 

    try:
        api_response = api_instance.get_project_annotator_supported_annotations(proj_key, options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnnotateApi->get_project_annotator_supported_annotations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **options** | **object**|  | 

### Return type

[**SupportedAnnotatorAnnotations**](SupportedAnnotatorAnnotations.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

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
    api_instance = deepsearch.cps.apis.public.AnnotateApi(api_client)
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
        print("Exception when calling AnnotateApi->list_project_inspection_report: %s\n" % e)
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

