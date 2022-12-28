# Team

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Team name | 
**description** | **str** | A short description of the team motivations | [optional] 
**email** | **str** | The team email will be used to notify all members | [optional] 
**access** | [**AccessType**](AccessType.md) |  | 
**id** | [**TeamId**](TeamId.md) |  | 
**icon_hash** | **str** | Hash associated to the Team&#x27;s icon. Use it with the &lt;a href&#x3D;\&quot;/v2/documentation#tag/Image/operation/GetImage\&quot;&gt;&lt;code&gt;GET /image&lt;/code&gt; endpoint&lt;/a&gt; to fetch the icon binaries. | 
**owners** | [**list[Email]**](Email.md) | Team owner&#x27;s email | 
**members_count** | **float** | Total count of members, including the owner(s). | 
**members** | [**list[TeamMember]**](TeamMember.md) | List of users that are part of the team | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

