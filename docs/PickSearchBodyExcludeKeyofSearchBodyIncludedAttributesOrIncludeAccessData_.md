# PickSearchBodyExcludeKeyofSearchBodyIncludedAttributesOrIncludeAccessData_

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | [**SearchQuery**](SearchQuery.md) |  | [optional] 
**version_id** | **str** | Version to search in. &lt;br&gt;  If &#x60;versionId&#x60; is not provided, the search scope will be extended to all the workspaces you have access to. | [optional] 
**limit** | **float** | Maximum number of objects returned | [optional] [default to 50]
**filters** | [**list[SearchFilter]**](SearchFilter.md) | Use filters to refines your search result | [optional] 
**save_search_payload** | **bool** | If set to &lt;code&gt;true&lt;/code&gt;, the search payload will be saved in the &lt;b&gt;queries history&lt;/b&gt;.\\ Request the &lt;code&gt;GET /history/search/queries&lt;/code&gt; to retrieve it. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

