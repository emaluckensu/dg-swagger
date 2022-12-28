# swagger_client.FieldsApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_field**](FieldsApi.md#create_field) | **POST** /fields/{versionId}/{structureId} | Create a field.
[**creation_bulk_fields**](FieldsApi.md#creation_bulk_fields) | **POST** /fields/bulk/{versionId}/{parentId} | Bulk create fields.
[**delete_bulk_field**](FieldsApi.md#delete_bulk_field) | **DELETE** /fields/bulk/{versionId} | Bulk delete fields
[**delete_fields**](FieldsApi.md#delete_fields) | **DELETE** /fields/{versionId}/{fieldId} | Delete a field.
[**get_field**](FieldsApi.md#get_field) | **GET** /fields/{versionId}/{fieldId} | Return a field.
[**get_fields_list**](FieldsApi.md#get_fields_list) | **GET** /fields | Return a list of fields.
[**get_types**](FieldsApi.md#get_types) | **GET** /fields/types | List the field types.
[**update_bulk_fields**](FieldsApi.md#update_bulk_fields) | **PUT** /fields/bulk/{versionId}/{parentId} | Bulk edit fields.
[**update_field**](FieldsApi.md#update_field) | **PUT** /fields/{versionId}/{fieldId} | Edit a field.

# **create_field**
> EntityLocation create_field(body, version_id, structure_id)

Create a field.

Create a <b>field</b> inside the specified <b>structure</b>.<br><br> Available field types can be found thanks to the <code>GET /types</code> endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FieldsApi(swagger_client.ApiClient(configuration))
body = NULL # dict(str, AdditionalCustomAttribute) | 
version_id = swagger_client.VersionId() # VersionId | 
structure_id = swagger_client.DoubleUuid() # DoubleUuid | 

try:
    # Create a field.
    api_response = api_instance.create_field(body, version_id, structure_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldsApi->create_field: %s\n" % e)
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

# **creation_bulk_fields**
> BulkResult creation_bulk_fields(body, version_id, parent_id)

Bulk create fields.

Massively create <b>fields</b> in the specified <b>parent</b>. (max 250 000)<br> <br>Available field types can be found thanks to the <code>GET /types</code> endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FieldsApi(swagger_client.ApiClient(configuration))
body = [swagger_client.FieldBulkCreation()] # list[FieldBulkCreation] | 
version_id = swagger_client.VersionId() # VersionId | 
parent_id = swagger_client.DoubleUuid() # DoubleUuid | 

try:
    # Bulk create fields.
    api_response = api_instance.creation_bulk_fields(body, version_id, parent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldsApi->creation_bulk_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[FieldBulkCreation]**](FieldBulkCreation.md)|  | 
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

# **delete_bulk_field**
> BulkDeleteResponse delete_bulk_field(body, version_id)

Bulk delete fields

Deletes a list of **fields** referenced by their id. <br><br> **Warning: deleting a field will delete its children objects in the process** <br> Deleted children objects will be included in the total count.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FieldsApi(swagger_client.ApiClient(configuration))
body = [swagger_client.DoubleUuid()] # list[DoubleUuid] | List of ids referencing fields
version_id = swagger_client.VersionId() # VersionId | 

try:
    # Bulk delete fields
    api_response = api_instance.delete_bulk_field(body, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldsApi->delete_bulk_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[DoubleUuid]**](DoubleUuid.md)| List of ids referencing fields | 
 **version_id** | [**VersionId**](.md)|  | 

### Return type

[**BulkDeleteResponse**](BulkDeleteResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fields**
> delete_fields(version_id, field_id)

Delete a field.

Deletes the specified <b>field</b>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FieldsApi(swagger_client.ApiClient(configuration))
version_id = swagger_client.VersionId() # VersionId | 
field_id = swagger_client.DoubleUuid() # DoubleUuid | 

try:
    # Delete a field.
    api_instance.delete_fields(version_id, field_id)
except ApiException as e:
    print("Exception when calling FieldsApi->delete_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **field_id** | [**DoubleUuid**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_field**
> Entity get_field(version_id, field_id)

Return a field.

Return the <b>details</b> of the specified <b>field</b>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FieldsApi(swagger_client.ApiClient(configuration))
version_id = swagger_client.VersionId() # VersionId | 
field_id = swagger_client.DoubleUuid() # DoubleUuid | 

try:
    # Return a field.
    api_response = api_instance.get_field(version_id, field_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldsApi->get_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **field_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**Entity**](Entity.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fields_list**
> PaginatedResponseEntitySummary_ get_fields_list(version_id, parent_id=parent_id, name=name, technical_name=technical_name, type=type, include_access_data=include_access_data, include_attributes=include_attributes, include_links=include_links, limit=limit, page=page, max_depth=max_depth)

Return a list of fields.

Return a list of <b>fields</b> contained by a <b>structure</b>. If <b>parentId</b> belongs to a <b>source or workspace</b>, a list of fields contained by all the structures of this <b>source or workspace</b> will be returned.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FieldsApi(swagger_client.ApiClient(configuration))
version_id = swagger_client.VersionId() # VersionId | 
parent_id = swagger_client.DoubleUuid() # DoubleUuid |  (optional)
name = 'name_example' # str |  (optional)
technical_name = 'technical_name_example' # str |  (optional)
type = swagger_client.FieldType() # FieldType |  (optional)
include_access_data = swagger_client.IncludeAccessData() # IncludeAccessData |  (optional)
include_attributes = swagger_client.IncludeAttributes() # IncludeAttributes |  (optional)
include_links = swagger_client.IncludeLinks() # IncludeLinks |  (optional)
limit = 20 # float |  (optional) (default to 20)
page = 1 # float |  (optional) (default to 1)
max_depth = swagger_client.MaxDepth() # MaxDepth |  (optional)

try:
    # Return a list of fields.
    api_response = api_instance.get_fields_list(version_id, parent_id=parent_id, name=name, technical_name=technical_name, type=type, include_access_data=include_access_data, include_attributes=include_attributes, include_links=include_links, limit=limit, page=page, max_depth=max_depth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldsApi->get_fields_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **parent_id** | [**DoubleUuid**](.md)|  | [optional] 
 **name** | **str**|  | [optional] 
 **technical_name** | **str**|  | [optional] 
 **type** | [**FieldType**](.md)|  | [optional] 
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

List the field types.

Return the list of <b>field types</b> and their compatible <b>parent types</b>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FieldsApi(swagger_client.ApiClient(configuration))

try:
    # List the field types.
    api_response = api_instance.get_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldsApi->get_types: %s\n" % e)
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

# **update_bulk_fields**
> BulkResult update_bulk_fields(body, version_id, parent_id)

Bulk edit fields.

Massively edit <b>fields</b> in the specified parent. (max 250 000)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FieldsApi(swagger_client.ApiClient(configuration))
body = [swagger_client.FieldBulkUpdate()] # list[FieldBulkUpdate] | 
version_id = swagger_client.VersionId() # VersionId | 
parent_id = swagger_client.DoubleUuid() # DoubleUuid | 

try:
    # Bulk edit fields.
    api_response = api_instance.update_bulk_fields(body, version_id, parent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldsApi->update_bulk_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[FieldBulkUpdate]**](FieldBulkUpdate.md)|  | 
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

# **update_field**
> EntityLocation update_field(body, version_id, field_id)

Edit a field.

Modifies one or more <b>attributes</b> of the specified <b>field</b>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FieldsApi(swagger_client.ApiClient(configuration))
body = NULL # dict(str, AdditionalCustomAttribute) | 
version_id = swagger_client.VersionId() # VersionId | 
field_id = swagger_client.DoubleUuid() # DoubleUuid | 

try:
    # Edit a field.
    api_response = api_instance.update_field(body, version_id, field_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldsApi->update_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, AdditionalCustomAttribute)**](dict.md)|  | 
 **version_id** | [**VersionId**](.md)|  | 
 **field_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**EntityLocation**](EntityLocation.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

