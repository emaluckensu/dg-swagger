# kensu_datagalaxy_client.ScreensApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_attributes_screens**](ScreensApi.md#get_attributes_screens) | **GET** /attributes/screens | Return a list of attribute screen layouts
[**get_attributes_screens_data_type**](ScreensApi.md#get_attributes_screens_data_type) | **GET** /attributes/screens/{dataType} | Return a list of attribute screen layouts filtered by dataType
[**get_attributes_screens_full_types**](ScreensApi.md#get_attributes_screens_full_types) | **GET** /attributes/screens/{dataType}/{type} | Return a list of attribute screen layouts filtered by dataType and entity type
[**reset_screen**](ScreensApi.md#reset_screen) | **DELETE** /attributes/screens/{dataType}/{type} | Reset an Attribute Screen
[**update_screen**](ScreensApi.md#update_screen) | **PUT** /attributes/screens/{dataType}/{type} | Update an attribute screen layout

# **get_attributes_screens**
> list[AttributesLayout] get_attributes_screens(version_id=version_id)

Return a list of attribute screen layouts

Return a list of attribute screen layouts.<br> An attribute screen layout displays which attributes exists on each entity type, ordered by entity type and categories.<br><br>  Note: there is 2 level of attribute screens: <a href=\"https://datagalaxy.freshdesk.com/en/support/solutions/articles/35000130620--basics-manage-the-clientspace\" target=\"_blank\">ClientSpace</a> level and <a href=\"https://datagalaxy.freshdesk.com/en/support/solutions/articles/35000130839--basics-administrate-a-workspace\" target=\"_blank\">Workspace</a> level.<br>  Learn more about attribute screen basics with this <a href=\"https://datagalaxy.freshdesk.com/en/support/solutions/articles/35000131901--basics-the-object-card-and-the-screens\" target=\"_blank\">this article</a>. Learn more about attributes with <a href=\"https://datagalaxy.freshdesk.com/en/support/solutions/articles/35000132213--basics-presentation-of-attributes\" target=\"_blank\">this article</a>.  <i>Tip: attribute screen layouts returned by this route are basically a JSON-stringified version of the Screen section <br> found on DataGalaxy Platform.</i>

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.ScreensApi(kensu_datagalaxy_client.ApiClient(configuration))
version_id = kensu_datagalaxy_client.Uuid() # Uuid | By default, this request will return <b>clientspace</b> level screen layouts.<br> If <code>versionId</code> is specified, this request will return <b>workspace</b> level screen layouts. (optional)

try:
    # Return a list of attribute screen layouts
    api_response = api_instance.get_attributes_screens(version_id=version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreensApi->get_attributes_screens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**Uuid**](.md)| By default, this request will return &lt;b&gt;clientspace&lt;/b&gt; level screen layouts.&lt;br&gt; If &lt;code&gt;versionId&lt;/code&gt; is specified, this request will return &lt;b&gt;workspace&lt;/b&gt; level screen layouts. | [optional] 

### Return type

[**list[AttributesLayout]**](AttributesLayout.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attributes_screens_data_type**
> list[AttributesLayout] get_attributes_screens_data_type(data_type, version_id=version_id)

Return a list of attribute screen layouts filtered by dataType

Return a list of attribute screen layouts.<br> An attribute screen layout displays which attributes exists on each entity type, ordered by entity type and categories.<br><br>  Note: there is 2 level of attribute screens: <a href=\"https://datagalaxy.freshdesk.com/en/support/solutions/articles/35000130620--basics-manage-the-clientspace\" target=\"_blank\">ClientSpace</a> level and <a href=\"https://datagalaxy.freshdesk.com/en/support/solutions/articles/35000130839--basics-administrate-a-workspace\" target=\"_blank\">Workspace</a> level.<br>  Learn more about attribute screen basics with this <a href=\"https://datagalaxy.freshdesk.com/en/support/solutions/articles/35000131901--basics-the-object-card-and-the-screens\" target=\"_blank\">this article</a>. Learn more about attributes with <a href=\"https://datagalaxy.freshdesk.com/en/support/solutions/articles/35000132213--basics-presentation-of-attributes\" target=\"_blank\">this article</a>.  <i>Tip: attribute screen layouts returned by this route are basically a JSON-stringified version of the Screen section <br> found on DataGalaxy Platform.</i>

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.ScreensApi(kensu_datagalaxy_client.ApiClient(configuration))
data_type = kensu_datagalaxy_client.ScreenDataTypes() # ScreenDataTypes | 
version_id = kensu_datagalaxy_client.Uuid() # Uuid | By default, this request will return <b>clientspace</b> level screen layouts.<br> If <code>versionId</code> is specified, this request will return <b>workspace</b> level screen layouts. (optional)

try:
    # Return a list of attribute screen layouts filtered by dataType
    api_response = api_instance.get_attributes_screens_data_type(data_type, version_id=version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreensApi->get_attributes_screens_data_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_type** | [**ScreenDataTypes**](.md)|  | 
 **version_id** | [**Uuid**](.md)| By default, this request will return &lt;b&gt;clientspace&lt;/b&gt; level screen layouts.&lt;br&gt; If &lt;code&gt;versionId&lt;/code&gt; is specified, this request will return &lt;b&gt;workspace&lt;/b&gt; level screen layouts. | [optional] 

### Return type

[**list[AttributesLayout]**](AttributesLayout.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attributes_screens_full_types**
> list[AttributesLayout] get_attributes_screens_full_types(data_type, type, version_id=version_id)

Return a list of attribute screen layouts filtered by dataType and entity type

Return a list of attribute screen layouts.<br> An attribute screen layout displays which attributes exists on each entity type, ordered by entity type and categories.<br><br>  Note: there is 2 level of attribute screens: <a href=\"https://datagalaxy.freshdesk.com/en/support/solutions/articles/35000130620--basics-manage-the-clientspace\" target=\"_blank\">ClientSpace</a> level and <a href=\"https://datagalaxy.freshdesk.com/en/support/solutions/articles/35000130839--basics-administrate-a-workspace\" target=\"_blank\">Workspace</a> level.<br>  Learn more about attribute screen basics with this <a href=\"https://datagalaxy.freshdesk.com/en/support/solutions/articles/35000131901--basics-the-object-card-and-the-screens\" target=\"_blank\">this article</a>. Learn more about attributes with <a href=\"https://datagalaxy.freshdesk.com/en/support/solutions/articles/35000132213--basics-presentation-of-attributes\" target=\"_blank\">this article</a>.  <i>Tip: attribute screen layouts returned by this route are basically a JSON-stringified version of the Screen section <br> found on DataGalaxy Platform.</i>

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.ScreensApi(kensu_datagalaxy_client.ApiClient(configuration))
data_type = kensu_datagalaxy_client.ScreenDataTypes() # ScreenDataTypes | 
type = kensu_datagalaxy_client.LowerCaseAllTypes() # LowerCaseAllTypes | 
version_id = kensu_datagalaxy_client.Uuid() # Uuid | By default, this request will return <b>clientspace</b> level screen layouts.<br> If <code>versionId</code> is specified, this request will return <b>workspace</b> level screen layouts. (optional)

try:
    # Return a list of attribute screen layouts filtered by dataType and entity type
    api_response = api_instance.get_attributes_screens_full_types(data_type, type, version_id=version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreensApi->get_attributes_screens_full_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_type** | [**ScreenDataTypes**](.md)|  | 
 **type** | [**LowerCaseAllTypes**](.md)|  | 
 **version_id** | [**Uuid**](.md)| By default, this request will return &lt;b&gt;clientspace&lt;/b&gt; level screen layouts.&lt;br&gt; If &lt;code&gt;versionId&lt;/code&gt; is specified, this request will return &lt;b&gt;workspace&lt;/b&gt; level screen layouts. | [optional] 

### Return type

[**list[AttributesLayout]**](AttributesLayout.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_screen**
> AttributesLayout reset_screen(data_type, type, version_id=version_id)

Reset an Attribute Screen

Reset an attribute screen to its default layout.  Learn more about attributes with <a href=\"https://datagalaxy.freshdesk.com/en/support/solutions/articles/35000132213--basics-presentation-of-attributes\" target=\"_blank\">this article</a>.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.ScreensApi(kensu_datagalaxy_client.ApiClient(configuration))
data_type = kensu_datagalaxy_client.ScreenDataTypes() # ScreenDataTypes | Target dataType
type = kensu_datagalaxy_client.LowerCaseAllTypes() # LowerCaseAllTypes | Target entity type
version_id = kensu_datagalaxy_client.Uuid() # Uuid | By default, this request will reset <b>clientspace</b> level screen layouts.<br> If <code>versionId</code> is specified, this request will reset <b>workspace</b> level screen layouts. (optional)

try:
    # Reset an Attribute Screen
    api_response = api_instance.reset_screen(data_type, type, version_id=version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreensApi->reset_screen: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_type** | [**ScreenDataTypes**](.md)| Target dataType | 
 **type** | [**LowerCaseAllTypes**](.md)| Target entity type | 
 **version_id** | [**Uuid**](.md)| By default, this request will reset &lt;b&gt;clientspace&lt;/b&gt; level screen layouts.&lt;br&gt; If &lt;code&gt;versionId&lt;/code&gt; is specified, this request will reset &lt;b&gt;workspace&lt;/b&gt; level screen layouts. | [optional] 

### Return type

[**AttributesLayout**](AttributesLayout.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_screen**
> AttributesLayout update_screen(body, data_type, type, version_id=version_id)

Update an attribute screen layout

Update an entire attribute screen layout.<br><br>  Here are some tips for your updates: <br> - <b>create a new category</b>: add a new element to your body with just a <code>name</code> and <code>attributes</code><br> - <b>update an existing category</b>: specify its <code>id</code> and change any other property (<code>name</code>, <code>isHidden</code>, <code>attributes</code>)<br> - <b>remove a category</b>: if your body does not contain it, it will be removed<br> - <b>remove an attribute</b>: if <code>attributes</code> does not contain it, it will be removed<br> - <b>change a category or attribute position/order</b>: categories and attributes order in your body will be applied<br><br>  Find existing categories <code>id</code> and layout with <b>GET /attributes/screens</b> routes.<br> Find attribute names with <b>GET /attributes</b>.  Learn more about attribute screen basics with this <a href=\"https://datagalaxy.freshdesk.com/en/support/solutions/articles/35000131901--basics-the-object-card-and-the-screens\" target=\"_blank\">this article</a>. Learn more about attributes with <a href=\"https://datagalaxy.freshdesk.com/en/support/solutions/articles/35000132213--basics-presentation-of-attributes\" target=\"_blank\">this article</a>.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.ScreensApi(kensu_datagalaxy_client.ApiClient(configuration))
body = [kensu_datagalaxy_client.CategoryBodyAttributeName_()] # list[CategoryBodyAttributeName_] | This represents your screen layout. <b>Categories and attributes order matters</b>
data_type = kensu_datagalaxy_client.ScreenDataTypes() # ScreenDataTypes | Target dataType
type = kensu_datagalaxy_client.LowerCaseAllTypes() # LowerCaseAllTypes | Target entity type
version_id = kensu_datagalaxy_client.Uuid() # Uuid | By default, this request will update <b>clientspace</b> level screen layouts.<br> If <code>versionId</code> is specified, this request will update <b>workspace</b> level screen layouts. (optional)

try:
    # Update an attribute screen layout
    api_response = api_instance.update_screen(body, data_type, type, version_id=version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScreensApi->update_screen: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[CategoryBodyAttributeName_]**](CategoryBodyAttributeName_.md)| This represents your screen layout. &lt;b&gt;Categories and attributes order matters&lt;/b&gt; | 
 **data_type** | [**ScreenDataTypes**](.md)| Target dataType | 
 **type** | [**LowerCaseAllTypes**](.md)| Target entity type | 
 **version_id** | [**Uuid**](.md)| By default, this request will update &lt;b&gt;clientspace&lt;/b&gt; level screen layouts.&lt;br&gt; If &lt;code&gt;versionId&lt;/code&gt; is specified, this request will update &lt;b&gt;workspace&lt;/b&gt; level screen layouts. | [optional] 

### Return type

[**AttributesLayout**](AttributesLayout.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

