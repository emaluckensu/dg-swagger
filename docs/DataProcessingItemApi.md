# swagger_client.DataProcessingItemApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_dpi_creation**](DataProcessingItemApi.md#bulk_dpi_creation) | **POST** /dataProcessingItem/bulk/{versionId}/{dataProcessingId} | Bulk upsert data processing items.
[**create_dpi**](DataProcessingItemApi.md#create_dpi) | **POST** /dataProcessingItem/{versionId}/{dataProcessingId} | Create a data processing item.
[**delete_dpi**](DataProcessingItemApi.md#delete_dpi) | **DELETE** /dataProcessingItem/{versionId}/{dataProcessingId}/{dataProcessingItemId} | Delete a data processing item.
[**get_dpi_list**](DataProcessingItemApi.md#get_dpi_list) | **GET** /dataProcessingItem | Return the list of dataProcessingItems contained in the specified data processing.
[**get_types**](DataProcessingItemApi.md#get_types) | **GET** /dataProcessingItem/types | List the data processing items types.
[**update_dpi**](DataProcessingItemApi.md#update_dpi) | **PUT** /dataProcessingItem/{versionId}/{dataProcessingId}/{dataProcessingItemId} | Update a data processing item.

# **bulk_dpi_creation**
> BulkResult bulk_dpi_creation(body, version_id, data_processing_id)

Bulk upsert data processing items.

Create multiple <b>data processing items</b> and their inputs and outputs in the specified <b>data processing</b>.<br> <b>Inputs</b> and <b>outputs</b> paths must have the following format: <pre><code> {   entityPath: \"\\\\foo\\\\bar\",   typePath: \"\\\\NoSql\\\\Table\" }</code></pre> <br>Available data processing item types can be found thanks to the <code>GET /types</code> endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DataProcessingItemApi(swagger_client.ApiClient(configuration))
body = [swagger_client.DpiBulkModel()] # list[DpiBulkModel] | 
version_id = swagger_client.VersionId() # VersionId | 
data_processing_id = swagger_client.DoubleUuid() # DoubleUuid | 

try:
    # Bulk upsert data processing items.
    api_response = api_instance.bulk_dpi_creation(body, version_id, data_processing_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataProcessingItemApi->bulk_dpi_creation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[DpiBulkModel]**](DpiBulkModel.md)|  | 
 **version_id** | [**VersionId**](.md)|  | 
 **data_processing_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**BulkResult**](BulkResult.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dpi**
> DpiId create_dpi(body, version_id, data_processing_id)

Create a data processing item.

Create a <b>data processing item</b> and its inputs and outputs in the specified <b>data processing</b>.<br> An input/output shall be a sourceId/structureId/fieldId. <br>Available data processing item types can be found thanks to the <code>GET /types</code> endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DataProcessingItemApi(swagger_client.ApiClient(configuration))
body = swagger_client.DpiCreationBody() # DpiCreationBody | 
version_id = swagger_client.VersionId() # VersionId | 
data_processing_id = swagger_client.DoubleUuid() # DoubleUuid | 

try:
    # Create a data processing item.
    api_response = api_instance.create_dpi(body, version_id, data_processing_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataProcessingItemApi->create_dpi: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DpiCreationBody**](DpiCreationBody.md)|  | 
 **version_id** | [**VersionId**](.md)|  | 
 **data_processing_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**DpiId**](DpiId.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dpi**
> delete_dpi(version_id, data_processing_id, data_processing_item_id)

Delete a data processing item.

Delete a data processing item.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DataProcessingItemApi(swagger_client.ApiClient(configuration))
version_id = swagger_client.VersionId() # VersionId | 
data_processing_id = swagger_client.DoubleUuid() # DoubleUuid | 
data_processing_item_id = swagger_client.DoubleUuid() # DoubleUuid | 

try:
    # Delete a data processing item.
    api_instance.delete_dpi(version_id, data_processing_id, data_processing_item_id)
except ApiException as e:
    print("Exception when calling DataProcessingItemApi->delete_dpi: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **data_processing_id** | [**DoubleUuid**](.md)|  | 
 **data_processing_item_id** | [**DoubleUuid**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dpi_list**
> PaginatedResponseDpiData_ get_dpi_list(version_id, data_processing_id, name=name, technical_name=technical_name, type=type, limit=limit, page=page)

Return the list of dataProcessingItems contained in the specified data processing.

Return the list of <b>dataProcessingItems</b> contained in the specified <b>data processing</b>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DataProcessingItemApi(swagger_client.ApiClient(configuration))
version_id = swagger_client.VersionId() # VersionId | 
data_processing_id = swagger_client.DoubleUuid() # DoubleUuid | 
name = 'name_example' # str |  (optional)
technical_name = 'technical_name_example' # str |  (optional)
type = swagger_client.DataProcessingItemType() # DataProcessingItemType |  (optional)
limit = 20 # float |  (optional) (default to 20)
page = 1 # float |  (optional) (default to 1)

try:
    # Return the list of dataProcessingItems contained in the specified data processing.
    api_response = api_instance.get_dpi_list(version_id, data_processing_id, name=name, technical_name=technical_name, type=type, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataProcessingItemApi->get_dpi_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**VersionId**](.md)|  | 
 **data_processing_id** | [**DoubleUuid**](.md)|  | 
 **name** | **str**|  | [optional] 
 **technical_name** | **str**|  | [optional] 
 **type** | [**DataProcessingItemType**](.md)|  | [optional] 
 **limit** | **float**|  | [optional] [default to 20]
 **page** | **float**|  | [optional] [default to 1]

### Return type

[**PaginatedResponseDpiData_**](PaginatedResponseDpiData_.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_types**
> list[CompatibilityDefinition] get_types()

List the data processing items types.

Return the list of <b>dataProcessingItem types</b> and their compatible <b>inputs/outputs types</b>.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DataProcessingItemApi(swagger_client.ApiClient(configuration))

try:
    # List the data processing items types.
    api_response = api_instance.get_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataProcessingItemApi->get_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CompatibilityDefinition]**](CompatibilityDefinition.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dpi**
> DpiId update_dpi(body, version_id, data_processing_id, data_processing_item_id)

Update a data processing item.

Update a data processing item and its inputs and outputs in the specified data processing.<br> An input/output shall be a sourceId/structureId/fieldId.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DataProcessingItemApi(swagger_client.ApiClient(configuration))
body = swagger_client.DpiUpdateBody() # DpiUpdateBody | 
version_id = swagger_client.VersionId() # VersionId | 
data_processing_id = swagger_client.DoubleUuid() # DoubleUuid | 
data_processing_item_id = swagger_client.DoubleUuid() # DoubleUuid | 

try:
    # Update a data processing item.
    api_response = api_instance.update_dpi(body, version_id, data_processing_id, data_processing_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataProcessingItemApi->update_dpi: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DpiUpdateBody**](DpiUpdateBody.md)|  | 
 **version_id** | [**VersionId**](.md)|  | 
 **data_processing_id** | [**DoubleUuid**](.md)|  | 
 **data_processing_item_id** | [**DoubleUuid**](.md)|  | 

### Return type

[**DpiId**](DpiId.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

