Entidad: Curva  
==============  
Esta especificación es una **versión temporal**. Se genera automáticamente a partir de las propiedades documentadas descritas en el schema.json condensadas en el archivo `model.yaml`. Se ha creado un archivo temporal `nuevo_modelo.yaml` en cada modelo de datos para evitar el impacto en los scripts existentes. Por lo tanto, la especificación estará incompleta mientras el schema.json no se actualice al nuevo formato (documentando las propiedades). Una vez actualizado el `modelo.yaml` (`nuevo_modelo.yaml`) necesita ser actualizado también (automáticamente) . Más información en este [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Mientras sea un formato provisional cualquier [feedback es bienvenido en este formulario](https://smartdatamodels.org/index.php/submit-an-issue-2/) eligiendo la opción `Feedback on the new specification`.  
Descripción global: **Esta entidad contiene una descripción armonizada de una curva genérica hecha para el dominio de la gestión de la red de agua. Esta entidad está principalmente asociada con la gestión vertical del agua y las aplicaciones relacionadas con la IO**.  

## Lista de propiedades  

`curveType`:   `description`:   `tag`:   `type`: Tipo de entidad NGSI-LD. Debe ser igual a Curva.  `xData`:   `yData`:     
El texto se incluirá entre el título general y la descripción.  
## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente  
```yaml  
Curve:    
  description: 'This entity contains a harmonised description of a generic curve made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.'    
  properties:    
    curveType:    
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
            - FLOW-HEAD    
            - FLOW-EFFICIENCY    
            - FLOW-HEADLOSS    
            - LEVEL-VOLUME    
          type:    
            - number    
            - string    
            - array    
      required:    
        - type    
        - value    
      type: object    
    description:    
      properties: &curve_-_properties_-_tag_-_properties    
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
      required: &curve_-_properties_-_tag_-_required    
        - type    
        - value    
      type: object    
    tag:    
      properties: *curve_-_properties_-_tag_-_properties    
      required: *curve_-_properties_-_tag_-_required    
      type: object    
    type:    
      description: 'NGSI-LD Entity Type. It must be equal to Curve.'    
      enum:    
        - Curve    
      type: Property    
    xData:    
      properties: *curve_-_properties_-_tag_-_properties    
      required: *curve_-_properties_-_tag_-_required    
      type: object    
    yData:    
      properties: *curve_-_properties_-_tag_-_properties    
      required: *curve_-_properties_-_tag_-_required    
      type: object    
  required:    
    - id    
    - type    
    - curveType    
    - xData    
    - yData    
  type: object    
```  
El texto se incluirá después de la lista de propiedades  
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
Aquí hay un ejemplo de una curva en formato JSON como normalizada. Es compatible con NGSI V2 cuando se utiliza "opciones=valores clave" y devuelve los datos de contexto de una entidad individual.  
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
Aquí hay un ejemplo de una curva en formato JSON-LD como valores clave. Es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
