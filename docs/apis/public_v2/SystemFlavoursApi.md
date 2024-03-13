# deepsearch.cps.apis.public_v2.SystemFlavoursApi

All URIs are relative to */api/cps/public/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_flavour**](SystemFlavoursApi.md#delete_flavour) | **DELETE** /system/admin/delete_flavour/{flavour_name} | Delete Flavour
[**get_flavour**](SystemFlavoursApi.md#get_flavour) | **GET** /system/admin/get_flavour/{flavour_name} | Get Flavour
[**list_all_flavours**](SystemFlavoursApi.md#list_all_flavours) | **GET** /system/admin/list_all_flavours | List All Flavours
[**list_flavours_by_project**](SystemFlavoursApi.md#list_flavours_by_project) | **GET** /system/admin/get_project_flavours/{proj_key} | List Flavours By Project
[**list_projects_flavours**](SystemFlavoursApi.md#list_projects_flavours) | **GET** /system/admin/list_projects_flavours | List Projects Flavours
[**save_flavour**](SystemFlavoursApi.md#save_flavour) | **PUT** /system/admin/save_flavour | Save Flavour
[**save_project_flavours**](SystemFlavoursApi.md#save_project_flavours) | **PUT** /system/admin/save_project_flavours | Save Project Flavours


# **delete_flavour**
> object delete_flavour(flavour_name)

Delete Flavour

Delete flavour from db.

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
    api_instance = deepsearch.cps.apis.public_v2.SystemFlavoursApi(api_client)
    flavour_name = 'flavour_name_example' # str | 

    try:
        # Delete Flavour
        api_response = api_instance.delete_flavour(flavour_name)
        print("The response of SystemFlavoursApi->delete_flavour:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemFlavoursApi->delete_flavour: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flavour_name** | **str**|  | 

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

# **get_flavour**
> BagFlavourFullData get_flavour(flavour_name)

Get Flavour

Get flavour from db.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.bag_flavour_full_data import BagFlavourFullData
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
    api_instance = deepsearch.cps.apis.public_v2.SystemFlavoursApi(api_client)
    flavour_name = 'flavour_name_example' # str | 

    try:
        # Get Flavour
        api_response = api_instance.get_flavour(flavour_name)
        print("The response of SystemFlavoursApi->get_flavour:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemFlavoursApi->get_flavour: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flavour_name** | **str**|  | 

### Return type

[**BagFlavourFullData**](BagFlavourFullData.md)

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

# **list_all_flavours**
> List[BagFlavourFullData] list_all_flavours()

List All Flavours

Get all KG flavours storage on db.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.bag_flavour_full_data import BagFlavourFullData
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
    api_instance = deepsearch.cps.apis.public_v2.SystemFlavoursApi(api_client)

    try:
        # List All Flavours
        api_response = api_instance.list_all_flavours()
        print("The response of SystemFlavoursApi->list_all_flavours:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemFlavoursApi->list_all_flavours: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[BagFlavourFullData]**](BagFlavourFullData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_flavours_by_project**
> ListProjectFlavours list_flavours_by_project(proj_key)

List Flavours By Project

Get project assignment flavours.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.list_project_flavours import ListProjectFlavours
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
    api_instance = deepsearch.cps.apis.public_v2.SystemFlavoursApi(api_client)
    proj_key = 'proj_key_example' # str | 

    try:
        # List Flavours By Project
        api_response = api_instance.list_flavours_by_project(proj_key)
        print("The response of SystemFlavoursApi->list_flavours_by_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemFlavoursApi->list_flavours_by_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 

### Return type

[**ListProjectFlavours**](ListProjectFlavours.md)

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

# **list_projects_flavours**
> List[ProjectsFlavours] list_projects_flavours()

List Projects Flavours

Get all projects and their flavours.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.projects_flavours import ProjectsFlavours
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
    api_instance = deepsearch.cps.apis.public_v2.SystemFlavoursApi(api_client)

    try:
        # List Projects Flavours
        api_response = api_instance.list_projects_flavours()
        print("The response of SystemFlavoursApi->list_projects_flavours:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemFlavoursApi->list_projects_flavours: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ProjectsFlavours]**](ProjectsFlavours.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_flavour**
> object save_flavour(new_flavour, bag_flavour_full_data)

Save Flavour

Save flavour on db.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.bag_flavour_full_data import BagFlavourFullData
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
    api_instance = deepsearch.cps.apis.public_v2.SystemFlavoursApi(api_client)
    new_flavour = True # bool | 
    bag_flavour_full_data = deepsearch.cps.apis.public_v2.BagFlavourFullData() # BagFlavourFullData | 

    try:
        # Save Flavour
        api_response = api_instance.save_flavour(new_flavour, bag_flavour_full_data)
        print("The response of SystemFlavoursApi->save_flavour:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemFlavoursApi->save_flavour: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_flavour** | **bool**|  | 
 **bag_flavour_full_data** | [**BagFlavourFullData**](BagFlavourFullData.md)|  | 

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

# **save_project_flavours**
> object save_project_flavours(projects_flavours)

Save Project Flavours

Save project flavours assignment on db.

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.projects_flavours import ProjectsFlavours
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
    api_instance = deepsearch.cps.apis.public_v2.SystemFlavoursApi(api_client)
    projects_flavours = deepsearch.cps.apis.public_v2.ProjectsFlavours() # ProjectsFlavours | 

    try:
        # Save Project Flavours
        api_response = api_instance.save_project_flavours(projects_flavours)
        print("The response of SystemFlavoursApi->save_project_flavours:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemFlavoursApi->save_project_flavours: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_flavours** | [**ProjectsFlavours**](ProjectsFlavours.md)|  | 

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

