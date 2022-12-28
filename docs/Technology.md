# Technology

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | 
**technology_code** | **str** | This code is the technology&#x27;s identifier | 
**modules** | [**list[TechnologyModule]**](TechnologyModule.md) | Modules where technology is available | 
**description** | **str** | Technology description | 
**image_hash** | **str** | Use this hash to fetch the technology&#x27;s image with the &#x60;GET /image?hash&#x3D;{hash}&#x60; endpoint | 
**thumbnail_hash** | **str** | Use this hash to fetch the technology&#x27;s thumbnail with the &#x60;GET /image?hash&#x3D;{hash}&#x60; endpoint | 
**svg_image_hash** | **str** | Use this hash to fetch the technology&#x27;s svg with the &#x60;GET /image?hash&#x3D;{hash}&#x60; endpoint | 
**creation_time** | **str** |  | 
**creation_user_id** | [**Uuid**](Uuid.md) |  | 
**last_modification_time** | **str** |  | [optional] 
**last_modification_user_id** | [**Uuid**](Uuid.md) |  | [optional] 
**last_usage_time** | **str** |  | [optional] 
**last_usage_user_id** | [**Uuid**](Uuid.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

