Entity: Reservoir  
=================  
[Open License](https://github.com/smart-data-models//dataModel.WaterDistributionManagementEPANET/blob/master/Reservoir/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Global description: **This entity contains a harmonised description of a generic Reservoir made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.**  

## List of properties  

- `address`: The mailing address  - `alternateName`: An alternative name for this item  - `areaServed`: The geographic area where a service or offered item is provided  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `elevation`: The elevation above some common reference of the Reservoir. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.  - `hasInlet`: A relationship indicating the water inlet points of the Reservoir  - `hasOutlet`: A relationship indicating the water outlet points of the Reservoir  - `head`: Observed head at the node (junction, tank or reservoir)  - `headPattern`: The ID label of a time pattern used to model time variation in the reservoir's total head  - `id`: Unique identifier of the entity  - `initialQuality`: Initial quality in the network component  - `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name`: The name of this item.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `pressure`: Observed pressure at the node (junction, tank or reservoir)  - `quality`: Observed quality in the network component  - `reservoirHead`: The hydraulic head (elevation + pressure head) of water in the Reservoir. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.  - `seeAlso`: list of uri pointing to additional resources about the item  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `sourceCategory`: Description of the quality of source flow entering the network at a specific node.  - `sourceMassInflow`: Property.. Observed source mass inflow at the node (junction, tank or reservoir)  - `supply`: Observed supply at the node (junction, tank or reservoir)  - `tag`: An optional text string used to assign the pipe to a category, perhaps one based on age or material  - `type`: NGSI-LD Entity Type. It must be equal to Reservoir.    
Required properties  
- `id`  - `location`  - `reservoirHead`  - `type`  ## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Reservoir:    
  description: 'This entity contains a harmonised description of a generic Reservoir made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    elevation:    
      description: 'The elevation above some common reference of the Reservoir. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: Metre    
    hasInlet:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A relationship indicating the water inlet points of the Reservoir'    
      type: Relationship    
    hasOutlet:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A relationship indicating the water outlet points of the Reservoir'    
      type: Relationship    
    head:    
      description: 'Observed head at the node (junction, tank or reservoir)'    
      properties:    
        observedBy:    
          anyOf:    
            - description: 'Property. Identifier format of any NGSI entity'    
              maxLength: 256    
              minLength: 1    
              pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
              type: string    
            - description: 'Property. Identifier format of any NGSI entity'    
              format: uri    
              type: string    
        value:    
          type: number    
      type: Property    
    headPattern:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'The ID label of a time pattern used to model time variation in the reservoir''s total head'    
      type: Relationship    
    id:    
      anyOf: &reservoir_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      type: Property    
    initialQuality:    
      description: 'Initial quality in the network component'    
      properties:    
        observedBy:    
          anyOf:    
            - description: 'Property. Identifier format of any NGSI entity'    
              maxLength: 256    
              minLength: 1    
              pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
              type: string    
            - description: 'Property. Identifier format of any NGSI entity'    
              format: uri    
              type: string    
        value:    
          type: number    
      type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
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
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
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
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *reservoir_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    pressure:    
      description: 'Observed pressure at the node (junction, tank or reservoir)'    
      properties:    
        observedBy:    
          anyOf:    
            - description: 'Property. Identifier format of any NGSI entity'    
              maxLength: 256    
              minLength: 1    
              pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
              type: string    
            - description: 'Property. Identifier format of any NGSI entity'    
              format: uri    
              type: string    
        value:    
          type: number    
      type: Property    
    quality:    
      description: 'Observed quality in the network component'    
      properties:    
        observedBy:    
          anyOf:    
            - description: 'Property. Identifier format of any NGSI entity'    
              maxLength: 256    
              minLength: 1    
              pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
              type: string    
            - description: 'Property. Identifier format of any NGSI entity'    
              format: uri    
              type: string    
        value:    
          type: number    
      type: Property    
    reservoirHead:    
      description: 'The hydraulic head (elevation + pressure head) of water in the Reservoir. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: Metre    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    sourceCategory:    
      description: 'Description of the quality of source flow entering the network at a specific node.'    
      properties:    
        sourcePattern:    
          anyOf:    
            - description: 'Property. Identifier format of any NGSI entity'    
              maxLength: 256    
              minLength: 1    
              pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
              type: string    
            - description: 'Property. Identifier format of any NGSI entity'    
              format: uri    
              type: string    
          description: 'Relationship. A relationship to the pattern pf the sourceCategory property'    
        sourceQuality:    
          description: 'Property. Model:''https://schema.org/Number''. Units: ''mg/L''. Baseline or average concentration (or mass flow rate) of source. A sub-property of the Property ''sourceCategory''. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
          type: number    
        sourceType:    
          description: 'Property. Model:''https://schema.org/Text''. A sub-property of the Property ''sourceCategory'''    
          enum:    
            - CONCEN    
            - MASS    
            - FLOWPACED    
            - SETPOINT    
          type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    sourceMassInflow:    
      description: 'Property.. Observed source mass inflow at the node (junction, tank or reservoir)'    
      properties:    
        observedBy:    
          anyOf:    
            - description: 'Property. Identifier format of any NGSI entity'    
              maxLength: 256    
              minLength: 1    
              pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
              type: string    
            - description: 'Property. Identifier format of any NGSI entity'    
              format: uri    
              type: string    
        value:    
          type: number    
      type: object    
    supply:    
      description: 'Observed supply at the node (junction, tank or reservoir)'    
      properties:    
        observedBy:    
          anyOf:    
            - description: 'Property. Identifier format of any NGSI entity'    
              maxLength: 256    
              minLength: 1    
              pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
              type: string    
            - description: 'Property. Identifier format of any NGSI entity'    
              format: uri    
              type: string    
        value:    
          type: number    
      type: Property    
    tag:    
      description: 'An optional text string used to assign the pipe to a category, perhaps one based on age or material'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    type:    
      description: 'NGSI-LD Entity Type. It must be equal to Reservoir.'    
      enum:    
        - Reservoir    
      type: Property    
  required:    
    - id    
    - type    
    - location    
    - reservoirHead    
  type: object    
```  
</details>    
## Example payloads    
#### Reservoir NGSI-v2 key-values Example    
Here is an example of a Reservoir in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "1863179e-3768-4480-9167-ff21f870dd19",  
  "type": "Reservoir",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      24.30623,  
      60.07966  
    ]  
  },  
  "reservoirHead": 59.00,  
  "headPattern": "fbcb5fc8-8ca3-4533",  
  "elevation": 105.8,  
  "description": "This entity contains a harmonised description of a Reservoir",  
  "initialQuality": {  
    "value": 0.5  
  },  
  "sourceCategory": {  
    "value": "CategroyX",  
    "sourceType": "MASS",  
    "sourceQuality": 1.2,  
    "sourcePattern": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
  },  
  "tag": "DMA1"  
}  
```  
#### Reservoir NGSI-v2 normalized Example    
Here is an example of a Reservoir in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "1863179e-3768-4480-9167-ff21f870dd19",  
  "type": "Reservoir",  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        24.30623,  
        60.07966  
      ]  
    }  
  },  
  "reservoirHead": {  
    "type": "Number",  
    "value": 59.00  
  },  
  "headPattern": {  
    "type": "Relationship",  
    "object": "fbcb5fc8-8ca3-4533"  
  },  
  "elevation": {  
    "type": "Number",  
    "value": 105.8  
  },  
  "description": {  
    "type": "Text",  
    "value": "This entity contains a harmonised description of a Reservoir"  
  },  
  "initialQuality": {  
    "type": "Number",  
    "value": 0.5  
  },  
  "sourceCategory": {  
    "type": "object",  
    "value": {  
      "value": "CategoryX",  
      "sourceType": "MASS",  
      "sourceQuality": 1.2,  
      "sourcePattern": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
    }  
  },  
  "tag": {  
    "type": "Text",  
    "value": "DMA1"  
  },  
  "pressure": {  
    "type": "object",  
    "value": {  
      "value": 20,  
      "observedBy": "device-9845A"  
    }  
  },  
  "supply": {  
    "type": "object",  
    "value": {  
      "value": 150,  
      "observedBy": "device-9845A"  
    }  
  },  
  "head": {  
    "type": "object",  
    "value": {  
      "value": 20,  
      "observedBy": "device-9845A"  
    }  
  },  
  "quality": {  
    "type": "object",  
    "value": {  
      "value": 0.5,  
      "observedBy": "device-9845A"  
    }  
  },  
  "sourceMassInflow": {  
    "type": "object",  
    "value": {  
      "value": 100,  
      "observedBy": "device-9845A"  
    }  
  }  
}  
```  
#### Reservoir NGSI-LD key-values Example    
Here is an example of a Reservoir in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ],  
  "createdAt": "2020-03-02T15:42:00Z",  
  "description": "This entity contains a harmonised description of a Reservoir",  
  "elevation": 105.8,  
  "headPattern": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533",  
  "id": "urn:ngsi-ld:Reservoir:1863179e-3768-4480-9167-ff21f870dd19",  
  "initialQuality": 0.5,  
  "location": {  
    "coordinates": [  
      24.30623,  
      60.07966  
    ],  
    "type": "Point"  
  },  
  "modifiedAt": "2020-03-02T15:45:00Z",  
  "reservoirHead": 59.0,  
  "sourceCategory": "CategroyX",  
  "tag": "DMA1",  
  "type": "Reservoir"  
}  
```  
#### Reservoir NGSI-LD normalized Example    
Here is an example of a Reservoir in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:Reservoir:1863179e-3768-4480-9167-ff21f870dd19",  
  "type": "Reservoir",  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        24.30623,  
        60.07966  
      ]  
    }  
  },  
  "reservoirHead": {  
    "type": "Property",  
    "value": 59.0,  
    "unitCode": "MTR"  
  },  
  "headPattern": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533"  
  },  
  "elevation": {  
    "type": "Property",  
    "value": 105.8,  
    "unitCode": "MTR"  
  },  
  "description": {  
    "type": "Property",  
    "value": "This entity contains a harmonised description of a Reservoir"  
  },  
  "initialQuality": {  
    "type": "Property",  
    "value": 0.5,  
    "unitCode": "M1"  
  },  
  "sourceCategory": {  
    "type": "Property",  
    "value": {  
      "type": "Property",  
      "value": "CategoryX"  
    },  
    "sourceType": {  
      "type": "Property",  
      "value": "MASS"  
    },  
    "sourceQuality": {  
      "type": "Property",  
      "value": 1.2,  
      "unitCode": "M1"  
    },  
    "sourcePattern": {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
    }  
  },  
  "tag": {  
    "type": "Property",  
    "value": "DMA1"  
  },  
  "pressure": {  
    "type": "Property",  
    "value": {  
      "type": "Property",  
      "value": 20,  
      "unitCode": "MTR"  
    },  
    "observedBy": {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:Device:device-9845A"  
    }  
  },  
  "supply": {  
    "type": "Property",  
    "value": {  
      "type": "Property",  
      "value": 150,  
      "unitCode": "LTR"  
    },  
    "observedBy": {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:Device:device-9845A"  
    }  
  },  
  "head": {  
    "type": "Property",  
    "value": {  
      "type": "Property",  
      "value": 20,  
      "unitCode": "MTR"  
    },  
    "observedBy": {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:Device:device-9845A"  
    }  
  },  
  "quality": {  
    "type": "Property",  
    "value": {  
      "type": "Property",  
      "value": 0.5,  
      "unitCode": "M1"  
    },  
    "observedBy": {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:Device:device-9845A"  
    }  
  },  
  "sourceMassInflow": {  
    "type": "Property",  
    "value": {  
      "type": "Property",  
      "value": 100,  
      "unitCode": "F27"  
    },  
    "observedBy": {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:Device:device-9845A"  
    }  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
