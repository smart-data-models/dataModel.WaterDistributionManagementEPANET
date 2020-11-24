Entité : Pipe  
=============  
Cette spécification est une **version temporelle**. Elle est générée automatiquement à partir des propriétés documentées décrites dans le schema.json condensé dans le fichier `model.yaml`. Un fichier temporaire `nouveau_modèle.yaml` a été créé dans chaque modèle de données pour éviter d'avoir un impact sur les scripts existants. Ainsi, la spécification sera incomplète tant que le fichier schema.json n'est pas mis à jour au nouveau format (documentation des propriétés). Une fois mis à jour, le fichier `model.yaml` (`nouveau_model.yaml`) doit être mis à jour également (automatiquement) . Plus d'informations dans ce [lien](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Tant qu'il s'agit d'un format provisoire, tout [feedback est le bienvenu dans ce formulaire](https://smartdatamodels.org/index.php/submit-an-issue-2/) en choisissant l'option "Feedback sur la nouvelle spécification".  
Description globale : **Cette entité contient une description harmonisée d'une canalisation générique faite pour le domaine de la gestion des réseaux d'eau. Cette entité est principalement associée aux applications verticales de gestion de l'eau et aux applications IdO connexes.**  

## Liste des biens  

`bulkCoeff`:   `diameter`:   `endsAt`:   `initialStatus`:   `length`:   `minorLoss`:   `roughness`:   `startsAt`:   `status`:   `tag`:   `type`: Type d'entité NGSI-LD  `vertices`:   `wallCoeff`:   ## Modèle de données description des biens  
Classement par ordre alphabétique  
```yaml  
Pipe:    
  description: 'This entity contains a harmonised description of a generic pipe made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.'    
  properties:    
    bulkCoeff:    
      properties: &pipe_-_properties_-_diameter_-_properties    
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
      required: &pipe_-_properties_-_diameter_-_required    
        - type    
        - value    
      type: object    
    diameter:    
      properties: *pipe_-_properties_-_diameter_-_properties    
      required: *pipe_-_properties_-_diameter_-_required    
      type: object    
    endsAt:    
      properties: &pipe_-_properties_-_startsat_-_properties    
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
      required: &pipe_-_properties_-_startsat_-_required    
        - type    
        - object    
      type: object    
    initialStatus:    
      properties: &pipe_-_properties_-_status_-_properties    
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
            - OPEN    
            - CLOSED    
            - CV    
          type:    
            - number    
            - string    
            - array    
      required: &pipe_-_properties_-_status_-_required    
        - type    
        - value    
      type: object    
    length:    
      properties: *pipe_-_properties_-_diameter_-_properties    
      required: *pipe_-_properties_-_diameter_-_required    
      type: object    
    minorLoss:    
      properties: *pipe_-_properties_-_diameter_-_properties    
      required: *pipe_-_properties_-_diameter_-_required    
      type: object    
    roughness:    
      properties: *pipe_-_properties_-_diameter_-_properties    
      required: *pipe_-_properties_-_diameter_-_required    
      type: object    
    startsAt:    
      properties: *pipe_-_properties_-_startsat_-_properties    
      required: *pipe_-_properties_-_startsat_-_required    
      type: object    
    status:    
      properties: *pipe_-_properties_-_status_-_properties    
      required: *pipe_-_properties_-_status_-_required    
      type: object    
    tag:    
      properties: *pipe_-_properties_-_diameter_-_properties    
      required: *pipe_-_properties_-_diameter_-_required    
      type: object    
    type:    
      description: 'NGSI-LD Entity Type'    
      enum:    
        - Pipe    
      type: string    
    vertices:    
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
    wallCoeff:    
      properties: *pipe_-_properties_-_diameter_-_properties    
      required: *pipe_-_properties_-_diameter_-_required    
      type: object    
  required:    
    - id    
    - type    
    - initialStatus    
    - length    
    - diameter    
    - roughness    
    - minorLoss    
    - startsAt    
    - endsAt    
  type: object    
```  
Voici un exemple de Pipe en format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "74azsty-70d4l-4da9-b7d0-3340ef655nnb",  
    "type": "Pipe",  
    "initialStatus": "OPEN",  
    "status": "OPEN",  
    "length": 52.90,  
    "diameter": 203.00,  
    "roughness": 72.4549,  
    "minorLoss": 72.4549,  
    "tag": "DMA1",  
    "description": "Free Text",  
    "startsAt": "63fe7d79-0d4c-4da9-b7d0-3340efa0656a",  
    "endsAt": "1863179e-3768-4480-9167-ff21f870dd19",  
    "bulkCoeff": 72.4549,  
    "wallCoeff": 72.4549  
}  
```  
Voici un exemple de tuyau au format JSON tel que normalisé. Il est compatible avec NGSI V2 lorsqu'il utilise "options=valeurs clés" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "74azsty-70d4l-4da9-b7d0-3340ef655nnb",  
    "type": "Pipe",  
    "initialStatus": {  
        "value": "OPEN"  
    },  
    "status": {  
        "value": "OPEN"  
    },  
    "length": {  
        "value": 52.90  
    },  
    "diameter": {  
        "value": 203.00  
    },  
    "roughness": {  
        "value": 72.4549  
    },  
    "minorLoss": {  
        "value": 72.4549  
    },  
    "tag": {  
        "value": "DMA1"  
    },  
    "description": {  
        "value": "Free Text"  
    },  
    "startsAt": {  
        "type": "Relationship",  
        "value": "63fe7d79-0d4c-4da9-b7d0-3340efa0656a"  
    },  
    "endsAt": {  
        "type": "Relationship",  
        "value": "1863179e-3768-4480-9167-ff21f870dd19"  
    },  
    "bulkCoeff": {  
        "value": 72.4549  
    },  
    "wallCoeff": {  
        "value": 72.4549  
    }  
}  
```  
Voici un exemple de Pipe en format JSON-LD comme valeurs clés. Il est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context"],  
 "bulkCoeff": 72.4549,  
 "createdAt": "2020-02-20T15:42:00Z",  
 "description": "Free Text",  
 "diameter": 203.0,  
 "endsAt": "urn:ngsi-ld:Reservoir:1863179e-3768-4480-9167-ff21f870dd19",  
 "id": "urn:ngsi-ld:Pipe:74azsty-70d4l-4da9-b7d0-3340ef655nnb",  
 "initialStatus": "OPEN",  
 "length": 52.9,  
 "minorLoss": 72.4549,  
 "modifiedAt": "2020-02-20T15:45:00Z",  
 "roughness": 72.4549,  
 "startsAt": "urn:ngsi-ld:Junction:63fe7d79-0d4c-4da9-b7d0-3340efa0656a",  
 "status": "OPEN",  
 "tag": "DMA1",  
 "type": "Pipe",  
 "wallCoeff": 72.4549}  
