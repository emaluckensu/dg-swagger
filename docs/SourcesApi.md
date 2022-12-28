# swagger_client.SourcesApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bulk_sources**](SourcesApi.md#create_bulk_sources) | **POST** /sources/bulk/{versionId} | Bulk create sources.
[**create_fk**](SourcesApi.md#create_fk) | **PUT** /sources/{versionId}/{sourceId}/foreignKeys | Update/create the foreign keys of a relational source.
[**create_pk**](SourcesApi.md#create_pk) | **PUT** /sources/{versionId}/{sourceId}/primaryKeys | Update/create the primary keys of a relational source.
[**create_sources**](SourcesApi.md#create_sources) | **POST** /sources/{versionId} | Create a source.
[**create_sources_bulk_tree**](SourcesApi.md#create_sources_bulk_tree) | **POST** /sources/bulktree/{versionId} | Bulk upsert a dictionary entities tree
[**delete_bulk_source**](SourcesApi.md#delete_bulk_source) | **DELETE** /sources/bulk/{versionId} | Bulk delete sources
[**delete_fk**](SourcesApi.md#delete_fk) | **DELETE** /sources/{versionId}/{sourceId}/foreignKey/{foreignKeyId} | Delete a foreignKey.
[**delete_pk**](SourcesApi.md#delete_pk) | **DELETE** /sources/{versionId}/{sourceId}/privateKey/{columnId} | Remove column from privateKey.
[**delete_source**](SourcesApi.md#delete_source) | **DELETE** /sources/{versionId}/{sourceId} | Delete a source.
[**get_fk**](SourcesApi.md#get_fk) | **GET** /sources/{versionId}/{sourceId}/foreignKeys | Get Foreign Keys list.
[**get_pk**](SourcesApi.md#get_pk) | **GET** /sources/{versionId}/{sourceId}/primaryKey | Get Primary Keys list.
[**get_source**](SourcesApi.md#get_source) | **GET** /sources/{versionId}/{sourceId} | Return a source.
[**get_sources_list**](SourcesApi.md#get_sources_list) | **GET** /sources | Return a list of sources.
[**get_types**](SourcesApi.md#get_types) | **GET** /sources/types | List the source types.
[**update_bulk_source**](SourcesApi.md#update_bulk_source) | **PUT** /sources/bulk/{versionId} | Bulk edit sources.
[**update_source**](SourcesApi.md#update_source) | **PUT** /sources/{versionId}/{sourceId} | Edit a source.

# **create_bulk_sources**
> BulkResult create_bulk_sources(body, version_id)

Bulk create sources.

Create <b>sources</b> in bulk mode (max 100) in the specified workspace.<br> <br>Available structure types can be found thanks to the <code>GET /types</code> endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SourcesApi(swagger_client.ApiClient(configuration))
body = [swagger_client.SourceBulkCreation()] # list[SourceBulkCreation] | 
version_id = swagger_client.VersionId() # VersionId | 

try:
    # Bulk create sources.
    api_response = api_instance.create_bulk_sources(body, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesApi->create_bulk_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[SourceBulkCreation]**](SourceBulkCreation.md)|  | 
 **version_id** | [**VersionId**](.md)|  | 

### Return type

[**BulkResult**](BulkResult.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fk**
> BulkResult create_fk(body, version_id, source_id)

Update/create the foreign keys of a relational source.

Update or create the primary keys of a relational source.<br> Path properties have the following format: <code>pkTablePath: \"\\\\\\containerName\\\\\\tableName\"</code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SourcesApi(swagger_client.ApiClient(configuration))
body = [swagger_client.ForeignKeyPayload()] # list[ForeignKeyPayload] | 
version_id = swagger_client.VersionId() # VersionId | 
source_id = swagger_client.DoubleUuid() # DoubleUuid | 

try:
    # Update/create the foreign keys of a relational source.
    api_response = api_instance.create_fk(body, version_id, source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesApi->create_fk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ForeignKeyPayload]**](ForeignKeyPayload.md)|  | 
 **version_id** | [**VersionId**](.md)|  | 
 **source_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**BulkResult**](BulkResult.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pk**
> BulkResult create_pk(body, version_id, source_id)

Update/create the primary keys of a relational source.

Update or create the primary keys of a relational source.<br> <code>tablePath</code> has the following format: <code>tablePath: \"\\\\\\containerName\\\\\\tableName\"</code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SourcesApi(swagger_client.ApiClient(configuration))
body = [swagger_client.PrimaryKeyPayload()] # list[PrimaryKeyPayload] | 
version_id = swagger_client.VersionId() # VersionId | 
source_id = swagger_client.DoubleUuid() # DoubleUuid | 

try:
    # Update/create the primary keys of a relational source.
    api_response = api_instance.create_pk(body, version_id, source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesApi->create_pk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[PrimaryKeyPayload]**](PrimaryKeyPayload.md)|  | 
 **version_id** | [**VersionId**](.md)|  | 
 **source_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**BulkResult**](BulkResult.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sources**
> EntityLocation create_sources(body, version_id)

Create a source.

Create a <b>source</b> in the specified <b>workspace</b>.<br><br> Available source types can be found thanks to the <code>GET /types</code> endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SourcesApi(swagger_client.ApiClient(configuration))
body = NULL # dict(str, AdditionalCustomAttribute) | 
version_id = swagger_client.VersionId() # VersionId | 

try:
    # Create a source.
    api_response = api_instance.create_sources(body, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesApi->create_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, AdditionalCustomAttribute)**](dict.md)|  | 
 **version_id** | [**VersionId**](.md)|  | 

### Return type

[**EntityLocation**](EntityLocation.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sources_bulk_tree**
> BulkResult create_sources_bulk_tree(body, version_id)

Bulk upsert a dictionary entities tree

This route upserts a Source and all it's children up to a total of 250 000 entities.<br> Existing entities are updated and non-existing ones are created. Upsert also applies to entities attributes.<br> Read our <a href=\"https://datagalaxy.freshdesk.com/en/support/solutions/articles/35000151776-mass-entity-creation-with-bulktree-routes\" target='_new'>article on bulktree</a> for more informations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SourcesApi(swagger_client.ApiClient(configuration))
body = NULL # dict(str, AdditionalCustomAttributeBulk) | 
version_id = swagger_client.VersionId() # VersionId | 

try:
    # Bulk upsert a dictionary entities tree
    api_response = api_instance.create_sources_bulk_tree(body, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesApi->create_sources_bulk_tree: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, AdditionalCustomAttributeBulk)**](dict.md)|  | 
 **version_id** | [**VersionId**](.md)|  | 

### Return type

[**BulkResult**](BulkResult.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bulk_source**
> BulkDeleteResponse delete_bulk_source(body, version_id)

Bulk delete sources

Deletes a list of **sources** referenced by their id. <br><br> **Warning: deleting a source will delete its children objects in the process** <br> Deleted children objects will be included in the total count.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SourcesApi(swagger_client.ApiClient(configuration))
body = [swagger_client.DoubleUuid()] # list[DoubleUuid] | List of ids referencing sources
version_id = swagger_client.VersionId() # VersionId | 

try:
    # Bulk delete sources
    api_response = api_instance.delete_bulk_source(body, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesApi->delete_bulk_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[DoubleUuid]**](DoubleUuid.md)| List of ids referencing sources | 
 **version_id** | [**VersionId**](.md)|  | 

### Return type

[**BulkDeleteResponse**](BulkDeleteResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fk**
> delete_fk(version_id, source_id, foreign_key_id)

Delete a foreignKey.

Deletes the specified <b>foreignKey</b>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SourcesApi(swagger_client.ApiClient(configuration))
version_id = swagger_client.VersionId() # VersionId | 
source_id = swagger_client.DoubleUuid() # DoubleUuid | 
foreign_key_id = swagger_client.DoubleUuid() # DoubleUuid | 

try:
    # Delete a foreignKey.
    api_instance.delete_fk(version_id, source_id, foreign_key_id)
except ApiException as e:
    print("Exception when calling SourcesApi->delete_fk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **source_id** | [**DoubleUuid**](.md)|  | 
 **foreign_key_id** | [**DoubleUuid**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pk**
> delete_pk(version_id, source_id, column_id)

Remove column from privateKey.

Remove the specified <b>column</b> from its attributed privateKey.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SourcesApi(swagger_client.ApiClient(configuration))
version_id = swagger_client.VersionId() # VersionId | 
source_id = swagger_client.DoubleUuid() # DoubleUuid | 
column_id = swagger_client.DoubleUuid() # DoubleUuid | 

try:
    # Remove column from privateKey.
    api_instance.delete_pk(version_id, source_id, column_id)
except ApiException as e:
    print("Exception when calling SourcesApi->delete_pk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **source_id** | [**DoubleUuid**](.md)|  | 
 **column_id** | [**DoubleUuid**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_source**
> delete_source(version_id, source_id)

Delete a source.

Deletes the specified <b>source</b>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SourcesApi(swagger_client.ApiClient(configuration))
version_id = swagger_client.VersionId() # VersionId | 
source_id = swagger_client.DoubleUuid() # DoubleUuid | 

try:
    # Delete a source.
    api_instance.delete_source(version_id, source_id)
except ApiException as e:
    print("Exception when calling SourcesApi->delete_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **source_id** | [**DoubleUuid**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fk**
> list[ForeignKey] get_fk(version_id, source_id)

Get Foreign Keys list.

Return the list of Primary Keys in the specified <b>source</b>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SourcesApi(swagger_client.ApiClient(configuration))
version_id = swagger_client.VersionId() # VersionId | 
source_id = swagger_client.DoubleUuid() # DoubleUuid | 

try:
    # Get Foreign Keys list.
    api_response = api_instance.get_fk(version_id, source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesApi->get_fk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **source_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**list[ForeignKey]**](ForeignKey.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pk**
> list[PrimaryKey] get_pk(version_id, source_id)

Get Primary Keys list.

Return the list of Primary Keys in the specified <b>source</b>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SourcesApi(swagger_client.ApiClient(configuration))
version_id = swagger_client.VersionId() # VersionId | 
source_id = swagger_client.DoubleUuid() # DoubleUuid | 

try:
    # Get Primary Keys list.
    api_response = api_instance.get_pk(version_id, source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesApi->get_pk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **source_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**list[PrimaryKey]**](PrimaryKey.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source**
> Entity get_source(version_id, source_id)

Return a source.

Return the <b>details</b> of the specified <b>source</b>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SourcesApi(swagger_client.ApiClient(configuration))
version_id = swagger_client.VersionId() # VersionId | 
source_id = swagger_client.DoubleUuid() # DoubleUuid | 

try:
    # Return a source.
    api_response = api_instance.get_source(version_id, source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesApi->get_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **source_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**Entity**](Entity.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sources_list**
> PaginatedResponseEntitySummary_ get_sources_list(version_id, name=name, technical_name=technical_name, type=type, include_access_data=include_access_data, include_attributes=include_attributes, include_links=include_links, limit=limit, page=page, max_depth=max_depth)

Return a list of sources.

Return a list of all <b>sources</b> contained in the specified <b>workspace</b>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SourcesApi(swagger_client.ApiClient(configuration))
version_id = swagger_client.VersionId() # VersionId | 
name = 'name_example' # str |  (optional)
technical_name = 'technical_name_example' # str |  (optional)
type = swagger_client.SourceType() # SourceType |  (optional)
include_access_data = swagger_client.IncludeAccessData() # IncludeAccessData |  (optional)
include_attributes = swagger_client.IncludeAttributes() # IncludeAttributes |  (optional)
include_links = swagger_client.IncludeLinks() # IncludeLinks |  (optional)
limit = 20 # float |  (optional) (default to 20)
page = 1 # float |  (optional) (default to 1)
max_depth = swagger_client.MaxDepth() # MaxDepth |  (optional)

try:
    # Return a list of sources.
    api_response = api_instance.get_sources_list(version_id, name=name, technical_name=technical_name, type=type, include_access_data=include_access_data, include_attributes=include_attributes, include_links=include_links, limit=limit, page=page, max_depth=max_depth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesApi->get_sources_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **name** | **str**|  | [optional] 
 **technical_name** | **str**|  | [optional] 
 **type** | [**SourceType**](.md)|  | [optional] 
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

List the source types.

Return the list of <b>source types</b> and their compatible <b>children types</b>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SourcesApi(swagger_client.ApiClient(configuration))

try:
    # List the source types.
    api_response = api_instance.get_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesApi->get_types: %s\n" % e)
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

# **update_bulk_source**
> BulkResult update_bulk_source(body, version_id)

Bulk edit sources.

Edit <b>sources</b> in bulk mode (max 100) in the specified workspace.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SourcesApi(swagger_client.ApiClient(configuration))
body = [swagger_client.SourceBulkUpdate()] # list[SourceBulkUpdate] | 
version_id = swagger_client.VersionId() # VersionId | 

try:
    # Bulk edit sources.
    api_response = api_instance.update_bulk_source(body, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesApi->update_bulk_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[SourceBulkUpdate]**](SourceBulkUpdate.md)|  | 
 **version_id** | [**VersionId**](.md)|  | 

### Return type

[**BulkResult**](BulkResult.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_source**
> EntityLocation update_source(body, version_id, source_id)

Edit a source.

Modifies one or more attributes of the specified <b>source</b>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SourcesApi(swagger_client.ApiClient(configuration))
body = NULL # dict(str, AdditionalCustomAttribute) | 
version_id = swagger_client.VersionId() # VersionId | 
source_id = swagger_client.DoubleUuid() # DoubleUuid | 

try:
    # Edit a source.
    api_response = api_instance.update_source(body, version_id, source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesApi->update_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, AdditionalCustomAttribute)**](dict.md)|  | 
 **version_id** | [**VersionId**](.md)|  | 
 **source_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**EntityLocation**](EntityLocation.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

