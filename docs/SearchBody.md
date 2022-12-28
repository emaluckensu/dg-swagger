# SearchBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | [**SearchQuery**](SearchQuery.md) |  | [optional] 
**version_id** | **str** | Version to search in. &lt;br&gt;  If &#x60;versionId&#x60; is not provided, the search scope will be extended to all the workspaces you have access to. | [optional] 
**limit** | **object** | Maximum number of objects returned | [optional] 
**included_attributes** | **list[str]** | List of attributes, identified by their &lt;code&gt;attributeKey&lt;/code&gt; or &lt;code&gt;attributePath&lt;/code&gt;, to be returned in the search result  In case of an attribute linked to a dataType, &lt;code&gt;attributePath&lt;/code&gt; should be used | [optional] 
**include_access_data** | **bool** | If set to &lt;code&gt;true&lt;/code&gt;, returns access rights the current token has on each item | [optional] 
**filters** | [**list[SearchFilter]**](SearchFilter.md) | Use filters to refines your search result | [optional] 
**save_search_payload** | **object** | If set to &lt;code&gt;true&lt;/code&gt;, the search payload will be saved in the &lt;b&gt;queries history&lt;/b&gt;.\\ Request the &lt;code&gt;GET /history/search/queries&lt;/code&gt; to retrieve it. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

