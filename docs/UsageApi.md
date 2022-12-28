# swagger_client.UsageApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_usages**](UsageApi.md#create_usages) | **POST** /usages/{versionId}/{parentId} | Create a usage.
[**create_usages_bulk_tree**](UsageApi.md#create_usages_bulk_tree) | **POST** /usages/bulktree/{versionId} | Bulk upsert a usage tree
[**delete_bulk_usage**](UsageApi.md#delete_bulk_usage) | **DELETE** /usages/bulk/{versionId} | Bulk delete usages
[**delete_usage**](UsageApi.md#delete_usage) | **DELETE** /usages/{versionId}/{usageId} | Delete a usage.
[**get_types**](UsageApi.md#get_types) | **GET** /usages/types | List the usage types.
[**get_usage**](UsageApi.md#get_usage) | **GET** /usages/{versionId}/{usageId} | Return a usage.
[**get_usages_list**](UsageApi.md#get_usages_list) | **GET** /usages | Return a list of usages.
[**update_usage**](UsageApi.md#update_usage) | **PUT** /usages/{versionId}/{usageId} | Edit a usage.

# **create_usages**
> EntityLocation create_usages(body, version_id, parent_id)

Create a usage.

Create a <b>usage</b> in the specified <b>parent</b> (workspace or compatible usage). <br>Available usage types can be found thanks to the <code>GET /types</code> endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsageApi(swagger_client.ApiClient(configuration))
body = NULL # dict(str, AdditionalCustomAttribute) | 
version_id = swagger_client.VersionId() # VersionId | 
parent_id = swagger_client.DoubleUuid() # DoubleUuid | 

try:
    # Create a usage.
    api_response = api_instance.create_usages(body, version_id, parent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->create_usages: %s\n" % e)
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

# **create_usages_bulk_tree**
> BulkResult create_usages_bulk_tree(body, version_id)

Bulk upsert a usage tree

This route creates or update multiple usages and all their children up to a total of 250 000 entities.<br> This route uses the Upsert method. Existing entities are updated and non-existing ones are created.<br> Read our <a href=\"https://datagalaxy.freshdesk.com/en/support/solutions/articles/35000151776-mass-entity-creation-with-bulktree-routes\" target='_new'>article on bulktree</a> for more informations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsageApi(swagger_client.ApiClient(configuration))
body = [swagger_client.UsageBulktreeCreation()] # list[UsageBulktreeCreation] | 
version_id = swagger_client.VersionId() # VersionId | 

try:
    # Bulk upsert a usage tree
    api_response = api_instance.create_usages_bulk_tree(body, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->create_usages_bulk_tree: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[UsageBulktreeCreation]**](UsageBulktreeCreation.md)|  | 
 **version_id** | [**VersionId**](.md)|  | 

### Return type

[**BulkResult**](BulkResult.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bulk_usage**
> BulkDeleteResponse delete_bulk_usage(body, version_id)

Bulk delete usages

Deletes a list of **usages** referenced by their id. <br><br> **Warning: deleting a usage will delete its children objects in the process** <br> Deleted children objects will be included in the total count.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsageApi(swagger_client.ApiClient(configuration))
body = [swagger_client.DoubleUuid()] # list[DoubleUuid] | List of ids referencing usages
version_id = swagger_client.VersionId() # VersionId | 

try:
    # Bulk delete usages
    api_response = api_instance.delete_bulk_usage(body, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->delete_bulk_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[DoubleUuid]**](DoubleUuid.md)| List of ids referencing usages | 
 **version_id** | [**VersionId**](.md)|  | 

### Return type

[**BulkDeleteResponse**](BulkDeleteResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_usage**
> delete_usage(version_id, usage_id)

Delete a usage.

Deletes the specified <b>usage</b>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsageApi(swagger_client.ApiClient(configuration))
version_id = swagger_client.VersionId() # VersionId | 
usage_id = swagger_client.Uuid() # Uuid | 

try:
    # Delete a usage.
    api_instance.delete_usage(version_id, usage_id)
except ApiException as e:
    print("Exception when calling UsageApi->delete_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **usage_id** | [**Uuid**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_types**
> list[CompatibilityDefinition] get_types()

List the usage types.

Return the list of <b>Usage types</b> and their compatible <b>children types</b>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsageApi(swagger_client.ApiClient(configuration))

try:
    # List the usage types.
    api_response = api_instance.get_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->get_types: %s\n" % e)
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

# **get_usage**
> Entity get_usage(version_id, usage_id)

Return a usage.

Return the <b>details</b> of the specified <b>usage</b>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsageApi(swagger_client.ApiClient(configuration))
version_id = swagger_client.VersionId() # VersionId | 
usage_id = swagger_client.DoubleUuid() # DoubleUuid | 

try:
    # Return a usage.
    api_response = api_instance.get_usage(version_id, usage_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->get_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **usage_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**Entity**](Entity.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usages_list**
> PaginatedResponseEntitySummary_ get_usages_list(version_id, parent_id=parent_id, name=name, technical_name=technical_name, include_access_data=include_access_data, include_attributes=include_attributes, include_links=include_links, type=type, limit=limit, page=page, max_depth=max_depth)

Return a list of usages.

Return a list of all <b>usage</b> contained in the specified <b>parent</b>. A <b>parent</b> can be a <b>workspace</b> or another <b>usage</b>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsageApi(swagger_client.ApiClient(configuration))
version_id = swagger_client.VersionId() # VersionId | 
parent_id = swagger_client.DoubleUuid() # DoubleUuid |  (optional)
name = 'name_example' # str |  (optional)
technical_name = 'technical_name_example' # str |  (optional)
include_access_data = swagger_client.IncludeAccessData() # IncludeAccessData |  (optional)
include_attributes = swagger_client.IncludeAttributes() # IncludeAttributes |  (optional)
include_links = swagger_client.IncludeLinks() # IncludeLinks |  (optional)
type = swagger_client.UsageType() # UsageType |  (optional)
limit = 20 # float |  (optional) (default to 20)
page = 1 # float |  (optional) (default to 1)
max_depth = swagger_client.MaxDepth() # MaxDepth |  (optional)

try:
    # Return a list of usages.
    api_response = api_instance.get_usages_list(version_id, parent_id=parent_id, name=name, technical_name=technical_name, include_access_data=include_access_data, include_attributes=include_attributes, include_links=include_links, type=type, limit=limit, page=page, max_depth=max_depth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->get_usages_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **parent_id** | [**DoubleUuid**](.md)|  | [optional] 
 **name** | **str**|  | [optional] 
 **technical_name** | **str**|  | [optional] 
 **include_access_data** | [**IncludeAccessData**](.md)|  | [optional] 
 **include_attributes** | [**IncludeAttributes**](.md)|  | [optional] 
 **include_links** | [**IncludeLinks**](.md)|  | [optional] 
 **type** | [**UsageType**](.md)|  | [optional] 
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

# **update_usage**
> EntityLocation update_usage(body, version_id, usage_id)

Edit a usage.

Modifies one or more attributes of the specified <b>usage</b>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsageApi(swagger_client.ApiClient(configuration))
body = NULL # dict(str, AdditionalCustomAttribute) | 
version_id = swagger_client.VersionId() # VersionId | 
usage_id = swagger_client.DoubleUuid() # DoubleUuid | 

try:
    # Edit a usage.
    api_response = api_instance.update_usage(body, version_id, usage_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->update_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, AdditionalCustomAttribute)**](dict.md)|  | 
 **version_id** | [**VersionId**](.md)|  | 
 **usage_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**EntityLocation**](EntityLocation.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

