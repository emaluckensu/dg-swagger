# swagger_client.SearchApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search**](SearchApi.md#search) | **POST** /search | Search DataGalaxy objects

# **search**
> SearchResponse search(body)

Search DataGalaxy objects

Search DataGalaxy objects with queries and filters <br>  <h3>Exact Matches</h3> An exact match occure when your <code>query</code> perfectly matches an object's text attribute value.<br>  <h4>Exact match requirements</h4> Attributes have to be indexed for exact match.  <h4>Finding exact matches in the search result</h4>  Exact matches can be determined using the <code>isExactMatch</code> boolean (<code>result.entities[n].isExactMatch</code>).<br> Each search result returned carries this flag.<br>  <h3>Filters</h3> Filters help you refine your search.<br> They are applied to object's attribute values.<br><br> Here is an array documenting which attribute types you can filter and what operators you can use on them:<br>   |              Attribute type              |                                                                                                                  Compatible filter operators                                                                                                                 |  |:----------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|  |             Text, Hyperlink, FormattedText |                                                                                            `contains`, `equals`, `startsWith`, `endsWith`, `isEmpty`, `isNotEmpty`                                                                                           |  |                  Boolean                 |                                                                                                                           `equals`                                                                                                                           |  |         Number, TimeSeriesObject         |                                                                  `equals`, `greaterThan`, `lowerThan`, `greaterOrEqualTo`, `lowerThan`, `lowerOrEqualTo`,  `range`, `isEmpty`, `isNotEmpty`                                                                  |  |                   Date                   | `contains`, `pastHour`, `today`, `yesterday`, `currentWeek`, `pastWeek`,  `beforeCurrentWeek`, `beforePastWeek`, `currentMonth`, `pastMonth`, `beforeCurrentMonth`, `beforePastMonth`,  `bedoreToday`, `currentYear`, `last365days`, `isEmpty`, `isNotEmpty` |  |                 ValueList                |                                                                                                               `contains`, `excludes`, `equals`                                                                                                               |  | MultiValueList, Hierarchy, Person, User, ManagedTags  |                                                                                                  `contains`, `isEmpty`, `isNotEmpty`, `matchAll`, `excludes`                                                                                                 |                                                                                                 `contains`, `isEmpty`, `isNotEmpty`, `matchAll`, `excludes`                                                                                                 |

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
body = swagger_client.SearchBody() # SearchBody | 

try:
    # Search DataGalaxy objects
    api_response = api_instance.search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchBody**](SearchBody.md)|  | 

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [IntegrationToken](../README.md#IntegrationToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

