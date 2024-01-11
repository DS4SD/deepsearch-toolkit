# deepsearch.cps.apis.public.DataIndicesApi

All URIs are relative to *http://localhost/api/cps/public/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ccs_convert_upload_file_project_data_index**](DataIndicesApi.md#ccs_convert_upload_file_project_data_index) | **POST** /project/{proj_key}/data_indices/{index_key}/actions/ccs_convert_upload | 
[**create_project_data_index**](DataIndicesApi.md#create_project_data_index) | **POST** /project/{proj_key}/data_indices | 
[**create_project_data_index_delete_token**](DataIndicesApi.md#create_project_data_index_delete_token) | **POST** /project/{proj_key}/data_indices/{index_key}/delete_token | 
[**delete_project_data_index**](DataIndicesApi.md#delete_project_data_index) | **DELETE** /project/{proj_key}/data_indices/{index_key} | 
[**get_attachment_upload_data**](DataIndicesApi.md#get_attachment_upload_data) | **GET** /project/{proj_key}/data_indices/{index_key}/documents/{index_item_id}/attachment_url/{filename} | 
[**get_project_data_index**](DataIndicesApi.md#get_project_data_index) | **GET** /project/{proj_key}/data_indices/{index_key} | 
[**get_project_data_indices**](DataIndicesApi.md#get_project_data_indices) | **GET** /project/{proj_key}/data_indices | 
[**html_print_convert_upload**](DataIndicesApi.md#html_print_convert_upload) | **POST** /project/{proj_key}/data_indices/{index_key}/actions/html_print_convert_upload | 
[**register_attachment**](DataIndicesApi.md#register_attachment) | **POST** /project/{proj_key}/data_indices/{index_key}/documents/{index_item_id}/attachment | 
[**update_project_data_index**](DataIndicesApi.md#update_project_data_index) | **PATCH** /project/{proj_key}/data_indices/{index_key} | 
[**upload_project_data_index_file**](DataIndicesApi.md#upload_project_data_index_file) | **POST** /project/{proj_key}/data_indices/{index_key}/actions/upload | 


# **ccs_convert_upload_file_project_data_index**
> CpsTask ccs_convert_upload_file_project_data_index(proj_key, index_key, body)



Convert files via CCS and upload to a project data index (only for indices with 'deepsearch-doc' schema)

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
    api_instance = deepsearch.cps.apis.public.DataIndicesApi(api_client)
    proj_key = 'proj_key_example' # str | 
index_key = 'index_key_example' # str | 
body = deepsearch.cps.apis.public.DataIndexUploadFileSource() # DataIndexUploadFileSource | 

    try:
        api_response = api_instance.ccs_convert_upload_file_project_data_index(proj_key, index_key, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataIndicesApi->ccs_convert_upload_file_project_data_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **index_key** | **str**|  | 
 **body** | [**DataIndexUploadFileSource**](DataIndexUploadFileSource.md)|  | 

### Return type

[**CpsTask**](CpsTask.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CPS task info |  -  |
**404** | Project data index not found. |  -  |
**500** | Error occured on the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_data_index**
> ProjectDataIndexWithStatus create_project_data_index(proj_key, data)



Create a project data index

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
    api_instance = deepsearch.cps.apis.public.DataIndicesApi(api_client)
    proj_key = 'proj_key_example' # str | 
data = None # object | 

    try:
        api_response = api_instance.create_project_data_index(proj_key, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataIndicesApi->create_project_data_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **data** | **object**|  | 

### Return type

[**ProjectDataIndexWithStatus**](ProjectDataIndexWithStatus.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project data index. |  -  |
**404** | Project data index not found. |  -  |
**500** | Error occured on the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_data_index_delete_token**
> TokenResponse create_project_data_index_delete_token(proj_key, index_key)



Get a token used to confirm the deletion of a project data index.

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
    api_instance = deepsearch.cps.apis.public.DataIndicesApi(api_client)
    proj_key = 'proj_key_example' # str | 
index_key = 'index_key_example' # str | 

    try:
        api_response = api_instance.create_project_data_index_delete_token(proj_key, index_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataIndicesApi->create_project_data_index_delete_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **index_key** | **str**|  | 

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
**200** | Project data index deletion token. |  -  |
**404** | Data flow template not found. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_data_index**
> delete_project_data_index(proj_key, index_key, confirmation_token)



Delete a project index data

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
    api_instance = deepsearch.cps.apis.public.DataIndicesApi(api_client)
    proj_key = 'proj_key_example' # str | 
index_key = 'index_key_example' # str | 
confirmation_token = 'confirmation_token_example' # str | The delete confirmation token

    try:
        api_instance.delete_project_data_index(proj_key, index_key, confirmation_token)
    except ApiException as e:
        print("Exception when calling DataIndicesApi->delete_project_data_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **index_key** | **str**|  | 
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
**200** | Project data index deleted successfully. |  -  |
**404** | Project data index not found. |  -  |
**500** | Error occured on the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachment_upload_data**
> AttachmentUploadData get_attachment_upload_data(proj_key, index_key, index_item_id, filename)



Get url and path to upload an attachment to a project data index

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
    api_instance = deepsearch.cps.apis.public.DataIndicesApi(api_client)
    proj_key = 'proj_key_example' # str | 
index_key = 'index_key_example' # str | 
index_item_id = 'index_item_id_example' # str | 
filename = 'filename_example' # str | 

    try:
        api_response = api_instance.get_attachment_upload_data(proj_key, index_key, index_item_id, filename)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataIndicesApi->get_attachment_upload_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **index_key** | **str**|  | 
 **index_item_id** | **str**|  | 
 **filename** | **str**|  | 

### Return type

[**AttachmentUploadData**](AttachmentUploadData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attachment upload url and path |  -  |
**404** | Project data index or document ID not found. |  -  |
**500** | Error occured on the server |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_data_index**
> ProjectDataIndexWithStatus get_project_data_index(proj_key, index_key)



Get project data index

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
    api_instance = deepsearch.cps.apis.public.DataIndicesApi(api_client)
    proj_key = 'proj_key_example' # str | 
index_key = 'index_key_example' # str | 

    try:
        api_response = api_instance.get_project_data_index(proj_key, index_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataIndicesApi->get_project_data_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **index_key** | **str**|  | 

### Return type

[**ProjectDataIndexWithStatus**](ProjectDataIndexWithStatus.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project data index. |  -  |
**404** | Project data index not found. |  -  |
**500** | Error occured on the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_data_indices**
> list[ProjectDataIndexWithStatus] get_project_data_indices(proj_key)



Get project data indices

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
    api_instance = deepsearch.cps.apis.public.DataIndicesApi(api_client)
    proj_key = 'proj_key_example' # str | 

    try:
        api_response = api_instance.get_project_data_indices(proj_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataIndicesApi->get_project_data_indices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 

### Return type

[**list[ProjectDataIndexWithStatus]**](ProjectDataIndexWithStatus.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project data indices. |  -  |
**404** | Project data index not found. |  -  |
**500** | Error occured on the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **html_print_convert_upload**
> CpsTask html_print_convert_upload(proj_key, index_key, body)



Convert a list of HTML pages to PDF, convert them via CCS and upload to a project data index (only for indices with 'deepsearch-doc' schema)

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
    api_instance = deepsearch.cps.apis.public.DataIndicesApi(api_client)
    proj_key = 'proj_key_example' # str | 
index_key = 'index_key_example' # str | 
body = deepsearch.cps.apis.public.DataIndexUploadFileSource1() # DataIndexUploadFileSource1 | 

    try:
        api_response = api_instance.html_print_convert_upload(proj_key, index_key, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataIndicesApi->html_print_convert_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **index_key** | **str**|  | 
 **body** | [**DataIndexUploadFileSource1**](DataIndexUploadFileSource1.md)|  | 

### Return type

[**CpsTask**](CpsTask.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CPS task info |  -  |
**404** | Project data index not found. |  -  |
**500** | Error occured on the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_attachment**
> register_attachment(proj_key, index_key, index_item_id, params)



Notify upload completion of an attachment to a project data index

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
    api_instance = deepsearch.cps.apis.public.DataIndicesApi(api_client)
    proj_key = 'proj_key_example' # str | 
index_key = 'index_key_example' # str | 
index_item_id = 'index_item_id_example' # str | 
params = deepsearch.cps.apis.public.InlineObject5() # InlineObject5 | 

    try:
        api_instance.register_attachment(proj_key, index_key, index_item_id, params)
    except ApiException as e:
        print("Exception when calling DataIndicesApi->register_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **index_key** | **str**|  | 
 **index_item_id** | **str**|  | 
 **params** | [**InlineObject5**](InlineObject5.md)|  | 

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
**204** | Attachment notify successfull |  -  |
**404** | Project data index or document ID not found. |  -  |
**500** | Error occured on the server |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_data_index**
> ProjectDataIndexWithStatus update_project_data_index(proj_key, index_key, data)



Update a project data index

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
    api_instance = deepsearch.cps.apis.public.DataIndicesApi(api_client)
    proj_key = 'proj_key_example' # str | 
index_key = 'index_key_example' # str | 
data = None # object | 

    try:
        api_response = api_instance.update_project_data_index(proj_key, index_key, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataIndicesApi->update_project_data_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **index_key** | **str**|  | 
 **data** | **object**|  | 

### Return type

[**ProjectDataIndexWithStatus**](ProjectDataIndexWithStatus.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated project data index. |  -  |
**404** | Project data index not found. |  -  |
**500** | Error occured on the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_project_data_index_file**
> CpsTask upload_project_data_index_file(proj_key, index_key, params)



Upload a file to a project data index

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
    api_instance = deepsearch.cps.apis.public.DataIndicesApi(api_client)
    proj_key = 'proj_key_example' # str | 
index_key = 'index_key_example' # str | 
params = deepsearch.cps.apis.public.InlineObject4() # InlineObject4 | 

    try:
        api_response = api_instance.upload_project_data_index_file(proj_key, index_key, params)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataIndicesApi->upload_project_data_index_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **index_key** | **str**|  | 
 **params** | [**InlineObject4**](InlineObject4.md)|  | 

### Return type

[**CpsTask**](CpsTask.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CPS task info |  -  |
**404** | Project data index not found. |  -  |
**500** | Error occured on the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

