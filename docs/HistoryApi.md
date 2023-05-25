# kensu_datagalaxy_client.HistoryApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**objects_history**](HistoryApi.md#objects_history) | **GET** /history/objects | Return recently accessed objects
[**queries_history**](HistoryApi.md#queries_history) | **GET** /history/search/queries | Return saved search queries

# **objects_history**
> ObjectsHistoryResult objects_history(limit=limit)

Return recently accessed objects

The object history feature keeps a record of your recently accessed objects. \\ \\ Each entry of the object history contains the object’s main informations, including properties to help retrieve it such as <code>objectUrl</code> (which points to the object’s detail page in DataGalaxy platform) and <code>location</code> (which is a prebuild API endpoint’s path to the object’s details).\\ \\ New objects are automatically added to the history when you fetch an object's details using the <code>GET /{dataType}/{versionId}/{objectId}</code> (e.g.: <a href=\"/v2/documentation/beta#operation/GetProperty\">GET /properties/{versionId}/{objectId}</a>). <h3>Disclaimer</h3> <i>This endpoint is meant to be requested using an <code>accessToken</code> generated from a Personal Access Token (PAT). Using a PAT will tie the endpoint's response to the user's history. </i>

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.HistoryApi(kensu_datagalaxy_client.ApiClient(configuration))
limit = 20 # float |  (optional) (default to 20)

try:
    # Return recently accessed objects
    api_response = api_instance.objects_history(limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HistoryApi->objects_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**|  | [optional] [default to 20]

### Return type

[**ObjectsHistoryResult**](ObjectsHistoryResult.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **queries_history**
> QueriesHistoryResult queries_history(limit=limit)

Return saved search queries

The <b>queries history feature</b> helps you retrieve search payloads you previously requested either with the <code>POST /search</code> endpoint or via the DataGalaxy web application.\\ This history is saved manually. If you want to add an entry to it, set the <code>saveSearchPayload</code> property to <code>true</code> in your <code>POST /search</code> request payload.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.HistoryApi(kensu_datagalaxy_client.ApiClient(configuration))
limit = 20 # float |  (optional) (default to 20)

try:
    # Return saved search queries
    api_response = api_instance.queries_history(limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HistoryApi->queries_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**|  | [optional] [default to 20]

### Return type

[**QueriesHistoryResult**](QueriesHistoryResult.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

