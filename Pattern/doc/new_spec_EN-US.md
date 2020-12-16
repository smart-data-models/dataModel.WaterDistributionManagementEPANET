Entity: Pattern  
===============  
This specification is a **temporal version**. It is automatically generated from the  documented properties described in the schema.json condensed into the file `model.yaml`. A temporary `new_model.yaml` file has been created in every data model to avoid impacting into existing scripts. Thus, the specification will be incomplete as long as the schema.json is not updated to the new format (documenting properties). Once updated the `model.yaml` (`new_model.yaml`) needs to be updated as well (automatically) . Further info in this [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). As long as it is a provisional format any [feedback is welcomed in this form](https://smartdatamodels.org/index.php/submit-an-issue-2/) choosing option `Feedback on the new specification`  
Global description: **This entity contains a harmonised description of a generic pattern made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.**  

## List of properties  

- `description`: An optional text that describes other significant information about the junction  - `multipliers`: Multipliers define how some base quantity (e.g., demand) is adjusted for each time period  - `startTime`: The time at which the pattern starts  - `tag`: An optional text string used to assign the pipe to a category, perhaps one based on age or material  - `timeStep`: The time step used for the multipliers. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.  - `type`: NGSI-LD Entity Type. It has to be Pattern    
Required properties  
- `id`  - `multipliers`  - `startTime`  - `timeStep`  - `type`  ## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Pattern:    
  description: 'This entity contains a harmonised description of a generic pattern made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.'    
  properties:    
    description:    
      description: 'An optional text that describes other significant information about the junction'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    multipliers:    
      description: 'Multipliers define how some base quantity (e.g., demand) is adjusted for each time period'    
      items:    
        type: number    
      type: Property    
    startTime:    
      description: 'The time at which the pattern starts'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Time    
    tag:    
      description: 'An optional text string used to assign the pipe to a category, perhaps one based on age or material'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    timeStep:    
      description: 'The time step used for the multipliers. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        units: Second    
    type:    
      description: 'NGSI-LD Entity Type. It has to be Pattern'    
      enum:    
        - Pattern    
      type: Property    
  required:    
    - id    
    - type    
    - multipliers    
    - timeStep    
    - startTime    
  type: object    
```  
</details>    
## Example payloads    
#### Pattern NGSI V2 key-values Example    
Here is an example of a Pattern in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
    "id": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
    "type": "Pattern",  
    "multipliers": [  
        0.5692,  
        0.4647,  
        0.4385,  
        0.3604,  
        0.3098,  
        0.3345  
    ],  
    "timeStep": 3600,  
    "description": "Open Text",  
    "tag": "DMA1"  
}  
```  
#### Pattern NGSI V2 normalized Example    
Here is an example of a Pattern in JSON format as normalized. This is compatible with NGSI V2 when not using options and returns the context data of an individual entity.  
```json  
{  
    "id": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
    "type": "Pattern",  
    "multipliers": {  
        "value": [  
            0.5692,  
            0.4647,  
            0.4385,  
            0.3604,  
            0.3098,  
            0.3345  
        ]  
    },  
    "timeStep": {  
        "value": 3600  
    },  
    "description": {  
        "value": "Open Text"  
    },  
    "tag": {  
        "value": "DMA1"  
    }  
}  
```  
#### Pattern NGSI-LD key-values Example    
Here is an example of a Pattern in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context"],  
 "createdAt": "2020-02-20T17:43:00Z",  
 "description": "Open Text",  
 "id": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
 "modifiedAt": "2020-02-20T17:43:00Z",  
 "multipliers": [0.5692, 0.4647, 0.4385, 0.3604, 0.3098, 0.3345],  
 "startTime": "00:00",  
 "tag": "DMA1",  
 "timeStep": 3600,  
 "type": "Pattern"}  
```  
#### Pattern NGSI-LD normalized Example    
Here is an example of a Pattern in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
    "id": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
    "type": "Pattern",  
    "createdAt": "2020-02-20T17:43:00Z",  
    "modifiedAt": "2020-02-20T17:43:00Z",  
    "multipliers": {  
        "type": "Property",  
        "value": [0.5692, 0.4647, 0.4385, 0.3604, 0.3098, 0.3345],  
        "unitCode":"C62"  
    },  
    "timeStep": {  
        "type": "Property",  
        "value": 3600,  
        "unitCode": "SEC"  
    },  
    "description": {  
        "type": "Property",  
        "value": "Open Text"  
    },  
    "startTime": {  
        "type": "Property",  
        "value": "00:00"  
    },  
    "tag": {  
        "type": "Property",  
        "value": "DMA1"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context"  
    ]  
}  
```  
