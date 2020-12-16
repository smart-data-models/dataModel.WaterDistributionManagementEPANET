Entity: Pump  
============  
[Open License](https://github.com/smart-data-models//dataModel.WaterNetworkManagement/blob/master/Pump/LICENSE.md)  
Global description: **This entity contains a harmonised description of a generic pump made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.**  

## List of properties  

- `description`: An optional text that describes other significant information about the junction  - `efficCurve`: The ID label of the curve that represents the pump's wire-to-water efficiency as a function of flow rate.  - `endsAt`: The ID of the node on the discharge side of the pump  - `energyPattern`: The ID label of the time pattern used to describe the variation in energy price throughout the day.  - `energyPrice`: The average or nominal price of energy in monetary units. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.  - `headCurve`: The ID label of the pump curve used to describe the relationship between the head delivered by the pump and the flow through the Pump.  - `initialStatus`: The node status at the start of the simulation.  - `power`: The power supplied by the pump. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.  - `pumpPattern`: The ID label of a time pattern used to control the pump's operation. The multipliers of the pattern are equivalent to speed settings. A multiplier of zero implies that the pump will be shut off during the corresponding time period  - `speed`: The relative speed setting of the Pump. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.  - `startsAt`: The ID of the node on the suction side of the pump  - `status`: The dynamic state of the node  - `tag`: An optional text string used to assign the pipe to a category, perhaps one based on age or material  - `type`: NGSI-LD Entity Type. It must be equal to Pump.  - `vertices`: Coordinates of all vertices in the pump, ordered from the startsAt node to the endsAt node and encoded as a GeoJSON     
Required properties  
- `endsAt`  - `id`  - `initialStatus`  - `startsAt`  - `type`  ## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Pump:    
  description: 'This entity contains a harmonised description of a generic pump made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.'    
  properties:    
    description:    
      description: 'An optional text that describes other significant information about the junction'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    efficCurve:    
      description: 'The ID label of the curve that represents the pump''s wire-to-water efficiency as a function of flow rate.'    
      format: uri    
      type: Relationship    
    endsAt:    
      description: 'The ID of the node on the discharge side of the pump'    
      format: uri    
      type: Relationship    
    energyPattern:    
      description: 'The ID label of the time pattern used to describe the variation in energy price throughout the day.'    
      format: uri    
      type: Relationship    
    energyPrice:    
      description: 'The average or nominal price of energy in monetary units. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        units: 'No unit'    
    headCurve:    
      description: 'The ID label of the pump curve used to describe the relationship between the head delivered by the pump and the flow through the Pump.'    
      format: uri    
      type: Relationship    
    initialStatus:    
      description: 'The node status at the start of the simulation.'    
      enum:    
        - OPEN    
        - CLOSED    
        - CV    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    power:    
      description: 'The power supplied by the pump. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: KiloWatt    
    pumpPattern:    
      description: 'The ID label of a time pattern used to control the pump''s operation. The multipliers of the pattern are equivalent to speed settings. A multiplier of zero implies that the pump will be shut off during the corresponding time period'    
      format: uri    
      type: Relationship    
    speed:    
      description: 'The relative speed setting of the Pump. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'Metre per Second'    
    startsAt:    
      description: 'The ID of the node on the suction side of the pump'    
      format: uri    
      type: Relationship    
    status:    
      description: 'The dynamic state of the node'    
      enum:    
        - OPEN    
        - CLOSED    
        - CV    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    tag:    
      description: 'An optional text string used to assign the pipe to a category, perhaps one based on age or material'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    type:    
      description: 'NGSI-LD Entity Type. It must be equal to Pump.'    
      enum:    
        - Pump    
      type: Property    
    vertices:    
      description: 'Coordinates of all vertices in the pump, ordered from the startsAt node to the endsAt node and encoded as a GeoJSON '    
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
      type: Geoproperty    
  required:    
    - id    
    - type    
    - initialStatus    
    - startsAt    
    - endsAt    
  type: object    
```  
</details>    
## Example payloads    
#### Pump NGSI V2 key-values Example    
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
#### Pump NGSI V2 normalized Example    
Here is an example of a Pump in JSON format as normalized. This is compatible with NGSI V2 when not using options and returns the context data of an individual entity.  
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
#### Pump NGSI-LD key-values Example    
Here is an example of a Pump in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### Pump NGSI-LD normalized Example    
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
