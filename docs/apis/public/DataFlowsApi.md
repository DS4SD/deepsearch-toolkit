# deepsearch.cps.apis.public.DataFlowsApi

All URIs are relative to *http://localhost/api/cps/public/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assemble_project_data_flow**](DataFlowsApi.md#assemble_project_data_flow) | **POST** /project/{proj_key}/kgc/dataflows/actions/run | 
[**assemble_project_data_flow_template_into_knowledge_graph**](DataFlowsApi.md#assemble_project_data_flow_template_into_knowledge_graph) | **POST** /project/{proj_key}/kgc/dataflow_templates/{df_tpl_key}/actions/run | 
[**assemble_project_raw_data_flow_template_into_knowledge_graph**](DataFlowsApi.md#assemble_project_raw_data_flow_template_into_knowledge_graph) | **POST** /project/{proj_key}/kgc/raw_dataflow_templates/actions/run | 
[**create_project_data_flow_template**](DataFlowsApi.md#create_project_data_flow_template) | **POST** /project/{proj_key}/kgc/dataflow_templates | 
[**create_project_data_flow_template_delete_token**](DataFlowsApi.md#create_project_data_flow_template_delete_token) | **POST** /project/{proj_key}/kgc/dataflow_templates/{df_tpl_key}/delete_token | 
[**create_project_knowledge_graph_assemble_report**](DataFlowsApi.md#create_project_knowledge_graph_assemble_report) | **POST** /project/{proj_key}/dataset_assembles/{task_id}/report | 
[**debug_project_data_flow_template**](DataFlowsApi.md#debug_project_data_flow_template) | **POST** /project/{proj_key}/kgc_dataflow_templates/debug/{df_tpl_key} | 
[**delete_project_data_flow_template**](DataFlowsApi.md#delete_project_data_flow_template) | **DELETE** /project/{proj_key}/kgc/dataflow_templates/{df_tpl_key} | 
[**export_project_data_flow_template**](DataFlowsApi.md#export_project_data_flow_template) | **POST** /project/{proj_key}/kgc/dataflow_templates/{df_tpl_key}/export.json | 
[**export_public_data_flow_template**](DataFlowsApi.md#export_public_data_flow_template) | **POST** /project/public/kgc/dataflow_templates/{df_tpl_key}/export.json | 
[**get_project_data_flow**](DataFlowsApi.md#get_project_data_flow) | **GET** /project/{proj_key}/kgc/dataflow_templates/{df_tpl_key} | 
[**get_project_data_flow_template_topology**](DataFlowsApi.md#get_project_data_flow_template_topology) | **POST** /project/{proj_key}/kgc/dataflow_templates/{df_tpl_key}/topology | 
[**get_public_data_flow_template**](DataFlowsApi.md#get_public_data_flow_template) | **GET** /project/public/kgc/dataflow_templates/{df_tpl_key} | 
[**list_project_data_flow_templates**](DataFlowsApi.md#list_project_data_flow_templates) | **GET** /project/{proj_key}/kgc/dataflow_templates | 
[**list_public_data_flow_templates**](DataFlowsApi.md#list_public_data_flow_templates) | **GET** /project/public/kgc/dataflow_templates | 
[**load_project_data_flow**](DataFlowsApi.md#load_project_data_flow) | **POST** /project/{proj_key}/kgc/dataflows/actions/load | 
[**load_project_data_flow_template_into_knowledge_graph**](DataFlowsApi.md#load_project_data_flow_template_into_knowledge_graph) | **POST** /project/{proj_key}/kgc/dataflow_templates/{df_tpl_key}/actions/load | 
[**render_project_data_flow_template**](DataFlowsApi.md#render_project_data_flow_template) | **POST** /project/{proj_key}/kgc/dataflow_templates/{df_tpl_key}/actions/render | 
[**update_project_data_flow_template**](DataFlowsApi.md#update_project_data_flow_template) | **PUT** /project/{proj_key}/kgc/dataflow_templates/{df_tpl_key} | 
[**upload_project_data_flow_template**](DataFlowsApi.md#upload_project_data_flow_template) | **POST** /project/{proj_key}/kgc/dataflow_templates/from_json | 
[**validate_project_data_flow**](DataFlowsApi.md#validate_project_data_flow) | **POST** /project/{proj_key}/kgc/dataflows/actions/validate | 


# **assemble_project_data_flow**
> Task assemble_project_data_flow(proj_key, dataflow)



Run a dataflow

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
    api_instance = deepsearch.cps.apis.public.DataFlowsApi(api_client)
    proj_key = 'proj_key_example' # str | 
dataflow = deepsearch.cps.apis.public.KgcDataInput() # KgcDataInput | 

    try:
        api_response = api_instance.assemble_project_data_flow(proj_key, dataflow)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataFlowsApi->assemble_project_data_flow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **dataflow** | [**KgcDataInput**](KgcDataInput.md)|  | 

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
**200** | Task started. |  -  |
**400** | Invalid dataflow. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assemble_project_data_flow_template_into_knowledge_graph**
> Task assemble_project_data_flow_template_into_knowledge_graph(proj_key, df_tpl_key, options)



Render a single data flow template, replacing the variable placeholders by their actual values and run it.

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
    api_instance = deepsearch.cps.apis.public.DataFlowsApi(api_client)
    proj_key = 'proj_key_example' # str | 
df_tpl_key = 'df_tpl_key_example' # str | 
options = deepsearch.cps.apis.public.RunDataFlowTemplateOptions() # RunDataFlowTemplateOptions | 

    try:
        api_response = api_instance.assemble_project_data_flow_template_into_knowledge_graph(proj_key, df_tpl_key, options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataFlowsApi->assemble_project_data_flow_template_into_knowledge_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **df_tpl_key** | **str**|  | 
 **options** | [**RunDataFlowTemplateOptions**](RunDataFlowTemplateOptions.md)|  | 

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
**200** | Task started. |  -  |
**400** | Invalid dataflow. |  -  |
**404** | Data flow template doesn&#39;t exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assemble_project_raw_data_flow_template_into_knowledge_graph**
> Task assemble_project_raw_data_flow_template_into_knowledge_graph(proj_key, options)



Render a single data flow template, replacing the variable placeholders by their actual values and run it.

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
    api_instance = deepsearch.cps.apis.public.DataFlowsApi(api_client)
    proj_key = 'proj_key_example' # str | 
options = deepsearch.cps.apis.public.RunDataFlowTemplateOptions1() # RunDataFlowTemplateOptions1 | 

    try:
        api_response = api_instance.assemble_project_raw_data_flow_template_into_knowledge_graph(proj_key, options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataFlowsApi->assemble_project_raw_data_flow_template_into_knowledge_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **options** | [**RunDataFlowTemplateOptions1**](RunDataFlowTemplateOptions1.md)|  | 

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
**200** | Task started. |  -  |
**400** | Invalid dataflow. |  -  |
**404** | Data flow template doesn&#39;t exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_data_flow_template**
> DataFlow create_project_data_flow_template(proj_key, options)



Create a data flow template

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
    api_instance = deepsearch.cps.apis.public.DataFlowsApi(api_client)
    proj_key = 'proj_key_example' # str | 
options = deepsearch.cps.apis.public.CreateDataFlowTemplateOptions() # CreateDataFlowTemplateOptions | 

    try:
        api_response = api_instance.create_project_data_flow_template(proj_key, options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataFlowsApi->create_project_data_flow_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **options** | [**CreateDataFlowTemplateOptions**](CreateDataFlowTemplateOptions.md)|  | 

### Return type

[**DataFlow**](DataFlow.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dataflow created. |  -  |
**400** | Invalid dataflow. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_data_flow_template_delete_token**
> TokenResponse create_project_data_flow_template_delete_token(proj_key, df_tpl_key)



Get a token used to confirm the deletion of a data flow template.

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
    api_instance = deepsearch.cps.apis.public.DataFlowsApi(api_client)
    proj_key = 'proj_key_example' # str | 
df_tpl_key = 'df_tpl_key_example' # str | 

    try:
        api_response = api_instance.create_project_data_flow_template_delete_token(proj_key, df_tpl_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataFlowsApi->create_project_data_flow_template_delete_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **df_tpl_key** | **str**|  | 

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
**200** | Data flow deletion token. |  -  |
**404** | Data flow template not found. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_knowledge_graph_assemble_report**
> DataFlowAssembleReport create_project_knowledge_graph_assemble_report(proj_key, task_id, options)



Create a report for a data flow task assemble.

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
    api_instance = deepsearch.cps.apis.public.DataFlowsApi(api_client)
    proj_key = 'proj_key_example' # str | 
task_id = 'task_id_example' # str | 
options = deepsearch.cps.apis.public.DataFlowAssembleReportOptions() # DataFlowAssembleReportOptions | 

    try:
        api_response = api_instance.create_project_knowledge_graph_assemble_report(proj_key, task_id, options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataFlowsApi->create_project_knowledge_graph_assemble_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **task_id** | **str**|  | 
 **options** | [**DataFlowAssembleReportOptions**](DataFlowAssembleReportOptions.md)|  | 

### Return type

[**DataFlowAssembleReport**](DataFlowAssembleReport.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report. |  -  |
**404** | Task not found, or is not a data flow assemble. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_project_data_flow_template**
> object debug_project_data_flow_template(proj_key, df_tpl_key, options)



(Debug) get the fully rendered data flow, with all the coordinates set.

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
    api_instance = deepsearch.cps.apis.public.DataFlowsApi(api_client)
    proj_key = 'proj_key_example' # str | 
df_tpl_key = 'df_tpl_key_example' # str | 
options = deepsearch.cps.apis.public.FullyRenderedDataFlow() # FullyRenderedDataFlow | 

    try:
        api_response = api_instance.debug_project_data_flow_template(proj_key, df_tpl_key, options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataFlowsApi->debug_project_data_flow_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **df_tpl_key** | **str**|  | 
 **options** | [**FullyRenderedDataFlow**](FullyRenderedDataFlow.md)|  | 

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
**200** | Rendered data flow. |  -  |
**400** | Invalid dataflow. |  -  |
**404** | Data flow template doesn&#39;t exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_data_flow_template**
> delete_project_data_flow_template(proj_key, df_tpl_key, confirmation_token)



Delete a single data flow template

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
    api_instance = deepsearch.cps.apis.public.DataFlowsApi(api_client)
    proj_key = 'proj_key_example' # str | 
df_tpl_key = 'df_tpl_key_example' # str | 
confirmation_token = 'confirmation_token_example' # str | 

    try:
        api_instance.delete_project_data_flow_template(proj_key, df_tpl_key, confirmation_token)
    except ApiException as e:
        print("Exception when calling DataFlowsApi->delete_project_data_flow_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **df_tpl_key** | **str**|  | 
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
**204** | Data flow deleted. |  -  |
**404** | Data flow template doesn&#39;t exist. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_project_data_flow_template**
> file export_project_data_flow_template(proj_key, df_tpl_key)



Export a single data flow template

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
    api_instance = deepsearch.cps.apis.public.DataFlowsApi(api_client)
    proj_key = 'proj_key_example' # str | 
df_tpl_key = 'df_tpl_key_example' # str | 

    try:
        api_response = api_instance.export_project_data_flow_template(proj_key, df_tpl_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataFlowsApi->export_project_data_flow_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **df_tpl_key** | **str**|  | 

### Return type

**file**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.ibm.cps.df-template+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data flow template. |  -  |
**404** | Data flow template doesn&#39;t exist. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_public_data_flow_template**
> file export_public_data_flow_template(df_tpl_key)



Export a single public data flow template

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
    api_instance = deepsearch.cps.apis.public.DataFlowsApi(api_client)
    df_tpl_key = 'df_tpl_key_example' # str | 

    try:
        api_response = api_instance.export_public_data_flow_template(df_tpl_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataFlowsApi->export_public_data_flow_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **df_tpl_key** | **str**|  | 

### Return type

**file**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.ibm.cps.df-template+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data flow template. |  -  |
**404** | Data flow template doesn&#39;t exist. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_data_flow**
> DataFlow get_project_data_flow(proj_key, df_tpl_key)



Get a single data flow template

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
    api_instance = deepsearch.cps.apis.public.DataFlowsApi(api_client)
    proj_key = 'proj_key_example' # str | 
df_tpl_key = 'df_tpl_key_example' # str | 

    try:
        api_response = api_instance.get_project_data_flow(proj_key, df_tpl_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataFlowsApi->get_project_data_flow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **df_tpl_key** | **str**|  | 

### Return type

[**DataFlow**](DataFlow.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data flow template. |  -  |
**404** | Data flow template doesn&#39;t exist. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_data_flow_template_topology**
> Topology get_project_data_flow_template_topology(proj_key, df_tpl_key, options)



Render a single data flow template, replacing the variable placeholders by their actual values and get the resulting Knowledge Graph topology from it.

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
    api_instance = deepsearch.cps.apis.public.DataFlowsApi(api_client)
    proj_key = 'proj_key_example' # str | 
df_tpl_key = 'df_tpl_key_example' # str | 
options = deepsearch.cps.apis.public.DataFlowTopologyOptions() # DataFlowTopologyOptions | 

    try:
        api_response = api_instance.get_project_data_flow_template_topology(proj_key, df_tpl_key, options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataFlowsApi->get_project_data_flow_template_topology: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **df_tpl_key** | **str**|  | 
 **options** | [**DataFlowTopologyOptions**](DataFlowTopologyOptions.md)|  | 

### Return type

[**Topology**](Topology.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data flow topology. |  -  |
**400** | Invalid dataflow. |  -  |
**404** | Data flow template doesn&#39;t exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_data_flow_template**
> DataFlow get_public_data_flow_template(df_tpl_key)



Get a single data flow template

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
    api_instance = deepsearch.cps.apis.public.DataFlowsApi(api_client)
    df_tpl_key = 'df_tpl_key_example' # str | 

    try:
        api_response = api_instance.get_public_data_flow_template(df_tpl_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataFlowsApi->get_public_data_flow_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **df_tpl_key** | **str**|  | 

### Return type

[**DataFlow**](DataFlow.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data flow. |  -  |
**404** | Data flow template doesn&#39;t exist. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_data_flow_templates**
> list[DataFlowTemplateListItem] list_project_data_flow_templates(proj_key, query=query)



List a data flow templates

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
    api_instance = deepsearch.cps.apis.public.DataFlowsApi(api_client)
    proj_key = 'proj_key_example' # str | 
query = 'query_example' # str |  (optional)

    try:
        api_response = api_instance.list_project_data_flow_templates(proj_key, query=query)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataFlowsApi->list_project_data_flow_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **query** | **str**|  | [optional] 

### Return type

[**list[DataFlowTemplateListItem]**](DataFlowTemplateListItem.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of data flow templates. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_public_data_flow_templates**
> list[DataFlowTemplateListItem] list_public_data_flow_templates(query=query)



List public data flow templates

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
    api_instance = deepsearch.cps.apis.public.DataFlowsApi(api_client)
    query = 'query_example' # str |  (optional)

    try:
        api_response = api_instance.list_public_data_flow_templates(query=query)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataFlowsApi->list_public_data_flow_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | [optional] 

### Return type

[**list[DataFlowTemplateListItem]**](DataFlowTemplateListItem.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of data flow templates. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_project_data_flow**
> Task load_project_data_flow(proj_key, options)



Load a dataflow into a KG

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
    api_instance = deepsearch.cps.apis.public.DataFlowsApi(api_client)
    proj_key = 'proj_key_example' # str | 
options = deepsearch.cps.apis.public.LoadKgcDataInput() # LoadKgcDataInput | 

    try:
        api_response = api_instance.load_project_data_flow(proj_key, options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataFlowsApi->load_project_data_flow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **options** | [**LoadKgcDataInput**](LoadKgcDataInput.md)|  | 

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
**200** | Task started. |  -  |
**400** | Invalid dataflow. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_project_data_flow_template_into_knowledge_graph**
> Task load_project_data_flow_template_into_knowledge_graph(proj_key, df_tpl_key, options)



Render a single data flow template, replacing the variable placeholders by their actual values and load it into a Knowledge Graph.

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
    api_instance = deepsearch.cps.apis.public.DataFlowsApi(api_client)
    proj_key = 'proj_key_example' # str | 
df_tpl_key = 'df_tpl_key_example' # str | 
options = deepsearch.cps.apis.public.LoadDataFlowIntoKnowledgeGraphOptions1() # LoadDataFlowIntoKnowledgeGraphOptions1 | 

    try:
        api_response = api_instance.load_project_data_flow_template_into_knowledge_graph(proj_key, df_tpl_key, options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataFlowsApi->load_project_data_flow_template_into_knowledge_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **df_tpl_key** | **str**|  | 
 **options** | [**LoadDataFlowIntoKnowledgeGraphOptions1**](LoadDataFlowIntoKnowledgeGraphOptions1.md)|  | 

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
**200** | Task started. |  -  |
**400** | Invalid dataflow. |  -  |
**404** | Data flow template doesn&#39;t exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_project_data_flow_template**
> object render_project_data_flow_template(proj_key, df_tpl_key, options)



Render a single data flow template, replacing the variable placeholders by their actual values.

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
    api_instance = deepsearch.cps.apis.public.DataFlowsApi(api_client)
    proj_key = 'proj_key_example' # str | 
df_tpl_key = 'df_tpl_key_example' # str | 
options = deepsearch.cps.apis.public.RenderDataFlowTemplateOptions() # RenderDataFlowTemplateOptions | 

    try:
        api_response = api_instance.render_project_data_flow_template(proj_key, df_tpl_key, options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataFlowsApi->render_project_data_flow_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **df_tpl_key** | **str**|  | 
 **options** | [**RenderDataFlowTemplateOptions**](RenderDataFlowTemplateOptions.md)|  | 

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
**200** | Rendered data flow |  -  |
**400** | Invalid dataflow. |  -  |
**404** | Data flow template doesn&#39;t exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_data_flow_template**
> DataFlow update_project_data_flow_template(proj_key, df_tpl_key, options)



Update a data flow template

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
    api_instance = deepsearch.cps.apis.public.DataFlowsApi(api_client)
    proj_key = 'proj_key_example' # str | 
df_tpl_key = 'df_tpl_key_example' # str | 
options = deepsearch.cps.apis.public.UpdateDataFlowOptions() # UpdateDataFlowOptions | 

    try:
        api_response = api_instance.update_project_data_flow_template(proj_key, df_tpl_key, options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataFlowsApi->update_project_data_flow_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **df_tpl_key** | **str**|  | 
 **options** | [**UpdateDataFlowOptions**](UpdateDataFlowOptions.md)|  | 

### Return type

[**DataFlow**](DataFlow.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dataflow updated. |  -  |
**400** | Invalid dataflow. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_project_data_flow_template**
> DataFlow upload_project_data_flow_template(proj_key, contents, name=name, description=description, public=public)



Create a data flow template from a JSON file. **DEPRECATED**: use `create_project_data_flow_template` 

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
    api_instance = deepsearch.cps.apis.public.DataFlowsApi(api_client)
    proj_key = 'proj_key_example' # str | 
contents = '/path/to/file' # file | 
name = 'name_example' # str |  (optional)
description = 'description_example' # str |  (optional)
public = True # bool |  (optional)

    try:
        api_response = api_instance.upload_project_data_flow_template(proj_key, contents, name=name, description=description, public=public)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataFlowsApi->upload_project_data_flow_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **contents** | **file**|  | 
 **name** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **public** | **bool**|  | [optional] 

### Return type

[**DataFlow**](DataFlow.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dataflow created. |  -  |
**400** | Invalid dataflow. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_project_data_flow**
> validate_project_data_flow(proj_key, dataflow)



Validate a dataflow

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
    api_instance = deepsearch.cps.apis.public.DataFlowsApi(api_client)
    proj_key = 'proj_key_example' # str | 
dataflow = deepsearch.cps.apis.public.KgcDataInput() # KgcDataInput | 

    try:
        api_instance.validate_project_data_flow(proj_key, dataflow)
    except ApiException as e:
        print("Exception when calling DataFlowsApi->validate_project_data_flow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **dataflow** | [**KgcDataInput**](KgcDataInput.md)|  | 

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
**200** | Validation successful. |  -  |
**400** | Invalid dataflow. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

