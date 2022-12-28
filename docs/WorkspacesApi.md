# swagger_client.WorkspacesApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_versions**](WorkspacesApi.md#get_versions) | **GET** /workspaces/{workspaceId}/versions | Lists the versions of a workspace.
[**get_workspaces**](WorkspacesApi.md#get_workspaces) | **GET** /workspaces | List all workspaces.

# **get_versions**
> PaginatedResponseVersion_ get_versions(workspace_id, limit=limit, page=page)

Lists the versions of a workspace.

Return the list of versions available in the specified workspace.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))
workspace_id = swagger_client.DoubleUuid() # DoubleUuid | 
limit = 20 # float |  (optional) (default to 20)
page = 1 # float |  (optional) (default to 1)

try:
    # Lists the versions of a workspace.
    api_response = api_instance.get_versions(workspace_id, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | [**DoubleUuid**](.md)|  | 
 **limit** | **float**|  | [optional] [default to 20]
 **page** | **float**|  | [optional] [default to 1]

### Return type

[**PaginatedResponseVersion_**](PaginatedResponseVersion_.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspaces**
> Workspaces get_workspaces(name=name)

List all workspaces.

Provide a <b>name</b> to find a specific workspace. \\ If no querystring is provided a list of all workspaces will be returned.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.WorkspacesApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str |  (optional)

try:
    # List all workspaces.
    api_response = api_instance.get_workspaces(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_workspaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 

### Return type

[**Workspaces**](Workspaces.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

