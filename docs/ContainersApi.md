# kensu_datagalaxy_client.ContainersApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bulk_containers**](ContainersApi.md#create_bulk_containers) | **POST** /containers/bulk/{versionId}/{parentId} | Bulk create containers.
[**create_container**](ContainersApi.md#create_container) | **POST** /containers/{versionId}/{parentId} | Create a container.
[**delete_bulk_container**](ContainersApi.md#delete_bulk_container) | **DELETE** /containers/bulk/{versionId} | Bulk delete containers
[**delete_container**](ContainersApi.md#delete_container) | **DELETE** /containers/{versionId}/{containerId} | Delete a container.
[**get_container**](ContainersApi.md#get_container) | **GET** /containers/{versionId}/{containerId} | Return the details of a container.
[**get_containers_list**](ContainersApi.md#get_containers_list) | **GET** /containers | Return a list of containers.
[**get_types**](ContainersApi.md#get_types) | **GET** /containers/types | List the container types.
[**update_bulk_containers**](ContainersApi.md#update_bulk_containers) | **PUT** /containers/bulk/{versionId}/{parentId} | Bulk edit containers.
[**update_container**](ContainersApi.md#update_container) | **PUT** /containers/{versionId}/{containerId} | Edit a container.

# **create_bulk_containers**
> BulkResult create_bulk_containers(body, version_id, parent_id)

Bulk create containers.

Massively create <b>containers</b> in the specified <b>parent</b>. (max 250 000)<br> <br>Available container types can be found thanks to the <code>GET /types</code> endpoint.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.ContainersApi(kensu_datagalaxy_client.ApiClient(configuration))
body = [kensu_datagalaxy_client.ContainerBulkCreation()] # list[ContainerBulkCreation] | 
version_id = kensu_datagalaxy_client.VersionId() # VersionId | 
parent_id = kensu_datagalaxy_client.DoubleUuid() # DoubleUuid | 

try:
    # Bulk create containers.
    api_response = api_instance.create_bulk_containers(body, version_id, parent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->create_bulk_containers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ContainerBulkCreation]**](ContainerBulkCreation.md)|  | 
 **version_id** | [**VersionId**](.md)|  | 
 **parent_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**BulkResult**](BulkResult.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_container**
> EntityLocation create_container(body, version_id, parent_id)

Create a container.

Create a <b>container</b> in the specified <b>parent</b>.<br><br> Available container types can be found thanks to the <code>GET /types</code> endpoint.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.ContainersApi(kensu_datagalaxy_client.ApiClient(configuration))
body = NULL # dict(str, AdditionalCustomAttribute) | 
version_id = kensu_datagalaxy_client.VersionId() # VersionId | 
parent_id = kensu_datagalaxy_client.DoubleUuid() # DoubleUuid | 

try:
    # Create a container.
    api_response = api_instance.create_container(body, version_id, parent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->create_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, AdditionalCustomAttribute)**](dict.md)|  | 
 **version_id** | [**VersionId**](.md)|  | 
 **parent_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**EntityLocation**](EntityLocation.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bulk_container**
> BulkDeleteResponse delete_bulk_container(body, version_id)

Bulk delete containers

Deletes a list of **container** referenced by their id. <br><br> **Warning: deleting a container will delete its children objects in the process** <br> Deleted children objects will be included in the total count.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.ContainersApi(kensu_datagalaxy_client.ApiClient(configuration))
body = [kensu_datagalaxy_client.DoubleUuid()] # list[DoubleUuid] | List of ids referencing containers
version_id = kensu_datagalaxy_client.VersionId() # VersionId | 

try:
    # Bulk delete containers
    api_response = api_instance.delete_bulk_container(body, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->delete_bulk_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[DoubleUuid]**](DoubleUuid.md)| List of ids referencing containers | 
 **version_id** | [**VersionId**](.md)|  | 

### Return type

[**BulkDeleteResponse**](BulkDeleteResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_container**
> delete_container(version_id, container_id)

Delete a container.

Deletes the specified <b>container</b>.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.ContainersApi(kensu_datagalaxy_client.ApiClient(configuration))
version_id = kensu_datagalaxy_client.VersionId() # VersionId | 
container_id = kensu_datagalaxy_client.DoubleUuid() # DoubleUuid | 

try:
    # Delete a container.
    api_instance.delete_container(version_id, container_id)
except ApiException as e:
    print("Exception when calling ContainersApi->delete_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **container_id** | [**DoubleUuid**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_container**
> Entity get_container(version_id, container_id)

Return the details of a container.

Return the details of a container.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.ContainersApi(kensu_datagalaxy_client.ApiClient(configuration))
version_id = kensu_datagalaxy_client.VersionId() # VersionId | 
container_id = kensu_datagalaxy_client.DoubleUuid() # DoubleUuid | 

try:
    # Return the details of a container.
    api_response = api_instance.get_container(version_id, container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->get_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **container_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**Entity**](Entity.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_containers_list**
> PaginatedResponseEntitySummary_ get_containers_list(version_id, parent_id=parent_id, name=name, technical_name=technical_name, type=type, include_access_data=include_access_data, include_attributes=include_attributes, include_links=include_links, limit=limit, page=page, max_depth=max_depth)

Return a list of containers.

Return a list of all <b>containers</b> contained in the specified <b>source / container</b>.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.ContainersApi(kensu_datagalaxy_client.ApiClient(configuration))
version_id = kensu_datagalaxy_client.VersionId() # VersionId | 
parent_id = kensu_datagalaxy_client.DoubleUuid() # DoubleUuid |  (optional)
name = 'name_example' # str |  (optional)
technical_name = 'technical_name_example' # str |  (optional)
type = kensu_datagalaxy_client.ContainerType() # ContainerType |  (optional)
include_access_data = kensu_datagalaxy_client.IncludeAccessData() # IncludeAccessData |  (optional)
include_attributes = kensu_datagalaxy_client.IncludeAttributes() # IncludeAttributes |  (optional)
include_links = kensu_datagalaxy_client.IncludeLinks() # IncludeLinks |  (optional)
limit = 20 # float |  (optional) (default to 20)
page = 1 # float |  (optional) (default to 1)
max_depth = kensu_datagalaxy_client.MaxDepth() # MaxDepth |  (optional)

try:
    # Return a list of containers.
    api_response = api_instance.get_containers_list(version_id, parent_id=parent_id, name=name, technical_name=technical_name, type=type, include_access_data=include_access_data, include_attributes=include_attributes, include_links=include_links, limit=limit, page=page, max_depth=max_depth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->get_containers_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **parent_id** | [**DoubleUuid**](.md)|  | [optional] 
 **name** | **str**|  | [optional] 
 **technical_name** | **str**|  | [optional] 
 **type** | [**ContainerType**](.md)|  | [optional] 
 **include_access_data** | [**IncludeAccessData**](.md)|  | [optional] 
 **include_attributes** | [**IncludeAttributes**](.md)|  | [optional] 
 **include_links** | [**IncludeLinks**](.md)|  | [optional] 
 **limit** | **float**|  | [optional] [default to 20]
 **page** | **float**|  | [optional] [default to 1]
 **max_depth** | [**MaxDepth**](.md)|  | [optional] 

### Return type

[**PaginatedResponseEntitySummary_**](PaginatedResponseEntitySummary_.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_types**
> list[CompatibilityDefinition] get_types()

List the container types.

Return the list of <b>containers types</b> and their compatible <b>children types</b>,.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.ContainersApi(kensu_datagalaxy_client.ApiClient(configuration))

try:
    # List the container types.
    api_response = api_instance.get_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->get_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CompatibilityDefinition]**](CompatibilityDefinition.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bulk_containers**
> BulkResult update_bulk_containers(body, version_id, parent_id)

Bulk edit containers.

Massively edit <b>containers</b> in the specified <b>parent</b>. (max 250 000)

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.ContainersApi(kensu_datagalaxy_client.ApiClient(configuration))
body = [kensu_datagalaxy_client.ContainerBulkUpdate()] # list[ContainerBulkUpdate] | 
version_id = kensu_datagalaxy_client.VersionId() # VersionId | 
parent_id = kensu_datagalaxy_client.DoubleUuid() # DoubleUuid | 

try:
    # Bulk edit containers.
    api_response = api_instance.update_bulk_containers(body, version_id, parent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->update_bulk_containers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ContainerBulkUpdate]**](ContainerBulkUpdate.md)|  | 
 **version_id** | [**VersionId**](.md)|  | 
 **parent_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**BulkResult**](BulkResult.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_container**
> EntityLocation update_container(body, version_id, container_id)

Edit a container.

Modifies one or more attributes of the specified <b>container</b>.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.ContainersApi(kensu_datagalaxy_client.ApiClient(configuration))
body = NULL # dict(str, AdditionalCustomAttribute) | 
version_id = kensu_datagalaxy_client.VersionId() # VersionId | 
container_id = kensu_datagalaxy_client.DoubleUuid() # DoubleUuid | 

try:
    # Edit a container.
    api_response = api_instance.update_container(body, version_id, container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->update_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, AdditionalCustomAttribute)**](dict.md)|  | 
 **version_id** | [**VersionId**](.md)|  | 
 **container_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**EntityLocation**](EntityLocation.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

