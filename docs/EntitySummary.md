# EntitySummary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**DoubleUuid**](DoubleUuid.md) |  | 
**name** | **str** | Entity functional name | 
**technical_name** | **str** | Entity technical name | [optional] 
**type** | **str** | Entity type | 
**data_type** | **str** | Entity dataType | 
**version_id** | [**VersionId**](VersionId.md) |  | 
**path** | **str** | Path to entity. Composed of entity&#x27;s parents technical names | 
**type_path** | **str** | Path to entity. Composed of entity&#x27;s parents types | 
**location** | [**ObjectLocation**](ObjectLocation.md) |  | 
**object_url** | **str** | Object URL in DataGalaxy&#x27;s web application | 
**children_count** | **float** | Total number of descendants the current entity has | [optional] 
**access_data** | [**AccessData**](AccessData.md) |  | [optional] 
**attributes** | [**EntityAttributes**](EntityAttributes.md) |  | [optional] 
**links** | [**LinkedEntities**](LinkedEntities.md) |  | [optional] 
**parent** | [**EntityBase**](EntityBase.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

