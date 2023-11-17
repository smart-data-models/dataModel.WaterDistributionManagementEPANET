<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entity: Pipe    
============<!-- /10-Header -->    
<!-- 15-License -->    
[Open License](https://github.com/smart-data-models//dataModel.WaterDistributionManagementEPANET/blob/master/Pipe/LICENSE.md)    
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Global description: **This entity contains a harmonised description of a generic pipe made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.**    
version: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## List of properties    
<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>    
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: The country. For example, Spain  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: The locality in which the street address is, and which is in the region  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: The region in which the locality is, and which is in the country  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: A district is a type of administrative division that, in some countries, is managed by the local government      
	- `postOfficeBoxNumber[string]`: The post office box number for PO box addresses. For example, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: The postal code. For example, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: The street address  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `bulkCoeff[number]`: Use a positive value for growth and a negative value for decay. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `description[string]`: A description of this item  - `diameter[number]`: The pipe diameter  . Model: [https://schema.org/Number](https://schema.org/Number)- `endsAt[uri]`: The ID of the node where the pipe ends  - `flow[object]`: Rate of flow from `startsAt` node to `endsAt` node, measured by a device at the link (pipe, valve or pump)  	- `observedBy`:       
- `id[*]`: Unique identifier of the entity  - `initialStatus[string]`: The link status at the start of the simulation. Enum:'OPEN, CLOSED, CV'  . Model: [https://schema.org/Text](https://schema.org/Text)- `length[number]`: The actual length of the pipe. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `minorLoss[number]`: Unitless minor loss coefficient associated with bends, fittings, etc  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: The name of this item  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `quality[object]`: Observed quality in the network component  	- `observedBy`:       
- `roughness[number]`: The roughness coefficient of the Pipe  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `startsAt[uri]`: The ID of the node where the pipe begins  - `status[string]`: The dynamic state of the node. Enum:'OPEN, CLOSED, CV'  . Model: [https://schema.org/Text](https://schema.org/Text)- `tag[string]`: An optional text string used to assign the pipe to a category, perhaps one based on age or material  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI-LD Entity Type. It has to be Pipe  - `velocity[object]`: Observed velocity in the link (pipe, valve or pump)  	- `observedBy[uri]`: Where the velocity has been observed      
- `vertices[*]`: Geoproperty. Coordinates of all vertices in the pipe, ordered from the startsAt node to the endsAt node and encoded as a GeoJSON   - `wallCoeff[number]`: The wall reaction coefficient for the pipe. Use a positive value for growth and a negative value for decay. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Required properties    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Data Model description of properties    
Sorted alphabetically (click for details)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
Pipe:      
  description: This entity contains a harmonised description of a generic pipe made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.      
  properties:      
    address:      
      description: The mailing address      
      properties:      
        addressCountry:      
          description: 'The country. For example, Spain'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressCountry      
            type: Property      
        addressLocality:      
          description: 'The locality in which the street address is, and which is in the region'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressLocality      
            type: Property      
        addressRegion:      
          description: 'The region in which the locality is, and which is in the country'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressRegion      
            type: Property      
        district:      
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'      
          type: string      
          x-ngsi:      
            type: Property      
        postOfficeBoxNumber:      
          description: 'The post office box number for PO box addresses. For example, 03578'      
          type: string      
          x-ngsi:      
            model: https://schema.org/postOfficeBoxNumber      
            type: Property      
        postalCode:      
          description: 'The postal code. For example, 24004'      
          type: string      
          x-ngsi:      
            model: https://schema.org/https://schema.org/postalCode      
            type: Property      
        streetAddress:      
          description: The street address      
          type: string      
          x-ngsi:      
            model: https://schema.org/streetAddress      
            type: Property      
        streetNr:      
          description: Number identifying a specific property on a public street      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/address      
        type: Property      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    areaServed:      
      description: The geographic area where a service or offered item is provided      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    bulkCoeff:      
      description: 'Use a positive value for growth and a negative value for decay. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code'      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: reciprocal day The bulk reaction coefficient for the pipe      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dateCreated:      
      description: Entity creation timestamp. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    diameter:      
      description: The pipe diameter      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: Millimetre      
    endsAt:      
      description: The ID of the node where the pipe ends      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    flow:      
      description: 'Rate of flow from `startsAt` node to `endsAt` node, measured by a device at the link (pipe, valve or pump)'      
      properties:      
        observedBy:      
          anyOf:      
            - description: Identifier format of any NGSI entity      
              maxLength: 256      
              minLength: 1      
              pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
              type: string      
              x-ngsi:      
                type: Property      
            - description: Identifier format of any NGSI entity      
              format: uri      
              type: string      
              x-ngsi:      
                type: Property      
        value:      
          description: Value of the flow      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
    id:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Unique identifier of the entity      
      x-ngsi:      
        type: Property      
    initialStatus:      
      description: 'The link status at the start of the simulation. Enum:''OPEN, CLOSED, CV'''      
      enum:      
        - OPEN      
        - CLOSED      
        - CV      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    length:      
      description: 'The actual length of the pipe. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code'      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: Metre      
    location:      
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
      oneOf:      
        - description: Geojson reference to the item. Point      
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
          title: GeoJSON Point      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. LineString      
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
          title: GeoJSON LineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. Polygon      
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
          title: GeoJSON Polygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiPoint      
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
          title: GeoJSON MultiPoint      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
          title: GeoJSON MultiLineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
          title: GeoJSON MultiPolygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
      x-ngsi:      
        type: GeoProperty      
    minorLoss:      
      description: 'Unitless minor loss coefficient associated with bends, fittings, etc'      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: No unit      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    owner:      
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    quality:      
      description: Observed quality in the network component      
      properties:      
        observedBy:      
          anyOf:      
            - description: Identifier format of any NGSI entity      
              maxLength: 256      
              minLength: 1      
              pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
              type: string      
              x-ngsi:      
                type: Property      
            - description: Identifier format of any NGSI entity      
              format: uri      
              type: string      
              x-ngsi:      
                type: Property      
        value:      
          description: Numerical value of the quality      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
    roughness:      
      description: The roughness coefficient of the Pipe      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: No unit      
    seeAlso:      
      description: list of uri pointing to additional resources about the item      
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    startsAt:      
      description: The ID of the node where the pipe begins      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    status:      
      description: 'The dynamic state of the node. Enum:''OPEN, CLOSED, CV'''      
      enum:      
        - OPEN      
        - CLOSED      
        - CV      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    tag:      
      description: 'An optional text string used to assign the pipe to a category, perhaps one based on age or material'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    type:      
      description: NGSI-LD Entity Type. It has to be Pipe      
      enum:      
        - Pipe      
      type: string      
      x-ngsi:      
        type: Property      
    velocity:      
      description: 'Observed velocity in the link (pipe, valve or pump)'      
      properties:      
        observedBy:      
          description: Where the velocity has been observed      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
        value:      
          description: Value of the velocity      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
    vertices:      
      description: 'Geoproperty. Coordinates of all vertices in the pipe, ordered from the startsAt node to the endsAt node and encoded as a GeoJSON '      
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
          title: GeoJSON MultiPoint      
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
          title: GeoJSON Point      
          type: object      
    wallCoeff:      
      description: 'The wall reaction coefficient for the pipe. Use a positive value for growth and a negative value for decay. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code'      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: mg/m²/day      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.WaterDistributionManagementEPANET/blob/master/Pipe/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.WaterDistributionManagementEPANET/Pipe/schema.json      
  x-model-tags: FIWARE4WATER      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Example payloads      
#### Pipe NGSI-v2 key-values Example      
Here is an example of a Pipe in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "74azsty-70d4l-4da9-b7d0-3340ef655nnb",  
  "type": "Pipe",  
  "initialStatus": "OPEN",  
  "status": "OPEN",  
  "length": 52.9,  
  "diameter": 203.0,  
  "roughness": 72.4549,  
  "minorLoss": 72.4549,  
  "tag": "DMA1",  
  "description": "Free Text",  
  "startsAt": "ngsi:63fe7d79-0d4c-4da9-b7d0-3340efa0656a",  
  "endsAt": "ngsi:1863179e-3768-4480-9167-ff21f870dd19",  
  "bulkCoeff": 72.4549,  
  "wallCoeff": 72.4549  
}  
```  
</details>    
#### Pipe NGSI-v2 normalized Example      
Here is an example of a Pipe in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "74azsty-70d4l-4da9-b7d0-3340ef655nnb",  
  "type": "Pipe",  
  "initialStatus": {  
    "type": "Text",  
    "value": "OPEN"  
  },  
  "status": {  
    "type": "Text",  
    "value": "OPEN"  
  },  
  "length": {  
    "type": "Number",  
    "value": 52.9  
  },  
  "diameter": {  
    "type": "Number",  
    "value": 203.0  
  },  
  "roughness": {  
    "type": "Number",  
    "value": 72.4549  
  },  
  "minorLoss": {  
    "type": "Number",  
    "value": 72.4549  
  },  
  "tag": {  
    "type": "Text",  
    "value": "DMA1"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Free Text"  
  },  
  "startsAt": {  
    "type": "Text",  
    "value": "63fe7d79-0d4c-4da9-b7d0-3340efa0656a"  
  },  
  "endsAt": {  
    "type": "Text",  
    "value": "1863179e-3768-4480-9167-ff21f870dd19"  
  },  
  "bulkCoeff": {  
    "type": "Number",  
    "value": 72.4549  
  },  
  "wallCoeff": {  
    "type": "Number",  
    "value": 72.4549  
  },  
  "flow": {  
    "type": "StructuredValue",  
    "value": {  
      "value": 20,  
      "observedBy": "device-9845A"  
    }  
  },  
  "velocity": {  
    "type": "StructuredValue",  
    "value": {  
      "value": 2,  
      "observedBy": "device-9845A"  
    }  
  },  
  "quality": {  
    "type": "StructuredValue",  
    "value": {  
      "value": 0.5,  
      "observedBy": "device-9845A"  
    }  
  }  
}  
```  
</details>    
#### Pipe NGSI-LD key-values Example      
Here is an example of a Pipe in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Pipe:74azsty-70d4l-4da9-b7d0-3340ef655nnb",  
  "type": "Pipe",  
  "bulkCoeff": 72.4549,  
  "createdAt": "2020-02-20T15:42:00Z",  
  "description": "Free Text",  
  "diameter": 203.0,  
  "endsAt": "urn:ngsi-ld:Reservoir:1863179e-3768-4480-9167-ff21f870dd19",  
  "initialStatus": "OPEN",  
  "length": 52.9,  
  "minorLoss": 72.4549,  
  "modifiedAt": "2020-02-20T15:45:00Z",  
  "roughness": 72.4549,  
  "startsAt": "urn:ngsi-ld:Junction:63fe7d79-0d4c-4da9-b7d0-3340efa0656a",  
  "status": "OPEN",  
  "tag": "DMA1",  
  "wallCoeff": 72.4549,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.WaterDistributionManagementEPANET/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### Pipe NGSI-LD normalized Example      
Here is an example of a Pipe in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:Pipe:74azsty-70d4l-4da9-b7d0-3340ef655nnb",  
    "type": "Pipe",  
    "bulkCoeff": {  
        "type": "Property",  
        "value": 72.4549,  
        "unitCode": "E91"  
    },  
    "description": {  
        "type": "Property",  
        "value": "Free Text"  
    },  
    "diameter": {  
        "type": "Property",  
        "value": 203.0,  
        "unitCode": "MMT"  
    },  
    "endsAt": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Reservoir:1863179e-3768-4480-9167-ff21f870dd19"  
    },  
    "flow": {  
        "type": "Property",  
        "value": {  
            "type": "Property",  
            "value": 20,  
            "unitCode": "G51"  
        },  
        "observedBy": {  
            "type": "Relationship",  
            "object": "urn:ngsi-ld:Device:device-9845A"  
        }  
    },  
    "initialStatus": {  
        "type": "Property",  
        "value": "OPEN"  
    },  
    "length": {  
        "type": "Property",  
        "value": 52.9,  
        "unitCode": "MTR"  
    },  
    "minorLoss": {  
        "type": "Property",  
        "value": 72.4549,  
        "unitCode": "C62"  
    },  
    "quality": {  
        "type": "Property",  
        "value": {  
            "type": "Property",  
            "value": 0.5,  
            "unitCode": "F27"  
        },  
        "observedBy": {  
            "type": "Relationship",  
            "object": "urn:ngsi-ld:Device:device-9845A"  
        }  
    },  
    "roughness": {  
        "type": "Property",  
        "value": 72.4549,  
        "unitCode": "C62"  
    },  
    "startsAt": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Junction:63fe7d79-0d4c-4da9-b7d0-3340efa0656a"  
    },  
    "status": {  
        "type": "Property",  
        "value": "OPEN"  
    },  
    "tag": {  
        "type": "Property",  
        "value": "DMA1"  
    },  
    "velocity": {  
        "type": "Property",  
        "value": {  
            "type": "Property",  
            "value": 2,  
            "unitCode": "MTS"  
        },  
        "observedBy": {  
            "type": "Relationship",  
            "object": "urn:ngsi-ld:Device:device-9845A"  
        }  
    },  
    "vertices": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "MultiPoint",  
            "coordinates": [  
                [  
                    24.40623,  
                    60.17966  
                ],  
                [  
                    24.50623,  
                    60.27966  
                ]  
            ]  
        }  
    },  
    "wallCoeff": {  
        "type": "Property",  
        "value": 72.4549,  
        "unitCode": "RRC"  
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