```  
Voici un exemple de tuyau au format JSON-LD tel que normalisé. Il est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "urn:ngsi-ld:Pipe:74azsty-70d4l-4da9-b7d0-3340ef655nnb",  
    "type": "Pipe",  
    "createdAt": "2020-02-20T15:42:00Z",  
    "modifiedAt": "2020-02-20T15:45:00Z",  
    "initialStatus": {  
        "type": "Property",  
        "value": "OPEN"  
    },  
    "status": {  
        "type": "Property",  
        "value": "OPEN"  
    },  
    "length": {  
        "type": "Property",  
        "value": 52.90,  
        "unitCode": "MTR"  
    },  
    "diameter": {  
        "type": "Property",  
        "value": 203.00,  
        "unitCode": "MMT"  
    },  
    "roughness": {  
        "type": "Property",  
        "value": 72.4549,  
        "unitCode": "C62"  
    },  
    "minorLoss": {  
        "type": "Property",  
        "value": 72.4549,  
        "unitCode": "C62"  
    },  
    "tag": {  
        "type": "Property",  
        "value": "DMA1"  
    },  
     "description": {  
        "type": "Property",  
        "value": "Free Text"  
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
    "bulkCoeff":{  
        "type": "Property",  
        "value": 72.4549,  
        "unitCode": "E91"  
    },  
    "wallCoeff":{  
        "type": "Property",  
        "value": 72.4549,  
        "unitCode": "RRC"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context"  
    ]  
}  
```  
