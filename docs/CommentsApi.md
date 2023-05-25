# kensu_datagalaxy_client.CommentsApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_comment**](CommentsApi.md#delete_comment) | **DELETE** /comments/{versionId}/{entityId}/{commentId} | Delete a comment
[**get_comment**](CommentsApi.md#get_comment) | **GET** /comments/{versionId}/{entityId} | Return a list of comments.
[**post_comment**](CommentsApi.md#post_comment) | **POST** /comments/{versionId}/{entityId} | Create a comment.
[**put_comment**](CommentsApi.md#put_comment) | **PUT** /comments/{versionId}/{entityId}/{commentId} | Update a comment

# **delete_comment**
> delete_comment(version_id, entity_id, comment_id)

Delete a comment

Delete a <b>comment</b> associated with the specified <b>entity</b>.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.CommentsApi(kensu_datagalaxy_client.ApiClient(configuration))
version_id = kensu_datagalaxy_client.VersionId() # VersionId | 
entity_id = kensu_datagalaxy_client.DoubleUuid() # DoubleUuid | 
comment_id = kensu_datagalaxy_client.DoubleUuid() # DoubleUuid | 

try:
    # Delete a comment
    api_instance.delete_comment(version_id, entity_id, comment_id)
except ApiException as e:
    print("Exception when calling CommentsApi->delete_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **entity_id** | [**DoubleUuid**](.md)|  | 
 **comment_id** | [**DoubleUuid**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comment**
> list[SocialComment] get_comment(version_id, entity_id)

Return a list of comments.

Return a list of all <b>comments details</b> in the specified <b>entity</b>.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.CommentsApi(kensu_datagalaxy_client.ApiClient(configuration))
version_id = kensu_datagalaxy_client.VersionId() # VersionId | 
entity_id = kensu_datagalaxy_client.DoubleUuid() # DoubleUuid | 

try:
    # Return a list of comments.
    api_response = api_instance.get_comment(version_id, entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentsApi->get_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **entity_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**list[SocialComment]**](SocialComment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_comment**
> SocialComment post_comment(body, version_id, entity_id)

Create a comment.

Create a <b>comment</b> in the specified <b>entity</b>.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.CommentsApi(kensu_datagalaxy_client.ApiClient(configuration))
body = kensu_datagalaxy_client.CommentPayload() # CommentPayload | 
version_id = kensu_datagalaxy_client.VersionId() # VersionId | 
entity_id = kensu_datagalaxy_client.DoubleUuid() # DoubleUuid | 

try:
    # Create a comment.
    api_response = api_instance.post_comment(body, version_id, entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentsApi->post_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CommentPayload**](CommentPayload.md)|  | 
 **version_id** | [**VersionId**](.md)|  | 
 **entity_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**SocialComment**](SocialComment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_comment**
> SocialComment put_comment(body, version_id, entity_id, comment_id)

Update a comment

Update a <b>comment</b> in the specified <b>entity</b>.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.CommentsApi(kensu_datagalaxy_client.ApiClient(configuration))
body = kensu_datagalaxy_client.CommentPayload() # CommentPayload | 
version_id = kensu_datagalaxy_client.VersionId() # VersionId | 
entity_id = kensu_datagalaxy_client.DoubleUuid() # DoubleUuid | 
comment_id = kensu_datagalaxy_client.DoubleUuid() # DoubleUuid | 

try:
    # Update a comment
    api_response = api_instance.put_comment(body, version_id, entity_id, comment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentsApi->put_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CommentPayload**](CommentPayload.md)|  | 
 **version_id** | [**VersionId**](.md)|  | 
 **entity_id** | [**DoubleUuid**](.md)|  | 
 **comment_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**SocialComment**](SocialComment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

