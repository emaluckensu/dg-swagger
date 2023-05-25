# kensu_datagalaxy_client.StructuresApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_structure**](StructuresApi.md#create_structure) | **POST** /structures/{versionId}/{parentId} | Create a structure.
[**creation_bulk_structures**](StructuresApi.md#creation_bulk_structures) | **POST** /structures/bulk/{versionId}/{parentId} | Bulk create structures
[**delete_bulk_structure**](StructuresApi.md#delete_bulk_structure) | **DELETE** /structures/bulk/{versionId} | Bulk delete structures
[**delete_structure**](StructuresApi.md#delete_structure) | **DELETE** /structures/{versionId}/{structureId} | Delete a structure.
[**get_structure**](StructuresApi.md#get_structure) | **GET** /structures/{versionId}/{structureId} | Return a structure.
[**get_structures_list**](StructuresApi.md#get_structures_list) | **GET** /structures | Return a list of structures.
[**get_types**](StructuresApi.md#get_types) | **GET** /structures/types | List the structure types.
[**update_bulk_structures**](StructuresApi.md#update_bulk_structures) | **PUT** /structures/bulk/{versionId}/{parentId} | Bulk edit structures
[**update_structure**](StructuresApi.md#update_structure) | **PUT** /structures/{versionId}/{structureId} | Edit a structure.

# **create_structure**
> EntityLocation create_structure(body, version_id, parent_id)

Create a structure.

Create a <b>structure</b> inside the specified <b>parent entity</b>.<br><br> Available structure types can be found thanks to the <code>GET /types</code> endpoint.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.StructuresApi(kensu_datagalaxy_client.ApiClient(configuration))
body = NULL # dict(str, AdditionalCustomAttribute) | 
version_id = kensu_datagalaxy_client.VersionId() # VersionId | 
parent_id = kensu_datagalaxy_client.DoubleUuid() # DoubleUuid | 

try:
    # Create a structure.
    api_response = api_instance.create_structure(body, version_id, parent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StructuresApi->create_structure: %s\n" % e)
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

# **creation_bulk_structures**
> BulkResult creation_bulk_structures(body, version_id, parent_id)

Bulk create structures

Massively create <b>structures</b> in the specified parent. (max 250 000)<br> <br>Available structure types can be found thanks to the <code>GET /types</code> endpoint.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.StructuresApi(kensu_datagalaxy_client.ApiClient(configuration))
body = [kensu_datagalaxy_client.StructureBulkCreation()] # list[StructureBulkCreation] | 
version_id = kensu_datagalaxy_client.VersionId() # VersionId | 
parent_id = kensu_datagalaxy_client.DoubleUuid() # DoubleUuid | 

try:
    # Bulk create structures
    api_response = api_instance.creation_bulk_structures(body, version_id, parent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StructuresApi->creation_bulk_structures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[StructureBulkCreation]**](StructureBulkCreation.md)|  | 
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

# **delete_bulk_structure**
> BulkDeleteResponse delete_bulk_structure(body, version_id)

Bulk delete structures

Deletes a list of **structures** referenced by their id. <br><br> **Warning: deleting a structure will delete its children objects in the process** <br> Deleted children objects will be included in the total count.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.StructuresApi(kensu_datagalaxy_client.ApiClient(configuration))
body = [kensu_datagalaxy_client.DoubleUuid()] # list[DoubleUuid] | List of ids referencing structures
version_id = kensu_datagalaxy_client.VersionId() # VersionId | 

try:
    # Bulk delete structures
    api_response = api_instance.delete_bulk_structure(body, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StructuresApi->delete_bulk_structure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[DoubleUuid]**](DoubleUuid.md)| List of ids referencing structures | 
 **version_id** | [**VersionId**](.md)|  | 

### Return type

[**BulkDeleteResponse**](BulkDeleteResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_structure**
> delete_structure(version_id, structure_id)

Delete a structure.

Deletes the specified <b>structure</b>.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.StructuresApi(kensu_datagalaxy_client.ApiClient(configuration))
version_id = kensu_datagalaxy_client.VersionId() # VersionId | 
structure_id = kensu_datagalaxy_client.DoubleUuid() # DoubleUuid | 

try:
    # Delete a structure.
    api_instance.delete_structure(version_id, structure_id)
except ApiException as e:
    print("Exception when calling StructuresApi->delete_structure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **structure_id** | [**DoubleUuid**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_structure**
> Entity get_structure(version_id, structure_id)

Return a structure.

Return the <b>details</b> of the specified <b>structure</b>.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.StructuresApi(kensu_datagalaxy_client.ApiClient(configuration))
version_id = kensu_datagalaxy_client.VersionId() # VersionId | 
structure_id = kensu_datagalaxy_client.DoubleUuid() # DoubleUuid | 

try:
    # Return a structure.
    api_response = api_instance.get_structure(version_id, structure_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StructuresApi->get_structure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **structure_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**Entity**](Entity.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_structures_list**
> PaginatedResponseEntitySummary_ get_structures_list(version_id, parent_id=parent_id, name=name, technical_name=technical_name, type=type, include_access_data=include_access_data, include_attributes=include_attributes, include_links=include_links, limit=limit, page=page, max_depth=max_depth)

Return a list of structures.

Return a list of all existing <b>structures</b> contained in the specified <b>source</b>. If <b>parentId</b> belongs to a <b>workspace</b>, a list of structures contained by all the sources of this <b>workspace</b> will be returned.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.StructuresApi(kensu_datagalaxy_client.ApiClient(configuration))
version_id = kensu_datagalaxy_client.VersionId() # VersionId | 
parent_id = kensu_datagalaxy_client.DoubleUuid() # DoubleUuid |  (optional)
name = 'name_example' # str |  (optional)
technical_name = 'technical_name_example' # str |  (optional)
type = kensu_datagalaxy_client.StructureType() # StructureType |  (optional)
include_access_data = kensu_datagalaxy_client.IncludeAccessData() # IncludeAccessData |  (optional)
include_attributes = kensu_datagalaxy_client.IncludeAttributes() # IncludeAttributes |  (optional)
include_links = kensu_datagalaxy_client.IncludeLinks() # IncludeLinks |  (optional)
limit = 20 # float |  (optional) (default to 20)
page = 1 # float |  (optional) (default to 1)
max_depth = kensu_datagalaxy_client.MaxDepth() # MaxDepth |  (optional)

try:
    # Return a list of structures.
    api_response = api_instance.get_structures_list(version_id, parent_id=parent_id, name=name, technical_name=technical_name, type=type, include_access_data=include_access_data, include_attributes=include_attributes, include_links=include_links, limit=limit, page=page, max_depth=max_depth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StructuresApi->get_structures_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **parent_id** | [**DoubleUuid**](.md)|  | [optional] 
 **name** | **str**|  | [optional] 
 **technical_name** | **str**|  | [optional] 
 **type** | [**StructureType**](.md)|  | [optional] 
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

List the structure types.

Return the list of <b>structure types</b> and their compatible <b>field types</b>,.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.StructuresApi(kensu_datagalaxy_client.ApiClient(configuration))

try:
    # List the structure types.
    api_response = api_instance.get_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StructuresApi->get_types: %s\n" % e)
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

# **update_bulk_structures**
> BulkResult update_bulk_structures(body, version_id, parent_id)

Bulk edit structures

Massively edit <b>structures</b> in the specified parent. (max 250 000)

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.StructuresApi(kensu_datagalaxy_client.ApiClient(configuration))
body = [kensu_datagalaxy_client.StructureBulkUpdate()] # list[StructureBulkUpdate] | 
version_id = kensu_datagalaxy_client.VersionId() # VersionId | 
parent_id = kensu_datagalaxy_client.DoubleUuid() # DoubleUuid | 

try:
    # Bulk edit structures
    api_response = api_instance.update_bulk_structures(body, version_id, parent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StructuresApi->update_bulk_structures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[StructureBulkUpdate]**](StructureBulkUpdate.md)|  | 
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

# **update_structure**
> EntityLocation update_structure(body, version_id, structure_id)

Edit a structure.

Modifies one or more <b>attributes</b> of the specified <b>structure</b>.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.StructuresApi(kensu_datagalaxy_client.ApiClient(configuration))
body = NULL # dict(str, AdditionalCustomAttribute) | 
version_id = kensu_datagalaxy_client.VersionId() # VersionId | 
structure_id = kensu_datagalaxy_client.DoubleUuid() # DoubleUuid | 

try:
    # Edit a structure.
    api_response = api_instance.update_structure(body, version_id, structure_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StructuresApi->update_structure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, AdditionalCustomAttribute)**](dict.md)|  | 
 **version_id** | [**VersionId**](.md)|  | 
 **structure_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**EntityLocation**](EntityLocation.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

