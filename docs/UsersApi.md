# kensu_datagalaxy_client.UsersApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UsersApi.md#create_user) | **POST** /users | Create a user.
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /users/{userId} | Delete a user
[**get_candidates**](UsersApi.md#get_candidates) | **GET** /users/{versionId} | Return a list of users eligible to be stewards or owners.
[**get_client_users**](UsersApi.md#get_client_users) | **GET** /users | Return a list of users.
[**get_users_authorizations**](UsersApi.md#get_users_authorizations) | **GET** /users/authorizations | Return a list of users with their authorizations.
[**get_users_roles**](UsersApi.md#get_users_roles) | **GET** /users/roles | Fetch governance users
[**update_user**](UsersApi.md#update_user) | **PUT** /users/{userId} | Update the properties of a user.
[**update_users_authorizations**](UsersApi.md#update_users_authorizations) | **PUT** /users/authorizations | Update the authorizations of a list of users

# **create_user**
> User create_user(body)

Create a user.

Create a user and add it to your account. <br>A user can be created with no license. You can add it later using <code>PUT /user/{userId}</code>. <br>Available licenses can be found thanks to the <code>GET /licenses</code> endpoint.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.UsersApi(kensu_datagalaxy_client.ApiClient(configuration))
body = kensu_datagalaxy_client.UserCreationBody() # UserCreationBody | 

try:
    # Create a user.
    api_response = api_instance.create_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserCreationBody**](UserCreationBody.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = kensu_datagalaxy_client.UsersApi(kensu_datagalaxy_client.ApiClient(configuration))
user_id = kensu_datagalaxy_client.Uuid() # Uuid | 

try:
    # Delete a user
    api_instance.delete_user(user_id)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user: %s\n" % e)
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

# **get_candidates**
> PaginatedResponseUser_ get_candidates(role, version_id, user_id=user_id, email=email, limit=limit, page=page)

Return a list of users eligible to be stewards or owners.

Return a list of <b>users</b> eligible to be <b>stewards</b> or <b>owners</b> in the specified <b>version</b> of your workspace.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.UsersApi(kensu_datagalaxy_client.ApiClient(configuration))
role = kensu_datagalaxy_client.Roles() # Roles | 
version_id = kensu_datagalaxy_client.VersionId() # VersionId | 
user_id = kensu_datagalaxy_client.Uuid() # Uuid |  (optional)
email = kensu_datagalaxy_client.Email() # Email |  (optional)
limit = 20 # float |  (optional) (default to 20)
page = 1 # float |  (optional) (default to 1)

try:
    # Return a list of users eligible to be stewards or owners.
    api_response = api_instance.get_candidates(role, version_id, user_id=user_id, email=email, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_candidates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | [**Roles**](.md)|  | 
 **version_id** | [**VersionId**](.md)|  | 
 **user_id** | [**Uuid**](.md)|  | [optional] 
 **email** | [**Email**](.md)|  | [optional] 
 **limit** | **float**|  | [optional] [default to 20]
 **page** | **float**|  | [optional] [default to 1]

### Return type

[**PaginatedResponseUser_**](PaginatedResponseUser_.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_users**
> PaginatedResponseUser_ get_client_users(user_id=user_id, email=email, limit=limit, page=page)

Return a list of users.

Return a list of all the <b>users</b> owned by your account.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.UsersApi(kensu_datagalaxy_client.ApiClient(configuration))
user_id = kensu_datagalaxy_client.Uuid() # Uuid |  (optional)
email = kensu_datagalaxy_client.Email() # Email |  (optional)
limit = 20 # float |  (optional) (default to 20)
page = 1 # float |  (optional) (default to 1)

try:
    # Return a list of users.
    api_response = api_instance.get_client_users(user_id=user_id, email=email, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_client_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**Uuid**](.md)|  | [optional] 
 **email** | [**Email**](.md)|  | [optional] 
 **limit** | **float**|  | [optional] [default to 20]
 **page** | **float**|  | [optional] [default to 1]

### Return type

[**PaginatedResponseUser_**](PaginatedResponseUser_.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_authorizations**
> PaginatedResponseUserAuthorizations_ get_users_authorizations(version_id, user_id=user_id, email=email, limit=limit, page=page)

Return a list of users with their authorizations.

Return the list of all users owned by your account with the authorizations they have in your workspace and its modules. <br><br>  <b><i>Note:</b><br> Your integrationToken must have an admin access on the target workspace.</i><br><br>  <b><i>Deprecation:</b><br> In order to avoid a beaking change with previous versions, requesting this route <b>without</b> pagination parameters will result in a <b>non-paginated</b> response payload.<br> Pagination is standard as of version <b>2.5.0</b>.</i><br>

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.UsersApi(kensu_datagalaxy_client.ApiClient(configuration))
version_id = kensu_datagalaxy_client.VersionId() # VersionId | 
user_id = kensu_datagalaxy_client.Uuid() # Uuid |  (optional)
email = kensu_datagalaxy_client.Email() # Email |  (optional)
limit = 20 # float |  (optional) (default to 20)
page = 1 # float |  (optional) (default to 1)

try:
    # Return a list of users with their authorizations.
    api_response = api_instance.get_users_authorizations(version_id, user_id=user_id, email=email, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users_authorizations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **user_id** | [**Uuid**](.md)|  | [optional] 
 **email** | [**Email**](.md)|  | [optional] 
 **limit** | **float**|  | [optional] [default to 20]
 **page** | **float**|  | [optional] [default to 1]

### Return type

[**PaginatedResponseUserAuthorizations_**](PaginatedResponseUserAuthorizations_.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_roles**
> GovernanceUsers get_users_roles(role=role, version_id=version_id, user_id=user_id, email=email)

Fetch governance users

Return list of users assigned to each of the 6 governance roles: **Owner, Steward, CDO, DPO, CISO, Expert**.<br><br>  **Query string arrays are supported** and will be logically joined with OR operator

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.UsersApi(kensu_datagalaxy_client.ApiClient(configuration))
role = [kensu_datagalaxy_client.Roles()] # list[Roles] |  (optional)
version_id = kensu_datagalaxy_client.Uuid() # Uuid |  (optional)
user_id = [kensu_datagalaxy_client.Uuid()] # list[Uuid] |  (optional)
email = [kensu_datagalaxy_client.Email()] # list[Email] |  (optional)

try:
    # Fetch governance users
    api_response = api_instance.get_users_roles(role=role, version_id=version_id, user_id=user_id, email=email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | [**list[Roles]**](Roles.md)|  | [optional] 
 **version_id** | [**Uuid**](.md)|  | [optional] 
 **user_id** | [**list[Uuid]**](Uuid.md)|  | [optional] 
 **email** | [**list[Email]**](Email.md)|  | [optional] 

### Return type

[**GovernanceUsers**](GovernanceUsers.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> User update_user(body, user_id)

Update the properties of a user.

Update the properties of a user. Set <code>licenseId</code> to <i>null</i> to remove its license.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.UsersApi(kensu_datagalaxy_client.ApiClient(configuration))
body = kensu_datagalaxy_client.UserUpdateBody() # UserUpdateBody | 
user_id = kensu_datagalaxy_client.Uuid() # Uuid | 

try:
    # Update the properties of a user.
    api_response = api_instance.update_user(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserUpdateBody**](UserUpdateBody.md)|  | 
 **user_id** | [**Uuid**](.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_users_authorizations**
> list[UserAuthorizations] update_users_authorizations(body)

Update the authorizations of a list of users

Update the authorizations of a list of users on a workspace and its modules.<br> An authorization update to the <b>glossary</b>, <b>dataProcessings</b> or <b>uses</b> is applied at the module level, i.e., to all the entities they contain.<br> An authorization update to the <b>catalog</b> is applied to the specified <code>sourceId</code>.<br><br> Check the Request body Schema bellow for more informations on the expected structure and available values.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.UsersApi(kensu_datagalaxy_client.ApiClient(configuration))
body = kensu_datagalaxy_client.UsersUpdateAuthorizationsBody() # UsersUpdateAuthorizationsBody | 

try:
    # Update the authorizations of a list of users
    api_response = api_instance.update_users_authorizations(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_users_authorizations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersUpdateAuthorizationsBody**](UsersUpdateAuthorizationsBody.md)|  | 

### Return type

[**list[UserAuthorizations]**](UserAuthorizations.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

