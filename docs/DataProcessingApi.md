# swagger_client.DataProcessingApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dp**](DataProcessingApi.md#create_dp) | **POST** /dataProcessing/{versionId}/{parentId} | Create a data processing.
[**data_processing_bulk_creation**](DataProcessingApi.md#data_processing_bulk_creation) | **POST** /dataProcessing/bulktree/{versionId} | Bulk upsert data processing tree
[**delete_bulk_dp**](DataProcessingApi.md#delete_bulk_dp) | **DELETE** /dataProcessing/bulk/{versionId} | Bulk delete data processings
[**delete_dp**](DataProcessingApi.md#delete_dp) | **DELETE** /dataProcessing/{versionId}/{dataProcessingId} | Delete a data processing.
[**get_dp**](DataProcessingApi.md#get_dp) | **GET** /dataProcessing/{versionId}/{dataProcessingId} | Return a data processing.
[**get_dp_list**](DataProcessingApi.md#get_dp_list) | **GET** /dataProcessing | Return a list of data processing.
[**get_types**](DataProcessingApi.md#get_types) | **GET** /dataProcessing/types | List the data processing types.
[**update_dp**](DataProcessingApi.md#update_dp) | **PUT** /dataProcessing/{versionId}/{dataProcessingId} | Update a data processing.

# **create_dp**
> EntityLocation create_dp(body, parent_id, version_id)

Create a data processing.

Create a <b>data processing</b> in the specified <b>parent</b> with its inputs and outputs.<br> An input/output shall be a sourceId/structureId/fieldId. <br>Available data processing types can be found thanks to the <code>GET /types</code> endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DataProcessingApi(swagger_client.ApiClient(configuration))
body = NULL # dict(str, AdditionalCustomAttribute) | 
parent_id = swagger_client.DoubleUuid() # DoubleUuid | 
version_id = swagger_client.VersionId() # VersionId | 

try:
    # Create a data processing.
    api_response = api_instance.create_dp(body, parent_id, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataProcessingApi->create_dp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, AdditionalCustomAttribute)**](dict.md)|  | 
 **parent_id** | [**DoubleUuid**](.md)|  | 
 **version_id** | [**VersionId**](.md)|  | 

### Return type

[**EntityLocation**](EntityLocation.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_processing_bulk_creation**
> DataProcessingBulkResponse data_processing_bulk_creation(body, version_id)

Bulk upsert data processing tree

This route massively creates dataProcessings with their inputs/outputs and their dataProcessingItems.<br> This route uses the Upsert method. Existing entities are updated and non-existing ones are created.<br> Read our <a href=\"https://datagalaxy.freshdesk.com/en/support/solutions/articles/35000151776-mass-entity-creation-with-bulktree-routes\" target='_new'>article on bulktree</a> for more informations.<br><br> <b>Inputs</b> and <b>outputs</b> paths must be in the following format: <pre><code> {   entityPath: \"\\\\foo\\\\bar\",   typePath: \"\\\\NoSql\\\\Table\" }</code></pre>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DataProcessingApi(swagger_client.ApiClient(configuration))
body = [swagger_client.DataProcessingBulkCreation()] # list[DataProcessingBulkCreation] | 
version_id = swagger_client.VersionId() # VersionId | 

try:
    # Bulk upsert data processing tree
    api_response = api_instance.data_processing_bulk_creation(body, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataProcessingApi->data_processing_bulk_creation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[DataProcessingBulkCreation]**](DataProcessingBulkCreation.md)|  | 
 **version_id** | [**VersionId**](.md)|  | 

### Return type

[**DataProcessingBulkResponse**](DataProcessingBulkResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bulk_dp**
> BulkDeleteResponse delete_bulk_dp(body, version_id)

Bulk delete data processings

Deletes a list of **data processing** referenced by their id. <br><br> **Warning: deleting a data processing will delete its children objects in the process** <br> Deleted children objects will be included in the total count.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DataProcessingApi(swagger_client.ApiClient(configuration))
body = [swagger_client.DoubleUuid()] # list[DoubleUuid] | List of ids referencing data processings
version_id = swagger_client.VersionId() # VersionId | 

try:
    # Bulk delete data processings
    api_response = api_instance.delete_bulk_dp(body, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataProcessingApi->delete_bulk_dp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[DoubleUuid]**](DoubleUuid.md)| List of ids referencing data processings | 
 **version_id** | [**VersionId**](.md)|  | 

### Return type

[**BulkDeleteResponse**](BulkDeleteResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dp**
> delete_dp(version_id, data_processing_id)

Delete a data processing.

Deletes the specified <b>data processing</b>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DataProcessingApi(swagger_client.ApiClient(configuration))
version_id = swagger_client.VersionId() # VersionId | 
data_processing_id = swagger_client.DoubleUuid() # DoubleUuid | 

try:
    # Delete a data processing.
    api_instance.delete_dp(version_id, data_processing_id)
except ApiException as e:
    print("Exception when calling DataProcessingApi->delete_dp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **data_processing_id** | [**DoubleUuid**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dp**
> DataProcessingEntity get_dp(version_id, data_processing_id)

Return a data processing.

Return the details of the specified <b>data processing</b>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DataProcessingApi(swagger_client.ApiClient(configuration))
version_id = swagger_client.VersionId() # VersionId | 
data_processing_id = swagger_client.DoubleUuid() # DoubleUuid | 

try:
    # Return a data processing.
    api_response = api_instance.get_dp(version_id, data_processing_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataProcessingApi->get_dp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **data_processing_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**DataProcessingEntity**](DataProcessingEntity.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dp_list**
> PaginatedResponseEntitySummary_ get_dp_list(version_id, name=name, technical_name=technical_name, type=type, include_access_data=include_access_data, include_attributes=include_attributes, include_links=include_links, limit=limit, page=page, max_depth=max_depth)

Return a list of data processing.

Return the list of <b>data processing</b> contained in the specified <b>workspace</b>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DataProcessingApi(swagger_client.ApiClient(configuration))
version_id = swagger_client.VersionId() # VersionId | 
name = 'name_example' # str |  (optional)
technical_name = 'technical_name_example' # str |  (optional)
type = swagger_client.DataProcessingType() # DataProcessingType |  (optional)
include_access_data = swagger_client.IncludeAccessData() # IncludeAccessData |  (optional)
include_attributes = swagger_client.IncludeAttributes() # IncludeAttributes |  (optional)
include_links = swagger_client.IncludeLinks() # IncludeLinks |  (optional)
limit = 20 # float |  (optional) (default to 20)
page = 1 # float |  (optional) (default to 1)
max_depth = swagger_client.MaxDepth() # MaxDepth |  (optional)

try:
    # Return a list of data processing.
    api_response = api_instance.get_dp_list(version_id, name=name, technical_name=technical_name, type=type, include_access_data=include_access_data, include_attributes=include_attributes, include_links=include_links, limit=limit, page=page, max_depth=max_depth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataProcessingApi->get_dp_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **name** | **str**|  | [optional] 
 **technical_name** | **str**|  | [optional] 
 **type** | [**DataProcessingType**](.md)|  | [optional] 
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

List the data processing types.

Return the list of <b>source types</b> and their compatible <b>structure types</b>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DataProcessingApi(swagger_client.ApiClient(configuration))

try:
    # List the data processing types.
    api_response = api_instance.get_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataProcessingApi->get_types: %s\n" % e)
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

# **update_dp**
> EntityLocation update_dp(body, version_id, data_processing_id)

Update a data processing.

Modifies one or more attributes of the specified <b>data processing</b> and its inputs and outputs.<br> An input/output shall be a sourceId/structureId/fieldId.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DataProcessingApi(swagger_client.ApiClient(configuration))
body = NULL # dict(str, AdditionalCustomAttribute) | 
version_id = swagger_client.VersionId() # VersionId | 
data_processing_id = swagger_client.DoubleUuid() # DoubleUuid | 

try:
    # Update a data processing.
    api_response = api_instance.update_dp(body, version_id, data_processing_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataProcessingApi->update_dp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, AdditionalCustomAttribute)**](dict.md)|  | 
 **version_id** | [**VersionId**](.md)|  | 
 **data_processing_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**EntityLocation**](EntityLocation.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

