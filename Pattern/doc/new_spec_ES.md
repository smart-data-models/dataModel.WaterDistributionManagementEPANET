Entidad: Patrón  
===============  
[Licencia abierta](https://github.com/smart-data-models//dataModel.WaterNetworkManagement/blob/master/Pattern/LICENSE.md)  
Descripción global: **Esta entidad contiene una descripción armonizada de un patrón genérico hecho para el dominio de la gestión de la red de agua. Esta entidad está principalmente asociada con la gestión vertical del agua y las aplicaciones de IO conexas**.  

## Lista de propiedades  

- `description`: Un texto opcional que describe otra información significativa sobre la unión  - `multipliers`: Los multiplicadores definen cómo se ajusta alguna cantidad base (por ejemplo, la demanda) para cada período de tiempo  - `startTime`: El momento en que el patrón comienza  - `tag`: Una cadena de texto opcional utilizada para asignar la pipa a una categoría, tal vez una basada en la edad o el material  - `timeStep`: El paso de tiempo usado para los multiplicadores. Todas las unidades son aceptadas en el código [CEFACT](https://www.unece.org/cefact.html).  - `type`: Tipo de entidad NGSI-LD. Tiene que ser el patrón    
Propiedades requeridas  
- `id`  - `multipliers`  - `startTime`  - `timeStep`  - `type`  ## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Pattern:    
  description: 'This entity contains a harmonised description of a generic pattern made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.'    
  properties:    
    description:    
      description: 'An optional text that describes other significant information about the junction'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    multipliers:    
      description: 'Multipliers define how some base quantity (e.g., demand) is adjusted for each time period'    
      items:    
        type: number    
      type: Property    
    startTime:    
      description: 'The time at which the pattern starts'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Time    
    tag:    
      description: 'An optional text string used to assign the pipe to a category, perhaps one based on age or material'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    timeStep:    
      description: 'The time step used for the multipliers. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        units: Second    
    type:    
      description: 'NGSI-LD Entity Type. It has to be Pattern'    
      enum:    
        - Pattern    
      type: Property    
  required:    
    - id    
    - type    
    - multipliers    
    - timeStep    
    - startTime    
  type: object    
```  
</details>    
## Ejemplo de cargas útiles  
#### Patrón NGSI V2 valores clave Ejemplo  
Aquí hay un ejemplo de un patrón en formato JSON como valores clave. Es compatible con NGSI V2 cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
    "type": "Pattern",  
    "multipliers": [  
        0.5692,  
        0.4647,  
        0.4385,  
        0.3604,  
        0.3098,  
        0.3345  
    ],  
    "timeStep": 3600,  
    "description": "Open Text",  
    "tag": "DMA1"  
}  
```  
#### Patrón NGSI V2 normalizado Ejemplo  
Aquí hay un ejemplo de un patrón en formato JSON como normalizado. Es compatible con NGSI V2 cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
    "type": "Pattern",  
    "multipliers": {  
        "value": [  
            0.5692,  
            0.4647,  
            0.4385,  
            0.3604,  
            0.3098,  
            0.3345  
        ]  
    },  
    "timeStep": {  
        "value": 3600  
    },  
    "description": {  
        "value": "Open Text"  
    },  
    "tag": {  
        "value": "DMA1"  
    }  
}  
```  
#### Patrón NGSI-LD valores clave Ejemplo  
Aquí hay un ejemplo de un patrón en formato JSON-LD como valores clave. Es compatible con NGSI-LD cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context"],  
 "createdAt": "2020-02-20T17:43:00Z",  
 "description": "Open Text",  
 "id": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
 "modifiedAt": "2020-02-20T17:43:00Z",  
 "multipliers": [0.5692, 0.4647, 0.4385, 0.3604, 0.3098, 0.3345],  
 "startTime": "00:00",  
 "tag": "DMA1",  
 "timeStep": 3600,  
 "type": "Pattern"}  
```  
#### Patrón NGSI-LD normalizado Ejemplo  
Aquí hay un ejemplo de un patrón en formato JSON-LD normalizado. Este es compatible con NGSI-LD cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
    "type": "Pattern",  
    "createdAt": "2020-02-20T17:43:00Z",  
    "modifiedAt": "2020-02-20T17:43:00Z",  
    "multipliers": {  
        "type": "Property",  
        "value": [0.5692, 0.4647, 0.4385, 0.3604, 0.3098, 0.3345],  
        "unitCode":"C62"  
    },  
    "timeStep": {  
        "type": "Property",  
        "value": 3600,  
        "unitCode": "SEC"  
    },  
    "description": {  
        "type": "Property",  
        "value": "Open Text"  
    },  
    "startTime": {  
        "type": "Property",  
        "value": "00:00"  
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
