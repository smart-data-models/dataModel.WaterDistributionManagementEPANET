Entité : Courbe  
===============  
Cette spécification est une **version temporelle**. Elle est générée automatiquement à partir des propriétés documentées décrites dans le schema.json condensé dans le fichier `model.yaml`. Un fichier temporaire `nouveau_modèle.yaml` a été créé dans chaque modèle de données pour éviter d'avoir un impact sur les scripts existants. Ainsi, la spécification sera incomplète tant que le fichier schema.json n'est pas mis à jour au nouveau format (documentation des propriétés). Une fois mis à jour, le fichier `model.yaml` (`nouveau_model.yaml`) doit être mis à jour également (automatiquement) . Plus d'informations dans ce [lien](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Tant qu'il s'agit d'un format provisoire, tout [feedback est le bienvenu dans ce formulaire](https://smartdatamodels.org/index.php/submit-an-issue-2/) en choisissant l'option "Feedback sur la nouvelle spécification".  
Description globale : **Cette entité contient une description harmonisée d'une courbe générique réalisée pour le domaine de la gestion des réseaux d'eau. Cette entité est principalement associée à la gestion verticale de l'eau et aux applications IdO connexes.  

## Liste des biens  

- `curveType`:   - `description`: Une description de cet article  - `tag`: Une chaîne de texte optionnelle utilisée pour assigner la courbe à une catégorie.  - `type`: Type d'entité NGSI-LD. Il doit être égal à Curve.  - `xData`: X points de données pour la courbe  - `yData`: Points de données Y pour la courbe    
Texte à inclure entre le titre général et la description.  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
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
</details>    
Texte à inclure après la liste des biens  
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
Voici un exemple de courbe au format JSON normalisé. Elle est compatible avec NGSI V2 lorsque l'on utilise "options=valeurs clés" et renvoie les données de contexte d'une entité individuelle.  
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
Voici un exemple de courbe au format JSON-LD comme valeurs clés. Cette courbe est compatible avec le format JSON-LD lorsqu'elle n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
Le texte après tout  
