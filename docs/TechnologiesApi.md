# swagger_client.TechnologiesApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_techonogy**](TechnologiesApi.md#create_techonogy) | **POST** /technologies | 
[**delete_technology**](TechnologiesApi.md#delete_technology) | **DELETE** /technologies/{technologyCode} | 
[**get_technologies**](TechnologiesApi.md#get_technologies) | **GET** /technologies | 
[**update_technology**](TechnologiesApi.md#update_technology) | **PUT** /technologies/{technologyCode} | 

# **create_techonogy**
> Technology create_techonogy(body)



Add a custom technology to DataGalaxy using this endpoint.<br>  <h4>Adding technologies to DataGalaxy objects</h4>  Technologies can then be added to an object details using the <code>technologyCode</code> property in a creation or update request payload.<br> Example: <br> <pre><code> POST /sources/bulktree/{versionId} {   \"name\": \"foo\",   \"type\": \"Relational\",   \"technologyCode\": \"azuresql\",   \"children\": [ ... ] } </code></pre>  Read our <a href=\"https://datagalaxy.freshdesk.com/en/support/solutions/articles/35000194800--basics-technologies-overview\" target='_new'>article on technologies</a> for more informations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TechnologiesApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateTechnologyBody() # CreateTechnologyBody | 

try:
    api_response = api_instance.create_techonogy(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TechnologiesApi->create_techonogy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTechnologyBody**](CreateTechnologyBody.md)|  | 

### Return type

[**Technology**](Technology.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_technology**
> delete_technology(technology_code)



Delete a technology.<br> Read our <a href=\"https://datagalaxy.freshdesk.com/en/support/solutions/articles/35000194800--basics-technologies-overview\" target='_new'>article on technologies</a> for more informations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TechnologiesApi(swagger_client.ApiClient(configuration))
technology_code = 'technology_code_example' # str | 

try:
    api_instance.delete_technology(technology_code)
except ApiException as e:
    print("Exception when calling TechnologiesApi->delete_technology: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **technology_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_technologies**
> GetTechnologiesResult get_technologies()



Use this endpoint in order to fetch Technologies, their associated <i>modules</i>, their <i>description</i>, <i>images</i> and <i>metadatas</i> related to creation, modification and usage.<br> Read our <a href=\"https://datagalaxy.freshdesk.com/en/support/solutions/articles/35000194800--basics-technologies-overview\" target='_new'>article on technologies</a> for more informations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TechnologiesApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_technologies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TechnologiesApi->get_technologies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetTechnologiesResult**](GetTechnologiesResult.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_technology**
> Technology update_technology(body, technology_code)



Update a technology's <code>displayName</code>, <code>description</code> and associated <code>modules</code> using this endpoint.<br> Read our <a href=\"https://datagalaxy.freshdesk.com/en/support/solutions/articles/35000194800--basics-technologies-overview\" target='_new'>article on technologies</a> for more informations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TechnologiesApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateTechnologyBody() # UpdateTechnologyBody | 
technology_code = 'technology_code_example' # str | 

try:
    api_response = api_instance.update_technology(body, technology_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TechnologiesApi->update_technology: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTechnologyBody**](UpdateTechnologyBody.md)|  | 
 **technology_code** | **str**|  | 

### Return type

[**Technology**](Technology.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

