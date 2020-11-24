Entidad: Unión  
==============  
Esta especificación es una **versión temporal**. Se genera automáticamente a partir de las propiedades documentadas descritas en el schema.json condensadas en el archivo `model.yaml`. Se ha creado un archivo temporal `nuevo_modelo.yaml` en cada modelo de datos para evitar el impacto en los scripts existentes. Por lo tanto, la especificación estará incompleta mientras el schema.json no se actualice al nuevo formato (documentando las propiedades). Una vez actualizado el `modelo.yaml` (`nuevo_modelo.yaml`) necesita ser actualizado también (automáticamente) . Más información en este [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Mientras sea un formato provisional cualquier [feedback es bienvenido en este formulario](https://smartdatamodels.org/index.php/submit-an-issue-2/) eligiendo la opción `Feedback on the new specification`.  
Descripción global: **Esta entidad contiene una descripción armonizada de un empalme genérico hecho para el dominio de la gestión de la red de agua. Esta entidad está principalmente asociada con la gestión de la red de agua vertical y las aplicaciones de IO conexas**.  

## Lista de propiedades  

`address`: La dirección postal.  `areaServed`: La zona geográfica donde se presta un servicio o se ofrece un artículo.  `demandCategory`:   `description`:   `elevation`:   `emitterCoefficient`:   `initialQuality`:   `location`:   `sourceCategory`:   `tag`:   `type`: Tipo de entidad NGSI-LD  ## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente  
```yaml  
Junction:    
  description: 'This entity contains a harmonised description of a generic junction made for the Water Network Management domain. This entity is primarily associated with the water network management vertical and related IoT applications.'    
  properties:    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          type: string    
        addressLocality:    
          type: string    
        addressRegion:    
          type: string    
        areaServed:    
          type: string    
        postOfficeBoxNumber:    
          type: string    
        postalCode:    
          type: string    
        streetAddress:    
          type: string    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided.'    
      type: Property    
    demandCategory:    
      properties:    
        baseDemand:    
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
              type:    
                - number    
                - string    
          required:    
            - type    
            - value    
          type: object    
        createdAt:    
          format: date-time    
          type: string    
        demandPattern:    
          properties:    
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
          required:    
            - type    
            - object    
          type: object    
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
      required:    
        - type    
        - value    
        - baseDemand    
        - demandPattern    
      type: object    
    description:    
      properties: &junction_-_properties_-_elevation_-_properties    
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
      required: &junction_-_properties_-_elevation_-_required    
        - type    
        - value    
      type: object    
    elevation:    
      properties: *junction_-_properties_-_elevation_-_properties    
      required: *junction_-_properties_-_elevation_-_required    
      type: object    
    emitterCoefficient:    
      properties: *junction_-_properties_-_elevation_-_properties    
      required: *junction_-_properties_-_elevation_-_required    
      type: object    
    initialQuality:    
      properties: *junction_-_properties_-_elevation_-_properties    
      required: *junction_-_properties_-_elevation_-_required    
      type: object    
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
    sourceCategory:    
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
        sourcePattern:    
          properties:    
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
          required:    
            - type    
            - object    
          type: object    
        sourceQuality:    
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
              type:    
                - number    
                - string    
          required:    
            - type    
            - value    
          type: object    
        sourceType:    
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
                - CONCEN    
                - MASS    
                - FLOWPACED    
                - SETPOINT    
              type:    
                - number    
                - string    
          required:    
            - type    
            - value    
          type: object    
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
      required:    
        - type    
        - value    
        - sourceType    
        - sourceQuality    
        - sourcePattern    
      type: object    
    tag:    
      properties: *junction_-_properties_-_elevation_-_properties    
      required: *junction_-_properties_-_elevation_-_required    
      type: object    
    type:    
      description: 'NGSI-LD Entity Type'    
      enum:    
        - Junction    
      type: string    
  required:    
    - id    
    - type    
    - location    
    - elevation    
  type: object    
```  
Aquí hay un ejemplo de una unión en formato JSON como valores clave. Es compatible con NGSI V2 cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "63fe7d79-0d4c-4da9-b7d0-3340efa0656a",  
    "type": "Junction",  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            24.30623,  
            60.07966  
        ]  
    },  
    "elevation": 105.8,  
    "demandCategory": {  
        "value": "agriculture demand",  
        "baseDemand": "1.763868462",  
        "demandPattern": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
    },  
    "sourceCategory": {  
        "value": "CategoryX",  
        "sourceType": "MASS",  
        "sourceQuality": 1.2,  
        "sourcePattern": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
    },  
    "tag": "DMA1",  
    "description": "This entity contains a harmonised description of a Junction",  
    "initialQuality": 0.5,  
    "emitterCoefficient": 0.526  
}  
```  
Aquí hay un ejemplo de una unión en formato JSON como normalizado. Es compatible con NGSI V2 cuando se utiliza `opciones=valores clave` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "63fe7d79-0d4c-4da9-b7d0-3340efa0656a",  
    "type": "Junction",  
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
        "value": 105.8  
    },  
    "demandCategory": {  
        "value": {  
            "value": "agriculture demand",  
            "baseDemand": {  
                "value": "1.763868462"  
            },  
            "demandPattern": {  
                "type": "Relationship",  
                "value": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
            }  
        }  
    },  
    "sourceCategory": {  
        "value": {  
            "value": "CategoryX",  
            "sourceType": {  
                "value": "MASS"  
            },  
            "sourceQuality": {  
                "value": 1.2  
            },  
            "sourcePattern": {  
                "type": "Relationship",  
                "value": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
            }  
        }  
    },  
    "tag": {  
        "value": "DMA1"  
    },  
    "description": {  
        "value": "This entity contains a harmonised description of a Junction"  
    },  
    "initialQuality": {  
        "value": 0.5  
    },  
    "emitterCoefficient": {  
        "value": 0.526  
    }  
}  
```  
Aquí hay un ejemplo de una unión en formato JSON-LD como valores clave. Esto es compatible con NGSI-LD cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context"],  
 "createdAt": "2020-02-20T15:42:00Z",  
 "demandCategory": "agriculture demand",  
 "description": "This entity contains a harmonised description of a Junction",  
 "elevation": 105.8,  
 "emitterCoefficient": 0.526,  
 "id": "urn:ngsi-ld:Junction:63fe7d79-0d4c-4da9-b7d0-3340efa0656a",  
 "initialQuality": 0.5,  
 "location": {"coordinates": [24.30623, 60.07966], "type": "Point"},  
 "modifiedAt": "2020-02-20T15:45:00Z",  
 "sourceCategory": "CategoryX",  
 "tag": "DMA1",  
 "type": "Junction"}  
```  
Aquí hay un ejemplo de una unión en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "urn:ngsi-ld:Junction:63fe7d79-0d4c-4da9-b7d0-3340efa0656a",  
    "type": "Junction",  
    "createdAt": "2020-02-20T15:42:00Z",  
    "modifiedAt": "2020-02-20T15:45:00Z",  
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
        "value": 105.8,  
        "unitCode": "MTR"  
    },  
    "demandCategory": {  
        "type": "Property",  
        "value": "agriculture demand",  
        "baseDemand": {  
            "type": "Property",  
            "value": "1.763868462",  
            "unitCode": "MQS"  
        },  
        "demandPattern": {  
            "type": "Relationship",  
            "object": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533"  
        }  
    },  
    "sourceCategory": {  
        "type": "Property",  
        "value": "CategoryX",  
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
    "description": {  
        "type": "Property",  
        "value": "This entity contains a harmonised description of a Junction"  
    },  
    "initialQuality": {  
        "type": "Property",  
        "value": 0.5,  
        "unitCode":"M1"  
    },  
    "emitterCoefficient": {  
        "type": "Property",  
        "value": 0.526,  
        "unitCode": "S4"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context"  
    ]  
}  
```  
