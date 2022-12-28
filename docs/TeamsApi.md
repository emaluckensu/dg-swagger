# swagger_client.TeamsApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_delete_teams**](TeamsApi.md#bulk_delete_teams) | **DELETE** /teams/bulk | Delete multiple teams
[**create_team**](TeamsApi.md#create_team) | **POST** /teams | Create team
[**delete_team**](TeamsApi.md#delete_team) | **DELETE** /teams/{id} | Delete a team
[**list_teams**](TeamsApi.md#list_teams) | **GET** /teams | List teams
[**update_team**](TeamsApi.md#update_team) | **PUT** /teams/{id} | Update team

# **bulk_delete_teams**
> bulk_delete_teams(body)

Delete multiple teams

This endpoint deletes a list of teams, specified by their <code>id</code> given in the request payload.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TeamsApi(swagger_client.ApiClient(configuration))
body = [swagger_client.TeamId()] # list[TeamId] | 

try:
    # Delete multiple teams
    api_instance.bulk_delete_teams(body)
except ApiException as e:
    print("Exception when calling TeamsApi->bulk_delete_teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[TeamId]**](TeamId.md)|  | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_team**
> Team create_team(body)

Create team

This endpoint create a team.<br> You can optionally add a list of <code>members</code>, a <code>description</code> and a team <code>email</code>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TeamsApi(swagger_client.ApiClient(configuration))
body = swagger_client.OmitTeamIdOrIconHashOrMembersCount_() # OmitTeamIdOrIconHashOrMembersCount_ | 

try:
    # Create team
    api_response = api_instance.create_team(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->create_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OmitTeamIdOrIconHashOrMembersCount_**](OmitTeamIdOrIconHashOrMembersCount_.md)|  | 

### Return type

[**Team**](Team.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_team**
> delete_team(id)

Delete a team

This endpoint deletes the team associated to the <code>id</code> given in the request params.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TeamsApi(swagger_client.ApiClient(configuration))
id = swagger_client.TeamId() # TeamId | 

try:
    # Delete a team
    api_instance.delete_team(id)
except ApiException as e:
    print("Exception when calling TeamsApi->delete_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TeamId**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_teams**
> TeamsResult list_teams(id=id, name=name, access=access, include_members=include_members)

List teams

This endpoint fetches each team existing in your client space.<br> Each team is represented by a JSON Object containing basic informations and a list of the members.<br> Make sure you read the <a href=\"#tag/Teams\">Teams short introduction</a> to get a grasp of the main concepts.<br><br>  This endpoint supports <b>multivalue filters</b> passed as Querystrings, such as <code>id</code>, <code>name</code> and <code>access</code>.<br> If a filter contains multiple values the <code>OR</code> operator is applied.<br> So for example, filtering your result to match <i>private teams named <b>DreamTeam</b> or <b>ATeam</b></i> can be done as follow :<br> <pre>/v2/teams?name=DreamTeam&name=ATeam&access=private</pre>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TeamsApi(swagger_client.ApiClient(configuration))
id = [swagger_client.DoubleUuid()] # list[DoubleUuid] | Filters result to match **team id** (optional)
name = ['name_example'] # list[str] | Filters result to match **team name** (optional)
access = [swagger_client.AccessType()] # list[AccessType] | Filters result to match **team access** (optional)
include_members = false # bool | When <code>true</code>, adds a <code>members</code> property to each teams in the response payload. This property will contain a list of users composing the team. (optional) (default to false)

try:
    # List teams
    api_response = api_instance.list_teams(id=id, name=name, access=access, include_members=include_members)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->list_teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[DoubleUuid]**](DoubleUuid.md)| Filters result to match **team id** | [optional] 
 **name** | [**list[str]**](str.md)| Filters result to match **team name** | [optional] 
 **access** | [**list[AccessType]**](AccessType.md)| Filters result to match **team access** | [optional] 
 **include_members** | **bool**| When &lt;code&gt;true&lt;/code&gt;, adds a &lt;code&gt;members&lt;/code&gt; property to each teams in the response payload. This property will contain a list of users composing the team. | [optional] [default to false]

### Return type

[**TeamsResult**](TeamsResult.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_team**
> Team update_team(body, id)

Update team

This endpoint updates the team associated to the <code>id</code> given in the request params.<br><br> <code>owners</code> and <code>members</code> properties will be updated with the exact value you provide in your request payload.<br> This means you can remove users from these lists by simply omitting them from your request.<br> On the other hand, if you wish to add users, you need to send the whole existing users list with the additional users.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TeamsApi(swagger_client.ApiClient(configuration))
body = swagger_client.PartialTeamCreationPayload_() # PartialTeamCreationPayload_ | 
id = swagger_client.TeamId() # TeamId | 

try:
    # Update team
    api_response = api_instance.update_team(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->update_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PartialTeamCreationPayload_**](PartialTeamCreationPayload_.md)|  | 
 **id** | [**TeamId**](.md)|  | 

### Return type

[**Team**](Team.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

