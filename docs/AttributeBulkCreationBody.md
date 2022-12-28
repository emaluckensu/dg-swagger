# AttributeBulkCreationBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**format** | [**AttributeFormats**](AttributeFormats.md) |  | 
**description** | **str** |  | [optional] 
**default_value** | **AnyOfAttributeBulkCreationBodyDefaultValue** |  | [optional] 
**enforce_uniqueness** | **bool** | When set to true, duplicate creations will throw an error | [optional] [default to False]
**time_series_frequency** | [**TimeSeriesFrequency**](TimeSeriesFrequency.md) |  | [optional] 
**time_series_color_rule** | [**TimeSeriesColorRule**](TimeSeriesColorRule.md) |  | [optional] 
**data_type** | [**ModuleNames**](ModuleNames.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

