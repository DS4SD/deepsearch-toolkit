# deepsearch.cps.apis.public.DataCatalogsApi

All URIs are relative to *http://localhost/api/cps/public/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clone_project_data_catalog**](DataCatalogsApi.md#clone_project_data_catalog) | **POST** /project/{proj_key}/data_catalogues/{dc_key}/actions/clone | 
[**clone_public_data_catalog**](DataCatalogsApi.md#clone_public_data_catalog) | **POST** /project/public/data_catalogues/{dc_key}/actions/clone | 
[**create_project_data_catalog**](DataCatalogsApi.md#create_project_data_catalog) | **POST** /project/{proj_key}/data_catalogues | 
[**create_project_data_catalog_collection**](DataCatalogsApi.md#create_project_data_catalog_collection) | **POST** /project/{proj_key}/data_catalogues/{dc_key}/collections | 
[**create_project_data_catalog_delete_token**](DataCatalogsApi.md#create_project_data_catalog_delete_token) | **POST** /project/{proj_key}/data_catalogues/{dc_key}/delete_token | 
[**delete_project_data_catalog**](DataCatalogsApi.md#delete_project_data_catalog) | **DELETE** /project/{proj_key}/data_catalogues/{dc_key} | 
[**delete_project_data_catalog_collection**](DataCatalogsApi.md#delete_project_data_catalog_collection) | **DELETE** /project/{proj_key}/data_catalogues/{dc_key}/collections/{collection_name} | 
[**export_dataset**](DataCatalogsApi.md#export_dataset) | **POST** /project/{proj_key}/bags/{bag_key}/tasks/export_dataset | 
[**export_project_data_catalog_collection_data**](DataCatalogsApi.md#export_project_data_catalog_collection_data) | **POST** /project/{proj_key}/data_catalogues/{dc_key}/collections/{collection_name}/actions/export | 
[**export_project_data_catalog_data**](DataCatalogsApi.md#export_project_data_catalog_data) | **POST** /project/{proj_key}/data_catalogues/{dc_key}/actions/export | 
[**get_data_catalog_collection_data**](DataCatalogsApi.md#get_data_catalog_collection_data) | **GET** /project/{proj_key}/data_catalogues/{dc_key}/collections/{collection_name}/data | 
[**get_project_data_catalog**](DataCatalogsApi.md#get_project_data_catalog) | **GET** /project/{proj_key}/data_catalogues/{dc_key} | 
[**get_public_data_catalog**](DataCatalogsApi.md#get_public_data_catalog) | **GET** /project/public/data_catalogues/{dc_key} | 
[**import_project_data_catalog_collection_data**](DataCatalogsApi.md#import_project_data_catalog_collection_data) | **POST** /project/{proj_key}/data_catalogues/{dc_key}/collections/{collection_name}/actions/import | 
[**import_project_data_catalog_data**](DataCatalogsApi.md#import_project_data_catalog_data) | **POST** /project/{proj_key}/data_catalogues/{dc_key}/actions/import | 
[**import_project_data_catalog_from_mongo**](DataCatalogsApi.md#import_project_data_catalog_from_mongo) | **POST** /project/{proj_key}/data_catalogues/from_mongo | 
[**import_project_data_catalog_from_url**](DataCatalogsApi.md#import_project_data_catalog_from_url) | **POST** /project/{proj_key}/data_catalogues/from_url | 
[**infer_project_data_catalog_category_schema**](DataCatalogsApi.md#infer_project_data_catalog_category_schema) | **POST** /project/{proj_key}/data_catalogues/{dc_key}/collections/{collection_name}/actions/infer_schema | 
[**list_data_catalogs_and_collections_from_schema**](DataCatalogsApi.md#list_data_catalogs_and_collections_from_schema) | **POST** /project/data_catalogues/with_schema | 
[**list_known_data_catalog_schemas**](DataCatalogsApi.md#list_known_data_catalog_schemas) | **GET** /project/data_cataloges/known_schemas | 
[**list_project_data_catalog_collections**](DataCatalogsApi.md#list_project_data_catalog_collections) | **GET** /project/{proj_key}/data_catalogues/{dc_key}/collections | 
[**list_project_data_catalogs**](DataCatalogsApi.md#list_project_data_catalogs) | **GET** /project/{proj_key}/data_catalogues | 
[**list_public_data_catalog_collections**](DataCatalogsApi.md#list_public_data_catalog_collections) | **GET** /project/public/data_catalogues/{dc_key}/collections | 
[**list_public_data_catalogs**](DataCatalogsApi.md#list_public_data_catalogs) | **GET** /project/public/data_catalogues | 
[**patch_project_data_catalog**](DataCatalogsApi.md#patch_project_data_catalog) | **PATCH** /project/{proj_key}/data_catalogues/{dc_key} | 
[**upload_project_data_catalog_collection_data**](DataCatalogsApi.md#upload_project_data_catalog_collection_data) | **POST** /project/{proj_key}/data_catalogues/{dc_key}/collections/{collection_name}/actions/upload | 
[**upload_project_data_catalog_data**](DataCatalogsApi.md#upload_project_data_catalog_data) | **POST** /project/{proj_key}/data_catalogues/{dc_key}/actions/upload | 


# **clone_project_data_catalog**
> CloneDataCatalogResult clone_project_data_catalog(proj_key, dc_key, options)



Clone an existing data catalogue

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
    api_instance = deepsearch.cps.apis.public.DataCatalogsApi(api_client)
    proj_key = 'proj_key_example' # str | 
dc_key = 'dc_key_example' # str | 
options = deepsearch.cps.apis.public.CloneDataCatalogOptions() # CloneDataCatalogOptions | 

    try:
        api_response = api_instance.clone_project_data_catalog(proj_key, dc_key, options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataCatalogsApi->clone_project_data_catalog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **dc_key** | **str**|  | 
 **options** | [**CloneDataCatalogOptions**](CloneDataCatalogOptions.md)|  | 

### Return type

[**CloneDataCatalogResult**](CloneDataCatalogResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data catalogue cloned, and data is being copied. |  -  |
**404** | Data catalogue not found |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_public_data_catalog**
> CloneDataCatalogResult clone_public_data_catalog(dc_key, options)



Clone an existing public data catalogue

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
    api_instance = deepsearch.cps.apis.public.DataCatalogsApi(api_client)
    dc_key = 'dc_key_example' # str | 
options = deepsearch.cps.apis.public.ClonePublicDataCatalogOptions() # ClonePublicDataCatalogOptions | 

    try:
        api_response = api_instance.clone_public_data_catalog(dc_key, options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataCatalogsApi->clone_public_data_catalog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dc_key** | **str**|  | 
 **options** | [**ClonePublicDataCatalogOptions**](ClonePublicDataCatalogOptions.md)|  | 

### Return type

[**CloneDataCatalogResult**](CloneDataCatalogResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data catalogue cloned, and data is being copied. |  -  |
**404** | Data catalogue not found |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_data_catalog**
> DataCatalogue create_project_data_catalog(proj_key, options)



Create an empty data catalog

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
    api_instance = deepsearch.cps.apis.public.DataCatalogsApi(api_client)
    proj_key = 'proj_key_example' # str | 
options = deepsearch.cps.apis.public.CreateDataCatalogOptions() # CreateDataCatalogOptions | 

    try:
        api_response = api_instance.create_project_data_catalog(proj_key, options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataCatalogsApi->create_project_data_catalog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **options** | [**CreateDataCatalogOptions**](CreateDataCatalogOptions.md)|  | 

### Return type

[**DataCatalogue**](DataCatalogue.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data catalog created. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_data_catalog_collection**
> create_project_data_catalog_collection(proj_key, dc_key, body)



Create a collection in a data catalog

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
    api_instance = deepsearch.cps.apis.public.DataCatalogsApi(api_client)
    proj_key = 'proj_key_example' # str | 
dc_key = 'dc_key_example' # str | 
body = deepsearch.cps.apis.public.CreateDataCatalogCollectionOptions() # CreateDataCatalogCollectionOptions | 

    try:
        api_instance.create_project_data_catalog_collection(proj_key, dc_key, body)
    except ApiException as e:
        print("Exception when calling DataCatalogsApi->create_project_data_catalog_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **dc_key** | **str**|  | 
 **body** | [**CreateDataCatalogCollectionOptions**](CreateDataCatalogCollectionOptions.md)|  | 

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

# **create_project_data_catalog_delete_token**
> TokenResponse create_project_data_catalog_delete_token(proj_key, dc_key)



Get a token used to confirm the deletion of a data catalog.

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
    api_instance = deepsearch.cps.apis.public.DataCatalogsApi(api_client)
    proj_key = 'proj_key_example' # str | 
dc_key = 'dc_key_example' # str | 

    try:
        api_response = api_instance.create_project_data_catalog_delete_token(proj_key, dc_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataCatalogsApi->create_project_data_catalog_delete_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **dc_key** | **str**|  | 

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
**200** | Data catalog deletion token. |  -  |
**404** | Data flow template not found. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_data_catalog**
> delete_project_data_catalog(proj_key, dc_key, confirmation_token)



Delete a single data catalog

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
    api_instance = deepsearch.cps.apis.public.DataCatalogsApi(api_client)
    proj_key = 'proj_key_example' # str | 
dc_key = 'dc_key_example' # str | 
confirmation_token = 'confirmation_token_example' # str | 

    try:
        api_instance.delete_project_data_catalog(proj_key, dc_key, confirmation_token)
    except ApiException as e:
        print("Exception when calling DataCatalogsApi->delete_project_data_catalog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **dc_key** | **str**|  | 
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
**204** | Data catalog deleted. |  -  |
**404** | Data catalog doesn&#39;t exist. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_data_catalog_collection**
> delete_project_data_catalog_collection(proj_key, dc_key, collection_name)



Delete a single data catalog's collection

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
    api_instance = deepsearch.cps.apis.public.DataCatalogsApi(api_client)
    proj_key = 'proj_key_example' # str | 
dc_key = 'dc_key_example' # str | 
collection_name = 'collection_name_example' # str | 

    try:
        api_instance.delete_project_data_catalog_collection(proj_key, dc_key, collection_name)
    except ApiException as e:
        print("Exception when calling DataCatalogsApi->delete_project_data_catalog_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **dc_key** | **str**|  | 
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

# **export_dataset**
> ProjectTask export_dataset(proj_key, bag_key, data)



Export dataset from a Knowledge Graph

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

# Configure API key authorization: KGAuth
configuration = deepsearch.cps.apis.public.Configuration(
    host = "http://localhost/api/cps/public/v1",
    api_key = {
        'X-CPS-KG-Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CPS-KG-Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with deepsearch.cps.apis.public.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deepsearch.cps.apis.public.DataCatalogsApi(api_client)
    proj_key = 'proj_key_example' # str | 
bag_key = 'bag_key_example' # str | 
data = deepsearch.cps.apis.public.InlineObject3() # InlineObject3 | 

    try:
        api_response = api_instance.export_dataset(proj_key, bag_key, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataCatalogsApi->export_dataset: %s\n" % e)
```

* Api Key Authentication (KGAuth):
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

# Configure API key authorization: KGAuth
configuration = deepsearch.cps.apis.public.Configuration(
    host = "http://localhost/api/cps/public/v1",
    api_key = {
        'X-CPS-KG-Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CPS-KG-Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with deepsearch.cps.apis.public.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deepsearch.cps.apis.public.DataCatalogsApi(api_client)
    proj_key = 'proj_key_example' # str | 
bag_key = 'bag_key_example' # str | 
data = deepsearch.cps.apis.public.InlineObject3() # InlineObject3 | 

    try:
        api_response = api_instance.export_dataset(proj_key, bag_key, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataCatalogsApi->export_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **bag_key** | **str**|  | 
 **data** | [**InlineObject3**](InlineObject3.md)|  | 

### Return type

[**ProjectTask**](ProjectTask.md)

### Authorization

[Bearer](../README.md#Bearer), [KGAuth](../README.md#KGAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task |  -  |
**404** | Task not found. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_project_data_catalog_collection_data**
> file export_project_data_catalog_collection_data(proj_key, dc_key, collection_name)



Export the contents of a data catalog's collection

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
    api_instance = deepsearch.cps.apis.public.DataCatalogsApi(api_client)
    proj_key = 'proj_key_example' # str | 
dc_key = 'dc_key_example' # str | 
collection_name = 'collection_name_example' # str | 

    try:
        api_response = api_instance.export_project_data_catalog_collection_data(proj_key, dc_key, collection_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataCatalogsApi->export_project_data_catalog_collection_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **dc_key** | **str**|  | 
 **collection_name** | **str**|  | 

### Return type

**file**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip, application/json, application/x-jsonlines

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data catalog collection contents. |  -  |
**404** | Data catalogue not found |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_project_data_catalog_data**
> file export_project_data_catalog_data(proj_key, dc_key)



Export the contents of a data catalog.

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
    api_instance = deepsearch.cps.apis.public.DataCatalogsApi(api_client)
    proj_key = 'proj_key_example' # str | 
dc_key = 'dc_key_example' # str | 

    try:
        api_response = api_instance.export_project_data_catalog_data(proj_key, dc_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataCatalogsApi->export_project_data_catalog_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **dc_key** | **str**|  | 

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
**200** | Data catalog contents. |  -  |
**404** | Data catalogue not found |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_catalog_collection_data**
> get_data_catalog_collection_data(proj_key, dc_key, collection_name, after=after, limit=limit)



Get Data Catalog Collection data.

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
    api_instance = deepsearch.cps.apis.public.DataCatalogsApi(api_client)
    proj_key = 'proj_key_example' # str | 
dc_key = 'dc_key_example' # str | 
collection_name = 'collection_name_example' # str | 
after = 'after_example' # str |  (optional)
limit = 50 # int |  (optional) (default to 50)

    try:
        api_instance.get_data_catalog_collection_data(proj_key, dc_key, collection_name, after=after, limit=limit)
    except ApiException as e:
        print("Exception when calling DataCatalogsApi->get_data_catalog_collection_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **dc_key** | **str**|  | 
 **collection_name** | **str**|  | 
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]

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
**200** | Get Data Catalog Collection data. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_data_catalog**
> DataCatalogue get_project_data_catalog(proj_key, dc_key, include_collections=include_collections)



Get a single data catalogue

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
    api_instance = deepsearch.cps.apis.public.DataCatalogsApi(api_client)
    proj_key = 'proj_key_example' # str | 
dc_key = 'dc_key_example' # str | 
include_collections = False # bool |  (optional) (default to False)

    try:
        api_response = api_instance.get_project_data_catalog(proj_key, dc_key, include_collections=include_collections)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataCatalogsApi->get_project_data_catalog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **dc_key** | **str**|  | 
 **include_collections** | **bool**|  | [optional] [default to False]

### Return type

[**DataCatalogue**](DataCatalogue.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data catalogue |  -  |
**404** | Data catalogue not found |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_data_catalog**
> DataCatalogue get_public_data_catalog(dc_key, include_collections=include_collections)



Get a single data catalogue that was made public

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
    api_instance = deepsearch.cps.apis.public.DataCatalogsApi(api_client)
    dc_key = 'dc_key_example' # str | 
include_collections = False # bool |  (optional) (default to False)

    try:
        api_response = api_instance.get_public_data_catalog(dc_key, include_collections=include_collections)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataCatalogsApi->get_public_data_catalog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dc_key** | **str**|  | 
 **include_collections** | **bool**|  | [optional] [default to False]

### Return type

[**DataCatalogue**](DataCatalogue.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data catalogue |  -  |
**404** | Data catalogue not found or is not public |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_project_data_catalog_collection_data**
> Task import_project_data_catalog_collection_data(proj_key, dc_key, collection_name, body)



Import data to a data catalog collection. The collection will be created if it doesn't exist.

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
    api_instance = deepsearch.cps.apis.public.DataCatalogsApi(api_client)
    proj_key = 'proj_key_example' # str | 
dc_key = 'dc_key_example' # str | 
collection_name = 'collection_name_example' # str | 
body = deepsearch.cps.apis.public.ImportToDataCatalogCollectionOptions() # ImportToDataCatalogCollectionOptions | 

    try:
        api_response = api_instance.import_project_data_catalog_collection_data(proj_key, dc_key, collection_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataCatalogsApi->import_project_data_catalog_collection_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **dc_key** | **str**|  | 
 **collection_name** | **str**|  | 
 **body** | [**ImportToDataCatalogCollectionOptions**](ImportToDataCatalogCollectionOptions.md)|  | 

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
**200** | Data is being processed. |  -  |
**404** | Data catalogue not found |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_project_data_catalog_data**
> Task import_project_data_catalog_data(proj_key, dc_key, body)



Import data to a data catalog. The collections will be created if they don't exist.

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
    api_instance = deepsearch.cps.apis.public.DataCatalogsApi(api_client)
    proj_key = 'proj_key_example' # str | 
dc_key = 'dc_key_example' # str | 
body = deepsearch.cps.apis.public.ImportToDataCatalogOptions() # ImportToDataCatalogOptions | 

    try:
        api_response = api_instance.import_project_data_catalog_data(proj_key, dc_key, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataCatalogsApi->import_project_data_catalog_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **dc_key** | **str**|  | 
 **body** | [**ImportToDataCatalogOptions**](ImportToDataCatalogOptions.md)|  | 

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
**200** | Data is being processed. |  -  |
**404** | Data catalogue not found |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_project_data_catalog_from_mongo**
> DataCatalogImportResult import_project_data_catalog_from_mongo(proj_key, body)



Create a data catalogue from a mongo database

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
    api_instance = deepsearch.cps.apis.public.DataCatalogsApi(api_client)
    proj_key = 'proj_key_example' # str | 
body = deepsearch.cps.apis.public.DataCatalogImportOptions() # DataCatalogImportOptions | 

    try:
        api_response = api_instance.import_project_data_catalog_from_mongo(proj_key, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataCatalogsApi->import_project_data_catalog_from_mongo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **body** | [**DataCatalogImportOptions**](DataCatalogImportOptions.md)|  | 

### Return type

[**DataCatalogImportResult**](DataCatalogImportResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data catalogue created, and data is being imported. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_project_data_catalog_from_url**
> DataCatalogImportResult import_project_data_catalog_from_url(proj_key, body)



Create a data catalogue from a URL to a file

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
    api_instance = deepsearch.cps.apis.public.DataCatalogsApi(api_client)
    proj_key = 'proj_key_example' # str | 
body = deepsearch.cps.apis.public.DataCatalogUrlImportOptions() # DataCatalogUrlImportOptions | 

    try:
        api_response = api_instance.import_project_data_catalog_from_url(proj_key, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataCatalogsApi->import_project_data_catalog_from_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **body** | [**DataCatalogUrlImportOptions**](DataCatalogUrlImportOptions.md)|  | 

### Return type

[**DataCatalogImportResult**](DataCatalogImportResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data catalogue created, and data is being imported. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **infer_project_data_catalog_category_schema**
> Task infer_project_data_catalog_category_schema(proj_key, dc_key, collection_name, body)



Infer the schema for a data catalog's collection.

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
    api_instance = deepsearch.cps.apis.public.DataCatalogsApi(api_client)
    proj_key = 'proj_key_example' # str | 
dc_key = 'dc_key_example' # str | 
collection_name = 'collection_name_example' # str | 
body = deepsearch.cps.apis.public.InferProjectDataCatalogCategorySchema() # InferProjectDataCatalogCategorySchema | 

    try:
        api_response = api_instance.infer_project_data_catalog_category_schema(proj_key, dc_key, collection_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataCatalogsApi->infer_project_data_catalog_category_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **dc_key** | **str**|  | 
 **collection_name** | **str**|  | 
 **body** | [**InferProjectDataCatalogCategorySchema**](InferProjectDataCatalogCategorySchema.md)|  | 

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

# **list_data_catalogs_and_collections_from_schema**
> list[DataCatalogue] list_data_catalogs_and_collections_from_schema(schema, proj_key=proj_key)



List data catalogues with specific schema

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
    api_instance = deepsearch.cps.apis.public.DataCatalogsApi(api_client)
    schema = None # dict(str, object) | 
proj_key = 'proj_key_example' # str |  (optional)

    try:
        api_response = api_instance.list_data_catalogs_and_collections_from_schema(schema, proj_key=proj_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataCatalogsApi->list_data_catalogs_and_collections_from_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema** | [**dict(str, object)**](object.md)|  | 
 **proj_key** | **str**|  | [optional] 

### Return type

[**list[DataCatalogue]**](DataCatalogue.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of data catalogues |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_known_data_catalog_schemas**
> list[DataCatalogSchema] list_known_data_catalog_schemas()



List System Known Data Catalog Schemas.

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
    api_instance = deepsearch.cps.apis.public.DataCatalogsApi(api_client)
    
    try:
        api_response = api_instance.list_known_data_catalog_schemas()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataCatalogsApi->list_known_data_catalog_schemas: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DataCatalogSchema]**](DataCatalogSchema.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Known Data Catalog Schemas. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_data_catalog_collections**
> list[DataCatalogCollection] list_project_data_catalog_collections(proj_key, dc_key)



Get the collections of a data catalog.

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
    api_instance = deepsearch.cps.apis.public.DataCatalogsApi(api_client)
    proj_key = 'proj_key_example' # str | 
dc_key = 'dc_key_example' # str | 

    try:
        api_response = api_instance.list_project_data_catalog_collections(proj_key, dc_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataCatalogsApi->list_project_data_catalog_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **dc_key** | **str**|  | 

### Return type

[**list[DataCatalogCollection]**](DataCatalogCollection.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data catalog collections |  -  |
**404** | Data catalogue not found |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_data_catalogs**
> list[DataCatalogue] list_project_data_catalogs(proj_key, query=query)



List data catalogues for a project

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
    api_instance = deepsearch.cps.apis.public.DataCatalogsApi(api_client)
    proj_key = 'proj_key_example' # str | 
query = 'query_example' # str |  (optional)

    try:
        api_response = api_instance.list_project_data_catalogs(proj_key, query=query)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataCatalogsApi->list_project_data_catalogs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **query** | **str**|  | [optional] 

### Return type

[**list[DataCatalogue]**](DataCatalogue.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of data catalogues |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_public_data_catalog_collections**
> list[DataCatalogCollection] list_public_data_catalog_collections(dc_key)



Get the collections of a data catalog.

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
    api_instance = deepsearch.cps.apis.public.DataCatalogsApi(api_client)
    dc_key = 'dc_key_example' # str | 

    try:
        api_response = api_instance.list_public_data_catalog_collections(dc_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataCatalogsApi->list_public_data_catalog_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dc_key** | **str**|  | 

### Return type

[**list[DataCatalogCollection]**](DataCatalogCollection.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data catalog collections |  -  |
**404** | Data catalogue not found |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_public_data_catalogs**
> list[DataCatalogue] list_public_data_catalogs(query=query)



List public data catalogues

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
    api_instance = deepsearch.cps.apis.public.DataCatalogsApi(api_client)
    query = 'query_example' # str |  (optional)

    try:
        api_response = api_instance.list_public_data_catalogs(query=query)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataCatalogsApi->list_public_data_catalogs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | [optional] 

### Return type

[**list[DataCatalogue]**](DataCatalogue.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of public data catalogues |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_project_data_catalog**
> DataCatalogue patch_project_data_catalog(proj_key, dc_key, options)



Update the metadata of a data catalog.

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
    api_instance = deepsearch.cps.apis.public.DataCatalogsApi(api_client)
    proj_key = 'proj_key_example' # str | 
dc_key = 'dc_key_example' # str | 
options = deepsearch.cps.apis.public.PatchDataCatalogOptions() # PatchDataCatalogOptions | 

    try:
        api_response = api_instance.patch_project_data_catalog(proj_key, dc_key, options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataCatalogsApi->patch_project_data_catalog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **dc_key** | **str**|  | 
 **options** | [**PatchDataCatalogOptions**](PatchDataCatalogOptions.md)|  | 

### Return type

[**DataCatalogue**](DataCatalogue.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data catalog updated. |  -  |
**404** | Data catalog not found. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_project_data_catalog_collection_data**
> Task upload_project_data_catalog_collection_data(proj_key, dc_key, collection_name, file)



Upload data to a data catalog collection. The collection will be created if it doesn't exist.

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
    api_instance = deepsearch.cps.apis.public.DataCatalogsApi(api_client)
    proj_key = 'proj_key_example' # str | 
dc_key = 'dc_key_example' # str | 
collection_name = 'collection_name_example' # str | 
file = '/path/to/file' # file | 

    try:
        api_response = api_instance.upload_project_data_catalog_collection_data(proj_key, dc_key, collection_name, file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataCatalogsApi->upload_project_data_catalog_collection_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **dc_key** | **str**|  | 
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
**404** | Data catalogue not found |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_project_data_catalog_data**
> Task upload_project_data_catalog_data(proj_key, dc_key, file)



Upload data to a data catalog. The collection name(s) will be inferred from the file name(s).

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
    api_instance = deepsearch.cps.apis.public.DataCatalogsApi(api_client)
    proj_key = 'proj_key_example' # str | 
dc_key = 'dc_key_example' # str | 
file = '/path/to/file' # file | 

    try:
        api_response = api_instance.upload_project_data_catalog_data(proj_key, dc_key, file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataCatalogsApi->upload_project_data_catalog_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **dc_key** | **str**|  | 
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
**404** | Data catalogue not found |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

