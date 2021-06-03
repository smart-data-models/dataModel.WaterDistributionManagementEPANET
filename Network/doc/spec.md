Entity: Network  
===============  
[Open License](https://github.com/smart-data-models//dataModel.WaterDistributionManagementEPANET/blob/master/Network/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Global description: **This entity contains a harmonised description of a generic network made for the Water Network Management domain. This entity is primarily associated with the water network management vertical and related IoT applications.**  

## List of properties  

- `address`: The mailing address  - `alternateName`: An alternative name for this item  - `areaServed`: The geographic area where a service or offered item is provided  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `hasSubNetwork`: Reference to an entity of type `Network`  - `id`: Unique identifier of the entity  - `isComposedOf`: Reference to the water component entities of the network, of type `Node (Reservoir, Junction, Tank)` or `Link (Pipe, Valve, Pump)`  - `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name`: The name of this item.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `seeAlso`: list of uri pointing to additional resources about the item  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `type`: NGSI-LD Entity Type. It has to be WaterNetwork    
Required properties  
- `id`  - `type`  ## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Network:    
  description: 'This entity contains a harmonised description of a generic network made for the Water Network Management domain. This entity is primarily associated with the water network management vertical and related IoT applications.'    
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
    hasSubNetwork:    
      description: 'Reference to an entity of type `Network`'    
      items:    
        anyOf:    
          - maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - format: uri    
            type: string    
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/Text    
    id:    
      anyOf: &network_-_properties_-_owner_-_items_-_anyof    
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
    isComposedOf:    
      description: 'Reference to the water component entities of the network, of type `Node (Reservoir, Junction, Tank)` or `Link (Pipe, Valve, Pump)`'    
      items:    
        anyOf:    
          - maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - format: uri    
            type: string    
      type: Relationship    
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
        anyOf: *network_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
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
    type:    
      description: 'NGSI-LD Entity Type. It has to be WaterNetwork'    
      enum:    
        - WaterNetwork    
      type: Property    
  required:    
    - id    
    - type    
  type: object    
```  
</details>    
## Example payloads    
#### Network NGSI-v2 key-values Example    
Here is an example of a Network in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:WaterNetwork:01",  
  "type": "WaterNetwork",  
  "description": "Free Text",  
  "isComposedOf": [  
    "urn:ngsi-ld:Tank:T1",  
    "urn:ngsi-ld:Pipe:P1",  
    "urn:ngsi-ld:Junction:J1"  
  ],  
  "hasSubNetwork": [  
    "urn:ngsi-ld:Network:12-70d4l-4da9",  
    "urn:ngsi-ld:Network:A14-14d4B-4vvc"  
  ]  
}  
```  
#### Network NGSI-v2 normalized Example    
Here is an example of a Network in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:WaterNetwork:01",  
  "type": "WaterNetwork",  
  "description": {  
    "type": "Property",  
    "value": "Free Text"  
  },  
  "isComposedOf": [  
    {  
      "type": "Relationship",  
      "value": "urn:ngsi-ld:Tank:T1"  
    },  
    {  
      "type": "Relationship",  
      "value": "urn:ngsi-ld:Pipe:P1"  
    },  
    {  
      "type": "Relationship",  
      "value": "urn:ngsi-ld:Junction:J1"  
    }  
  ],  
  "hasSubNetwork": [  
    {  
      "type": "Relationship",  
      "value": "urn:ngsi-ld:Network:12-70d4l-4da9"  
    },  
    {  
      "type": "Relationship",  
      "value": "urn:ngsi-ld:Network:A14-14d4B-4vvc"  
    }  
  ]  
}  
```  
#### Network NGSI-LD key-values Example    
Here is an example of a Network in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:WaterNetwork:01",  
  "type": "WaterNetwork",  
  "description": "Free Text",  
  "isComposedOf": [  
    "urn:ngsi-ld:Tank:T1",  
    "urn:ngsi-ld:Pipe:P1",  
    "urn:ngsi-ld:Junction:J1"  
  ],  
  "hasSubNetwork": [  
    "urn:ngsi-ld:Network:12-70d4l-4da9",  
    "urn:ngsi-ld:Network:A14-14d4B-4vvc"  
  ],  
  "@context": [  
    "https://smart-data-models.github.io//data-models/context.jsonld"  
  ]  
}  
```  
#### Network NGSI-LD normalized Example    
Here is an example of a Network in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:WaterNetwork:01",  
  "type": "WaterNetwork",  
  "description": {  
    "type": "Property",  
    "value": "Free Text"  
  },  
  "isComposedOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:Tank:T1",  
      "datasetId": "urn:ngsi-ld:Dataset:TankT1"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:Pipe:P1",  
      "datasetId": "urn:ngsi-ld:Dataset:PipeP1"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:Junction:J1",  
      "datasetId": "urn:ngsi-ld:Dataset:JunctionJ1"  
    }  
  ],  
  "hasSubNetwork": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:Network:12-70d4l-4da9",  
      "datasetId": "urn:ngsi-ld:Dataset:NetworkN1"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:Network:A14-14d4B-4vvc",  
      "datasetId": "urn:ngsi-ld:Dataset:NetworkN2"  
    }  
  ],  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
