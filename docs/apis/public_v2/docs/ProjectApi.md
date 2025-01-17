# deepsearch.cps.apis.public_v2.ProjectApi

All URIs are relative to */api/cps/public/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert_document**](ProjectApi.md#convert_document) | **POST** /project/{proj_key}/convert | Convert Document
[**delete_project_integration_config_genai**](ProjectApi.md#delete_project_integration_config_genai) | **DELETE** /project/{proj_key}/integrations/genai | Delete Project Integration Config Genai
[**get_convert_task**](ProjectApi.md#get_convert_task) | **GET** /project/{proj_key}/convert_tasks/{task_id} | Get Convert Task
[**get_project_default_values**](ProjectApi.md#get_project_default_values) | **GET** /project/{proj_key}/default_values | Get Project Default Values
[**get_project_integration_config_genai**](ProjectApi.md#get_project_integration_config_genai) | **GET** /project/{proj_key}/integrations/genai | Get Project Integration Config Genai
[**provision_project_packages**](ProjectApi.md#provision_project_packages) | **POST** /project/{proj_key}/packages | Provision Project Packages
[**update_project_default_values**](ProjectApi.md#update_project_default_values) | **POST** /project/{proj_key}/default_values | Update Project Default Values
[**update_project_integration_config_genai**](ProjectApi.md#update_project_integration_config_genai) | **POST** /project/{proj_key}/integrations/genai | Update Project Integration Config Genai


# **convert_document**
> CpsTask convert_document(proj_key, convert_document_request)

Convert Document

Convert a document directly with Docling.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.convert_document_request import ConvertDocumentRequest
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
    api_instance = deepsearch.cps.apis.public_v2.ProjectApi(api_client)
    proj_key = 'proj_key_example' # str | 
    convert_document_request = deepsearch.cps.apis.public_v2.ConvertDocumentRequest() # ConvertDocumentRequest | 

    try:
        # Convert Document
        api_response = api_instance.convert_document(proj_key, convert_document_request)
        print("The response of ProjectApi->convert_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->convert_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **convert_document_request** | [**ConvertDocumentRequest**](ConvertDocumentRequest.md)|  | 

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

# **delete_project_integration_config_genai**
> delete_project_integration_config_genai(proj_key)

Delete Project Integration Config Genai

Delete the GenAI config for a given project integration.

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
    api_instance = deepsearch.cps.apis.public_v2.ProjectApi(api_client)
    proj_key = 'proj_key_example' # str | 

    try:
        # Delete Project Integration Config Genai
        api_instance.delete_project_integration_config_genai(proj_key)
    except Exception as e:
        print("Exception when calling ProjectApi->delete_project_integration_config_genai: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_convert_task**
> TaskResult get_convert_task(task_id, proj_key, wait=wait)

Get Convert Task

Check status of a Docling conversion task; return presign urls for MD and JSON file if finished conversion successfully.

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
    api_instance = deepsearch.cps.apis.public_v2.ProjectApi(api_client)
    task_id = 'task_id_example' # str | 
    proj_key = 'proj_key_example' # str | 
    wait = deepsearch.cps.apis.public_v2.Wait() # Wait | Optionally block this method call for a few seconds to wait for the result instead of polling through multiple calls. (optional)

    try:
        # Get Convert Task
        api_response = api_instance.get_convert_task(task_id, proj_key, wait=wait)
        print("The response of ProjectApi->get_convert_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_convert_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 
 **proj_key** | **str**|  | 
 **wait** | [**Wait**](.md)| Optionally block this method call for a few seconds to wait for the result instead of polling through multiple calls. | [optional] 

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

# **get_project_default_values**
> DefaultValues get_project_default_values(proj_key)

Get Project Default Values

List project's default values.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.default_values import DefaultValues
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
    api_instance = deepsearch.cps.apis.public_v2.ProjectApi(api_client)
    proj_key = 'proj_key_example' # str | 

    try:
        # Get Project Default Values
        api_response = api_instance.get_project_default_values(proj_key)
        print("The response of ProjectApi->get_project_default_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_project_default_values: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 

### Return type

[**DefaultValues**](DefaultValues.md)

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

# **get_project_integration_config_genai**
> ResponseGetProjectIntegrationConfigGenai get_project_integration_config_genai(proj_key, decode_secrets=decode_secrets)

Get Project Integration Config Genai

Get the GenAI config for a given project.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.response_get_project_integration_config_genai import ResponseGetProjectIntegrationConfigGenai
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
    api_instance = deepsearch.cps.apis.public_v2.ProjectApi(api_client)
    proj_key = 'proj_key_example' # str | 
    decode_secrets = deepsearch.cps.apis.public_v2.DecodeSecrets() # DecodeSecrets |  (optional)

    try:
        # Get Project Integration Config Genai
        api_response = api_instance.get_project_integration_config_genai(proj_key, decode_secrets=decode_secrets)
        print("The response of ProjectApi->get_project_integration_config_genai:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_project_integration_config_genai: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **decode_secrets** | [**DecodeSecrets**](.md)|  | [optional] 

### Return type

[**ResponseGetProjectIntegrationConfigGenai**](ResponseGetProjectIntegrationConfigGenai.md)

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

# **provision_project_packages**
> TaskContext provision_project_packages(proj_key, project_package_instalation_manifest)

Provision Project Packages

Install packages on a project.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.project_package_instalation_manifest import ProjectPackageInstalationManifest
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
    api_instance = deepsearch.cps.apis.public_v2.ProjectApi(api_client)
    proj_key = 'proj_key_example' # str | 
    project_package_instalation_manifest = deepsearch.cps.apis.public_v2.ProjectPackageInstalationManifest() # ProjectPackageInstalationManifest | 

    try:
        # Provision Project Packages
        api_response = api_instance.provision_project_packages(proj_key, project_package_instalation_manifest)
        print("The response of ProjectApi->provision_project_packages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->provision_project_packages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **project_package_instalation_manifest** | [**ProjectPackageInstalationManifest**](ProjectPackageInstalationManifest.md)|  | 

### Return type

[**TaskContext**](TaskContext.md)

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

# **update_project_default_values**
> object update_project_default_values(proj_key, default_values)

Update Project Default Values

Update project's default values.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.default_values import DefaultValues
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
    api_instance = deepsearch.cps.apis.public_v2.ProjectApi(api_client)
    proj_key = 'proj_key_example' # str | 
    default_values = deepsearch.cps.apis.public_v2.DefaultValues() # DefaultValues | 

    try:
        # Update Project Default Values
        api_response = api_instance.update_project_default_values(proj_key, default_values)
        print("The response of ProjectApi->update_project_default_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->update_project_default_values: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **default_values** | [**DefaultValues**](DefaultValues.md)|  | 

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

# **update_project_integration_config_genai**
> update_project_integration_config_genai(proj_key, config)

Update Project Integration Config Genai

Update the GenAI config for a given project.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.config import Config
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
    api_instance = deepsearch.cps.apis.public_v2.ProjectApi(api_client)
    proj_key = 'proj_key_example' # str | 
    config = deepsearch.cps.apis.public_v2.Config() # Config | 

    try:
        # Update Project Integration Config Genai
        api_instance.update_project_integration_config_genai(proj_key, config)
    except Exception as e:
        print("Exception when calling ProjectApi->update_project_integration_config_genai: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **config** | [**Config**](Config.md)|  | 

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

