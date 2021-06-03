Entity: Tank  
============  
[Open License](https://github.com/smart-data-models//dataModel.WaterDistributionManagementEPANET/blob/master/Tank/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Global description: **This entity contains a harmonised description of a generic tank made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.**  

## List of properties  

- `address`: The mailing address  - `alternateName`: An alternative name for this item  - `areaServed`: The geographic area where a service or offered item is provided  - `bulkReactionCoefficient`: The bulk reaction coefficient used for modelling reactions in the tank. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `elevation`: The elevation above some common reference of the Tank. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.  - `hasInlet`: A relationship indicating the water inlet points of the Reservoir  - `hasOutlet`: A relationship indicating the water outlet points of the Reservoir  - `head`: Observed head at the node (junction, tank or reservoir)  - `id`: Unique identifier of the entity  - `initLevel`: The height of the water surface above the bottom elevation of the tank at the start of the simulation. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.  - `initialQuality`: Water quality level in the tank at the start of the simulation. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.  - `level`: Observed level in the element of the network  - `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `maxLevel`: The height of the water surface above the bottom elevation of the tank at the start of the simulation. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.  - `minLevel`: The minimum level that water in the tank can drop to. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.  - `minVolume`: The volume of water in the tank when it is at its minimum level. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.  - `mixingFraction`: The fraction of the tank's total volume that comprises the inlet-outlet compartment of the two-compartment (2COMP) mixing model. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.  - `mixingModel`: A sub-property of the Property sourceCategory. Enum:'2COMP, FIFO, LIFO, MIXED'  - `name`: The name of this item.  - `nominalDiameter`: The diameter of the tank. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `pressure`: Observed pressure at the node (junction, tank or reservoir)  - `quality`: Observed quality in the network component  - `seeAlso`: list of uri pointing to additional resources about the item  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `sourceCategory`: Description of the quality of source flow entering the network at a specific node.  - `sourceMassInflow`: Property.. Observed source mass inflow at the node (junction, tank or reservoir)  - `supply`: Observed supply at the node (junction, tank or reservoir)  - `tag`: An optional text string used to assign the pipe to a category, perhaps one based on age or material  - `type`: NGSI-LD Entity Type. It has to be Tank  - `volumeCurve`: The ID label of a curve used to describe the relation between tank volume and water level    
Required properties  
- `id`  - `location`  - `type`  ## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Tank:    
  description: 'This entity contains a harmonised description of a generic tank made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.'    
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
    bulkReactionCoefficient:    
      description: 'The bulk reaction coefficient used for modelling reactions in the tank. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 1/day    
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
      description: 'The elevation above some common reference of the Tank. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: metre    
    hasInlet:    
      description: 'A relationship indicating the water inlet points of the Reservoir'    
      format: uri    
      type: Relationship    
    hasOutlet:    
      description: 'A relationship indicating the water outlet points of the Reservoir'    
      format: uri    
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
    id:    
      anyOf: &tank_-_properties_-_owner_-_items_-_anyof    
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
    initLevel:    
      description: 'The height of the water surface above the bottom elevation of the tank at the start of the simulation. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: metre    
    initialQuality:    
      description: 'Water quality level in the tank at the start of the simulation. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: mg/L    
    level:    
      description: 'Observed level in the element of the network'    
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
    maxLevel:    
      description: 'The height of the water surface above the bottom elevation of the tank at the start of the simulation. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: metre    
    minLevel:    
      description: 'The minimum level that water in the tank can drop to. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: metre    
    minVolume:    
      description: 'The volume of water in the tank when it is at its minimum level. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'cubic metre'    
    mixingFraction:    
      description: 'The fraction of the tank''s total volume that comprises the inlet-outlet compartment of the two-compartment (2COMP) mixing model. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'No unit'    
    mixingModel:    
      description: 'A sub-property of the Property sourceCategory. Enum:''2COMP, FIFO, LIFO, MIXED'''    
      enum:    
        - 2COMP    
        - FIFO    
        - LIFO    
        - MIXED    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    name:    
      description: 'The name of this item.'    
      type: Property    
    nominalDiameter:    
      description: 'The diameter of the tank. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: Metre    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *tank_-_properties_-_owner_-_items_-_anyof    
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
      description: 'NGSI-LD Entity Type. It has to be Tank'    
      enum:    
        - Tank    
      type: Property    
    volumeCurve:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'The ID label of a curve used to describe the relation between tank volume and water level'    
      type: Relationship    
  required:    
    - id    
    - type    
    - location    
  type: object    
```  
</details>    
## Example payloads    
#### Tank NGSI-v2 key-values Example    
Here is an example of a Tank in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
    "id": "1863179e-3968-4493-9167-ee21f880cc02",  
    "type": "Tank",  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            24.30623,  
            60.07966  
        ]  
    },  
    "elevation": 112.9,  
    "initLevel": 3,  
    "minLevel": 0,  
    "maxLevel": 6.75,  
    "minVolume": 0,  
    "nominalDiameter": 13.73,  
    "description": "Free Text",  
    "initialQuality": 0.5,  
    "sourceCategory": {  
        "value": "category1",  
        "sourceType": "MASS",  
        "sourceQuality": 1.2,  
        "sourcePattern": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
    },  
    "mixingModel": "MIXED",  
    "volumeCurve": "fAM-8ca3-4533-a2eb-12015",  
    "mixingFraction": 0.7,  
    "bulkReactionCoefficient": 0.7,  
    "tag": "DMA1"  
}  
```  
#### Tank NGSI-v2 normalized Example    
Here is an example of a Tank in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "1863179e-3968-4493-9167-ee21f880cc02",  
  "type": "Tank",  
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
  "elevation": {  
    "type": "Number",  
    "value": 112.9  
  },  
  "initLevel": {  
    "type": "Number",  
    "value": 3  
  },  
  "minLevel": {  
    "type": "Number",  
    "value": 0  
  },  
  "maxLevel": {  
    "type": "Number",  
    "value": 6.75  
  },  
  "minVolume": {  
    "type": "Number",  
    "value": 0  
  },  
  "nominalDiameter": {  
    "type": "Number",  
    "value": 13.73  
  },  
  "description": {  
    "type": "Text",  
    "value": "Free Text"  
  },  
  "initialQuality": {  
    "type": "Number",  
    "value": 0.5  
  },  
  "sourceCategory": {  
    "type": "object",  
    "value": {  
      "value": "category1",  
      "sourceType": "MASS",  
      "sourceQuality": 1.2,  
      "sourcePattern": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
    }  
  },  
  "mixingModel": {  
    "type": "Text",  
    "value": "MIXED"  
  },  
  "volumeCurve": {  
    "type": "Relationship",  
    "value": "fAM-8ca3-4533-a2eb-12015"  
  },  
  "mixingFraction": {  
    "type": "Number",  
    "value": 0.7  
  },  
  "bulkReactionCoefficient": {  
    "type": "Number",  
    "value": 0.7  
  },  
  "tag": {  
    "type": "Text",  
    "value": "DMA1"  
  },  
  "level": {  
    "type": "object",  
    "value": {  
      "value": 20,  
      "observedBy": "device-9845A"  
    }  
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
#### Tank NGSI-LD key-values Example    
Here is an example of a Tank in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ],  
  "bulkReactionCoefficient": 0.7,  
  "createdAt": "2020-03-13T15:42:00Z",  
  "description": "Free Text",  
  "elevation": 112.9,  
  "id": "urn:ngsi-ld:Tank:1863179e-3968-4493-9167-ee21f880cc02",  
  "initLevel": 3,  
  "initialQuality": 0.5,  
  "location": {  
    "coordinates": [  
      24.30623,  
      60.07966  
    ],  
    "type": "Point"  
  },  
  "maxLevel": 6.75,  
  "minLevel": 0,  
  "minVolume": 0,  
  "mixingFraction": 0.7,  
  "mixingModel": "MIXED",  
  "modifiedAt": "2020-03-13T15:45:00Z",  
  "nominalDiameter": 13.73,  
  "sourceCategory": "category1",  
  "tag": "DMA1",  
  "type": "Tank",  
  "volumeCurve": "urn:ngsi-ld:Curve:fAM-8ca3-4533-a2eb-12015"  
}  
```  
#### Tank NGSI-LD normalized Example    
Here is an example of a Tank in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:Tank:1863179e-3968-4493-9167-ee21f880cc02",  
  "type": "Tank",  
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
  "elevation": {  
    "type": "Property",  
    "value": 112.9,  
    "unitCode": "MTR"  
  },  
  "initLevel": {  
    "type": "Property",  
    "value": 3,  
    "unitCode": "MTR"  
  },  
  "minLevel": {  
    "type": "Property",  
    "value": 0,  
    "unitCode": "MTR"  
  },  
  "maxLevel": {  
    "type": "Property",  
    "value": 6.75,  
    "unitCode": "MTR"  
  },  
  "minVolume": {  
    "type": "Property",  
    "value": 0,  
    "unitCode": "MTQ"  
  },  
  "nominalDiameter": {  
    "type": "Property",  
    "value": 13.73,  
    "unitCode": "MTR"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Free Text"  
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
      "value": "category1"  
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
  "mixingModel": {  
    "type": "Property",  
    "value": "MIXED"  
  },  
  "volumeCurve": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Curve:fAM-8ca3-4533-a2eb-12015"  
  },  
  "mixingFraction": {  
    "type": "Property",  
    "value": 0.7,  
    "unitCode": "C62"  
  },  
  "bulkReactionCoefficient": {  
    "type": "Property",  
    "value": 0.7,  
    "unitCode": "E91"  
  },  
  "tag": {  
    "type": "Property",  
    "value": "DMA1"  
  },  
  "level": {  
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
