# swagger_client.AttributesApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_create_attribute**](AttributesApi.md#bulk_create_attribute) | **POST** /attributes/bulk | Bulk create attributes
[**bulk_update_attribute**](AttributesApi.md#bulk_update_attribute) | **PUT** /attributes/bulk | Bulk edit attributes
[**create_attribute**](AttributesApi.md#create_attribute) | **POST** /attributes/{dataType} | Create a custom attribute
[**create_attribute_values**](AttributesApi.md#create_attribute_values) | **POST** /attributes/values | Add attribute values
[**delete_attribute**](AttributesApi.md#delete_attribute) | **DELETE** /attributes/{dataType}/{attributeKey} | Delete a custom attribute
[**get_attribute_values**](AttributesApi.md#get_attribute_values) | **GET** /attributes/values | List attribute values
[**get_attributes**](AttributesApi.md#get_attributes) | **GET** /attributes | Return a list of attributes
[**get_supported_attributes**](AttributesApi.md#get_supported_attributes) | **GET** /supportedAttributes/{versionId} | List of available attributes
[**get_tags**](AttributesApi.md#get_tags) | **GET** /tags | List available tags
[**post_tags**](AttributesApi.md#post_tags) | **POST** /tags | Create tag
[**update_attribute**](AttributesApi.md#update_attribute) | **PUT** /attributes/{dataType}/{attributeKey} | Update an attribute
[**update_attribute_values**](AttributesApi.md#update_attribute_values) | **PUT** /attributes/values | Update attribute values

# **bulk_create_attribute**
> list[Attribute] bulk_create_attribute(body)

Bulk create attributes

Learn more about attributes with <a href=\"https://datagalaxy.freshdesk.com/en/support/solutions/articles/35000132213--basics-presentation-of-attributes\" target=\"_blank\">this article</a>.  Create up to 50 attributes.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AttributesApi(swagger_client.ApiClient(configuration))
body = [swagger_client.AttributeBulkCreationBody()] # list[AttributeBulkCreationBody] | 

try:
    # Bulk create attributes
    api_response = api_instance.bulk_create_attribute(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->bulk_create_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[AttributeBulkCreationBody]**](AttributeBulkCreationBody.md)|  | 

### Return type

[**list[Attribute]**](Attribute.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_update_attribute**
> list[Attribute] bulk_update_attribute(body)

Bulk edit attributes

Learn more about attributes with <a href=\"https://datagalaxy.freshdesk.com/en/support/solutions/articles/35000132213--basics-presentation-of-attributes\" target=\"_blank\">this article</a>.  Update up to 50 attributes.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AttributesApi(swagger_client.ApiClient(configuration))
body = [swagger_client.AttributeBulkUpdateBody()] # list[AttributeBulkUpdateBody] | 

try:
    # Bulk edit attributes
    api_response = api_instance.bulk_update_attribute(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->bulk_update_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[AttributeBulkUpdateBody]**](AttributeBulkUpdateBody.md)|  | 

### Return type

[**list[Attribute]**](Attribute.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_attribute**
> Attribute create_attribute(body, data_type)

Create a custom attribute

Learn more about attributes with <a href=\"https://datagalaxy.freshdesk.com/en/support/solutions/articles/35000132213--basics-presentation-of-attributes\" target=\"_blank\">this article</a>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AttributesApi(swagger_client.ApiClient(configuration))
body = swagger_client.AttributeCreationBody() # AttributeCreationBody | 
data_type = swagger_client.AttributeDataTypeEnum() # AttributeDataTypeEnum | Specifies the <code>dataType</code> this attribute will be associated with

try:
    # Create a custom attribute
    api_response = api_instance.create_attribute(body, data_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->create_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AttributeCreationBody**](AttributeCreationBody.md)|  | 
 **data_type** | [**AttributeDataTypeEnum**](.md)| Specifies the &lt;code&gt;dataType&lt;/code&gt; this attribute will be associated with | 

### Return type

[**Attribute**](Attribute.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_attribute_values**
> InlineResponse200 create_attribute_values(body, data_type, attribute_key)

Add attribute values

This route adds up to 100 values to attributes with format:  - `ValueList`, - `Hierarchy`, - `MultiValueList`, - `ManagedTag`, - or `ClientTag`.  Attributes with format `ValueList` expect a list of string values.<br> Attributes with format `Hierarchy`, `MultiValueList`, `ManagedTag` and `ClientTag` expect a request body with `TagsBody` schema.  Learn more about attributes with <a href=\"https://datagalaxy.freshdesk.com/en/support/solutions/articles/35000132213--basics-presentation-of-attributes\" target=\"_blank\">this article</a>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AttributesApi(swagger_client.ApiClient(configuration))
body = swagger_client.AttributesValuesBody1() # AttributesValuesBody1 | 
data_type = swagger_client.AttributeDataTypeEnum() # AttributeDataTypeEnum | 
attribute_key = swagger_client.AttributeKey() # AttributeKey | 

try:
    # Add attribute values
    api_response = api_instance.create_attribute_values(body, data_type, attribute_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->create_attribute_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AttributesValuesBody1**](AttributesValuesBody1.md)|  | 
 **data_type** | [**AttributeDataTypeEnum**](.md)|  | 
 **attribute_key** | [**AttributeKey**](.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_attribute**
> Attribute delete_attribute(data_type, attribute_key)

Delete a custom attribute

Learn more about attributes with <a href=\"https://datagalaxy.freshdesk.com/en/support/solutions/articles/35000132213--basics-presentation-of-attributes\" target=\"_blank\">this article</a>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AttributesApi(swagger_client.ApiClient(configuration))
data_type = swagger_client.AttributeDataTypeEnum() # AttributeDataTypeEnum | Specifies the <code>dataType</code> associated with an attribute
attribute_key = swagger_client.AttributeKey() # AttributeKey | Unique attribute identifier. Can be found with GET /attributes or when creating attributes with POST /attributes

try:
    # Delete a custom attribute
    api_response = api_instance.delete_attribute(data_type, attribute_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->delete_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_type** | [**AttributeDataTypeEnum**](.md)| Specifies the &lt;code&gt;dataType&lt;/code&gt; associated with an attribute | 
 **attribute_key** | [**AttributeKey**](.md)| Unique attribute identifier. Can be found with GET /attributes or when creating attributes with POST /attributes | 

### Return type

[**Attribute**](Attribute.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attribute_values**
> InlineResponse200 get_attribute_values(data_type, attribute_key)

List attribute values

This route fetches available values for attributes with format:  - `ValueList`, - `Hierarchy`, - `MultiValueList`, - `ManagedTag`, - or `ClientTag`.  Learn more about attributes with <a href=\"https://datagalaxy.freshdesk.com/en/support/solutions/articles/35000132213--basics-presentation-of-attributes\" target=\"_blank\">this article</a>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AttributesApi(swagger_client.ApiClient(configuration))
data_type = swagger_client.AttributeDataTypeEnum() # AttributeDataTypeEnum | 
attribute_key = swagger_client.AttributeKey() # AttributeKey | 

try:
    # List attribute values
    api_response = api_instance.get_attribute_values(data_type, attribute_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->get_attribute_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_type** | [**AttributeDataTypeEnum**](.md)|  | 
 **attribute_key** | [**AttributeKey**](.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attributes**
> list[Attribute] get_attributes(data_type)

Return a list of attributes

Return a list of attributes available for a given <code>dataType</code>.<br> Note: <code>Common</code> attributes are not bound to one dataType and can therefore be used on any dataType.  Learn more about attributes with <a href=\"https://datagalaxy.freshdesk.com/en/support/solutions/articles/35000132213--basics-presentation-of-attributes\" target=\"_blank\">this article</a>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AttributesApi(swagger_client.ApiClient(configuration))
data_type = swagger_client.AttributeDataTypeEnum() # AttributeDataTypeEnum | 

try:
    # Return a list of attributes
    api_response = api_instance.get_attributes(data_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->get_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_type** | [**AttributeDataTypeEnum**](.md)|  | 

### Return type

[**list[Attribute]**](Attribute.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supported_attributes**
> PaginatedResponseAttributesResponseBody_ get_supported_attributes(version_id, module_name=module_name, limit=limit, page=page)

List of available attributes

<b><i>Deprecation warning: <br> This route is no longer maintained and is replaced by <code>GET /attributes</code>. </i></b>  Return a list of <b>attributes</b> available for the specified <b>dataType</b>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AttributesApi(swagger_client.ApiClient(configuration))
version_id = swagger_client.VersionId() # VersionId | 
module_name = 'module_name_example' # str |  (optional)
limit = 20 # float |  (optional) (default to 20)
page = 1 # float |  (optional) (default to 1)

try:
    # List of available attributes
    api_response = api_instance.get_supported_attributes(version_id, module_name=module_name, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->get_supported_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **module_name** | **str**|  | [optional] 
 **limit** | **float**|  | [optional] [default to 20]
 **page** | **float**|  | [optional] [default to 1]

### Return type

[**PaginatedResponseAttributesResponseBody_**](PaginatedResponseAttributesResponseBody_.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags**
> PaginatedResponseTagsResponseBody_ get_tags(limit=limit, page=page, color=color, is_native=is_native, is_active=is_active, is_user_suggestion_enabled=is_user_suggestion_enabled)

List available tags

<b><i>Deprecation warning: <br> This route is no longer maintained and is replaced by <code>GET /attributes/values</code>.<br> In order to reproduce this route's behavior, request <code>GET /attributes/values?dataType=common&attributeKey=Domains</code>. </i></b>  Return the list of all <b>tags</b> available.<br> Tags can be added to the <code>tag</code> field of an object.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AttributesApi(swagger_client.ApiClient(configuration))
limit = 20 # float |  (optional) (default to 20)
page = 1 # float |  (optional) (default to 1)
color = 'color_example' # str |  (optional)
is_native = true # bool |  (optional)
is_active = true # bool |  (optional)
is_user_suggestion_enabled = true # bool |  (optional)

try:
    # List available tags
    api_response = api_instance.get_tags(limit=limit, page=page, color=color, is_native=is_native, is_active=is_active, is_user_suggestion_enabled=is_user_suggestion_enabled)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->get_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**|  | [optional] [default to 20]
 **page** | **float**|  | [optional] [default to 1]
 **color** | **str**|  | [optional] 
 **is_native** | **bool**|  | [optional] 
 **is_active** | **bool**|  | [optional] 
 **is_user_suggestion_enabled** | **bool**|  | [optional] 

### Return type

[**PaginatedResponseTagsResponseBody_**](PaginatedResponseTagsResponseBody_.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tags**
> InlineResponse201 post_tags(body)

Create tag

<b><i>Deprecation warning: <br> This route is no longer maintained and is replaced by <code>POST /attributes/values</code>.<br> In order to reproduce this route's behavior, request <code>POST /attributes/values?dataType=common&attributeKey=Domains</code> and send the same request body. </i></b>  This route can creates up to 5 000 tags. <b>color</b> can be one of the values enumerated below, or an hexadecimal value.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AttributesApi(swagger_client.ApiClient(configuration))
body = [swagger_client.TagsBody()] # list[TagsBody] | 

try:
    # Create tag
    api_response = api_instance.post_tags(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->post_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[TagsBody]**](TagsBody.md)|  | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_attribute**
> Attribute update_attribute(body, data_type, attribute_key)

Update an attribute

Learn more about attributes with <a href=\"https://datagalaxy.freshdesk.com/en/support/solutions/articles/35000132213--basics-presentation-of-attributes\" target=\"_blank\">this article</a>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AttributesApi(swagger_client.ApiClient(configuration))
body = swagger_client.AttributeUpdateBody() # AttributeUpdateBody | 
data_type = swagger_client.AttributeDataTypeEnum() # AttributeDataTypeEnum | Specifies the <code>dataType</code> associated with an attribute
attribute_key = 'attribute_key_example' # str | Unique attribute identifier. Can be found with GET /attributes or when creating attributes with POST /attributes

try:
    # Update an attribute
    api_response = api_instance.update_attribute(body, data_type, attribute_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->update_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AttributeUpdateBody**](AttributeUpdateBody.md)|  | 
 **data_type** | [**AttributeDataTypeEnum**](.md)| Specifies the &lt;code&gt;dataType&lt;/code&gt; associated with an attribute | 
 **attribute_key** | **str**| Unique attribute identifier. Can be found with GET /attributes or when creating attributes with POST /attributes | 

### Return type

[**Attribute**](Attribute.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_attribute_values**
> InlineResponse200 update_attribute_values(body, data_type, attribute_key)

Update attribute values

This route updates up to 100 attribute values for attributes with format:  - `ValueList`, - `Hierarchy`, - `MultiValueList`, - `ManagedTag`, - or `ClientTag`. <br><br>  Attributes with format `ValueList` expect a request body with `AttributeValue` schema.<br> Attributes with format `Hierarchy`, `MultiValueList`, `ManagedTag` and `ClientTag` expect a request body with `TagsBody` schema.  Learn more about attributes with <a href=\"https://datagalaxy.freshdesk.com/en/support/solutions/articles/35000132213--basics-presentation-of-attributes\" target=\"_blank\">this article</a>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AttributesApi(swagger_client.ApiClient(configuration))
body = swagger_client.AttributesValuesBody() # AttributesValuesBody | 
data_type = swagger_client.AttributeDataTypeEnum() # AttributeDataTypeEnum | 
attribute_key = swagger_client.AttributeKey() # AttributeKey | 

try:
    # Update attribute values
    api_response = api_instance.update_attribute_values(body, data_type, attribute_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->update_attribute_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AttributesValuesBody**](AttributesValuesBody.md)|  | 
 **data_type** | [**AttributeDataTypeEnum**](.md)|  | 
 **attribute_key** | [**AttributeKey**](.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

