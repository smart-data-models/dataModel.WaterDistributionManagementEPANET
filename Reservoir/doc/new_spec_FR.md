Entité : Réservoir  
==================  
Cette spécification est une **version temporelle**. Elle est générée automatiquement à partir des propriétés documentées décrites dans le schema.json condensé dans le fichier `model.yaml`. Un fichier temporaire `nouveau_modèle.yaml` a été créé dans chaque modèle de données pour éviter d'avoir un impact sur les scripts existants. Ainsi, la spécification sera incomplète tant que le fichier schema.json n'est pas mis à jour au nouveau format (documentation des propriétés). Une fois mis à jour, le fichier `model.yaml` (`nouveau_model.yaml`) doit être mis à jour également (automatiquement) . Plus d'informations dans ce [lien](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Tant qu'il s'agit d'un format provisoire, tout [feedback est le bienvenu dans ce formulaire](https://smartdatamodels.org/index.php/submit-an-issue-2/) en choisissant l'option "Feedback sur la nouvelle spécification".  
Description globale : **Cette entité contient une description harmonisée d'un réservoir générique fait pour le domaine de la gestion des réseaux d'eau. Cette entité est principalement associée aux applications verticales de gestion de l'eau et aux applications IdO connexes.**  

## Liste des biens  

- `address`: L'adresse postale.  - `areaServed`: La zone géographique où un service ou un article offert est fourni.  - `description`:   - `elevation`:   - `hasInlet`:   - `hasOutlet`:   - `headPattern`:   - `initialQuality`:   - `location`:   - `reservoirHead`:   - `sourceCategory`:   - `tag`:   - `type`: Type d'entité NGSI-LD  ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Reservoir:    
  description: 'This entity contains a harmonised description of a generic Reservoir made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.'    
  properties:    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          type: string    
        addressLocality:    
          type: string    
        addressRegion:    
          type: string    
        areaServed:    
          type: string    
        postOfficeBoxNumber:    
          type: string    
        postalCode:    
          type: string    
        streetAddress:    
          type: string    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided.'    
      type: Property    
    description:    
      properties: &reservoir_-_properties_-_elevation_-_properties    
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
      required: &reservoir_-_properties_-_elevation_-_required    
        - type    
        - value    
      type: object    
    elevation:    
      properties: *reservoir_-_properties_-_elevation_-_properties    
      required: *reservoir_-_properties_-_elevation_-_required    
      type: object    
    hasInlet:    
      properties: &reservoir_-_properties_-_hasoutlet_-_properties    
        createdAt:    
          format: date-time    
          type: string    
        modifiedAt:    
          format: date-time    
          type: string    
        object:    
          format: uri    
          type:    
            - string    
        observedAt:    
          format: date-time    
          type: string    
        type:    
          enum:    
            - Relationship    
          type: string    
      required: &reservoir_-_properties_-_hasoutlet_-_required    
        - type    
        - object    
      type: object    
    hasOutlet:    
      properties: *reservoir_-_properties_-_hasoutlet_-_properties    
      required: *reservoir_-_properties_-_hasoutlet_-_required    
      type: object    
    headPattern:    
      properties: *reservoir_-_properties_-_hasoutlet_-_properties    
      required: *reservoir_-_properties_-_hasoutlet_-_required    
      type: object    
    initialQuality:    
      properties: *reservoir_-_properties_-_elevation_-_properties    
      required: *reservoir_-_properties_-_elevation_-_required    
      type: object    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
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
        - properties:    
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
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - properties:    
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
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      title: 'GeoJSON Geometry'    
    reservoirHead:    
      properties: *reservoir_-_properties_-_elevation_-_properties    
      required: *reservoir_-_properties_-_elevation_-_required    
      type: object    
    sourceCategory:    
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
        sourcePattern:    
          properties:    
            createdAt:    
              format: date-time    
              type: string    
            modifiedAt:    
              format: date-time    
              type: string    
            object:    
              format: uri    
              type:    
                - string    
            observedAt:    
              format: date-time    
              type: string    
            type:    
              enum:    
                - Relationship    
              type: string    
          required:    
            - type    
            - object    
          type: object    
        sourceQuality:    
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
              type:    
                - number    
                - string    
          required:    
            - type    
            - value    
          type: object    
        sourceType:    
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
                - CONCEN    
                - MASS    
                - FLOWPACED    
                - SETPOINT    
              type:    
                - number    
                - string    
          required:    
            - type    
            - value    
          type: object    
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
      required:    
        - type    
        - value    
        - sourceType    
        - sourceQuality    
        - sourcePattern    
      type: object    
    tag:    
      properties: *reservoir_-_properties_-_elevation_-_properties    
      required: *reservoir_-_properties_-_elevation_-_required    
      type: object    
    type:    
      description: 'NGSI-LD Entity Type'    
      enum:    
        - Reservoir    
      type: string    
  required:    
    - id    
    - type    
    - location    
    - reservoirHead    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### Réservoir NGSI V2 valeurs clés Exemple  
Voici un exemple de réservoir au format JSON en tant que valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "1863179e-3768-4480-9167-ff21f870dd19",  
    "type": "Reservoir",  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            24.30623,  
            60.07966  
        ]  
    },  
    "reservoirHead": 59.00,  
    "headPattern": "fbcb5fc8-8ca3-4533",  
    "elevation": 105.8,  
    "description": "This entity contains a harmonised description of a Reservoir",  
    "initialQuality": 0.5,  
    "sourceCategory": {  
        "value": "CategroyX",  
        "sourceType": "MASS",  
        "sourceQuality": 1.2,  
        "sourcePattern": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
    },  
    "tag": "DMA1"  
}  
```  
#### Réservoir NGSI V2 normalisé Exemple  
Voici un exemple de réservoir au format JSON tel que normalisé. Il est compatible avec NGSI V2 lorsqu'il utilise "options=valeurs clés" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "1863179e-3768-4480-9167-ff21f870dd19",  
    "type": "Reservoir",  
    "location": {  
        "type": "geo:json",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                24.30623,  
                60.07966  
            ]  
        }  
    },  
    "reservoirHead": {  
        "value": 59.00  
    },  
    "headPattern": {  
        "type": "Relationship",  
        "value": "fbcb5fc8-8ca3-4533"  
    },  
    "elevation": {  
        "value": 105.8  
    },  
    "description": {  
        "value": "This entity contains a harmonised description of a Reservoir"  
    },  
    "initialQuality": {  
        "value": 0.5  
    },  
    "sourceCategory": {  
        "value": {  
            "value": "CategroyX",  
            "sourceType": {  
                "value": "MASS"  
            },  
            "sourceQuality": {  
                "value": 1.2  
            },  
            "sourcePattern": {  
                "type": "Relationship",  
                "value": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
            }  
        }  
    },  
    "tag": {  
        "value": "DMA1"  
    }  
}  
```  
#### Réservoir NGSI-LD valeurs clés Exemple  
Voici un exemple de réservoir au format JSON-LD comme valeurs clés. Ce format est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context"],  
 "createdAt": "2020-03-02T15:42:00Z",  
 "description": "This entity contains a harmonised description of a Reservoir",  
 "elevation": 105.8,  
 "headPattern": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533",  
 "id": "urn:ngsi-ld:Reservoir:1863179e-3768-4480-9167-ff21f870dd19",  
 "initialQuality": 0.5,  
 "location": {"coordinates": [24.30623, 60.07966], "type": "Point"},  
 "modifiedAt": "2020-03-02T15:45:00Z",  
 "reservoirHead": 59.0,  
 "sourceCategory": "CategroyX",  
 "tag": "DMA1",  
 "type": "Reservoir"}  
