Entidad: Pipa  
=============  
[Licencia abierta](https://github.com/smart-data-models//dataModel.WaterNetworkManagement/blob/master/Pipe/LICENSE.md)  
Descripción global: **Esta entidad contiene una descripción armonizada de una tubería genérica hecha para el dominio de la gestión de la red de agua. Esta entidad está principalmente asociada con la gestión vertical del agua y las aplicaciones relacionadas con la IO**.  

## Lista de propiedades  

- `bulkCoeff`: Use un valor positivo para el crecimiento y un valor negativo para la decadencia. Todas las unidades son aceptadas en el código [CEFACT](https://www.unece.org/cefact.html).  - `description`: Un texto opcional que describe otra información significativa sobre la unión  - `diameter`: El diámetro del tubo  - `endsAt`: La identificación del nodo donde termina el tubo  - `initialStatus`: El estado del nodo al comienzo de la simulación.  - `length`: La longitud real del tubo. Todas las unidades son aceptadas en el código [CEFACT](https://www.unece.org/cefact.html).  - `minorLoss`: Coeficiente de pérdida menor unitario asociado a las curvas, accesorios, etc.  - `roughness`: El coeficiente de rugosidad de la tubería.  - `startsAt`: El ID del nodo donde comienza la tubería  - `status`: El estado dinámico del nodo  - `tag`: Una cadena de texto opcional utilizada para asignar la pipa a una categoría, tal vez una basada en la edad o el material  - `type`: Tipo de entidad NGSI-LD. Tiene que ser Tubo  - `vertices`: Las coordenadas de todos los vértices de la tubería, ordenadas desde el nodo de inicio hasta el nodo de fin y codificadas como un GeoJSON  - `wallCoeff`: El coeficiente de reacción de la pared del tubo. Use un valor positivo para el crecimiento y un valor negativo para la descomposición. Todas las unidades son aceptadas en el código [CEFACT](https://www.unece.org/cefact.html).    
Propiedades requeridas  
- `diameter`  - `endsAt`  - `id`  - `initialStatus`  - `length`  - `minorLoss`  - `roughness`  - `startsAt`  - `type`  ## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Pipe:    
  description: 'This entity contains a harmonised description of a generic pipe made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.'    
  properties:    
    bulkCoeff:    
      description: 'Use a positive value for growth and a negative value for decay. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'reciprocal day The bulk reaction coefficient for the pipe'    
    description:    
      description: 'An optional text that describes other significant information about the junction'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    diameter:    
      description: 'The pipe diameter'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: Millimetre    
    endsAt:    
      description: 'The ID of the node where the pipe ends'    
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
    length:    
      description: 'The actual length of the pipe. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: Metre    
    minorLoss:    
      description: 'Unitless minor loss coefficient associated with bends, fittings, etc'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'No unit'    
    roughness:    
      description: 'The roughness coefficient of the Pipe.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'No unit'    
    startsAt:    
      description: 'The ID of the node where the pipe begins'    
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
      description: 'NGSI-LD Entity Type. It has to be Pipe'    
      enum:    
        - Pipe    
      type: Property    
    vertices:    
      description: 'Coordinates of all vertices in the pipe, ordered from the startsAt node to the endsAt node and encoded as a GeoJSON '    
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
    wallCoeff:    
      description: 'The wall reaction coefficient for the pipe. Use a positive value for growth and a negative value for decay. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: mg/m²/day    
  required:    
    - id    
    - type    
    - initialStatus    
    - length    
    - diameter    
    - roughness    
    - minorLoss    
    - startsAt    
    - endsAt    
  type: object    
```  
</details>    
## Ejemplo de cargas útiles  
#### Tubo NGSI V2 Ejemplo de valores clave  
Aquí hay un ejemplo de una tubería en formato JSON como valores clave. Es compatible con NGSI V2 cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "74azsty-70d4l-4da9-b7d0-3340ef655nnb",  
    "type": "Pipe",  
    "initialStatus": "OPEN",  
    "status": "OPEN",  
    "length": 52.90,  
    "diameter": 203.00,  
    "roughness": 72.4549,  
    "minorLoss": 72.4549,  
    "tag": "DMA1",  
    "description": "Free Text",  
    "startsAt": "63fe7d79-0d4c-4da9-b7d0-3340efa0656a",  
    "endsAt": "1863179e-3768-4480-9167-ff21f870dd19",  
    "bulkCoeff": 72.4549,  
    "wallCoeff": 72.4549  
}  
```  
#### Tubo NGSI V2 normalizado Ejemplo  
Aquí hay un ejemplo de un tubo en formato JSON como normalizado. Es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "74azsty-70d4l-4da9-b7d0-3340ef655nnb",  
    "type": "Pipe",  
    "initialStatus": {  
        "value": "OPEN"  
    },  
    "status": {  
        "value": "OPEN"  
    },  
    "length": {  
        "value": 52.90  
    },  
    "diameter": {  
        "value": 203.00  
    },  
    "roughness": {  
        "value": 72.4549  
    },  
    "minorLoss": {  
        "value": 72.4549  
    },  
    "tag": {  
        "value": "DMA1"  
    },  
    "description": {  
        "value": "Free Text"  
    },  
    "startsAt": {  
        "type": "Relationship",  
        "value": "63fe7d79-0d4c-4da9-b7d0-3340efa0656a"  
    },  
    "endsAt": {  
        "type": "Relationship",  
        "value": "1863179e-3768-4480-9167-ff21f870dd19"  
    },  
    "bulkCoeff": {  
        "value": 72.4549  
    },  
    "wallCoeff": {  
        "value": 72.4549  
    }  
}  
```  
#### Tubo NGSI-LD llave-valores Ejemplo  
Aquí hay un ejemplo de un tubo en formato JSON-LD como valores clave. Esto es compatible con NGSI-LD cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context"],  
 "bulkCoeff": 72.4549,  
 "createdAt": "2020-02-20T15:42:00Z",  
 "description": "Free Text",  
 "diameter": 203.0,  
 "endsAt": "urn:ngsi-ld:Reservoir:1863179e-3768-4480-9167-ff21f870dd19",  
 "id": "urn:ngsi-ld:Pipe:74azsty-70d4l-4da9-b7d0-3340ef655nnb",  
 "initialStatus": "OPEN",  
 "length": 52.9,  
 "minorLoss": 72.4549,  
 "modifiedAt": "2020-02-20T15:45:00Z",  
 "roughness": 72.4549,  
 "startsAt": "urn:ngsi-ld:Junction:63fe7d79-0d4c-4da9-b7d0-3340efa0656a",  
 "status": "OPEN",  
 "tag": "DMA1",  
 "type": "Pipe",  
 "wallCoeff": 72.4549}  
```  
#### Tubo NGSI-LD normalizado Ejemplo  
Aquí hay un ejemplo de un tubo en formato JSON-LD como normalizado. Esto es compatible con NGSI-LD cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "urn:ngsi-ld:Pipe:74azsty-70d4l-4da9-b7d0-3340ef655nnb",  
    "type": "Pipe",  
    "createdAt": "2020-02-20T15:42:00Z",  
    "modifiedAt": "2020-02-20T15:45:00Z",  
    "initialStatus": {  
        "type": "Property",  
        "value": "OPEN"  
    },  
    "status": {  
        "type": "Property",  
        "value": "OPEN"  
    },  
    "length": {  
        "type": "Property",  
        "value": 52.90,  
        "unitCode": "MTR"  
    },  
    "diameter": {  
        "type": "Property",  
        "value": 203.00,  
        "unitCode": "MMT"  
    },  
    "roughness": {  
        "type": "Property",  
        "value": 72.4549,  
        "unitCode": "C62"  
    },  
    "minorLoss": {  
        "type": "Property",  
        "value": 72.4549,  
        "unitCode": "C62"  
    },  
    "tag": {  
        "type": "Property",  
        "value": "DMA1"  
    },  
     "description": {  
        "type": "Property",  
        "value": "Free Text"  
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
    "bulkCoeff":{  
        "type": "Property",  
        "value": 72.4549,  
        "unitCode": "E91"  
    },  
    "wallCoeff":{  
        "type": "Property",  
        "value": 72.4549,  
        "unitCode": "RRC"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context"  
    ]  
}  
```  
