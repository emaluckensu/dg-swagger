# swagger_client.TasksApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_task**](TasksApi.md#delete_task) | **DELETE** /tasks/{versionId}/{entityId}/{taskId} | Delete a task.
[**get_task**](TasksApi.md#get_task) | **GET** /tasks/{versionId}/{entityId} | List entity tasks
[**get_user_tasks**](TasksApi.md#get_user_tasks) | **GET** /tasks | List user tasks
[**post_task**](TasksApi.md#post_task) | **POST** /tasks/{versionId}/{entityId} | Create a task.
[**put_task**](TasksApi.md#put_task) | **PUT** /tasks/{versionId}/{entityId}/{taskId} | Update a task.

# **delete_task**
> delete_task(version_id, entity_id, task_id)

Delete a task.

Delete a <b>task</b> from the specified <b>entity</b>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TasksApi(swagger_client.ApiClient(configuration))
version_id = swagger_client.VersionId() # VersionId | 
entity_id = swagger_client.DoubleUuid() # DoubleUuid | 
task_id = swagger_client.DoubleUuid() # DoubleUuid | 

try:
    # Delete a task.
    api_instance.delete_task(version_id, entity_id, task_id)
except ApiException as e:
    print("Exception when calling TasksApi->delete_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **entity_id** | [**DoubleUuid**](.md)|  | 
 **task_id** | [**DoubleUuid**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task**
> list[Task] get_task(version_id, entity_id)

List entity tasks

Return a list of all <b>tasks</b> associated with an <b>entity</b>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TasksApi(swagger_client.ApiClient(configuration))
version_id = swagger_client.VersionId() # VersionId | 
entity_id = swagger_client.DoubleUuid() # DoubleUuid | 

try:
    # List entity tasks
    api_response = api_instance.get_task(version_id, entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **entity_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**list[Task]**](Task.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_tasks**
> list[Task] get_user_tasks(q=q, creator=creator, assignee=assignee, status=status, type=type, version_id=version_id)

List user tasks

Return the list of <b>tasks</b> of which the user associated to the integrationToken is the creator or the assigned manager.<br><br> `assignee` and `creator` parameters **support query string arrays** and will be logically joined with OR operator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TasksApi(swagger_client.ApiClient(configuration))
q = swagger_client.SearchQuery() # SearchQuery |  (optional)
creator = [swagger_client.Email()] # list[Email] |  (optional)
assignee = [swagger_client.Email()] # list[Email] |  (optional)
status = swagger_client.TaskStatus() # TaskStatus |  (optional)
type = swagger_client.TaskType() # TaskType |  (optional)
version_id = swagger_client.Uuid() # Uuid |  (optional)

try:
    # List user tasks
    api_response = api_instance.get_user_tasks(q=q, creator=creator, assignee=assignee, status=status, type=type, version_id=version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_user_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | [**SearchQuery**](.md)|  | [optional] 
 **creator** | [**list[Email]**](Email.md)|  | [optional] 
 **assignee** | [**list[Email]**](Email.md)|  | [optional] 
 **status** | [**TaskStatus**](.md)|  | [optional] 
 **type** | [**TaskType**](.md)|  | [optional] 
 **version_id** | [**Uuid**](.md)|  | [optional] 

### Return type

[**list[Task]**](Task.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_task**
> Task post_task(body, version_id, entity_id)

Create a task.

Create a <b>task</b> in the specified <b>entity</b>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TasksApi(swagger_client.ApiClient(configuration))
body = swagger_client.TaskCreationPayload() # TaskCreationPayload | 
version_id = swagger_client.VersionId() # VersionId | 
entity_id = swagger_client.DoubleUuid() # DoubleUuid | 

try:
    # Create a task.
    api_response = api_instance.post_task(body, version_id, entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->post_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TaskCreationPayload**](TaskCreationPayload.md)|  | 
 **version_id** | [**VersionId**](.md)|  | 
 **entity_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**Task**](Task.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_task**
> Task put_task(body, version_id, entity_id, task_id)

Update a task.

Update a <b>task</b> in the specified <b>entity</b>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TasksApi(swagger_client.ApiClient(configuration))
body = swagger_client.TaskUpdatePayload() # TaskUpdatePayload | 
version_id = swagger_client.VersionId() # VersionId | 
entity_id = swagger_client.DoubleUuid() # DoubleUuid | 
task_id = swagger_client.DoubleUuid() # DoubleUuid | 

try:
    # Update a task.
    api_response = api_instance.put_task(body, version_id, entity_id, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->put_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TaskUpdatePayload**](TaskUpdatePayload.md)|  | 
 **version_id** | [**VersionId**](.md)|  | 
 **entity_id** | [**DoubleUuid**](.md)|  | 
 **task_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**Task**](Task.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

