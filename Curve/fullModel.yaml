
Entity: Curve
=============
  
  
Global description: **This entity contains a harmonised description of a generic curve made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.**
## Data Model description of properties


```<br>Ordered alphabetically
Curve:
  description: 'This entity contains a harmonised description of a generic curve made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.'
  properties:
    curveType:
      properties:
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
          enum:
            - FLOW-HEAD
            - FLOW-EFFICIENCY
            - FLOW-HEADLOSS
            - LEVEL-VOLUME
          type:
            - number
            - string
            - array
      required:
        - type
        - value
      type: object
    description:
      properties: &curve_-_properties_-_tag_-_properties
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
      required: &curve_-_properties_-_tag_-_required
        - type
        - value
      type: object
    tag:
      properties: *curve_-_properties_-_tag_-_properties
      required: *curve_-_properties_-_tag_-_required
      type: object
    type:
      description: 'NGSI-LD Entity Type. It must be equal to Curve.'
      enum:
        - Curve
      type: Property
    xData:
      properties: *curve_-_properties_-_tag_-_properties
      required: *curve_-_properties_-_tag_-_required
      type: object
    yData:
      properties: *curve_-_properties_-_tag_-_properties
      required: *curve_-_properties_-_tag_-_required
      type: object
  required:
    - id
    - type
    - curveType
    - xData
    - yData
  type: object
```

## Examples
NGSI V2 key-values Example
```json
{
  "id": "fAM-8ca3-4533-a2eb-12015",
  "type": "Curve",
  "curveType": {
    "type": "Property",
    "value": "FLOW-HEAD"
  },
  "xData": {
    "type": "Property",
    "value": [
      0.5692,
      0.4647
    ]
  },
  "yData": {
    "type": "Property",
    "value": [
      0.5692,
      0.4647
    ]
  },
  "description": {
    "type": "Property",
    "value": "Free Text"
  },
  "tag": {
    "type": "Property",
    "value": "DMA1"
  }
}
```
NGSI V2 normalized Example
```json
{
    "id": "fAM-8ca3-4533-a2eb-12015",
    "type": "Curve",
    "dateCreated": {
        "type": "DateTime",
        "value": "2020-02-16T17:43:00Z"
    },
    "dateModified": {
        "type": "DateTime",
        "value": "2020-02-16T17:43:00Z"
    },
    "curveType": {
        "value": "FLOW-HEAD"
    },
    "xData": {
        "value": [
            0.5692,
            0.4647
        ]
    },
    "yData": {
        "value": [
            0.5692,
            0.4647
        ]
    },
    "description": {
        "value": "Free Text"
    },
    "tag": {
        "value": "DMA1"
    }
}
```
NGSI-LD key-values Example
```json
{
  "@context": [
    "https://schema.lab.fiware.org/ld/context"
  ],
  "id": "fAM-8ca3-4533-a2eb-12015",
  "type": "Curve",
  "curveType": {
    "type": "Property",
    "value": "FLOW-HEAD"
  },
  "xData": {
    "type": "Property",
    "value": [
      0.5692,
      0.4647
    ]
  },
  "yData": {
    "type": "Property",
    "value": [
      0.5692,
      0.4647
    ]
  },
  "description": {
    "type": "Property",
    "value": "Free Text"
  },
  "tag": {
    "type": "Property",
    "value": "DMA1"
  }
}
```
NGSI-LD normalized Example
```json
{
    "id": "urn:ngsi-ld:Curve:fAM-8ca3-4533-a2eb-12015",
    "type": "Curve",
    "createdAt": "2020-02-16T17:43:00Z",
    "modifiedAt": "2020-02-16T17:43:00Z",
    "curveType":{
        "type": "Property",
        "value": "FLOW-HEAD"
    },
    "xData": {
        "type": "Property",
        "value": [0.5692, 0.4647],
        "unitCode":"C62"
    },
    "yData": {
        "type": "Property",
        "value": [0.5692, 0.4647],
        "unitCode":"C62"
    },
    "description": {
        "type": "Property",
        "value": "Free Text"
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
