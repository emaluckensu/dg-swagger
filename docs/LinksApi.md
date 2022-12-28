# swagger_client.LinksApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bulk_links**](LinksApi.md#create_bulk_links) | **POST** /links/bulk/{versionId} | Bulk create links using entityIds
[**create_link**](LinksApi.md#create_link) | **POST** /links/{versionId}/{fromId} | Create an entity link.
[**create_links_bulktree**](LinksApi.md#create_links_bulktree) | **POST** /links/bulktree/{versionId} | Bulk create links using Paths
[**delete_link**](LinksApi.md#delete_link) | **DELETE** /links/{versionId}/{fromId}/{linkType}/{toId} | Delete a link.
[**get_links**](LinksApi.md#get_links) | **GET** /links/{versionId}/{fromId} | Return a list of links.

# **create_bulk_links**
> BulkLinksResult create_bulk_links(body, version_id)

Bulk create links using entityIds

This route creates multiple links between entities. <br> A link is defined by a <b>source entity</b> (<code>fromId</code>), a <b>target entity</b> (<code>toId</code>) and the <b>type of link</b> in between (<code>type</code>).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.LinksApi(swagger_client.ApiClient(configuration))
body = [swagger_client.BulkLinksPayload()] # list[BulkLinksPayload] | 
version_id = swagger_client.VersionId() # VersionId | 

try:
    # Bulk create links using entityIds
    api_response = api_instance.create_bulk_links(body, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->create_bulk_links: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[BulkLinksPayload]**](BulkLinksPayload.md)|  | 
 **version_id** | [**VersionId**](.md)|  | 

### Return type

[**BulkLinksResult**](BulkLinksResult.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_link**
> Links create_link(body, version_id, from_id)

Create an entity link.

Create a <b>link</b> between the specified <b>entity</b> and its <b>target</b>.<br> <br>Available link types can be found thanks to the <code>GET /types</code> endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.LinksApi(swagger_client.ApiClient(configuration))
body = swagger_client.LinksCreationRequest() # LinksCreationRequest | 
version_id = swagger_client.VersionId() # VersionId | 
from_id = swagger_client.DoubleUuid() # DoubleUuid | 

try:
    # Create an entity link.
    api_response = api_instance.create_link(body, version_id, from_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->create_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LinksCreationRequest**](LinksCreationRequest.md)|  | 
 **version_id** | [**VersionId**](.md)|  | 
 **from_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**Links**](Links.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_links_bulktree**
> BulkResult create_links_bulktree(body, version_id)

Bulk create links using Paths

This route creates multiple links between entities. <br> A link is defined with the following type of object:<br> <pre><code> {   fromPath: \"\\\\foo\\\\bar\",   fromType: \"\\\\NoSql\\\\Table\",   linkType: \"Implements\",   toPath: \"\\\\myLittleDimension\",   toType: \"\\\\Dimension\" }</code></pre>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.LinksApi(swagger_client.ApiClient(configuration))
body = [swagger_client.LinksBulktreePayload()] # list[LinksBulktreePayload] | 
version_id = swagger_client.VersionId() # VersionId | 

try:
    # Bulk create links using Paths
    api_response = api_instance.create_links_bulktree(body, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->create_links_bulktree: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[LinksBulktreePayload]**](LinksBulktreePayload.md)|  | 
 **version_id** | [**VersionId**](.md)|  | 

### Return type

[**BulkResult**](BulkResult.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_link**
> delete_link(version_id, from_id, link_type, to_id)

Delete a link.

Deletes the specified <b>link</b>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.LinksApi(swagger_client.ApiClient(configuration))
version_id = swagger_client.VersionId() # VersionId | 
from_id = swagger_client.DoubleUuid() # DoubleUuid | 
link_type = 'link_type_example' # str | 
to_id = swagger_client.DoubleUuid() # DoubleUuid | 

try:
    # Delete a link.
    api_instance.delete_link(version_id, from_id, link_type, to_id)
except ApiException as e:
    print("Exception when calling LinksApi->delete_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **from_id** | [**DoubleUuid**](.md)|  | 
 **link_type** | **str**|  | 
 **to_id** | [**DoubleUuid**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_links**
> list[Links] get_links(version_id, from_id)

Return a list of links.

Return a list of all <b>links</b> owned by the specified <b>entity</b>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.LinksApi(swagger_client.ApiClient(configuration))
version_id = swagger_client.VersionId() # VersionId | 
from_id = swagger_client.DoubleUuid() # DoubleUuid | 

try:
    # Return a list of links.
    api_response = api_instance.get_links(version_id, from_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->get_links: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **from_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**list[Links]**](Links.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

