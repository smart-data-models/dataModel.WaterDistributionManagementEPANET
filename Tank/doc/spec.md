<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: Tank  
============<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.WaterDistributionManagementEPANET/blob/master/Tank/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **This entity contains a harmonised description of a generic tank made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `bulkReactionCoefficient[number]`: The bulk reaction coefficient used for modelling reactions in the tank. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated[string]`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified[string]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description[string]`: A description of this item  - `elevation[number]`: The elevation above some common reference of the Tank. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.  . Model: [https://schema.org/Number](https://schema.org/Number)- `hasInlet[string]`: A relationship indicating the water inlet points of the Reservoir  - `hasOutlet[string]`: A relationship indicating the water outlet points of the Reservoir  - `head[object]`: Observed head at the node (junction, tank or reservoir)  - `id[*]`: Unique identifier of the entity  - `initLevel[number]`: The height of the water surface above the bottom elevation of the tank at the start of the simulation. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.  . Model: [https://schema.org/Number](https://schema.org/Number)- `initialQuality[number]`: Water quality level in the tank at the start of the simulation. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.  . Model: [https://schema.org/Number](https://schema.org/Number)- `level[object]`: Observed level in the element of the network  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `maxLevel[number]`: The height of the water surface above the bottom elevation of the tank at the start of the simulation. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.  . Model: [https://schema.org/Number](https://schema.org/Number)- `minLevel[number]`: The minimum level that water in the tank can drop to. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.  . Model: [https://schema.org/Number](https://schema.org/Number)- `minVolume[number]`: The volume of water in the tank when it is at its minimum level. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.  . Model: [https://schema.org/Number](https://schema.org/Number)- `mixingFraction[number]`: The fraction of the tank's total volume that comprises the inlet-outlet compartment of the two-compartment (2COMP) mixing model. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.  . Model: [https://schema.org/Number](https://schema.org/Number)- `mixingModel[string]`: A sub-property of the Property sourceCategory. Enum:'2COMP, FIFO, LIFO, MIXED'  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: The name of this item.  - `nominalDiameter[number]`: The diameter of the tank. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `pressure[object]`: Observed pressure at the node (junction, tank or reservoir)  - `quality[object]`: Observed quality in the network component  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `sourceCategory[object]`: Description of the quality of source flow entering the network at a specific node.  . Model: [https://schema.org/Text](https://schema.org/Text)- `sourceMassInflow[object]`: Observed source mass inflow at the node (junction, tank or reservoir)  - `supply[object]`: Observed supply at the node (junction, tank or reservoir)  - `tag[string]`: An optional text string used to assign the pipe to a category, perhaps one based on age or material  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI-LD Entity Type. It has to be Tank  - `volumeCurve[*]`: The ID label of a curve used to describe the relation between tank volume and water level  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
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
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    bulkReactionCoefficient:    
      description: 'The bulk reaction coefficient used for modelling reactions in the tank. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 1/day    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    elevation:    
      description: 'The elevation above some common reference of the Tank. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: metre    
    hasInlet:    
      description: 'A relationship indicating the water inlet points of the Reservoir'    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    hasOutlet:    
      description: 'A relationship indicating the water outlet points of the Reservoir'    
      format: uri    
      type: string    
      x-ngsi:    
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
      type: object    
      x-ngsi:    
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
      x-ngsi:    
        type: Property    
    initLevel:    
      description: 'The height of the water surface above the bottom elevation of the tank at the start of the simulation. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: metre    
    initialQuality:    
      description: 'Water quality level in the tank at the start of the simulation. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
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
      type: object    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
      x-ngsi:    
        type: GeoProperty    
    maxLevel:    
      description: 'The height of the water surface above the bottom elevation of the tank at the start of the simulation. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: metre    
    minLevel:    
      description: 'The minimum level that water in the tank can drop to. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: metre    
    minVolume:    
      description: 'The volume of water in the tank when it is at its minimum level. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'cubic metre'    
    mixingFraction:    
      description: 'The fraction of the tank''s total volume that comprises the inlet-outlet compartment of the two-compartment (2COMP) mixing model. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'No unit'    
    mixingModel:    
      description: 'A sub-property of the Property sourceCategory. Enum:''2COMP, FIFO, LIFO, MIXED'''    
      enum:    
        - 2COMP    
        - FIFO    
        - LIFO    
        - MIXED    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    nominalDiameter:    
      description: 'The diameter of the tank. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Metre    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *tank_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
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
      type: object    
      x-ngsi:    
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
      type: object    
      x-ngsi:    
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
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
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
        value:    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    sourceMassInflow:    
      description: 'Observed source mass inflow at the node (junction, tank or reservoir)'    
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
      x-ngsi:    
        type: Property    
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
      type: object    
      x-ngsi:    
        type: Property    
    tag:    
      description: 'An optional text string used to assign the pipe to a category, perhaps one based on age or material'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'NGSI-LD Entity Type. It has to be Tank'    
      enum:    
        - Tank    
      type: string    
      x-ngsi:    
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
      x-ngsi:    
        type: Relationship    
  required:    
    - id    
    - type    
    - location    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.WaterDistributionManagementEPANET/blob/master/Tank/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.WaterDistributionManagementEPANET/Tank/schema.json    
  x-model-tags: FIWARE4WATER    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
#### Tank NGSI-v2 key-values Example    
Here is an example of a Tank in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### Tank NGSI-v2 normalized Example    
Here is an example of a Tank in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### Tank NGSI-LD key-values Example    
Here is an example of a Tank in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Tank:1863179e-3968-4493-9167-ee21f880cc02",  
    "type": "Tank",  
    "bulkReactionCoefficient": 0.7,  
    "createdAt": "2020-03-13T15:42:00Z",  
    "description": "Free Text",  
    "elevation": 112.9,  
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
    "volumeCurve": "urn:ngsi-ld:Curve:fAM-8ca3-4533-a2eb-12015",  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.WaterDistributionManagementEPANET/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### Tank NGSI-LD normalized Example    
Here is an example of a Tank in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Tank:1863179e-3968-4493-9167-ee21f880cc02",  
    "type": "Tank",  
    "bulkReactionCoefficient": {  
        "type": "Property",  
        "value": 0.7,  
        "unitCode": "E91"  
    },  
    "description": {  
        "type": "Property",  
        "value": "Free Text"  
    },  
    "elevation": {  
        "type": "Property",  
        "value": 112.9,  
        "unitCode": "MTR"  
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
    "initLevel": {  
        "type": "Property",  
        "value": 3,  
        "unitCode": "MTR"  
    },  
    "initialQuality": {  
        "type": "Property",  
        "value": 0.5,  
        "unitCode": "M1"  
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
    "maxLevel": {  
        "type": "Property",  
        "value": 6.75,  
        "unitCode": "MTR"  
    },  
    "minLevel": {  
        "type": "Property",  
        "value": 0,  
        "unitCode": "MTR"  
    },  
    "minVolume": {  
        "type": "Property",  
        "value": 0,  
        "unitCode": "MTQ"  
    },  
    "mixingFraction": {  
        "type": "Property",  
        "value": 0.7,  
        "unitCode": "C62"  
    },  
    "mixingModel": {  
        "type": "Property",  
        "value": "MIXED"  
    },  
    "nominalDiameter": {  
        "type": "Property",  
        "value": 13.73,  
        "unitCode": "MTR"  
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
    "tag": {  
        "type": "Property",  
        "value": "DMA1"  
    },  
    "volumeCurve": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Curve:fAM-8ca3-4533-a2eb-12015"  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.WaterDistributionManagementEPANET/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
