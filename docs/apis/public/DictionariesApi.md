# deepsearch.cps.apis.public.DictionariesApi

All URIs are relative to *http://localhost/api/cps/public/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clone_project_dictionary**](DictionariesApi.md#clone_project_dictionary) | **POST** /project/{proj_key}/dictionaries/{dict_key}/actions/clone | 
[**clone_public_dictionary**](DictionariesApi.md#clone_public_dictionary) | **POST** /project/public/dictionaries/{dict_key}/actions/clone | 
[**create_project_dictionary**](DictionariesApi.md#create_project_dictionary) | **POST** /project/{proj_key}/dictionaries | 
[**create_project_dictionary_collection**](DictionariesApi.md#create_project_dictionary_collection) | **POST** /project/{proj_key}/dictionaries/{dict_key}/collections | 
[**create_project_dictionary_delete_token**](DictionariesApi.md#create_project_dictionary_delete_token) | **POST** /project/{proj_key}/dictionaries/{dict_key}/delete_token | 
[**delete_project_dictionary**](DictionariesApi.md#delete_project_dictionary) | **DELETE** /project/{proj_key}/dictionaries/{dict_key} | 
[**delete_project_dictionary_collection**](DictionariesApi.md#delete_project_dictionary_collection) | **DELETE** /project/{proj_key}/dictionaries/{dict_key}/collections/{collection_name} | 
[**export_project_dictionary_collection_data**](DictionariesApi.md#export_project_dictionary_collection_data) | **POST** /project/{proj_key}/dictionaries/{dict_key}/collections/{collection_name}/actions/export | 
[**export_project_dictionary_data**](DictionariesApi.md#export_project_dictionary_data) | **POST** /project/{proj_key}/dictionaries/{dict_key}/actions/export | 
[**get_project_dictionary**](DictionariesApi.md#get_project_dictionary) | **GET** /project/{proj_key}/dictionaries/{dict_key} | 
[**get_project_dictionary_collection_data**](DictionariesApi.md#get_project_dictionary_collection_data) | **GET** /project/{proj_key}/dictionaries/{dict_key}/collections/{collection_name}/data | 
[**get_public_dictionary**](DictionariesApi.md#get_public_dictionary) | **GET** /project/public/dictionaries/{dict_key} | 
[**import_project_dictionary_from_mongo**](DictionariesApi.md#import_project_dictionary_from_mongo) | **POST** /project/{proj_key}/dictionaries/from_mongo | 
[**list_project_dictionaries**](DictionariesApi.md#list_project_dictionaries) | **GET** /project/{proj_key}/dictionaries | 
[**list_project_dictionary_collections**](DictionariesApi.md#list_project_dictionary_collections) | **GET** /project/{proj_key}/dictionaries/{dict_key}/collections | 
[**list_public_dictionaries**](DictionariesApi.md#list_public_dictionaries) | **GET** /project/public/dictionaries | 
[**list_public_dictionary_collections**](DictionariesApi.md#list_public_dictionary_collections) | **GET** /project/public/dictionaries/{dict_key}/collections | 
[**update_project_dictionary**](DictionariesApi.md#update_project_dictionary) | **PATCH** /project/{proj_key}/dictionaries/{dict_key} | 
[**update_project_dictionary_collection_data**](DictionariesApi.md#update_project_dictionary_collection_data) | **PATCH** /project/{proj_key}/dictionaries/{dict_key}/collections/{collection_name}/data | 
[**upload_project_dictionary_collection_data**](DictionariesApi.md#upload_project_dictionary_collection_data) | **POST** /project/{proj_key}/dictionaries/{dict_key}/collections/{collection_name}/actions/upload | 
[**upload_project_dictionary_data**](DictionariesApi.md#upload_project_dictionary_data) | **POST** /project/{proj_key}/dictionaries/{dict_key}/actions/upload | 


# **clone_project_dictionary**
> DictionaryCloneResult clone_project_dictionary(proj_key, dict_key, body)



Clone an existing dictionary

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
    api_instance = deepsearch.cps.apis.public.DictionariesApi(api_client)
    proj_key = 'proj_key_example' # str | 
dict_key = 'dict_key_example' # str | 
body = deepsearch.cps.apis.public.CloneDictionaryOptions() # CloneDictionaryOptions | 

    try:
        api_response = api_instance.clone_project_dictionary(proj_key, dict_key, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DictionariesApi->clone_project_dictionary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **dict_key** | **str**|  | 
 **body** | [**CloneDictionaryOptions**](CloneDictionaryOptions.md)|  | 

### Return type

[**DictionaryCloneResult**](DictionaryCloneResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dictionary cloned, and data is being copied. |  -  |
**404** | Dictionary not found |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_public_dictionary**
> DictionaryCloneResult clone_public_dictionary(dict_key, body)



Clone an existing public dictionary

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
    api_instance = deepsearch.cps.apis.public.DictionariesApi(api_client)
    dict_key = 'dict_key_example' # str | 
body = deepsearch.cps.apis.public.ClonePublicDictionaryOptions() # ClonePublicDictionaryOptions | 

    try:
        api_response = api_instance.clone_public_dictionary(dict_key, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DictionariesApi->clone_public_dictionary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dict_key** | **str**|  | 
 **body** | [**ClonePublicDictionaryOptions**](ClonePublicDictionaryOptions.md)|  | 

### Return type

[**DictionaryCloneResult**](DictionaryCloneResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dictionary cloned, and data is being copied. |  -  |
**404** | Dictionary not found |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_dictionary**
> Dictionary create_project_dictionary(proj_key, body)



Create an empty dictionary

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
    api_instance = deepsearch.cps.apis.public.DictionariesApi(api_client)
    proj_key = 'proj_key_example' # str | 
body = deepsearch.cps.apis.public.CreateDictionaryOptions() # CreateDictionaryOptions | 

    try:
        api_response = api_instance.create_project_dictionary(proj_key, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DictionariesApi->create_project_dictionary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **body** | [**CreateDictionaryOptions**](CreateDictionaryOptions.md)|  | 

### Return type

[**Dictionary**](Dictionary.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dictionary created. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_dictionary_collection**
> create_project_dictionary_collection(proj_key, dict_key, body)



Create a collection in a dictionary

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
    api_instance = deepsearch.cps.apis.public.DictionariesApi(api_client)
    proj_key = 'proj_key_example' # str | 
dict_key = 'dict_key_example' # str | 
body = deepsearch.cps.apis.public.CreateCollectionInDictionaryOptions() # CreateCollectionInDictionaryOptions | 

    try:
        api_instance.create_project_dictionary_collection(proj_key, dict_key, body)
    except ApiException as e:
        print("Exception when calling DictionariesApi->create_project_dictionary_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **dict_key** | **str**|  | 
 **body** | [**CreateCollectionInDictionaryOptions**](CreateCollectionInDictionaryOptions.md)|  | 

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
**200** | Collection created. |  -  |
**404** | Dictionary doesn&#39;t exist. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_dictionary_delete_token**
> TokenResponse create_project_dictionary_delete_token(proj_key, dict_key)



Get a token used to confirm the deletion of a dictionary.

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
    api_instance = deepsearch.cps.apis.public.DictionariesApi(api_client)
    proj_key = 'proj_key_example' # str | 
dict_key = 'dict_key_example' # str | 

    try:
        api_response = api_instance.create_project_dictionary_delete_token(proj_key, dict_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DictionariesApi->create_project_dictionary_delete_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **dict_key** | **str**|  | 

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
**200** | Dictionary deletion token. |  -  |
**404** | Data flow template not found. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_dictionary**
> delete_project_dictionary(proj_key, dict_key, confirmation_token)



Delete a single dictionary

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
    api_instance = deepsearch.cps.apis.public.DictionariesApi(api_client)
    proj_key = 'proj_key_example' # str | 
dict_key = 'dict_key_example' # str | 
confirmation_token = 'confirmation_token_example' # str | 

    try:
        api_instance.delete_project_dictionary(proj_key, dict_key, confirmation_token)
    except ApiException as e:
        print("Exception when calling DictionariesApi->delete_project_dictionary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **dict_key** | **str**|  | 
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
**204** | Dictionary deleted. |  -  |
**404** | Dictionary doesn&#39;t exist. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_dictionary_collection**
> delete_project_dictionary_collection(proj_key, dict_key, collection_name)



Delete a single dictionary's collection

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
    api_instance = deepsearch.cps.apis.public.DictionariesApi(api_client)
    proj_key = 'proj_key_example' # str | 
dict_key = 'dict_key_example' # str | 
collection_name = 'collection_name_example' # str | 

    try:
        api_instance.delete_project_dictionary_collection(proj_key, dict_key, collection_name)
    except ApiException as e:
        print("Exception when calling DictionariesApi->delete_project_dictionary_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **dict_key** | **str**|  | 
 **collection_name** | **str**|  | 

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
**204** | Collection deleted. |  -  |
**404** | Collection doesn&#39;t exist. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_project_dictionary_collection_data**
> file export_project_dictionary_collection_data(proj_key, dict_key, collection_name, file_format=file_format)



Export the contents of a dictionary's collection

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
    api_instance = deepsearch.cps.apis.public.DictionariesApi(api_client)
    proj_key = 'proj_key_example' # str | 
dict_key = 'dict_key_example' # str | 
collection_name = 'collection_name_example' # str | 
file_format = 'file_format_example' # str |  (optional)

    try:
        api_response = api_instance.export_project_dictionary_collection_data(proj_key, dict_key, collection_name, file_format=file_format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DictionariesApi->export_project_dictionary_collection_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **dict_key** | **str**|  | 
 **collection_name** | **str**|  | 
 **file_format** | **str**|  | [optional] 

### Return type

**file**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dictionary collection contents. |  -  |
**404** | Dictionary not found |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_project_dictionary_data**
> file export_project_dictionary_data(proj_key, dict_key)



Export the contents of a dictionary.

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
    api_instance = deepsearch.cps.apis.public.DictionariesApi(api_client)
    proj_key = 'proj_key_example' # str | 
dict_key = 'dict_key_example' # str | 

    try:
        api_response = api_instance.export_project_dictionary_data(proj_key, dict_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DictionariesApi->export_project_dictionary_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **dict_key** | **str**|  | 

### Return type

**file**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dictionary contents. |  -  |
**404** | Dictionary not found |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_dictionary**
> Dictionary get_project_dictionary(proj_key, dict_key, include_collections=include_collections)



Get a single dictionary

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
    api_instance = deepsearch.cps.apis.public.DictionariesApi(api_client)
    proj_key = 'proj_key_example' # str | 
dict_key = 'dict_key_example' # str | 
include_collections = False # bool |  (optional) (default to False)

    try:
        api_response = api_instance.get_project_dictionary(proj_key, dict_key, include_collections=include_collections)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DictionariesApi->get_project_dictionary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **dict_key** | **str**|  | 
 **include_collections** | **bool**|  | [optional] [default to False]

### Return type

[**Dictionary**](Dictionary.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dictionary |  -  |
**404** | Dictionary not found |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_dictionary_collection_data**
> object get_project_dictionary_collection_data(proj_key, dict_key, collection_name, after=after, limit=limit, response_format=response_format)



Get a preview of the data in a dictionary

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
    api_instance = deepsearch.cps.apis.public.DictionariesApi(api_client)
    proj_key = 'proj_key_example' # str | 
dict_key = 'dict_key_example' # str | 
collection_name = 'collection_name_example' # str | 
after = 'after_example' # str |  (optional)
limit = 1000 # int |  (optional) (default to 1000)
response_format = 'object' # str |  (optional) (default to 'object')

    try:
        api_response = api_instance.get_project_dictionary_collection_data(proj_key, dict_key, collection_name, after=after, limit=limit, response_format=response_format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DictionariesApi->get_project_dictionary_collection_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **dict_key** | **str**|  | 
 **collection_name** | **str**|  | 
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 1000]
 **response_format** | **str**|  | [optional] [default to &#39;object&#39;]

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
**200** | Dictionary collection contents. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_dictionary**
> Dictionary get_public_dictionary(dict_key, include_collections=include_collections)



Get a single dictionary that was made public

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
    api_instance = deepsearch.cps.apis.public.DictionariesApi(api_client)
    dict_key = 'dict_key_example' # str | 
include_collections = False # bool |  (optional) (default to False)

    try:
        api_response = api_instance.get_public_dictionary(dict_key, include_collections=include_collections)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DictionariesApi->get_public_dictionary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dict_key** | **str**|  | 
 **include_collections** | **bool**|  | [optional] [default to False]

### Return type

[**Dictionary**](Dictionary.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dictionary |  -  |
**404** | Dictionary not found or is not public |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_project_dictionary_from_mongo**
> DictionaryImportResult import_project_dictionary_from_mongo(proj_key, body)



Create a dictionary from a mongo database

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
    api_instance = deepsearch.cps.apis.public.DictionariesApi(api_client)
    proj_key = 'proj_key_example' # str | 
body = deepsearch.cps.apis.public.DictionaryImportOptions() # DictionaryImportOptions | 

    try:
        api_response = api_instance.import_project_dictionary_from_mongo(proj_key, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DictionariesApi->import_project_dictionary_from_mongo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **body** | [**DictionaryImportOptions**](DictionaryImportOptions.md)|  | 

### Return type

[**DictionaryImportResult**](DictionaryImportResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dictionary created, and data is being imported. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_dictionaries**
> list[Dictionary] list_project_dictionaries(proj_key, query=query)



List dictionaries for a project

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
    api_instance = deepsearch.cps.apis.public.DictionariesApi(api_client)
    proj_key = 'proj_key_example' # str | 
query = 'query_example' # str |  (optional)

    try:
        api_response = api_instance.list_project_dictionaries(proj_key, query=query)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DictionariesApi->list_project_dictionaries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **query** | **str**|  | [optional] 

### Return type

[**list[Dictionary]**](Dictionary.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of dictionaries |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_dictionary_collections**
> list[DictionaryCollection] list_project_dictionary_collections(proj_key, dict_key)



Get the collections of a dictionary.

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
    api_instance = deepsearch.cps.apis.public.DictionariesApi(api_client)
    proj_key = 'proj_key_example' # str | 
dict_key = 'dict_key_example' # str | 

    try:
        api_response = api_instance.list_project_dictionary_collections(proj_key, dict_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DictionariesApi->list_project_dictionary_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **dict_key** | **str**|  | 

### Return type

[**list[DictionaryCollection]**](DictionaryCollection.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dictionary collections |  -  |
**404** | Dictionary not found |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_public_dictionaries**
> list[Dictionary] list_public_dictionaries(query=query)



List public dictionaries

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
    api_instance = deepsearch.cps.apis.public.DictionariesApi(api_client)
    query = 'query_example' # str |  (optional)

    try:
        api_response = api_instance.list_public_dictionaries(query=query)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DictionariesApi->list_public_dictionaries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | [optional] 

### Return type

[**list[Dictionary]**](Dictionary.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of public dictionaries |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_public_dictionary_collections**
> list[DictionaryCollection] list_public_dictionary_collections(dict_key)



Get the collections of a dictionary.

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
    api_instance = deepsearch.cps.apis.public.DictionariesApi(api_client)
    dict_key = 'dict_key_example' # str | 

    try:
        api_response = api_instance.list_public_dictionary_collections(dict_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DictionariesApi->list_public_dictionary_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dict_key** | **str**|  | 

### Return type

[**list[DictionaryCollection]**](DictionaryCollection.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dictionary collections |  -  |
**404** | Dictionary not found |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_dictionary**
> Dictionary update_project_dictionary(proj_key, dict_key, options)



Update the metadata of a dictionary

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
    api_instance = deepsearch.cps.apis.public.DictionariesApi(api_client)
    proj_key = 'proj_key_example' # str | 
dict_key = 'dict_key_example' # str | 
options = deepsearch.cps.apis.public.PatchDictionaryOptions() # PatchDictionaryOptions | 

    try:
        api_response = api_instance.update_project_dictionary(proj_key, dict_key, options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DictionariesApi->update_project_dictionary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **dict_key** | **str**|  | 
 **options** | [**PatchDictionaryOptions**](PatchDictionaryOptions.md)|  | 

### Return type

[**Dictionary**](Dictionary.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dictionary updated. |  -  |
**404** | Dictionary not found |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_dictionary_collection_data**
> update_project_dictionary_collection_data(proj_key, dict_key, collection_name, body)



Update the data in a dictionary's collection

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
    api_instance = deepsearch.cps.apis.public.DictionariesApi(api_client)
    proj_key = 'proj_key_example' # str | 
dict_key = 'dict_key_example' # str | 
collection_name = 'collection_name_example' # str | 
body = [deepsearch.cps.apis.public.DictionaryCollectionPatch()] # list[DictionaryCollectionPatch] | A subset of JSON Patch operation list. Only `add`, `replace`, and `remove` is supported. See http://jsonpatch.com/ for more details. 

    try:
        api_instance.update_project_dictionary_collection_data(proj_key, dict_key, collection_name, body)
    except ApiException as e:
        print("Exception when calling DictionariesApi->update_project_dictionary_collection_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **dict_key** | **str**|  | 
 **collection_name** | **str**|  | 
 **body** | [**list[DictionaryCollectionPatch]**](DictionaryCollectionPatch.md)| A subset of JSON Patch operation list. Only &#x60;add&#x60;, &#x60;replace&#x60;, and &#x60;remove&#x60; is supported. See http://jsonpatch.com/ for more details.  | 

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
**204** | Data updated. |  -  |
**404** | Dictionary not found |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_project_dictionary_collection_data**
> Task upload_project_dictionary_collection_data(proj_key, dict_key, collection_name, file)



Upload data to a dictionary collection. The collection will be created if it doesn't exist.

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
    api_instance = deepsearch.cps.apis.public.DictionariesApi(api_client)
    proj_key = 'proj_key_example' # str | 
dict_key = 'dict_key_example' # str | 
collection_name = 'collection_name_example' # str | 
file = '/path/to/file' # file | 

    try:
        api_response = api_instance.upload_project_dictionary_collection_data(proj_key, dict_key, collection_name, file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DictionariesApi->upload_project_dictionary_collection_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **dict_key** | **str**|  | 
 **collection_name** | **str**|  | 
 **file** | **file**|  | 

### Return type

[**Task**](Task.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data is being processed. |  -  |
**404** | Dictionary not found |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_project_dictionary_data**
> Task upload_project_dictionary_data(proj_key, dict_key, file)



Upload data to a dictionary. The collection name(s) will be inferred from the file name(s).

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
    api_instance = deepsearch.cps.apis.public.DictionariesApi(api_client)
    proj_key = 'proj_key_example' # str | 
dict_key = 'dict_key_example' # str | 
file = '/path/to/file' # file | 

    try:
        api_response = api_instance.upload_project_dictionary_data(proj_key, dict_key, file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DictionariesApi->upload_project_dictionary_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **dict_key** | **str**|  | 
 **file** | **file**|  | 

### Return type

[**Task**](Task.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data is being processed. |  -  |
**404** | Dictionary not found |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

