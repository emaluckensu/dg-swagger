# kensu_datagalaxy_client.SCIMUsersApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user**](SCIMUsersApi.md#delete_user) | **DELETE** /scim/Users/{userId} | Delete a user
[**get_user**](SCIMUsersApi.md#get_user) | **GET** /scim/Users/{userId} | Return a user.
[**get_users**](SCIMUsersApi.md#get_users) | **GET** /scim/Users | Return a list of users.
[**patch_user**](SCIMUsersApi.md#patch_user) | **PATCH** /scim/Users/{userId} | Patch a user.
[**post_user**](SCIMUsersApi.md#post_user) | **POST** /scim/Users | Create a user.

# **delete_user**
> delete_user(user_id)

Delete a user

Permanently deletes a user.<br><br> When deleting a user that had an owner or steward role on an object, the workspace's default owner / steward will automatically be assigned to the object.<br> Users that are default owners or stewards at workspace level cannot be deleted, an error will be thrown if you try to.<br>

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.SCIMUsersApi(kensu_datagalaxy_client.ApiClient(configuration))
user_id = kensu_datagalaxy_client.Uuid() # Uuid | 

try:
    # Delete a user
    api_instance.delete_user(user_id)
except ApiException as e:
    print("Exception when calling SCIMUsersApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**Uuid**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> SCIMUser get_user(user_id, filter=filter, excluded_attributes=excluded_attributes, attributes=attributes, sort_by=sort_by, sort_order=sort_order, start_index=start_index, count=count)

Return a user.

Return the corresponding <b>users</b> owned by your account in SCIM format as detailed in <a href=\"https://datatracker.ietf.org/doc/html/rfc7643|RFC-7643\">RFC 7643</a> and <a href=\"https://datatracker.ietf.org/doc/html/rfc7644|RFC-7644\">RFC 7644</a>.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.SCIMUsersApi(kensu_datagalaxy_client.ApiClient(configuration))
user_id = kensu_datagalaxy_client.Uuid() # Uuid | 
filter = 'filter_example' # str |  (optional)
excluded_attributes = 'excluded_attributes_example' # str |  (optional)
attributes = 'attributes_example' # str |  (optional)
sort_by = 'sort_by_example' # str |  (optional)
sort_order = 'sort_order_example' # str |  (optional)
start_index = 1.2 # float |  (optional)
count = 1.2 # float |  (optional)

try:
    # Return a user.
    api_response = api_instance.get_user(user_id, filter=filter, excluded_attributes=excluded_attributes, attributes=attributes, sort_by=sort_by, sort_order=sort_order, start_index=start_index, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SCIMUsersApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**Uuid**](.md)|  | 
 **filter** | **str**|  | [optional] 
 **excluded_attributes** | **str**|  | [optional] 
 **attributes** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_order** | **str**|  | [optional] 
 **start_index** | **float**|  | [optional] 
 **count** | **float**|  | [optional] 

### Return type

[**SCIMUser**](SCIMUser.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> list[SCIMListResponseUser_] get_users(filter=filter, excluded_attributes=excluded_attributes, attributes=attributes, sort_by=sort_by, sort_order=sort_order, start_index=start_index, count=count)

Return a list of users.

Return a list of all the <b>users</b> owned by your account in SCIM format as detailed in <a href=\"https://datatracker.ietf.org/doc/html/rfc7643|RFC-7643\">RFC 7643</a> and <a href=\"https://datatracker.ietf.org/doc/html/rfc7644|RFC-7644\">RFC 7644</a>.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.SCIMUsersApi(kensu_datagalaxy_client.ApiClient(configuration))
filter = 'filter_example' # str |  (optional)
excluded_attributes = 'excluded_attributes_example' # str |  (optional)
attributes = 'attributes_example' # str |  (optional)
sort_by = 'sort_by_example' # str |  (optional)
sort_order = 'sort_order_example' # str |  (optional)
start_index = 1.2 # float |  (optional)
count = 1.2 # float |  (optional)

try:
    # Return a list of users.
    api_response = api_instance.get_users(filter=filter, excluded_attributes=excluded_attributes, attributes=attributes, sort_by=sort_by, sort_order=sort_order, start_index=start_index, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SCIMUsersApi->get_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**|  | [optional] 
 **excluded_attributes** | **str**|  | [optional] 
 **attributes** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_order** | **str**|  | [optional] 
 **start_index** | **float**|  | [optional] 
 **count** | **float**|  | [optional] 

### Return type

[**list[SCIMListResponseUser_]**](SCIMListResponseUser_.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_user**
> SCIMUser patch_user(body, user_id)

Patch a user.

Patch a user.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.SCIMUsersApi(kensu_datagalaxy_client.ApiClient(configuration))
body = kensu_datagalaxy_client.SCIMPatchOperationPayload() # SCIMPatchOperationPayload | 
user_id = kensu_datagalaxy_client.Uuid() # Uuid | 

try:
    # Patch a user.
    api_response = api_instance.patch_user(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SCIMUsersApi->patch_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SCIMPatchOperationPayload**](SCIMPatchOperationPayload.md)|  | 
 **user_id** | [**Uuid**](.md)|  | 

### Return type

[**SCIMUser**](SCIMUser.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_user**
> SCIMUser post_user(body)

Create a user.

Create a user and add it to your account.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.SCIMUsersApi(kensu_datagalaxy_client.ApiClient(configuration))
body = kensu_datagalaxy_client.SCIMUser() # SCIMUser | 

try:
    # Create a user.
    api_response = api_instance.post_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SCIMUsersApi->post_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SCIMUser**](SCIMUser.md)|  | 

### Return type

[**SCIMUser**](SCIMUser.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

