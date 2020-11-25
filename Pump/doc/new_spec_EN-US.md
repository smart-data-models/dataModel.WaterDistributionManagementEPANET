Entity: Pump  
============  
This specification is a **temporal version**. It is automatically generated from the  documented properties described in the schema.json condensed into the file `model.yaml`. A temporary `new_model.yaml` file has been created in every data model to avoid impacting into existing scripts. Thus, the specification will be incomplete as long as the schema.json is not updated to the new format (documenting properties). Once updated the `model.yaml` (`new_model.yaml`) needs to be updated as well (automatically) . Further info in this [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). As long as it is a provisional format any [feedback is welcomed in this form](https://smartdatamodels.org/index.php/submit-an-issue-2/) choosing option `Feedback on the new specification`  
Global description: **This entity contains a harmonised description of a generic pump made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.**  

## List of properties  

`efficCurve`:   `endsAt`:   `energyPattern`:   `energyPrice`:   `headCurve`:   `initialStatus`:   `power`:   `pumpPattern`:   `speed`:   `startsAt`:   `status`:   `tag`:   `type`: NGSI-LD Entity Type  `vertices`:   ## Data Model description of properties  
Sorted alphabetically  
```yaml  
Pump:    
  description: 'This entity contains a harmonised description of a generic pump made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.'    
  properties:    
    efficCurve:    
      properties: &pump_-_properties_-_endsat_-_properties    
        createdAt:    
          format: date-time    
          type: string    
        modifiedAt:    
          format: date-time    
          type: string    
        object:    
          format: uri    
          type:    
            - string    
        observedAt:    
          format: date-time    
          type: string    
        type:    
          enum:    
            - Relationship    
          type: string    
      required: &pump_-_properties_-_endsat_-_required    
        - type    
        - object    
      type: object    
    endsAt:    
      properties: *pump_-_properties_-_endsat_-_properties    
      required: *pump_-_properties_-_endsat_-_required    
      type: object    
    energyPattern:    
      properties: *pump_-_properties_-_endsat_-_properties    
      required: *pump_-_properties_-_endsat_-_required    
      type: object    
    energyPrice:    
      properties: &pump_-_properties_-_power_-_properties    
        createdAt:    
          format: date-time    
          type: string    
        modifiedAt:    
          format: date-time    
          type: string    
        observedAt:    
          format: date-time    
          type: string    
        type:    
          enum:    
            - Property    
          type: string    
        unitCode:    
          type: string    
        value:    
          type:    
            - number    
            - string    
            - array    
      required: &pump_-_properties_-_power_-_required    
        - type    
        - value    
      type: object    
    headCurve:    
      properties: *pump_-_properties_-_endsat_-_properties    
      required: *pump_-_properties_-_endsat_-_required    
      type: object    
    initialStatus:    
      properties: &pump_-_properties_-_status_-_properties    
        observedAt:    
          format: date-time    
          type: string    
        type:    
          enum:    
            - Property    
          type: string    
        unitCode:    
          type: string    
        value:    
          enum:    
            - OPEN    
            - CLOSED    
            - CV    
          type:    
            - number    
            - string    
            - array    
      required: &pump_-_properties_-_status_-_required    
        - type    
        - value    
      type: object    
    power:    
      properties: *pump_-_properties_-_power_-_properties    
      required: *pump_-_properties_-_power_-_required    
      type: object    
    pumpPattern:    
      properties: *pump_-_properties_-_endsat_-_properties    
      required: *pump_-_properties_-_endsat_-_required    
      type: object    
    speed:    
      properties: *pump_-_properties_-_power_-_properties    
      required: *pump_-_properties_-_power_-_required    
      type: object    
    startsAt:    
      properties: *pump_-_properties_-_endsat_-_properties    
      required: *pump_-_properties_-_endsat_-_required    
      type: object    
    status:    
      properties: *pump_-_properties_-_status_-_properties    
      required: *pump_-_properties_-_status_-_required    
      type: object    
    tag:    
      properties: *pump_-_properties_-_power_-_properties    
      required: *pump_-_properties_-_power_-_required    
      type: object    
    type:    
      description: 'NGSI-LD Entity Type'    
      enum:    
        - Pump    
      type: string    
    vertices:    
      oneOf:    
        - $id: https://geojson.org/schema/MultiPoint.json    
          $schema: "http://json-schema.org/draft-07/schema#"    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - $id: https://geojson.org/schema/Point.json    
          $schema: "http://json-schema.org/draft-07/schema#"    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
  required:    
    - id    
    - type    
    - initialStatus    
    - startsAt    
    - endsAt    
  type: object    
```  
Here is an example of a Pump in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
    "id": "85zhnf58-0d4c-h4g854g-b7d0-3310klm",  
    "type": "Pump",  
    "initialStatus": "OPEN",  
    "status": "OPEN",  
    "power": 100,  
    "speed": 1.2,  
    "startsAt": "63fe7d79-0d4c-4da9-b7d0-3340efa0656a",  
    "endsAt": "1863179e-3768-4480-9167-ff21f870dd19",  
    "tag": "DMA1",  
    "pumpPattern": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
    "efficCurve": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
    "energyPrice": 0.8,  
    "energyPattern": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
}  
```  
Here is an example of a Pump in JSON format as normalized. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
    "id": "85zhnf58-0d4c-h4g854g-b7d0-3310klm",  
    "type": "Pump",  
    "initialStatus": {  
        "value": "OPEN"  
    },  
    "status": {  
        "value": "OPEN"  
    },  
    "power": {  
        "value": 100  
    },  
    "speed": {  
        "value": 1.2  
    },  
    "startsAt": {  
        "type": "Relationship",  
        "value": "63fe7d79-0d4c-4da9-b7d0-3340efa0656a"  
    },  
    "endsAt": {  
        "type": "Relationship",  
        "value": "1863179e-3768-4480-9167-ff21f870dd19"  
    },  
    "tag": {  
        "value": "DMA1"  
    },  
    "pumpPattern": {  
        "type": "Relationship",  
        "value": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
    },  
    "efficCurve": {  
        "type": "Relationship",  
        "value": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
    },  
    "energyPrice": {  
        "value": 0.8  
    },  
    "energyPattern": {  
        "type": "Relationship",  
        "value": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
    }  
}  
```  
Here is an example of a Pump in JSON-LD format as key-values. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:Pump:85zhnf58-0d4c-h4g854g-b7d0-3310klm",  
  "type": "Pump",  
  "createdAt": "2020-03-02T15:42:00Z",  
  "modifiedAt": "2020-03-02T15:45:00Z",  
  "initialStatus": "OPEN",  
  "status": "OPEN",  
  "power": 100,  
  "speed": 1.2,  
  "startsAt": "urn:ngsi-ld:Junction:63fe7d79-0d4c-4da9-b7d0-3340efa0656a",  
  "endsAt": "urn:ngsi-ld:Reservoir:1863179e-3768-4480-9167-ff21f870dd19",  
  "tag": "DMA1",  
  "pumpPattern": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
  "efficCurve": "urn:ngsi-ld:Curve:fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
  "energyPrice": 0.8,  
  "energyPattern": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/data-models/master/context.jsonld"  
  ]  
}  
```  
Here is an example of a Pump in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
    "id": "urn:ngsi-ld:Pump:85zhnf58-0d4c-h4g854g-b7d0-3310klm",  
    "type": "Pump",  
    "createdAt": "2020-03-02T15:42:00Z",  
    "modifiedAt": "2020-03-02T15:45:00Z",  
    "initialStatus": {  
        "type": "Property",  
        "value": "OPEN"  
    },  
    "status": {  
        "type": "Property",  
        "value": "OPEN"  
    },  
    "power": {  
        "type": "Property",  
        "value": 100,  
        "unitCode": "KWT"  
    },  
    "speed": {  
        "type": "Property",  
        "value": 1.2,  
        "unitCode": "MTS"  
    },  
    "startsAt": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Junction:63fe7d79-0d4c-4da9-b7d0-3340efa0656a"  
    },  
    "endsAt": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Reservoir:1863179e-3768-4480-9167-ff21f870dd19"  
    },  
    "vertices": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "MultiPoint",  
            "coordinates": [  
                [24.40623, 60.17966],  
                [24.50623, 60.27966]  
            ]  
        }  
    },  
    "tag": {  
        "type": "Property",  
        "value": "DMA1"  
    },  
    "pumpPattern":{  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
    },  
    "efficCurve":{  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Curve:fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
    },  
    "energyPrice":{  
        "type": "Property",  
        "value": 0.8,  
        "unitCode": "C62"  
    },  
    "energyPattern":{  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context"  
    ]  
}  
```  
