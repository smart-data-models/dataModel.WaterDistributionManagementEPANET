Entité : Jonction  
=================  
Cette spécification est une **version temporelle**. Elle est générée automatiquement à partir des propriétés documentées décrites dans le schema.json condensé dans le fichier `model.yaml`. Un fichier temporaire `nouveau_modèle.yaml` a été créé dans chaque modèle de données pour éviter d'avoir un impact sur les scripts existants. Ainsi, la spécification sera incomplète tant que le fichier schema.json n'est pas mis à jour au nouveau format (documentation des propriétés). Une fois mis à jour, le fichier `model.yaml` (`nouveau_model.yaml`) doit être mis à jour également (automatiquement) . Plus d'informations dans ce [lien](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Tant qu'il s'agit d'un format provisoire, tout [feedback est le bienvenu dans ce formulaire](https://smartdatamodels.org/index.php/submit-an-issue-2/) en choisissant l'option "Feedback sur la nouvelle spécification".  
Description globale : **Cette entité contient une description harmonisée d'une jonction générique faite pour le domaine de la gestion des réseaux d'eau. Cette entité est principalement associée à la gestion verticale des réseaux d'eau et aux applications IdO connexes.**  

## Liste des biens  

`address`: L'adresse postale.  `areaServed`: La zone géographique où un service ou un article offert est fourni.  `demandCategory`:   `description`:   `elevation`:   `emitterCoefficient`:   `initialQuality`:   `location`:   `sourceCategory`:   `tag`:   `type`: Type d'entité NGSI-LD  ## Modèle de données description des biens  
Classement par ordre alphabétique  
```yaml  
Junction:    
  description: 'This entity contains a harmonised description of a generic junction made for the Water Network Management domain. This entity is primarily associated with the water network management vertical and related IoT applications.'    
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
    demandCategory:    
      properties:    
        baseDemand:    
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
        createdAt:    
          format: date-time    
          type: string    
        demandPattern:    
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
        - baseDemand    
        - demandPattern    
      type: object    
    description:    
      properties: &junction_-_properties_-_elevation_-_properties    
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
      required: &junction_-_properties_-_elevation_-_required    
        - type    
        - value    
      type: object    
    elevation:    
      properties: *junction_-_properties_-_elevation_-_properties    
      required: *junction_-_properties_-_elevation_-_required    
      type: object    
    emitterCoefficient:    
      properties: *junction_-_properties_-_elevation_-_properties    
      required: *junction_-_properties_-_elevation_-_required    
      type: object    
    initialQuality:    
      properties: *junction_-_properties_-_elevation_-_properties    
      required: *junction_-_properties_-_elevation_-_required    
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
      properties: *junction_-_properties_-_elevation_-_properties    
      required: *junction_-_properties_-_elevation_-_required    
      type: object    
    type:    
      description: 'NGSI-LD Entity Type'    
      enum:    
        - Junction    
      type: string    
  required:    
    - id    
    - type    
    - location    
    - elevation    
  type: object    
```  
Voici un exemple d'une jonction au format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsque l'on utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "63fe7d79-0d4c-4da9-b7d0-3340efa0656a",  
    "type": "Junction",  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            24.30623,  
            60.07966  
        ]  
    },  
    "elevation": 105.8,  
    "demandCategory": {  
        "value": "agriculture demand",  
        "baseDemand": "1.763868462",  
        "demandPattern": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
    },  
    "sourceCategory": {  
        "value": "CategoryX",  
        "sourceType": "MASS",  
        "sourceQuality": 1.2,  
        "sourcePattern": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
    },  
    "tag": "DMA1",  
    "description": "This entity contains a harmonised description of a Junction",  
    "initialQuality": 0.5,  
    "emitterCoefficient": 0.526  
}  
```  
Voici un exemple de jonction au format JSON normalisé. Il est compatible avec NGSI V2 lorsqu'il utilise "options=valeurs clés" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "63fe7d79-0d4c-4da9-b7d0-3340efa0656a",  
    "type": "Junction",  
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
    "elevation": {  
        "value": 105.8  
    },  
    "demandCategory": {  
        "value": {  
            "value": "agriculture demand",  
            "baseDemand": {  
                "value": "1.763868462"  
            },  
            "demandPattern": {  
                "type": "Relationship",  
                "value": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
            }  
        }  
    },  
    "sourceCategory": {  
        "value": {  
            "value": "CategoryX",  
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
    },  
    "description": {  
        "value": "This entity contains a harmonised description of a Junction"  
    },  
    "initialQuality": {  
        "value": 0.5  
    },  
    "emitterCoefficient": {  
        "value": 0.526  
    }  
}  
```  
Voici un exemple d'une jonction au format JSON-LD comme valeurs clés. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context"],  
 "createdAt": "2020-02-20T15:42:00Z",  
 "demandCategory": "agriculture demand",  
 "description": "This entity contains a harmonised description of a Junction",  
 "elevation": 105.8,  
 "emitterCoefficient": 0.526,  
 "id": "urn:ngsi-ld:Junction:63fe7d79-0d4c-4da9-b7d0-3340efa0656a",  
 "initialQuality": 0.5,  
 "location": {"coordinates": [24.30623, 60.07966], "type": "Point"},  
 "modifiedAt": "2020-02-20T15:45:00Z",  
 "sourceCategory": "CategoryX",  
 "tag": "DMA1",  
 "type": "Junction"}  
```  
Voici un exemple d'une jonction au format JSON-LD telle que normalisée. Ce format est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "urn:ngsi-ld:Junction:63fe7d79-0d4c-4da9-b7d0-3340efa0656a",  
    "type": "Junction",  
    "createdAt": "2020-02-20T15:42:00Z",  
    "modifiedAt": "2020-02-20T15:45:00Z",  
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
    "elevation": {  
        "type": "Property",  
        "value": 105.8,  
        "unitCode": "MTR"  
    },  
    "demandCategory": {  
        "type": "Property",  
        "value": "agriculture demand",  
        "baseDemand": {  
            "type": "Property",  
            "value": "1.763868462",  
            "unitCode": "MQS"  
        },  
        "demandPattern": {  
            "type": "Relationship",  
            "object": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533"  
        }  
    },  
    "sourceCategory": {  
        "type": "Property",  
        "value": "CategoryX",  
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
    "description": {  
        "type": "Property",  
        "value": "This entity contains a harmonised description of a Junction"  
    },  
    "initialQuality": {  
        "type": "Property",  
        "value": 0.5,  
        "unitCode":"M1"  
    },  
    "emitterCoefficient": {  
        "type": "Property",  
        "value": 0.526,  
        "unitCode": "S4"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context"  
    ]  
}  
```  
