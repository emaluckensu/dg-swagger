# kensu_datagalaxy_client.LicensesApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_licences_list**](LicensesApi.md#get_licences_list) | **GET** /licenses | Return the list of licences owned by your account.

# **get_licences_list**
> LicenseList get_licences_list(assigned=assigned, license_level=license_level)

Return the list of licences owned by your account.

Return the list of <b>licenses</b> owned by your account. <br> Licenses are <b>grouped by license pools</b>.<br><br>  This route's response payload has a <code>licenses</code> field which contains an <i>array of objects</i>. <br> By default, objects found in this array can represent 2 things:  - assigned licenses. These objects have an <code>associateUser</code> field, it displays which user is associated to which license pool. - license pools. These objects have a boolean field <code>isLicensePool: true</code> and a number field <code>availableLicenses: <i>n</i></code>.<br>  In order to assign a license to a user and link them to a license pool, request <code>PUT /users/{userId}</code> and update their <code>licenseId</code> field with  one of your license pools <code>licenseId</code>.

### Example
```python
from __future__ import print_function
import time
import kensu_datagalaxy_client
from kensu_datagalaxy_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = kensu_datagalaxy_client.LicensesApi(kensu_datagalaxy_client.ApiClient(configuration))
assigned = true # bool |  (optional)
license_level = kensu_datagalaxy_client.LicenseLevel() # LicenseLevel |  (optional)

try:
    # Return the list of licences owned by your account.
    api_response = api_instance.get_licences_list(assigned=assigned, license_level=license_level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicensesApi->get_licences_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assigned** | **bool**|  | [optional] 
 **license_level** | [**LicenseLevel**](.md)|  | [optional] 

### Return type

[**LicenseList**](LicenseList.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

