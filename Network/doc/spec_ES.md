Entidad: Red  
============  
[Licencia abierta](https://github.com/smart-data-models//dataModel.WaterDistributionManagementEPANET/blob/master/Network/LICENSE.md)  
Descripción global: **Esta entidad contiene una descripción armonizada de una red genérica realizada para el dominio de la gestión de redes de agua. Esta entidad está asociada principalmente a la vertical de gestión de redes de agua y a las aplicaciones IoT relacionadas.**.  

## Lista de propiedades  

- `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `hasSubNetwork`: Referencia a una entidad de tipo `Red`.  - `id`: Identificador único de la entidad  - `isComposedOf`: Referencia a las entidades componentes del agua de la red, de tipo `Nodo (Depósito, Empalme, Cisterna)` o `Enlace (Tubería, Válvula, Bomba)`.  - `location`:   - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen, o la URL del objeto de origen.  - `type`: Tipo de entidad NGSI-LD. Tiene que ser WaterNetwork    
Propiedades requeridas  
- `id`  - `type`  ## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
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
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/areaServed'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/https://schema.org/postalCode'''    
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
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
      title: 'GeoJSON Geometry'    
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
            - format: uri    
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
## Ejemplo de carga útil  
#### Red NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de una Red en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### Red NGSI-v2 normalizada Ejemplo  
Aquí hay un ejemplo de una Red en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### Red NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de una Red en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### Red NGSI-LD normalizada Ejemplo  
Aquí hay un ejemplo de una Red en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
