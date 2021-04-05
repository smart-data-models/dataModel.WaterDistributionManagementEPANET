Entité : Pattern  
================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.WaterDistributionManagementEPANET/blob/master/Pattern/LICENSE.md)  
Description globale : **Cette entité contient une description harmonisée d'un patron générique réalisé pour le domaine de la gestion des réseaux d'eau. Cette entité est principalement associée à la gestion verticale de l'eau et aux applications IoT connexes**.  

## Liste des propriétés  

- `alternateName`: Un nom alternatif pour cet élément  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `multipliers`: Les multiplicateurs définissent comment une certaine quantité de base (par exemple, la demande) est ajustée pour chaque période de temps.  - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `startTime`: L'heure à laquelle le motif commence  - `tag`: Une chaîne de texte facultative utilisée pour affecter le tuyau à une catégorie, peut-être basée sur l'âge ou le matériau.  - `timeStep`: Le pas de temps utilisé pour les multiplicateurs. Toutes les unités sont acceptées en code [CEFACT](https://www.unece.org/cefact.html).  - `type`: Type d'entité NGSI-LD. Il doit être de type Pattern    
Propriétés requises  
- `id`  - `multipliers`  - `startTime`  - `timeStep`  - `type`  ## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Pattern:    
  description: 'This entity contains a harmonised description of a generic pattern made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    id:    
      anyOf: &pattern_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      type: Property    
    multipliers:    
      description: 'Multipliers define how some base quantity (e.g., demand) is adjusted for each time period'    
      items:    
        type: number    
      type: Property    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *pattern_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
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
## Exemples de charges utiles  
#### Modèle de valeurs clés NGSI-v2 Exemple  
Voici un exemple de Pattern au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### Modèle NGSI-v2 normalisé Exemple  
Voici un exemple d'un Pattern au format JSON-LD tel que normalisé. Ce format est compatible avec la NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### Modèle de valeurs clés NGSI-LD Exemple  
Voici un exemple de Pattern au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ],  
  "createdAt": "2020-02-20T17:43:00Z",  
  "description": "Open Text",  
  "id": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
  "modifiedAt": "2020-02-20T17:43:00Z",  
  "multipliers": [  
    0.5692,  
    0.4647,  
    0.4385,  
    0.3604,  
    0.3098,  
    0.3345  
  ],  
  "tag": "DMA1",  
  "timeStep": 3600,  
  "startTime": "2020-02-20T17:43:00Z",  
  "type": "Pattern"  
}  
```  
#### Modèle NGSI-LD normalisé Exemple  
Voici un exemple de Pattern au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
  "type": "Pattern",  
  "createdAt": "2020-02-20T17:43:00Z",  
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
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
