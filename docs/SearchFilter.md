# SearchFilter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_key** | **str** | AttributeKey you want your filter to be applied on. AttributeKeys can be found with the &#x60;GET /attributes&#x60; endpoint | 
**operator** | [**SearchFilterOperator**](SearchFilterOperator.md) |  | 
**values** | **AnyOfSearchFilterValues** | Values to be filtered.&lt;br&gt; Filters on attributes referencing users (User, Person) or tags (ManagedTags, ClientTags) expect their values to be arrays of ids (stringified Uuid)&lt;br&gt;  User ids can be found with &#x60;GET /users&#x60;, and other attribute ids with &#x60;GET /attributes/values&#x60; | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

