Entidad: Bomba  
==============  
[Licencia abierta](https://github.com/smart-data-models//dataModel.WaterNetworkManagement/blob/master/Pump/LICENSE.md)  
Descripción global: **Esta entidad contiene una descripción armonizada de una bomba genérica hecha para el dominio de la gestión de la red de agua. Esta entidad está asociada principalmente con la gestión vertical del agua y las aplicaciones relacionadas con la IO**.  

## Lista de propiedades  

- `description`: Un texto opcional que describe otra información significativa sobre la unión  - `efficCurve`: La etiqueta de identificación de la curva que representa la eficiencia de la bomba de cable a agua en función de la tasa de flujo.  - `endsAt`: La identificación del nodo en el lado de descarga de la bomba  - `energyPattern`: La etiqueta de identificación del patrón de tiempo usado para describir la variación del precio de la energía a lo largo del día.  - `energyPrice`: El precio medio o nominal de la energía en unidades monetarias. Todas las unidades son aceptadas en el código [CEFACT](https://www.unece.org/cefact.html).  - `headCurve`: La etiqueta de identificación de la curva de la bomba utilizada para describir la relación entre la altura suministrada por la bomba y el flujo a través de la misma.  - `initialStatus`: El estado del nodo al comienzo de la simulación.  - `power`: La energía suministrada por la bomba. Todas las unidades son aceptadas en el código [CEFACT](https://www.unece.org/cefact.html).  - `pumpPattern`: La etiqueta de identificación de un patrón de tiempo usado para controlar el funcionamiento de la bomba. Los multiplicadores del patrón son equivalentes a los ajustes de velocidad. Un multiplicador de cero implica que la bomba se apagará durante el período de tiempo correspondiente  - `speed`: El ajuste de la velocidad relativa de la bomba. Todas las unidades son aceptadas en el código [CEFACT](https://www.unece.org/cefact.html).  - `startsAt`: La identificación del nodo en el lado de la succión de la bomba  - `status`: El estado dinámico del nodo  - `tag`: Una cadena de texto opcional utilizada para asignar la pipa a una categoría, tal vez una basada en la edad o el material  - `type`: Tipo de entidad NGSI-LD. Debe ser igual a Bomba.  - `vertices`: Las coordenadas de todos los vértices de la bomba, ordenadas desde el nodo de inicio hasta el nodo de fin y codificadas como un GeoJSON    
Propiedades requeridas  
- `endsAt`  - `id`  - `initialStatus`  - `startsAt`  - `type`  ## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Pump:    
  description: 'This entity contains a harmonised description of a generic pump made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.'    
  properties:    
    description:    
      description: 'An optional text that describes other significant information about the junction'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    efficCurve:    
      description: 'The ID label of the curve that represents the pump''s wire-to-water efficiency as a function of flow rate.'    
      format: uri    
      type: Relationship    
    endsAt:    
      description: 'The ID of the node on the discharge side of the pump'    
      format: uri    
      type: Relationship    
    energyPattern:    
      description: 'The ID label of the time pattern used to describe the variation in energy price throughout the day.'    
      format: uri    
      type: Relationship    
    energyPrice:    
      description: 'The average or nominal price of energy in monetary units. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        units: 'No unit'    
    headCurve:    
      description: 'The ID label of the pump curve used to describe the relationship between the head delivered by the pump and the flow through the Pump.'    
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
    power:    
      description: 'The power supplied by the pump. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: KiloWatt    
    pumpPattern:    
      description: 'The ID label of a time pattern used to control the pump''s operation. The multipliers of the pattern are equivalent to speed settings. A multiplier of zero implies that the pump will be shut off during the corresponding time period'    
      format: uri    
      type: Relationship    
    speed:    
      description: 'The relative speed setting of the Pump. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'Metre per Second'    
    startsAt:    
      description: 'The ID of the node on the suction side of the pump'    
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
      description: 'NGSI-LD Entity Type. It must be equal to Pump.'    
      enum:    
        - Pump    
      type: Property    
    vertices:    
      description: 'Coordinates of all vertices in the pump, ordered from the startsAt node to the endsAt node and encoded as a GeoJSON '    
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
    - startsAt    
    - endsAt    
  type: object    
```  
</details>    
## Ejemplo de cargas útiles  
#### Bomba NGSI V2 valores clave Ejemplo  
Aquí hay un ejemplo de una bomba en formato JSON como valores clave. Esto es compatible con NGSI V2 cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "85zhnf58-0d4c-h4g854g-b7d0-3310klm",  
    "type": "Pump",  
    "initialStatus": "OPEN",  
    "status": "OPEN",  
    "power": 100,  
    "speed": 1.2,  
    "startsAt": "63fe7d79-0d4c-4da9-b7d0-3340efa0656a",  
    "endsAt": "1863179e-3768-4480-9167-ff21f870dd19",  
    "tag": "DMA1",  
    "pumpPattern": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
    "efficCurve": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
    "energyPrice": 0.8,  
    "energyPattern": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
}  
```  
#### Bomba NGSI V2 normalizada Ejemplo  
Aquí hay un ejemplo de una bomba en formato JSON como normalizada. Es compatible con NGSI V2 cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "85zhnf58-0d4c-h4g854g-b7d0-3310klm",  
    "type": "Pump",  
    "initialStatus": {  
        "value": "OPEN"  
    },  
    "status": {  
        "value": "OPEN"  
    },  
    "power": {  
        "value": 100  
    },  
    "speed": {  
        "value": 1.2  
    },  
    "startsAt": {  
        "type": "Relationship",  
        "value": "63fe7d79-0d4c-4da9-b7d0-3340efa0656a"  
    },  
    "endsAt": {  
        "type": "Relationship",  
        "value": "1863179e-3768-4480-9167-ff21f870dd19"  
    },  
    "tag": {  
        "value": "DMA1"  
    },  
    "pumpPattern": {  
        "type": "Relationship",  
        "value": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
    },  
    "efficCurve": {  
        "type": "Relationship",  
        "value": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
    },  
    "energyPrice": {  
        "value": 0.8  
    },  
    "energyPattern": {  
        "type": "Relationship",  
        "value": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
    }  
}  
```  
#### Bomba NGSI-LD valores clave Ejemplo  
Aquí hay un ejemplo de una bomba en formato JSON-LD como valores clave. Esto es compatible con NGSI-LD cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:Pump:85zhnf58-0d4c-h4g854g-b7d0-3310klm",  
  "type": "Pump",  
  "createdAt": "2020-03-02T15:42:00Z",  
  "modifiedAt": "2020-03-02T15:45:00Z",  
  "initialStatus": "OPEN",  
  "status": "OPEN",  
  "power": 100,  
  "speed": 1.2,  
  "startsAt": "urn:ngsi-ld:Junction:63fe7d79-0d4c-4da9-b7d0-3340efa0656a",  
  "endsAt": "urn:ngsi-ld:Reservoir:1863179e-3768-4480-9167-ff21f870dd19",  
  "tag": "DMA1",  
  "pumpPattern": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
  "efficCurve": "urn:ngsi-ld:Curve:fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
  "energyPrice": 0.8,  
  "energyPattern": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/data-models/master/context.jsonld"  
  ]  
}  
```  
#### Bomba NGSI-LD normalizada Ejemplo  
Aquí hay un ejemplo de una bomba en formato JSON-LD como normalizada. Esto es compatible con NGSI-LD cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "urn:ngsi-ld:Pump:85zhnf58-0d4c-h4g854g-b7d0-3310klm",  
    "type": "Pump",  
    "createdAt": "2020-03-02T15:42:00Z",  
    "modifiedAt": "2020-03-02T15:45:00Z",  
    "initialStatus": {  
        "type": "Property",  
        "value": "OPEN"  
    },  
    "status": {  
        "type": "Property",  
        "value": "OPEN"  
    },  
    "power": {  
        "type": "Property",  
        "value": 100,  
        "unitCode": "KWT"  
    },  
    "speed": {  
        "type": "Property",  
        "value": 1.2,  
        "unitCode": "MTS"  
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
    "tag": {  
        "type": "Property",  
        "value": "DMA1"  
    },  
    "pumpPattern":{  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
    },  
    "efficCurve":{  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Curve:fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
    },  
    "energyPrice":{  
        "type": "Property",  
        "value": 0.8,  
        "unitCode": "C62"  
    },  
    "energyPattern":{  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context"  
    ]  
}  
```  
