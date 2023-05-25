# kensu_datagalaxy_client.GlossaryApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_local_synonym**](GlossaryApi.md#create_local_synonym) | **POST** /properties/localSynonyms/{versionId}/{propertyId} | Create a local synonym
[**create_properties_bulk_tree**](GlossaryApi.md#create_properties_bulk_tree) | **POST** /properties/bulktree/{versionId} | Bulk upsert a property tree
[**create_property**](GlossaryApi.md#create_property) | **POST** /properties/{versionId}/{parentId} | Create a property.
[**delete_bulk_property**](GlossaryApi.md#delete_bulk_property) | **DELETE** /properties/bulk/{versionId} | Bulk delete properties
[**delete_local_synonym**](GlossaryApi.md#delete_local_synonym) | **DELETE** /properties/localSynonyms/{versionId}/{localSynonymId} | Delete a local synonym
[**delete_property**](GlossaryApi.md#delete_property) | **DELETE** /properties/{versionId}/{propertyId} | Delete a property.
[**get_local_synonyms**](GlossaryApi.md#get_local_synonyms) | **GET** /properties/localSynonyms/{versionId}/{propertyId} | Get local synonyms
[**get_properties_list**](GlossaryApi.md#get_properties_list) | **GET** /properties | Return a list of properties.
[**get_property**](GlossaryApi.md#get_property) | **GET** /properties/{versionId}/{propertyId} | Return a property.
[**get_types**](GlossaryApi.md#get_types) | **GET** /properties/types | List the property types.
[**udpate_local_synonym**](GlossaryApi.md#udpate_local_synonym) | **PUT** /properties/localSynonyms/{versionId}/{localSynonymId} | Update a local synonym
[**update_property**](GlossaryApi.md#update_property) | **PUT** /properties/{versionId}/{propertyId} | Edit a property.

# **create_local_synonym**
> LocalSynonym create_local_synonym(body, version_id, property_id)

Create a local synonym

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.GlossaryApi(kensu_datagalaxy_client.ApiClient(configuration))
body = kensu_datagalaxy_client.LocalSynonymCreationBody() # LocalSynonymCreationBody | Contains the name and description of your local synonym
version_id = kensu_datagalaxy_client.VersionId() # VersionId | 
property_id = kensu_datagalaxy_client.DoubleUuid() # DoubleUuid | 

try:
    # Create a local synonym
    api_response = api_instance.create_local_synonym(body, version_id, property_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GlossaryApi->create_local_synonym: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LocalSynonymCreationBody**](LocalSynonymCreationBody.md)| Contains the name and description of your local synonym | 
 **version_id** | [**VersionId**](.md)|  | 
 **property_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**LocalSynonym**](LocalSynonym.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_properties_bulk_tree**
> BulkResult create_properties_bulk_tree(body, version_id)

Bulk upsert a property tree

This route creates or update multiple properties and all their children up to a total of 250 000 entities.<br> This route uses the Upsert method. Existing entities are updated and non-existing ones are created.<br> Read our <a href=\"https://datagalaxy.freshdesk.com/en/support/solutions/articles/35000151776-mass-entity-creation-with-bulktree-routes\" target='_new'>article on bulktree</a> for more informations.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.GlossaryApi(kensu_datagalaxy_client.ApiClient(configuration))
body = [kensu_datagalaxy_client.PropertiesBulkTreeCreationRequest()] # list[PropertiesBulkTreeCreationRequest] | 
version_id = kensu_datagalaxy_client.VersionId() # VersionId | 

try:
    # Bulk upsert a property tree
    api_response = api_instance.create_properties_bulk_tree(body, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GlossaryApi->create_properties_bulk_tree: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[PropertiesBulkTreeCreationRequest]**](PropertiesBulkTreeCreationRequest.md)|  | 
 **version_id** | [**VersionId**](.md)|  | 

### Return type

[**BulkResult**](BulkResult.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_property**
> EntityLocation create_property(body, version_id, parent_id)

Create a property.

Create a <b>property</b> in the specified <b>parent</b> (workspace or compatible property). <br>Available property types can be found thanks to the <code>GET /types</code> endpoint.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.GlossaryApi(kensu_datagalaxy_client.ApiClient(configuration))
body = NULL # dict(str, AdditionalCustomAttribute) | 
version_id = kensu_datagalaxy_client.VersionId() # VersionId | 
parent_id = kensu_datagalaxy_client.DoubleUuid() # DoubleUuid | 

try:
    # Create a property.
    api_response = api_instance.create_property(body, version_id, parent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GlossaryApi->create_property: %s\n" % e)
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

# **delete_bulk_property**
> BulkDeleteResponse delete_bulk_property(body, version_id)

Bulk delete properties

Deletes a list of **properties** referenced by their id. <br><br> **Warning: deleting a property will delete its children objects in the process** <br> Deleted children objects will be included in the total count.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.GlossaryApi(kensu_datagalaxy_client.ApiClient(configuration))
body = [kensu_datagalaxy_client.DoubleUuid()] # list[DoubleUuid] | List of ids referencing properties
version_id = kensu_datagalaxy_client.VersionId() # VersionId | 

try:
    # Bulk delete properties
    api_response = api_instance.delete_bulk_property(body, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GlossaryApi->delete_bulk_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[DoubleUuid]**](DoubleUuid.md)| List of ids referencing properties | 
 **version_id** | [**VersionId**](.md)|  | 

### Return type

[**BulkDeleteResponse**](BulkDeleteResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_local_synonym**
> LocalSynonym delete_local_synonym(version_id, local_synonym_id)

Delete a local synonym

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.GlossaryApi(kensu_datagalaxy_client.ApiClient(configuration))
version_id = kensu_datagalaxy_client.VersionId() # VersionId | 
local_synonym_id = kensu_datagalaxy_client.DoubleUuid() # DoubleUuid | 

try:
    # Delete a local synonym
    api_response = api_instance.delete_local_synonym(version_id, local_synonym_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GlossaryApi->delete_local_synonym: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **local_synonym_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**LocalSynonym**](LocalSynonym.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_property**
> delete_property(version_id, property_id)

Delete a property.

Deletes the specified <b>property</b>.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.GlossaryApi(kensu_datagalaxy_client.ApiClient(configuration))
version_id = kensu_datagalaxy_client.VersionId() # VersionId | 
property_id = kensu_datagalaxy_client.DoubleUuid() # DoubleUuid | 

try:
    # Delete a property.
    api_instance.delete_property(version_id, property_id)
except ApiException as e:
    print("Exception when calling GlossaryApi->delete_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **property_id** | [**DoubleUuid**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_local_synonyms**
> list[LocalSynonym] get_local_synonyms(version_id, property_id)

Get local synonyms

Fetches the list of synonyms on a property.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.GlossaryApi(kensu_datagalaxy_client.ApiClient(configuration))
version_id = kensu_datagalaxy_client.VersionId() # VersionId | 
property_id = kensu_datagalaxy_client.DoubleUuid() # DoubleUuid | 

try:
    # Get local synonyms
    api_response = api_instance.get_local_synonyms(version_id, property_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GlossaryApi->get_local_synonyms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **property_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**list[LocalSynonym]**](LocalSynonym.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_properties_list**
> PaginatedResponseEntitySummary_ get_properties_list(version_id, parent_id=parent_id, name=name, type=type, include_access_data=include_access_data, include_attributes=include_attributes, include_links=include_links, limit=limit, page=page, max_depth=max_depth)

Return a list of properties.

Return a list of all <b>properties</b> contained in the specified <b>workspace</b>.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.GlossaryApi(kensu_datagalaxy_client.ApiClient(configuration))
version_id = kensu_datagalaxy_client.VersionId() # VersionId | 
parent_id = kensu_datagalaxy_client.Uuid() # Uuid |  (optional)
name = 'name_example' # str |  (optional)
type = kensu_datagalaxy_client.PropertyType() # PropertyType |  (optional)
include_access_data = kensu_datagalaxy_client.IncludeAccessData() # IncludeAccessData |  (optional)
include_attributes = kensu_datagalaxy_client.IncludeAttributes() # IncludeAttributes |  (optional)
include_links = kensu_datagalaxy_client.IncludeLinks() # IncludeLinks |  (optional)
limit = 20 # float |  (optional) (default to 20)
page = 1 # float |  (optional) (default to 1)
max_depth = kensu_datagalaxy_client.MaxDepth() # MaxDepth |  (optional)

try:
    # Return a list of properties.
    api_response = api_instance.get_properties_list(version_id, parent_id=parent_id, name=name, type=type, include_access_data=include_access_data, include_attributes=include_attributes, include_links=include_links, limit=limit, page=page, max_depth=max_depth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GlossaryApi->get_properties_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **parent_id** | [**Uuid**](.md)|  | [optional] 
 **name** | **str**|  | [optional] 
 **type** | [**PropertyType**](.md)|  | [optional] 
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

# **get_property**
> Entity get_property(version_id, property_id)

Return a property.

Return the <b>details</b> of the specified <b>property</b>.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.GlossaryApi(kensu_datagalaxy_client.ApiClient(configuration))
version_id = kensu_datagalaxy_client.VersionId() # VersionId | 
property_id = kensu_datagalaxy_client.Uuid() # Uuid | 

try:
    # Return a property.
    api_response = api_instance.get_property(version_id, property_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GlossaryApi->get_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **property_id** | [**Uuid**](.md)|  | 

### Return type

[**Entity**](Entity.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_types**
> list[CompatibilityDefinition] get_types()

List the property types.

Return the list of <b>properties types</b> and their compatible <b>entity types</b>.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.GlossaryApi(kensu_datagalaxy_client.ApiClient(configuration))

try:
    # List the property types.
    api_response = api_instance.get_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GlossaryApi->get_types: %s\n" % e)
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

# **udpate_local_synonym**
> LocalSynonym udpate_local_synonym(body, version_id, local_synonym_id)

Update a local synonym

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.GlossaryApi(kensu_datagalaxy_client.ApiClient(configuration))
body = kensu_datagalaxy_client.LocalSynonymUpdateBody() # LocalSynonymUpdateBody | 
version_id = kensu_datagalaxy_client.VersionId() # VersionId | 
local_synonym_id = kensu_datagalaxy_client.DoubleUuid() # DoubleUuid | 

try:
    # Update a local synonym
    api_response = api_instance.udpate_local_synonym(body, version_id, local_synonym_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GlossaryApi->udpate_local_synonym: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LocalSynonymUpdateBody**](LocalSynonymUpdateBody.md)|  | 
 **version_id** | [**VersionId**](.md)|  | 
 **local_synonym_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**LocalSynonym**](LocalSynonym.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_property**
> EntityLocation update_property(body, version_id, property_id)

Edit a property.

Modifies one or more attributes of the specified <b>property</b>.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.GlossaryApi(kensu_datagalaxy_client.ApiClient(configuration))
body = NULL # dict(str, AdditionalCustomAttribute) | 
version_id = kensu_datagalaxy_client.VersionId() # VersionId | 
property_id = kensu_datagalaxy_client.DoubleUuid() # DoubleUuid | 

try:
    # Edit a property.
    api_response = api_instance.update_property(body, version_id, property_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GlossaryApi->update_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, AdditionalCustomAttribute)**](dict.md)|  | 
 **version_id** | [**VersionId**](.md)|  | 
 **property_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**EntityLocation**](EntityLocation.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

