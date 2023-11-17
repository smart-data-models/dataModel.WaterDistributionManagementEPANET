<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entité : Modèle    
===============<!-- /10-Header -->    
<!-- 15-License -->    
[Licence ouverte] (https://github.com/smart-data-models//dataModel.WaterDistributionManagementEPANET/blob/master/Pattern/LICENSE.md)    
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Description globale : **Cette entité contient une description harmonisée d'un modèle générique réalisé pour le domaine de la gestion des réseaux d'eau. Cette entité est principalement associée au domaine vertical de la gestion de l'eau et aux applications IoT connexes.**    
version : 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste des propriétés    
<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.    
- `alternateName[string]`: Un nom alternatif pour ce poste  - `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `id[*]`: Identifiant unique de l'entité  - `multipliers[array]`: Les multiplicateurs définissent la manière dont une quantité de base (par exemple, la demande) est ajustée pour chaque période.  - `name[string]`: Le nom de cet élément  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `startTime[date-time]`: L'heure à laquelle le motif commence  . Model: [https://schema.org/Time](https://schema.org/Time)- `tag[string]`: Une chaîne de texte facultative utilisée pour classer le tuyau dans une catégorie, par exemple en fonction de l'âge ou du matériau.  . Model: [https://schema.org/Text](https://schema.org/Text)- `timeStep[number]`: Le pas de temps utilisé pour les multiplicateurs. Toutes les unités sont acceptées dans le code [CEFACT] (https://www.unece.org/cefact.html).  - `type[string]`: Type d'entité NGSI-LD. Il doit s'agir d'un motif  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propriétés requises    
- `id`  - `multipliers`  - `startTime`  - `timeStep`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modèle de données description des propriétés    
Classés par ordre alphabétique (cliquez pour plus de détails)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
Pattern:      
  description: This entity contains a harmonised description of a generic pattern made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.      
  properties:      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dateCreated:      
      description: Entity creation timestamp. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    id:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Unique identifier of the entity      
      x-ngsi:      
        type: Property      
    multipliers:      
      description: 'Multipliers define how some base quantity (e.g., demand) is adjusted for each time period'      
      items:      
        type: number      
      type: array      
      x-ngsi:      
        type: Property      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    owner:      
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    seeAlso:      
      description: list of uri pointing to additional resources about the item      
      oneOf:      
        - items:      
            format: uri      
            type: string      
          minItems: 1      
          type: array      
        - format: uri      
          type: string      
      x-ngsi:      
        type: Property      
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    startTime:      
      description: The time at which the pattern starts      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/Time      
        type: Property      
    tag:      
      description: 'An optional text string used to assign the pipe to a category, perhaps one based on age or material'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    timeStep:      
      description: 'The time step used for the multipliers. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code'      
      type: number      
      x-ngsi:      
        type: Property      
        units: Second      
    type:      
      description: NGSI-LD Entity Type. It has to be Pattern      
      enum:      
        - Pattern      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
    - multipliers      
    - timeStep      
    - startTime      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.WaterDistributionManagementEPANET/blob/master/Pattern/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.WaterDistributionManagementEPANET/Pattern/schema.json      
  x-model-tags: FIWARE4WATER      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Exemples de charges utiles    
#### Pattern NGSI-v2 key-values Exemple    
Voici un exemple de motif au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
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
  "tag": "DMA1",  
  "startTime": "2020-02-20T17:43:00Z"  
}  
```  
</details>    
#### Modèle NGSI-v2 normalisé Exemple    
Voici un exemple de motif au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec l'INSG-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
  "type": "Pattern",  
  "multipliers": {  
    "type": "StructuredValue",  
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
    "type": "Number",  
    "value": 3600  
  },  
  "startTime": {  
    "type": "DateTime",  
    "value": "2020-02-20T17:43:00Z"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Open Text"  
  },  
  "tag": {  
    "type": "Text",  
    "value": "DMA1"  
  }  
}  
```  
</details>    
#### Modèle de valeurs clés NGSI-LD Exemple    
Voici un exemple de motif au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
  "type": "Pattern",  
  "createdAt": "2020-02-20T17:43:00Z",  
  "description": "Open Text",  
  "modifiedAt": "2020-02-20T17:43:00Z",  
  "multipliers": [  
    0.5692,  
    0.4647,  
    0.4385,  
    0.3604,  
    0.3098,  
    0.3345  
  ],  
  "startTime": "2020-02-20T17:43:00Z",  
  "tag": "DMA1",  
  "timeStep": 3600,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.WaterDistributionManagementEPANET/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### Modèle NGSI-LD normalisé Exemple    
Voici un exemple de motif au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
    "type": "Pattern",  
    "createdAt": "2020-02-20T17:43:00Z",  
    "description": {  
        "type": "Property",  
        "value": "Open Text"  
    },  
    "modifiedAt": "2020-02-20T17:43:00Z",  
    "multipliers": {  
        "type": "Property",  
        "value": [  
            0.5692,  
            0.4647,  
            0.4385,  
            0.3604,  
            0.3098,  
            0.3345  
        ],  
        "unitCode": "C62"  
    },  
    "startTime": {  
        "type": "Property",  
        "value": "00:00"  
    },  
    "tag": {  
        "type": "Property",  
        "value": "DMA1"  
    },  
    "timeStep": {  
        "type": "Property",  
        "value": 3600,  
        "unitCode": "SEC"  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.WaterDistributionManagementEPANET/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
