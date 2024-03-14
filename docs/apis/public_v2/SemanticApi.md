# deepsearch.cps.apis.public_v2.SemanticApi

All URIs are relative to */api/cps/public/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ingest**](SemanticApi.md#ingest) | **POST** /project/{proj_key}/semantic/ingest | Ingest


# **ingest**
> CpsTask ingest(proj_key, semantic_ingest_request)

Ingest

Ingest documents and collections for RAG

### Example

* Api Key Authentication (Bearer):

```python
import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.models.cps_task import CpsTask
from deepsearch.cps.apis.public_v2.models.semantic_ingest_request import SemanticIngestRequest
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
    api_instance = deepsearch.cps.apis.public_v2.SemanticApi(api_client)
    proj_key = 'proj_key_example' # str | 
    semantic_ingest_request = deepsearch.cps.apis.public_v2.SemanticIngestRequest() # SemanticIngestRequest | 

    try:
        # Ingest
        api_response = api_instance.ingest(proj_key, semantic_ingest_request)
        print("The response of SemanticApi->ingest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SemanticApi->ingest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**|  | 
 **semantic_ingest_request** | [**SemanticIngestRequest**](SemanticIngestRequest.md)|  | 

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

