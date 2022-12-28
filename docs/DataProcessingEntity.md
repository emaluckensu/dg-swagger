# DataProcessingEntity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Entity functional name | 
**technical_name** | **str** | Entity technical name | 
**type** | **str** | Entity type | 
**id** | [**DoubleUuid**](DoubleUuid.md) |  | 
**version_id** | [**VersionId**](VersionId.md) |  | 
**path** | **str** | Path to entity. Composed of entity&#x27;s parents technical names | 
**type_path** | **str** | Path to entity. Composed of entity&#x27;s parents types | 
**object_url** | **str** | Object URL in DataGalaxy&#x27;s web application | 
**children_count** | **float** | Total number of descendants the current entity has | [optional] 
**attributes** | [**EntityAttributes**](EntityAttributes.md) |  | 
**dp_items** | [**list[DpiData]**](DpiData.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

