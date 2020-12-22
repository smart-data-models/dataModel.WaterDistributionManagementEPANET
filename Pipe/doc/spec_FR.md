Entité : Pipe  
=============  
[Licence ouverte](https://github.com/smart-data-models//dataModel.WaterNetworkManagement/blob/master/Pipe/LICENSE.md)  
Description globale : **Cette entité contient une description harmonisée d'une canalisation générique faite pour le domaine de la gestion des réseaux d'eau. Cette entité est principalement associée aux applications verticales de gestion de l'eau et aux applications IdO connexes.**  

## Liste des biens  

- `bulkCoeff`: Utilisez une valeur positive pour la croissance et une valeur négative pour la décroissance. Toutes les unités sont acceptées dans le code [CEFACT](https://www.unece.org/cefact.html).  - `description`: Un texte optionnel qui décrit d'autres informations importantes sur la jonction  - `diameter`: Le diamètre du tuyau  - `endsAt`: L'ID du nœud où se termine le tuyau  - `initialStatus`: L'état du nœud au début de la simulation.  - `length`: La longueur réelle du tuyau. Toutes les unités sont acceptées en code [CEFACT](https://www.unece.org/cefact.html).  - `minorLoss`: Coefficient de perte mineure sans unité associé aux coudes, raccords, etc.  - `roughness`: Le coefficient de rugosité du tuyau.  - `startsAt`: L'ID du nœud où commence le tuyau  - `status`: L'état dynamique du nœud  - `tag`: Une chaîne de texte facultative utilisée pour classer la pipe dans une catégorie, peut-être en fonction de l'âge ou du matériau  - `type`: Type d'entité NGSI-LD. Il doit s'agir de Pipe  - `vertices`: Coordonnées de tous les sommets du tuyau, ordonnées du nœud startsAt au nœud endsAt et codées en tant que GeoJSON  - `wallCoeff`: Le coefficient de réaction de la paroi du tuyau. Utilisez une valeur positive pour la croissance et une valeur négative pour la décroissance. Toutes les unités sont acceptées dans le code [CEFACT](https://www.unece.org/cefact.html).    
Propriétés requises  
- `diameter`  - `endsAt`  - `id`  - `initialStatus`  - `length`  - `minorLoss`  - `roughness`  - `startsAt`  - `type`  ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Pipe:    
  description: 'This entity contains a harmonised description of a generic pipe made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.'    
  properties:    
    bulkCoeff:    
      description: 'Use a positive value for growth and a negative value for decay. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'reciprocal day The bulk reaction coefficient for the pipe'    
    description:    
      description: 'An optional text that describes other significant information about the junction'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    diameter:    
      description: 'The pipe diameter'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: Millimetre    
    endsAt:    
      description: 'The ID of the node where the pipe ends'    
      format: uri    
      type: Relationship    
    initialStatus:    
      description: 'The node status at the start of the simulation.'    
      enum:    
        - OPEN    
        - CLOSED    
        - CV    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    length:    
      description: 'The actual length of the pipe. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: Metre    
    minorLoss:    
      description: 'Unitless minor loss coefficient associated with bends, fittings, etc'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'No unit'    
    roughness:    
      description: 'The roughness coefficient of the Pipe.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'No unit'    
    startsAt:    
      description: 'The ID of the node where the pipe begins'    
      format: uri    
      type: Relationship    
    status:    
      description: 'The dynamic state of the node'    
      enum:    
        - OPEN    
        - CLOSED    
        - CV    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    tag:    
      description: 'An optional text string used to assign the pipe to a category, perhaps one based on age or material'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    type:    
      description: 'NGSI-LD Entity Type. It has to be Pipe'    
      enum:    
        - Pipe    
      type: Property    
    vertices:    
      description: 'Coordinates of all vertices in the pipe, ordered from the startsAt node to the endsAt node and encoded as a GeoJSON '    
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
      type: Geoproperty    
    wallCoeff:    
      description: 'The wall reaction coefficient for the pipe. Use a positive value for growth and a negative value for decay. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: mg/m²/day    
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
</details>    
## Exemples de charges utiles  
#### Pipe NGSI V2 key-values Exemple  
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
#### Tuyau NGSI V2 normalisé Exemple  
Voici un exemple de tuyau au format JSON tel que normalisé. Il est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
#### Tuyau Valeurs clés NGSI-LD Exemple  
Voici un exemple de Pipe en format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
#### Tuyau NGSI-LD normalisé Exemple  
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