```  
#### Réservoir NGSI-LD normalisé Exemple  
Voici un exemple de réservoir au format JSON-LD tel que normalisé. Ce format est compatible avec JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "urn:ngsi-ld:Reservoir:1863179e-3768-4480-9167-ff21f870dd19",  
    "type": "Reservoir",  
    "createdAt": "2020-03-02T15:42:00Z",  
    "modifiedAt": "2020-03-02T15:45:00Z",  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                24.30623,  
                60.07966  
            ]  
        }  
    },  
    "reservoirHead": {  
        "type": "Property",  
        "value": 59.00,  
        "unitCode": "MTR"  
    },  
    "headPattern": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533"  
    },  
    "elevation": {  
        "type": "Property",  
        "value": 105.8,  
        "unitCode": "MTR"  
    },  
    "description": {  
        "type": "Property",  
        "value": "This entity contains a harmonised description of a Reservoir"  
    },  
    "initialQuality": {  
        "type": "Property",  
        "value": 0.5,  
        "unitCode":"M1"  
    },  
    "sourceCategory": {  
        "type": "Property",  
        "value": "CategroyX",  
        "sourceType": {  
            "type": "Property",  
            "value": "MASS"  
        },  
        "sourceQuality": {  
            "type": "Property",  
            "value": 1.2,  
            "unitCode": "M1"  
        },  
        "sourcePattern": {  
            "type": "Relationship",  
            "object": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
        }  
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
