# kensu_datagalaxy_client.FilteredViewsApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_filtered_view**](FilteredViewsApi.md#get_filtered_view) | **GET** /filteredViews/{filteredViewId} | Fetch FilteredView

# **get_filtered_view**
> FilteredView get_filtered_view(filtered_view_id)

Fetch FilteredView

This endpoint returns the details of a FilteredView. These objects are a set of search filters saved by a user.<br> Filters found in FilteredViews can be passed to enpoint `POST /search` body.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.FilteredViewsApi(kensu_datagalaxy_client.ApiClient(configuration))
filtered_view_id = 1.2 # float | 

try:
    # Fetch FilteredView
    api_response = api_instance.get_filtered_view(filtered_view_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilteredViewsApi->get_filtered_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filtered_view_id** | **float**|  | 

### Return type

[**FilteredView**](FilteredView.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

