Entidad: Válvula  
================  
Esta especificación es una **versión temporal**. Se genera automáticamente a partir de las propiedades documentadas descritas en el schema.json condensadas en el archivo `model.yaml`. Se ha creado un archivo temporal `nuevo_modelo.yaml` en cada modelo de datos para evitar el impacto en los scripts existentes. Por lo tanto, la especificación estará incompleta mientras el schema.json no se actualice al nuevo formato (documentando las propiedades). Una vez actualizado el `modelo.yaml` (`nuevo_modelo.yaml`) necesita ser actualizado también (automáticamente) . Más información en este [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Mientras sea un formato provisional cualquier [feedback es bienvenido en este formulario](https://smartdatamodels.org/index.php/submit-an-issue-2/) eligiendo la opción `Feedback on the new specification`.  
Descripción global: **Esta entidad contiene una descripción armonizada de una válvula genérica hecha para el dominio de la gestión de la red de agua. Esta entidad está principalmente asociada con la gestión vertical del agua y las aplicaciones relacionadas con la IO**.  

## Lista de propiedades  

`diameter`:   `endsAt`:   `initialStatus`:   `minorLoss`:   `setting`:   `startsAt`:   `status`:   `tag`:   `type`: Tipo de entidad NGSI-LD  `valveType`:   `vertices`:   ## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente  
```yaml  
Valve:    
  description: 'This entity contains a harmonised description of a generic Valve made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.'    
  properties:    
    diameter:    
      properties: &valve_-_properties_-_minorloss_-_properties    
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
      required: &valve_-_properties_-_minorloss_-_required    
        - type    
        - value    
      type: object    
    endsAt:    
      properties: &valve_-_properties_-_startsat_-_properties    
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
      required: &valve_-_properties_-_startsat_-_required    
        - type    
        - object    
      type: object    
    initialStatus:    
      properties: &valve_-_properties_-_status_-_properties    
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
            - OPEN    
            - CLOSED    
            - CV    
          type:    
            - number    
            - string    
            - array    
      required: &valve_-_properties_-_status_-_required    
        - type    
        - value    
      type: object    
    minorLoss:    
      properties: *valve_-_properties_-_minorloss_-_properties    
      required: *valve_-_properties_-_minorloss_-_required    
      type: object    
    setting:    
      properties: *valve_-_properties_-_minorloss_-_properties    
      required: *valve_-_properties_-_minorloss_-_required    
      type: object    
    startsAt:    
      properties: *valve_-_properties_-_startsat_-_properties    
      required: *valve_-_properties_-_startsat_-_required    
      type: object    
    status:    
      properties: *valve_-_properties_-_status_-_properties    
      required: *valve_-_properties_-_status_-_required    
      type: object    
    tag:    
      properties: *valve_-_properties_-_minorloss_-_properties    
      required: *valve_-_properties_-_minorloss_-_required    
      type: object    
    type:    
      description: 'NGSI-LD Entity Type'    
      enum:    
        - Valve    
      type: string    
    valveType:    
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
            - PRV    
            - PSV    
            - PBV    
            - FCV    
            - TCV    
            - GPV    
          type:    
            - string    
        valveCurve:    
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
          type: object    
      required:    
        - type    
        - value    
      type: object    
    vertices:    
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
          title: 'GeoJSON MultiPoint'    
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
          title: 'GeoJSON Point'    
          type: object    
  required:    
    - id    
    - type    
    - initialStatus    
    - diameter    
    - valveType    
    - setting    
    - minorLoss    
    - startsAt    
    - endsAt    
  type: object    
```  
Aquí hay un ejemplo de una válvula en formato JSON como valores clave. Es compatible con NGSI V2 cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "87fe7d79-0d4c-4da9-b7d0-3340efa0656awytsd",  
    "type": "Valve",  
    "initiaStatus": "OPEN",  
    "status": "OPEN",  
    "diameter": 203.20,  
    "valveType": "PRV",  
    "setting": 40.00,  
    "minorLoss": 0.00,  
    "tag": "DMA1",  
    "startsAt": "63fe7d79-0d4c-4da9-b7d0-3340efa0656a",  
    "endsAt": "1863179e-3768-4480-9167-ff21f870dd19"  
}  
```  
Aquí hay un ejemplo de una válvula en formato JSON como normalizada. Es compatible con NGSI V2 cuando se utiliza `opciones=valores clave` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "87fe7d79-0d4c-4da9-b7d0-3340efa0656awytsd",  
    "type": "Valve",  
    "initiaStatus": {  
        "value": "OPEN"  
    },  
    "status": {  
        "value": "OPEN"  
    },  
    "diameter": {  
        "value": 203.20  
    },  
    "valveType": {  
        "value": "PRV"  
    },  
    "setting": {  
        "value": 40.00  
    },  
    "minorLoss": {  
        "value": 0.00  
    },  
    "tag": {  
        "value": "DMA1"  
    },  
    "startsAt": {  
        "type": "Relationship",  
        "value": "63fe7d79-0d4c-4da9-b7d0-3340efa0656a"  
    },  
    "endsAt": {  
        "type": "Relationship",  
        "value": "1863179e-3768-4480-9167-ff21f870dd19"  
    }  
}  
```  
Aquí hay un ejemplo de una válvula en formato JSON-LD como valores clave. Esto es compatible con NGSI-LD cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context"],  
 "createdAt": "2020-03-02T15:42:00Z",  
 "diameter": 203.2,  
 "endsAt": "urn:ngsi-ld:Reservoir:1863179e-3768-4480-9167-ff21f870dd19",  
 "id": "urn:ngsi-ld:Valve:87fe7d79-0d4c-4da9-b7d0-3340efa0656awytsd",  
 "initiaStatus": "OPEN",  
 "minorLoss": 0.0,  
 "modifiedAt": "2020-03-02T15:45:00Z",  
 "setting": 40.0,  
 "startsAt": "urn:ngsi-ld:Junction:63fe7d79-0d4c-4da9-b7d0-3340efa0656a",  
 "status": "OPEN",  
 "tag": "DMA1",  
 "type": "Valve",  
 "valveType": "PRV"}  
```  
Aquí hay un ejemplo de una válvula en formato JSON-LD como normalizada. Esto es compatible con NGSI-LD cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "urn:ngsi-ld:Valve:87fe7d79-0d4c-4da9-b7d0-3340efa0656awytsd",  
    "type": "Valve",  
    "createdAt": "2020-03-02T15:42:00Z",  
    "modifiedAt": "2020-03-02T15:45:00Z",  
    "initiaStatus": {  
        "type": "Property",  
        "value": "OPEN"  
    },  
    "status": {  
        "type": "Property",  
        "value": "OPEN"  
    },  
    "diameter": {  
        "type": "Property",  
        "value": 203.20,  
        "unitCode": "MMT"  
    },  
    "valveType": {  
        "type": "Property",  
        "value": "PRV"  
    },  
    "setting": {  
        "type": "Property",  
        "value": 40.00,  
        "unitCode": "C62"  
    },  
    "minorLoss": {  
        "type": "Property",  
        "value": 0.00,  
        "unitCode": "C62"  
    },  
    "tag": {  
        "type": "Property",  
        "value": "DMA1"  
    },  
    "startsAt": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Junction:63fe7d79-0d4c-4da9-b7d0-3340efa0656a"  
    },  
    "endsAt": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Reservoir:1863179e-3768-4480-9167-ff21f870dd19"  
    },  
    "vertices": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "MultiPoint",  
            "coordinates": [  
                [24.40623, 60.17966],  
                [24.50623, 60.27966]  
            ]  
        }  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context"  
    ]  
}  
```  
