# deepsearch.cps.apis.public_v2.DataIndicesApi

All URIs are relative to */api/cps/public/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_data_index**](DataIndicesApi.md#create_project_data_index) | **POST** /project/{proj_key}/data_indices | Create Project Data Index
[**create_project_data_index_delete_token**](DataIndicesApi.md#create_project_data_index_delete_token) | **POST** /project/{proj_key}/data_indices/{index_key}/delete_token | Create Project Data Index Delete Token
[**delete_project_data_index**](DataIndicesApi.md#delete_project_data_index) | **DELETE** /project/{proj_key}/data_indices/{index_key} | Delete Project Data Index
[**get_project_data_index**](DataIndicesApi.md#get_project_data_index) | **GET** /project/{proj_key}/data_indices/{index_key} | Get Project Data Index
[**get_project_data_index_conversion_settings**](DataIndicesApi.md#get_project_data_index_conversion_settings) | **GET** /project/{proj_key}/data_indices/{index_key}/conversion_settings | Get Project Data Index Conversion Settings
[**get_project_data_indices**](DataIndicesApi.md#get_project_data_indices) | **GET** /project/{proj_key}/data_indices | Get Project Data Indices
[**update_project_data_index**](DataIndicesApi.md#update_project_data_index) | **PATCH** /project/{proj_key}/data_indices/{index_key} | Update Project Data Index
[**update_project_data_index_conversion_settings**](DataIndicesApi.md#update_project_data_index_conversion_settings) | **PATCH** /project/{proj_key}/data_indices/{index_key}/conversion_settings | Update Project Data Index Conversion Settings


# **create_project_data_index**
> ProjectDataIndexWithStatus create_project_data_index(proj_key, data)

Create Project Data Index

Create a project data index.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.data import Data
from deepsearch.cps.apis.public_v2.models.project_data_index_with_status import ProjectDataIndexWithStatus
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
    api_instance = deepsearch.cps.apis.public_v2.DataIndicesApi(api_client)
    proj_key = 'proj_key_example' # str | 
    data = deepsearch.cps.apis.public_v2.Data() # Data | 

    try:
        # Create Project Data Index
        api_response = api_instance.create_project_data_index(proj_key, data)
        print("The response of DataIndicesApi->create_project_data_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataIndicesApi->create_project_data_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **data** | [**Data**](Data.md)|  | 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_data_index_delete_token**
> TokenResponse create_project_data_index_delete_token(index_key, proj_key)

Create Project Data Index Delete Token

Get a token used to confirm the deletion of a project data index.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.token_response import TokenResponse
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
    api_instance = deepsearch.cps.apis.public_v2.DataIndicesApi(api_client)
    index_key = 'index_key_example' # str | 
    proj_key = 'proj_key_example' # str | 

    try:
        # Create Project Data Index Delete Token
        api_response = api_instance.create_project_data_index_delete_token(index_key, proj_key)
        print("The response of DataIndicesApi->create_project_data_index_delete_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataIndicesApi->create_project_data_index_delete_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_key** | **str**|  | 
 **proj_key** | **str**|  | 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_data_index**
> object delete_project_data_index(index_key, proj_key, confirmation_token)

Delete Project Data Index

Delete a project index data.

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
    api_instance = deepsearch.cps.apis.public_v2.DataIndicesApi(api_client)
    index_key = 'index_key_example' # str | 
    proj_key = 'proj_key_example' # str | 
    confirmation_token = 'confirmation_token_example' # str | 

    try:
        # Delete Project Data Index
        api_response = api_instance.delete_project_data_index(index_key, proj_key, confirmation_token)
        print("The response of DataIndicesApi->delete_project_data_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataIndicesApi->delete_project_data_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_key** | **str**|  | 
 **proj_key** | **str**|  | 
 **confirmation_token** | **str**|  | 

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

# **get_project_data_index**
> ProjectDataIndexWithStatus get_project_data_index(index_key, proj_key)

Get Project Data Index

Get project data index.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.project_data_index_with_status import ProjectDataIndexWithStatus
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
    api_instance = deepsearch.cps.apis.public_v2.DataIndicesApi(api_client)
    index_key = 'index_key_example' # str | 
    proj_key = 'proj_key_example' # str | 

    try:
        # Get Project Data Index
        api_response = api_instance.get_project_data_index(index_key, proj_key)
        print("The response of DataIndicesApi->get_project_data_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataIndicesApi->get_project_data_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_key** | **str**|  | 
 **proj_key** | **str**|  | 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_data_index_conversion_settings**
> ResponseGetProjectDataIndexConversionSettings get_project_data_index_conversion_settings(index_key, proj_key)

Get Project Data Index Conversion Settings

Get project data index conversion settings.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.response_get_project_data_index_conversion_settings import ResponseGetProjectDataIndexConversionSettings
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
    api_instance = deepsearch.cps.apis.public_v2.DataIndicesApi(api_client)
    index_key = 'index_key_example' # str | 
    proj_key = 'proj_key_example' # str | 

    try:
        # Get Project Data Index Conversion Settings
        api_response = api_instance.get_project_data_index_conversion_settings(index_key, proj_key)
        print("The response of DataIndicesApi->get_project_data_index_conversion_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataIndicesApi->get_project_data_index_conversion_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_key** | **str**|  | 
 **proj_key** | **str**|  | 

### Return type

[**ResponseGetProjectDataIndexConversionSettings**](ResponseGetProjectDataIndexConversionSettings.md)

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

# **get_project_data_indices**
> List[ProjectDataIndexWithStatus] get_project_data_indices(proj_key)

Get Project Data Indices

Get project data indices.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.project_data_index_with_status import ProjectDataIndexWithStatus
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
    api_instance = deepsearch.cps.apis.public_v2.DataIndicesApi(api_client)
    proj_key = 'proj_key_example' # str | 

    try:
        # Get Project Data Indices
        api_response = api_instance.get_project_data_indices(proj_key)
        print("The response of DataIndicesApi->get_project_data_indices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataIndicesApi->get_project_data_indices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 

### Return type

[**List[ProjectDataIndexWithStatus]**](ProjectDataIndexWithStatus.md)

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

# **update_project_data_index**
> ProjectDataIndexWithStatus update_project_data_index(index_key, proj_key, data)

Update Project Data Index

Update a project data index.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.data import Data
from deepsearch.cps.apis.public_v2.models.project_data_index_with_status import ProjectDataIndexWithStatus
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
    api_instance = deepsearch.cps.apis.public_v2.DataIndicesApi(api_client)
    index_key = 'index_key_example' # str | 
    proj_key = 'proj_key_example' # str | 
    data = deepsearch.cps.apis.public_v2.Data() # Data | 

    try:
        # Update Project Data Index
        api_response = api_instance.update_project_data_index(index_key, proj_key, data)
        print("The response of DataIndicesApi->update_project_data_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataIndicesApi->update_project_data_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_key** | **str**|  | 
 **proj_key** | **str**|  | 
 **data** | [**Data**](Data.md)|  | 

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
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_data_index_conversion_settings**
> ResponseUpdateProjectDataIndexConversionSettings update_project_data_index_conversion_settings(index_key, proj_key, project_data_index_conversion_settings_input)

Update Project Data Index Conversion Settings

Update a project data index conversion settings.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.project_data_index_conversion_settings_input import ProjectDataIndexConversionSettingsInput
from deepsearch.cps.apis.public_v2.models.response_update_project_data_index_conversion_settings import ResponseUpdateProjectDataIndexConversionSettings
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
    api_instance = deepsearch.cps.apis.public_v2.DataIndicesApi(api_client)
    index_key = 'index_key_example' # str | 
    proj_key = 'proj_key_example' # str | 
    project_data_index_conversion_settings_input = deepsearch.cps.apis.public_v2.ProjectDataIndexConversionSettingsInput() # ProjectDataIndexConversionSettingsInput | 

    try:
        # Update Project Data Index Conversion Settings
        api_response = api_instance.update_project_data_index_conversion_settings(index_key, proj_key, project_data_index_conversion_settings_input)
        print("The response of DataIndicesApi->update_project_data_index_conversion_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataIndicesApi->update_project_data_index_conversion_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_key** | **str**|  | 
 **proj_key** | **str**|  | 
 **project_data_index_conversion_settings_input** | [**ProjectDataIndexConversionSettingsInput**](ProjectDataIndexConversionSettingsInput.md)|  | 

### Return type

[**ResponseUpdateProjectDataIndexConversionSettings**](ResponseUpdateProjectDataIndexConversionSettings.md)

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

