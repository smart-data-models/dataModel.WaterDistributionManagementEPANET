Entidad: Curva  
==============  
[Licencia abierta](https://github.com/smart-data-models//dataModel.WaterNetworkManagement/blob/master/Curve/LICENSE.md)  
Descripción global: **Esta entidad contiene una descripción armonizada de una curva genérica hecha para el dominio de la gestión de la red de agua. Esta entidad está principalmente asociada con la gestión vertical del agua y las aplicaciones relacionadas con la IO**.  

## Lista de propiedades  

- `curveType`: El tipo de curva de la entidad.  - `description`: Un texto opcional que describe otra información significativa sobre la unión  - `tag`: Una cadena de texto opcional utilizada para asignar la pipa a una categoría, tal vez una basada en la edad o el material  - `type`: Tipo de entidad NGSI-LD. Debe ser igual a Curva.  - `xData`: X puntos de datos para la curva  - `yData`: Los puntos de datos Y de la curva    
Propiedades requeridas  
- `curveType`  - `id`  - `type`  - `xData`  - `yData`    
El texto se incluirá entre el título general y la descripción.  
## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Curve:    
  description: 'This entity contains a harmonised description of a generic curve made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.'    
  properties:    
    curveType:    
      description: 'Entity''s curve type.'    
      enum:    
        - FLOW-HEAD    
        - FLOW-EFFICIENCY    
        - FLOW-HEADLOSS    
        - LEVEL-VOLUME    
      type: Property    
    description:    
      description: 'An optional text that describes other significant information about the junction'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    tag:    
      description: 'An optional text string used to assign the pipe to a category, perhaps one based on age or material'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    type:    
      description: 'NGSI-LD Entity Type. It must be equal to Curve.'    
      enum:    
        - Curve    
      type: Property    
    xData:    
      description: 'X data points for the curve'    
      items:    
        type: number    
      type: Property    
    yData:    
      description: 'Y data points for the curve'    
      items:    
        type: number    
      type: Property    
  required:    
    - id    
    - type    
    - curveType    
    - xData    
    - yData    
  type: object    
```  
</details>    
El texto se incluirá después de la lista de propiedades  
## Ejemplo de cargas útiles  
#### Ejemplo de valores clave de la curva NGSI V2  
Aquí hay un ejemplo de una curva en formato JSON como valores clave. Es compatible con NGSI V2 cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "fAM-8ca3-4533-a2eb-12015",  
  "type": "Curve",  
  "curveType": {  
    "type": "Property",  
    "value": "FLOW-HEAD"  
  },  
  "xData": {  
    "type": "Property",  
    "value": [  
      0.5692,  
      0.4647  
    ]  
  },  
  "yData": {  
    "type": "Property",  
    "value": [  
      0.5692,  
      0.4647  
    ]  
  },  
  "description": {  
    "type": "Property",  
    "value": "Free Text"  
  },  
  "tag": {  
    "type": "Property",  
    "value": "DMA1"  
  }  
}  
```  
#### Curva NGSI V2 normalizada Ejemplo  
Aquí hay un ejemplo de una curva en formato JSON como normalizada. Es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "fAM-8ca3-4533-a2eb-12015",  
    "type": "Curve",  
    "dateCreated": {  
        "type": "DateTime",  
        "value": "2020-02-16T17:43:00Z"  
    },  
    "dateModified": {  
        "type": "DateTime",  
        "value": "2020-02-16T17:43:00Z"  
    },  
    "curveType": {  
        "value": "FLOW-HEAD"  
    },  
    "xData": {  
        "value": [  
            0.5692,  
            0.4647  
        ]  
    },  
    "yData": {  
        "value": [  
            0.5692,  
            0.4647  
        ]  
    },  
    "description": {  
        "value": "Free Text"  
    },  
    "tag": {  
        "value": "DMA1"  
    }  
}  
```  
#### Curva NGSI-LD clave-valores Ejemplo  
Aquí hay un ejemplo de una curva en formato JSON-LD como valores clave. Es compatible con NGSI-LD cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "@context": [  
    "https://schema.lab.fiware.org/ld/context"  
  ],  
  "id": "fAM-8ca3-4533-a2eb-12015",  
  "type": "Curve",  
  "curveType": {  
    "type": "Property",  
    "value": "FLOW-HEAD"  
  },  
  "xData": {  
    "type": "Property",  
    "value": [  
      0.5692,  
      0.4647  
    ]  
  },  
  "yData": {  
    "type": "Property",  
    "value": [  
      0.5692,  
      0.4647  
    ]  
  },  
  "description": {  
    "type": "Property",  
    "value": "Free Text"  
  },  
  "tag": {  
    "type": "Property",  
    "value": "DMA1"  
  }  
}  
```  
#### Curva NGSI-LD normalizada Ejemplo  
Aquí hay un ejemplo de una curva en formato JSON-LD normalizada. Es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "urn:ngsi-ld:Curve:fAM-8ca3-4533-a2eb-12015",  
    "type": "Curve",  
    "createdAt": "2020-02-16T17:43:00Z",  
    "modifiedAt": "2020-02-16T17:43:00Z",  
    "curveType":{  
        "type": "Property",  
        "value": "FLOW-HEAD"  
    },  
    "xData": {  
        "type": "Property",  
        "value": [0.5692, 0.4647],  
        "unitCode":"C62"  
    },  
    "yData": {  
        "type": "Property",  
        "value": [0.5692, 0.4647],  
        "unitCode":"C62"  
    },  
    "description": {  
        "type": "Property",  
        "value": "Free Text"  
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
El texto después de todo  
