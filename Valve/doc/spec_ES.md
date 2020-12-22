Entidad: Válvula  
================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.WaterNetworkManagement/blob/master/Valve/LICENSE.md)  
Descripción global: **Esta entidad contiene una descripción armonizada de una válvula genérica hecha para el dominio de la gestión de la red de agua. Esta entidad está principalmente asociada con la gestión vertical del agua y las aplicaciones relacionadas con la IO**.  

## Lista de propiedades  

- `description`: Un texto opcional que describe otra información significativa sobre la unión  - `diameter`: El diámetro de la válvula. Todas las unidades son aceptadas en el código [CEFACT](https://www.unece.org/cefact.html).  - `endsAt`: El ID del nodo en el lado nominal de la descarga de la válvula  - `initialStatus`: El estado del nodo al comienzo de la simulación.  - `minorLoss`: Coeficiente de pérdida menor sin unidad que se aplica cuando la válvula se abre completamente. Todas las unidades son aceptadas en el código [CEFACT](https://www.unece.org/cefact.html).  - `setting`: Un parámetro que describe el ajuste de funcionamiento de la válvula. Todas las unidades son aceptadas en el código [CEFACT](https://www.unece.org/cefact.html).  - `startsAt`: El ID del nodo en el lado nominal de entrada o salida de la válvula  - `status`: El estado dinámico del nodo  - `tag`: Una cadena de texto opcional utilizada para asignar la pipa a una categoría, tal vez una basada en la edad o el material  - `type`: Tipo de entidad NGSI-LD. Debe ser igual a Válvula.  - `valveCurve`: Una relación con la curva de la propiedad de ajuste. Sólo se requiere cuando el tipo de válvula es GPV  - `valveType`: El tipo de válvula del elemento  - `vertices`: Las coordenadas de todos los vértices de la válvula, ordenadas desde el nodo de inicio hasta el nodo de fin y codificadas como un GeoJSON    
Propiedades requeridas  
- `diameter`  - `endsAt`  - `id`  - `initialStatus`  - `minorLoss`  - `setting`  - `startsAt`  - `type`  - `valveType`  ## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Valve:    
  description: 'This entity contains a harmonised description of a generic Valve made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.'    
  properties:    
    description:    
      description: 'An optional text that describes other significant information about the junction'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    diameter:    
      description: 'The valve diameter. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        units: millimetre    
    endsAt:    
      description: 'The ID of the node on the nominal downstream or discharge side of the valve'    
      format: uri    
      type: Relationship    
    initialStatus:    
      description: 'The node status at the start of the simulation.'    
      enum:    
        - OPEN    
        - CLOSED    
        - CV    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    minorLoss:    
      description: 'Unitless minor loss coefficient that applies when the valve is completely opened. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'No unit'    
    setting:    
      description: 'A parameter that describes the valve''s operational setting. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'No unit'    
    startsAt:    
      description: 'The ID of the node on the nominal upstream or inflow side of the valve'    
      format: uri    
      type: Relationship    
    status:    
      description: 'The dynamic state of the node'    
      enum:    
        - OPEN    
        - CLOSED    
        - CV    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    tag:    
      description: 'An optional text string used to assign the pipe to a category, perhaps one based on age or material'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    type:    
      description: 'NGSI-LD Entity Type. It must be equal to Valve.'    
      enum:    
        - Valve    
      type: Property    
    valveCurve:    
      description: 'A relationship to the curve of the setting property. Only required when valveType is GPV'    
      format: uri    
      type: Relationship    
    valveType:    
      description: 'The valve type of the element'    
      enum:    
        - PRV    
        - PSV    
        - PBV    
        - FCV    
        - TCV    
        - GPV    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    vertices:    
      description: 'Coordinates of all vertices in the valve, ordered from the startsAt node to the endsAt node and encoded as a GeoJSON '    
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
      type: Geoproperty    
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
</details>    
## Ejemplo de cargas útiles  
#### Válvula NGSI V2 valores clave Ejemplo  
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
#### Válvula NGSI V2 normalizada Ejemplo  
Aquí hay un ejemplo de una válvula en formato JSON como normalizada. Es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### Válvula NGSI-LD llave-valores Ejemplo  
Aquí hay un ejemplo de una válvula en formato JSON-LD como valores clave. Esto es compatible con NGSI-LD cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
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
#### Válvula NGSI-LD normalizada Ejemplo  
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
