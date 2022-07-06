# Doorkomst


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entiteitnummer** | **str** | entiteit nummer | 
**lijnnummer** | **int** | lijn nummer | 
**richting** | **str** | richting van de rit | 
**haltenummer** | **str** | halte nummer (key waarde) | 
**dienstregeling_tijdstip** | **datetime** | doorkomsttijdstip volgens de dienstregeling van een rit aan de halte | 
**ritnummer** | **str** |  | [optional] 
**bestemming** | **str** | afgekorte halte naam van de laatste halte van de rit | [optional] 
**vias** | **[str]** | lijst van plaatsen die deze rit bedient als afwijkend t.o.v. de reguliere ritten | [optional] 
**real_time_tijdstip** | **datetime** | real-time doorkomsttijdstip van een rit aan de halte | [optional] [readonly] 
**vrtnum** | **str** | nummer van het voertuig | [optional] 
**prediction_statussen** | **[str]** | lijst van statussen van de meting van de realtime doorkomst | [optional] 
**links** | [**[Link]**](Link.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


