Entidad: Tanque  
===============  
Esta especificación es una **versión temporal**. Se genera automáticamente a partir de las propiedades documentadas descritas en el schema.json condensadas en el archivo `model.yaml`. Se ha creado un archivo temporal `nuevo_modelo.yaml` en cada modelo de datos para evitar el impacto en los scripts existentes. Por lo tanto, la especificación estará incompleta mientras el schema.json no se actualice al nuevo formato (documentando las propiedades). Una vez actualizado el `modelo.yaml` (`nuevo_modelo.yaml`) necesita ser actualizado también (automáticamente) . Más información en este [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Mientras sea un formato provisional cualquier [feedback es bienvenido en este formulario](https://smartdatamodels.org/index.php/submit-an-issue-2/) eligiendo la opción `Feedback on the new specification`.  
Descripción global: **Esta entidad contiene una descripción armonizada de un tanque genérico hecho para el dominio de la gestión de la red de agua. Esta entidad está principalmente asociada con la gestión vertical del agua y las aplicaciones de IO relacionadas**.  

## Lista de propiedades  

`address`: La dirección postal.  `areaServed`: La zona geográfica donde se presta un servicio o se ofrece un artículo.  `bulkReactionCoefficient`:   `description`:   `elevation`:   `hasInlet`:   `hasOutlet`:   `initLevel`:   `initialQuality`:   `location`:   `maxLevel`:   `minLevel`:   `minVolume`:   `mixingFraction`:   `mixingModel`:   `nominalDiameter`:   `sourceCategory`:   `tag`:   `type`: Tipo de entidad NGSI-LD  `volumeCurve`:   ## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente  
```yaml  
Tank:    
  description: 'This entity contains a harmonised description of a generic tank made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.'    
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
    bulkReactionCoefficient:    
      properties: &tank_-_properties_-_description_-_properties    
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
      required: &tank_-_properties_-_description_-_required    
        - type    
        - value    
      type: object    
    description:    
      properties: *tank_-_properties_-_description_-_properties    
      required: *tank_-_properties_-_description_-_required    
      type: object    
    elevation:    
      properties: *tank_-_properties_-_description_-_properties    
      required: *tank_-_properties_-_description_-_required    
      type: object    
    hasInlet:    
      properties: &tank_-_properties_-_hasoutlet_-_properties    
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
      required: &tank_-_properties_-_hasoutlet_-_required    
        - type    
        - object    
      type: object    
    hasOutlet:    
      properties: *tank_-_properties_-_hasoutlet_-_properties    
      required: *tank_-_properties_-_hasoutlet_-_required    
      type: object    
    initLevel:    
      properties: *tank_-_properties_-_description_-_properties    
      required: *tank_-_properties_-_description_-_required    
      type: object    
    initialQuality:    
      properties: *tank_-_properties_-_description_-_properties    
      required: *tank_-_properties_-_description_-_required    
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
    maxLevel:    
      properties: *tank_-_properties_-_description_-_properties    
      required: *tank_-_properties_-_description_-_required    
      type: object    
    minLevel:    
      properties: *tank_-_properties_-_description_-_properties    
      required: *tank_-_properties_-_description_-_required    
      type: object    
    minVolume:    
      properties: *tank_-_properties_-_description_-_properties    
      required: *tank_-_properties_-_description_-_required    
      type: object    
    mixingFraction:    
      properties: *tank_-_properties_-_description_-_properties    
      required: *tank_-_properties_-_description_-_required    
      type: object    
    mixingModel:    
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
            - MIXED    
            - 2COMP    
            - FIFO    
            - LIFO    
          type:    
            - number    
            - string    
            - array    
      required:    
        - type    
        - value    
      type: object    
    nominalDiameter:    
      properties: *tank_-_properties_-_description_-_properties    
      required: *tank_-_properties_-_description_-_required    
      type: object    
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
      properties: *tank_-_properties_-_description_-_properties    
      required: *tank_-_properties_-_description_-_required    
      type: object    
    type:    
      description: 'NGSI-LD Entity Type'    
      enum:    
        - Tank    
      type: string    
    volumeCurve:    
      properties: *tank_-_properties_-_hasoutlet_-_properties    
      required: *tank_-_properties_-_hasoutlet_-_required    
      type: object    
  required:    
    - id    
    - type    
    - location    
    - elevation    
    - initLevel    
    - maxLevel    
    - minVolume    
    - nominalDiameter    
  type: object    
```  
Aquí hay un ejemplo de un tanque en formato JSON como valores clave. Esto es compatible con NGSI V2 cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
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
Aquí hay un ejemplo de un tanque en formato JSON como normalizado. Es compatible con NGSI V2 cuando se utiliza `opciones=valores clave` y devuelve los datos de contexto de una entidad individual.  
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
        "value": 112.9  
    },  
    "initLevel": {  
        "value": 3  
    },  
    "minLevel": {  
        "value": 0  
    },  
    "maxLevel": {  
        "value": 6.75  
    },  
    "minVolume": {  
        "value": 0  
    },  
    "nominalDiameter": {  
        "value": 13.73  
    },  
    "description": {  
        "value": "Free Text"  
    },  
    "initialQuality": {  
        "value": 0.5  
    },  
    "sourceCategory": {  
        "value": {  
            "value": "category1",  
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
    "mixingModel": {  
        "value": "MIXED"  
    },  
    "volumeCurve": {  
        "type": "Relationship",  
        "value": "fAM-8ca3-4533-a2eb-12015"  
    },  
    "mixingFraction": {  
        "value": 0.7  
    },  
    "bulkReactionCoefficient": {  
        "value": 0.7  
    },  
    "tag": {  
        "value": "DMA1"  
    }  
}  
```  
Aquí hay un ejemplo de un tanque en formato JSON-LD como valores clave. Esto es compatible con NGSI-LD cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context"],  
 "bulkReactionCoefficient": 0.7,  
 "createdAt": "2020-03-13T15:42:00Z",  
 "description": "Free Text",  
 "elevation": 112.9,  
 "id": "urn:ngsi-ld:Tank:1863179e-3968-4493-9167-ee21f880cc02",  
 "initLevel": 3,  
 "initialQuality": 0.5,  
 "location": {"coordinates": [24.30623, 60.07966], "type": "Point"},  
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
 "volumeCurve": "urn:ngsi-ld:Curve:fAM-8ca3-4533-a2eb-12015"}  
```  
Aquí hay un ejemplo de un tanque en formato JSON-LD como normalizado. Este es compatible con NGSI-LD cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "urn:ngsi-ld:Tank:1863179e-3968-4493-9167-ee21f880cc02",  
    "type": "Tank",  
    "createdAt": "2020-03-13T15:42:00Z",  
    "modifiedAt": "2020-03-13T15:45:00Z",  
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
        "unitCode":"M1"  
    },  
    "sourceCategory": {  
        "type": "Property",  
        "value": "category1",  
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
    "@context": [  
        "https://schema.lab.fiware.org/ld/context"  
    ]  
}  
```  
