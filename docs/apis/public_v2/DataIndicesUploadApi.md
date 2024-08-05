# deepsearch.cps.apis.public_v2.DataIndicesUploadApi

All URIs are relative to */api/cps/public/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ccs_convert_file_project_data_index**](DataIndicesUploadApi.md#ccs_convert_file_project_data_index) | **POST** /project/{proj_key}/data_indices/{index_key}/actions/ccs_convert | Ccs Convert File Project Data Index
[**ccs_convert_upload_file_project_data_index**](DataIndicesUploadApi.md#ccs_convert_upload_file_project_data_index) | **POST** /project/{proj_key}/data_indices/{index_key}/actions/ccs_convert_upload | Ccs Convert Upload File Project Data Index
[**get_attachment_upload_data**](DataIndicesUploadApi.md#get_attachment_upload_data) | **GET** /project/{proj_key}/data_indices/{index_key}/documents/{index_item_id}/attachment_url/{filename} | Get Attachment Upload Data
[**html_print_convert_upload**](DataIndicesUploadApi.md#html_print_convert_upload) | **POST** /project/{proj_key}/data_indices/{index_key}/actions/html_print_convert_upload | Html Print Convert Upload
[**load_project_data_index_files_elastic**](DataIndicesUploadApi.md#load_project_data_index_files_elastic) | **POST** /project/{proj_key}/data_indices/{index_key}/actions/load_elastic | Load Project Data Index Files Elastic
[**register_attachment**](DataIndicesUploadApi.md#register_attachment) | **POST** /project/{proj_key}/data_indices/{index_key}/documents/{index_item_id}/attachment | Register Attachment
[**upload_project_data_index_file**](DataIndicesUploadApi.md#upload_project_data_index_file) | **POST** /project/{proj_key}/data_indices/{index_key}/actions/upload | Upload Project Data Index File
[**upload_register_project_documents**](DataIndicesUploadApi.md#upload_register_project_documents) | **POST** /project/{proj_key}/data_indices/{index_key}/actions/upload_register_documents | Upload Register Project Documents


# **ccs_convert_file_project_data_index**
> CpsTask ccs_convert_file_project_data_index(index_key, proj_key, convert_documents_request_body)

Ccs Convert File Project Data Index

Convert files via CCS previously registered and in a project data index.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.convert_documents_request_body import ConvertDocumentsRequestBody
from deepsearch.cps.apis.public_v2.models.cps_task import CpsTask
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
    api_instance = deepsearch.cps.apis.public_v2.DataIndicesUploadApi(api_client)
    index_key = 'index_key_example' # str | 
    proj_key = 'proj_key_example' # str | 
    convert_documents_request_body = deepsearch.cps.apis.public_v2.ConvertDocumentsRequestBody() # ConvertDocumentsRequestBody | 

    try:
        # Ccs Convert File Project Data Index
        api_response = api_instance.ccs_convert_file_project_data_index(index_key, proj_key, convert_documents_request_body)
        print("The response of DataIndicesUploadApi->ccs_convert_file_project_data_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataIndicesUploadApi->ccs_convert_file_project_data_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_key** | **str**|  | 
 **proj_key** | **str**|  | 
 **convert_documents_request_body** | [**ConvertDocumentsRequestBody**](ConvertDocumentsRequestBody.md)|  | 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ccs_convert_upload_file_project_data_index**
> CpsTask ccs_convert_upload_file_project_data_index(index_key, proj_key, convert_upload_documents_request_body)

Ccs Convert Upload File Project Data Index

Convert files via CCS and upload to a project data index (only for indices with 'deepsearch-doc' schema).

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.convert_upload_documents_request_body import ConvertUploadDocumentsRequestBody
from deepsearch.cps.apis.public_v2.models.cps_task import CpsTask
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
    api_instance = deepsearch.cps.apis.public_v2.DataIndicesUploadApi(api_client)
    index_key = 'index_key_example' # str | 
    proj_key = 'proj_key_example' # str | 
    convert_upload_documents_request_body = deepsearch.cps.apis.public_v2.ConvertUploadDocumentsRequestBody() # ConvertUploadDocumentsRequestBody | 

    try:
        # Ccs Convert Upload File Project Data Index
        api_response = api_instance.ccs_convert_upload_file_project_data_index(index_key, proj_key, convert_upload_documents_request_body)
        print("The response of DataIndicesUploadApi->ccs_convert_upload_file_project_data_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataIndicesUploadApi->ccs_convert_upload_file_project_data_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_key** | **str**|  | 
 **proj_key** | **str**|  | 
 **convert_upload_documents_request_body** | [**ConvertUploadDocumentsRequestBody**](ConvertUploadDocumentsRequestBody.md)|  | 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachment_upload_data**
> AttachmentUploadData get_attachment_upload_data(index_key, index_item_id, filename, proj_key)

Get Attachment Upload Data

Get url and path to upload an attachment to a project data index.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.attachment_upload_data import AttachmentUploadData
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
    api_instance = deepsearch.cps.apis.public_v2.DataIndicesUploadApi(api_client)
    index_key = 'index_key_example' # str | 
    index_item_id = 'index_item_id_example' # str | 
    filename = 'filename_example' # str | 
    proj_key = 'proj_key_example' # str | 

    try:
        # Get Attachment Upload Data
        api_response = api_instance.get_attachment_upload_data(index_key, index_item_id, filename, proj_key)
        print("The response of DataIndicesUploadApi->get_attachment_upload_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataIndicesUploadApi->get_attachment_upload_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_key** | **str**|  | 
 **index_item_id** | **str**|  | 
 **filename** | **str**|  | 
 **proj_key** | **str**|  | 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **html_print_convert_upload**
> CpsTask html_print_convert_upload(index_key, proj_key, data_index_upload_file_source)

Html Print Convert Upload

Convert a list of HTML pages to PDF, convert them via CCS and upload to a project data index (only for indices with 'deepsearch-doc' schema).

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.cps_task import CpsTask
from deepsearch.cps.apis.public_v2.models.data_index_upload_file_source import DataIndexUploadFileSource
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
    api_instance = deepsearch.cps.apis.public_v2.DataIndicesUploadApi(api_client)
    index_key = 'index_key_example' # str | 
    proj_key = 'proj_key_example' # str | 
    data_index_upload_file_source = deepsearch.cps.apis.public_v2.DataIndexUploadFileSource() # DataIndexUploadFileSource | 

    try:
        # Html Print Convert Upload
        api_response = api_instance.html_print_convert_upload(index_key, proj_key, data_index_upload_file_source)
        print("The response of DataIndicesUploadApi->html_print_convert_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataIndicesUploadApi->html_print_convert_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_key** | **str**|  | 
 **proj_key** | **str**|  | 
 **data_index_upload_file_source** | [**DataIndexUploadFileSource**](DataIndexUploadFileSource.md)|  | 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_project_data_index_files_elastic**
> CpsTask load_project_data_index_files_elastic(index_key, proj_key, upload_elastic_request_body)

Load Project Data Index Files Elastic

Load file(s) in a project data index to elastic.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.cps_task import CpsTask
from deepsearch.cps.apis.public_v2.models.upload_elastic_request_body import UploadElasticRequestBody
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
    api_instance = deepsearch.cps.apis.public_v2.DataIndicesUploadApi(api_client)
    index_key = 'index_key_example' # str | 
    proj_key = 'proj_key_example' # str | 
    upload_elastic_request_body = deepsearch.cps.apis.public_v2.UploadElasticRequestBody() # UploadElasticRequestBody | 

    try:
        # Load Project Data Index Files Elastic
        api_response = api_instance.load_project_data_index_files_elastic(index_key, proj_key, upload_elastic_request_body)
        print("The response of DataIndicesUploadApi->load_project_data_index_files_elastic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataIndicesUploadApi->load_project_data_index_files_elastic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_key** | **str**|  | 
 **proj_key** | **str**|  | 
 **upload_elastic_request_body** | [**UploadElasticRequestBody**](UploadElasticRequestBody.md)|  | 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_attachment**
> register_attachment(index_key, index_item_id, proj_key, attachment_upload_request_body)

Register Attachment

Notify upload completion of an attachment to a project data index.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.attachment_upload_request_body import AttachmentUploadRequestBody
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
    api_instance = deepsearch.cps.apis.public_v2.DataIndicesUploadApi(api_client)
    index_key = 'index_key_example' # str | 
    index_item_id = 'index_item_id_example' # str | 
    proj_key = 'proj_key_example' # str | 
    attachment_upload_request_body = deepsearch.cps.apis.public_v2.AttachmentUploadRequestBody() # AttachmentUploadRequestBody | 

    try:
        # Register Attachment
        api_instance.register_attachment(index_key, index_item_id, proj_key, attachment_upload_request_body)
    except Exception as e:
        print("Exception when calling DataIndicesUploadApi->register_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_key** | **str**|  | 
 **index_item_id** | **str**|  | 
 **proj_key** | **str**|  | 
 **attachment_upload_request_body** | [**AttachmentUploadRequestBody**](AttachmentUploadRequestBody.md)|  | 

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

# **upload_project_data_index_file**
> CpsTask upload_project_data_index_file(index_key, proj_key, json_upload_request_body)

Upload Project Data Index File

Upload a file to a project data index.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.cps_task import CpsTask
from deepsearch.cps.apis.public_v2.models.json_upload_request_body import JsonUploadRequestBody
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
    api_instance = deepsearch.cps.apis.public_v2.DataIndicesUploadApi(api_client)
    index_key = 'index_key_example' # str | 
    proj_key = 'proj_key_example' # str | 
    json_upload_request_body = deepsearch.cps.apis.public_v2.JsonUploadRequestBody() # JsonUploadRequestBody | 

    try:
        # Upload Project Data Index File
        api_response = api_instance.upload_project_data_index_file(index_key, proj_key, json_upload_request_body)
        print("The response of DataIndicesUploadApi->upload_project_data_index_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataIndicesUploadApi->upload_project_data_index_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_key** | **str**|  | 
 **proj_key** | **str**|  | 
 **json_upload_request_body** | [**JsonUploadRequestBody**](JsonUploadRequestBody.md)|  | 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_register_project_documents**
> CpsTask upload_register_project_documents(index_key, proj_key, convert_documents_sources)

Upload Register Project Documents

Upload and register documents to be converted later.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.convert_documents_sources import ConvertDocumentsSources
from deepsearch.cps.apis.public_v2.models.cps_task import CpsTask
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
    api_instance = deepsearch.cps.apis.public_v2.DataIndicesUploadApi(api_client)
    index_key = 'index_key_example' # str | 
    proj_key = 'proj_key_example' # str | 
    convert_documents_sources = deepsearch.cps.apis.public_v2.ConvertDocumentsSources() # ConvertDocumentsSources | 

    try:
        # Upload Register Project Documents
        api_response = api_instance.upload_register_project_documents(index_key, proj_key, convert_documents_sources)
        print("The response of DataIndicesUploadApi->upload_register_project_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataIndicesUploadApi->upload_register_project_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_key** | **str**|  | 
 **proj_key** | **str**|  | 
 **convert_documents_sources** | [**ConvertDocumentsSources**](ConvertDocumentsSources.md)|  | 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

