# deepsearch.cps.apis.public_v2.ProjectApi

All URIs are relative to */api/cps/public/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_project_integration_config**](ProjectApi.md#delete_project_integration_config) | **DELETE** /project/{proj_key}/integrations/{integration_name} | Delete Project Integration Config
[**get_project_default_values**](ProjectApi.md#get_project_default_values) | **GET** /project/{proj_key}/default_values | Get Project Default Values
[**get_project_integration_config**](ProjectApi.md#get_project_integration_config) | **GET** /project/{proj_key}/integrations/{integration_name} | Get Project Integration Config
[**provision_project_packages**](ProjectApi.md#provision_project_packages) | **POST** /project/{proj_key}/packages | Provision Project Packages
[**update_project_default_values**](ProjectApi.md#update_project_default_values) | **POST** /project/{proj_key}/default_values | Update Project Default Values
[**update_project_integration_config**](ProjectApi.md#update_project_integration_config) | **POST** /project/{proj_key}/integrations/{integration_name} | Update Project Integration Config


# **delete_project_integration_config**
> object delete_project_integration_config(integration_name, proj_key)

Delete Project Integration Config

Delete the config for a given project integration.

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
    integration_name = 'integration_name_example' # str | 
    proj_key = 'proj_key_example' # str | 

    try:
        # Delete Project Integration Config
        api_response = api_instance.delete_project_integration_config(integration_name, proj_key)
        print("The response of ProjectApi->delete_project_integration_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->delete_project_integration_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_name** | **str**|  | 
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

# **get_project_integration_config**
> ResponseGetProjectIntegrationConfig get_project_integration_config(integration_name, proj_key, decode_secrets=decode_secrets)

Get Project Integration Config

Get the config for a given project integration.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.response_get_project_integration_config import ResponseGetProjectIntegrationConfig
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
    integration_name = 'integration_name_example' # str | 
    proj_key = 'proj_key_example' # str | 
    decode_secrets = True # bool |  (optional)

    try:
        # Get Project Integration Config
        api_response = api_instance.get_project_integration_config(integration_name, proj_key, decode_secrets=decode_secrets)
        print("The response of ProjectApi->get_project_integration_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_project_integration_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_name** | **str**|  | 
 **proj_key** | **str**|  | 
 **decode_secrets** | **bool**|  | [optional] 

### Return type

[**ResponseGetProjectIntegrationConfig**](ResponseGetProjectIntegrationConfig.md)

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

# **update_project_integration_config**
> object update_project_integration_config(integration_name, proj_key, body)

Update Project Integration Config

Update the config for a given project integration.

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
    integration_name = 'integration_name_example' # str | 
    proj_key = 'proj_key_example' # str | 
    body = None # object | 

    try:
        # Update Project Integration Config
        api_response = api_instance.update_project_integration_config(integration_name, proj_key, body)
        print("The response of ProjectApi->update_project_integration_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->update_project_integration_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_name** | **str**|  | 
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

