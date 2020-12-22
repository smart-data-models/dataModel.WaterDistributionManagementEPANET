Entité : Courbe  
===============  
[Licence ouverte](https://github.com/smart-data-models//dataModel.WaterNetworkManagement/blob/master/Curve/LICENSE.md)  
Description globale : **Cette entité contient une description harmonisée d'une courbe générique réalisée pour le domaine de la gestion des réseaux d'eau. Cette entité est principalement associée à la gestion verticale de l'eau et aux applications IdO connexes.  

## Liste des biens  

- `curveType`: Type de courbe de l'entité.  - `description`: Un texte optionnel qui décrit d'autres informations importantes sur la jonction  - `tag`: Une chaîne de texte facultative utilisée pour classer la pipe dans une catégorie, peut-être en fonction de l'âge ou du matériau  - `type`: Type d'entité NGSI-LD. Il doit être égal à Curve.  - `xData`: X points de données pour la courbe  - `yData`: Points de données Y pour la courbe    
Propriétés requises  
- `curveType`  - `id`  - `type`  - `xData`  - `yData`  ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
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
## Exemples de charges utiles  
#### Courbe NGSI V2 valeurs clés Exemple  
Voici un exemple de courbe au format JSON comme valeurs clés. Elle est compatible avec NGSI V2 lorsque l'on utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
#### Courbe NGSI V2 normalisée Exemple  
Voici un exemple de courbe au format JSON normalisé. Elle est compatible avec la version 2 du NGSI lorsqu'elle n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
#### Courbe NGSI-LD valeurs clés Exemple  
Voici un exemple de courbe au format JSON-LD comme valeurs clés. Elle est compatible avec le format NGSI-LD lorsqu'on utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
#### Courbe NGSI-LD normalisée Exemple  
Voici un exemple d'une courbe au format JSON-LD telle que normalisée. Cette courbe est compatible avec le format JSON-LD lorsqu'elle n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
