# swagger_client.ImageApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_image**](ImageApi.md#get_image) | **GET** /image | Fetch an image
[**upload_image**](ImageApi.md#upload_image) | **POST** /image | Upload an image

# **get_image**
> str get_image(hash)

Fetch an image

Fetch the image associated to the <code>hash</code> given in parameters.<br/> The <code>Content-Type</code> can be <code>image/png</code>, <code>image/jpeg</code> or <code>image/svg</code>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImageApi()
hash = 'hash_example' # str | Image hash to get. <b>Must be URL-encoded</b>.

try:
    # Fetch an image
    api_response = api_instance.get_image(hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->get_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Image hash to get. &lt;b&gt;Must be URL-encoded&lt;/b&gt;. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png, image/jpeg, image/svg, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_image**
> ImageUploadResponse upload_image(image, category, workspace_id, technology_code)

Upload an image

Upload an image to DataGalaxy and associate it to a resource using the <code>category</code> property.  \\ The maximum supported size of uploaded images is <b>1MB</b>.  \\ \\ Supported resources are the following:  - <code>clientSpaceImage</code> update the Clientspace Home page image - <code>workspaceImage</code> update a Workspace Home page image. It can then be fetched using the <a href=\"/v2/documentation/beta#operation/GetWorkspaces\">GET /workspaces</a> endpoint. - <code>workspaceIcon</code> update a Workspace Icon. It can then be fetched using the <a href=\"/v2/documentation/beta#operation/GetWorkspaces\">GET /workspaces</a> endpoint. - <code>searchImage</code> update the Search page banner (<i>The recommended resolution for this image is 1860x200 px</i>) - <code>technologyIcon</code> update a Technology Icon. It can then be fetched using the <a href=\"/v2/documentation/beta#operation/GetTechnologies\">GET /technologies</a> endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImageApi()
image = 'image_example' # str | 
category = 'category_example' # str | 
workspace_id = 'workspace_id_example' # str | 
technology_code = 'technology_code_example' # str | 

try:
    # Upload an image
    api_response = api_instance.upload_image(image, category, workspace_id, technology_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->upload_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image** | **str**|  | 
 **category** | **str**|  | 
 **workspace_id** | **str**|  | 
 **technology_code** | **str**|  | 

### Return type

[**ImageUploadResponse**](ImageUploadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

