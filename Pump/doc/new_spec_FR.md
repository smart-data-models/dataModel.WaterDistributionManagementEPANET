Entité : Pompe  
==============  
[Licence ouverte](https://github.com/smart-data-models//dataModel.WaterNetworkManagement/blob/master/Pump/LICENSE.md)  
Description globale : **Cette entité contient une description harmonisée d'une pompe générique faite pour le domaine de la gestion des réseaux d'eau. Cette entité est principalement associée aux applications verticales de gestion de l'eau et aux applications IdO connexes.**  

## Liste des biens  

- `description`: Un texte optionnel qui décrit d'autres informations importantes sur la jonction  - `efficCurve`: L'étiquette d'identification de la courbe qui représente l'efficacité filaire de la pompe en fonction du débit.  - `endsAt`: L'ID du nœud du côté du refoulement de la pompe  - `energyPattern`: L'étiquette d'identification du schéma temporel utilisé pour décrire la variation du prix de l'énergie tout au long de la journée.  - `energyPrice`: Le prix moyen ou nominal de l'énergie en unités monétaires. Toutes les unités sont acceptées en code [CEFACT](https://www.unece.org/cefact.html).  - `headCurve`: L'étiquette d'identification de la courbe de la pompe utilisée pour décrire la relation entre la hauteur de charge délivrée par la pompe et le débit à travers la pompe.  - `initialStatus`: L'état du nœud au début de la simulation.  - `power`: L'énergie fournie par la pompe. Toutes les unités sont acceptées en code [CEFACT](https://www.unece.org/cefact.html).  - `pumpPattern`: L'étiquette d'identification d'un schéma temporel utilisé pour contrôler le fonctionnement de la pompe. Les multiplicateurs du modèle sont équivalents aux réglages de vitesse. Un multiplicateur de zéro implique que la pompe sera arrêtée pendant la période de temps correspondante  - `speed`: Le réglage de la vitesse relative de la pompe. Toutes les unités sont acceptées en code [CEFACT](https://www.unece.org/cefact.html).  - `startsAt`: L'ID du nœud du côté aspiration de la pompe  - `status`: L'état dynamique du nœud  - `tag`: Une chaîne de texte facultative utilisée pour classer la pipe dans une catégorie, peut-être en fonction de l'âge ou du matériau  - `type`: Type d'entité NGSI-LD. Il doit être égal à Pump.  - `vertices`: Coordonnées de tous les sommets de la pompe, ordonnées du nœud startsAt au nœud endsAt et encodées sous forme de GeoJSON    
Propriétés requises  
- `endsAt`  - `id`  - `initialStatus`  - `startsAt`  - `type`  ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Pump:    
  description: 'This entity contains a harmonised description of a generic pump made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.'    
  properties:    
    description:    
      description: 'An optional text that describes other significant information about the junction'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    efficCurve:    
      description: 'The ID label of the curve that represents the pump''s wire-to-water efficiency as a function of flow rate.'    
      format: uri    
      type: Relationship    
    endsAt:    
      description: 'The ID of the node on the discharge side of the pump'    
      format: uri    
      type: Relationship    
    energyPattern:    
      description: 'The ID label of the time pattern used to describe the variation in energy price throughout the day.'    
      format: uri    
      type: Relationship    
    energyPrice:    
      description: 'The average or nominal price of energy in monetary units. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        units: 'No unit'    
    headCurve:    
      description: 'The ID label of the pump curve used to describe the relationship between the head delivered by the pump and the flow through the Pump.'    
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
    power:    
      description: 'The power supplied by the pump. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: KiloWatt    
    pumpPattern:    
      description: 'The ID label of a time pattern used to control the pump''s operation. The multipliers of the pattern are equivalent to speed settings. A multiplier of zero implies that the pump will be shut off during the corresponding time period'    
      format: uri    
      type: Relationship    
    speed:    
      description: 'The relative speed setting of the Pump. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'Metre per Second'    
    startsAt:    
      description: 'The ID of the node on the suction side of the pump'    
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
      description: 'NGSI-LD Entity Type. It must be equal to Pump.'    
      enum:    
        - Pump    
      type: Property    
    vertices:    
      description: 'Coordinates of all vertices in the pump, ordered from the startsAt node to the endsAt node and encoded as a GeoJSON '    
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
  required:    
    - id    
    - type    
    - initialStatus    
    - startsAt    
    - endsAt    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### Pompe NGSI V2 valeurs clés Exemple  
Voici un exemple d'une pompe au format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "85zhnf58-0d4c-h4g854g-b7d0-3310klm",  
    "type": "Pump",  
    "initialStatus": "OPEN",  
    "status": "OPEN",  
    "power": 100,  
    "speed": 1.2,  
    "startsAt": "63fe7d79-0d4c-4da9-b7d0-3340efa0656a",  
    "endsAt": "1863179e-3768-4480-9167-ff21f870dd19",  
    "tag": "DMA1",  
    "pumpPattern": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
    "efficCurve": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
    "energyPrice": 0.8,  
    "energyPattern": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
}  
```  
#### Pompe NGSI V2 normalisée Exemple  
Voici un exemple de pompe au format JSON normalisé. Il est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "85zhnf58-0d4c-h4g854g-b7d0-3310klm",  
    "type": "Pump",  
    "initialStatus": {  
        "value": "OPEN"  
    },  
    "status": {  
        "value": "OPEN"  
    },  
    "power": {  
        "value": 100  
    },  
    "speed": {  
        "value": 1.2  
    },  
    "startsAt": {  
        "type": "Relationship",  
        "value": "63fe7d79-0d4c-4da9-b7d0-3340efa0656a"  
    },  
    "endsAt": {  
        "type": "Relationship",  
        "value": "1863179e-3768-4480-9167-ff21f870dd19"  
    },  
    "tag": {  
        "value": "DMA1"  
    },  
    "pumpPattern": {  
        "type": "Relationship",  
        "value": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
    },  
    "efficCurve": {  
        "type": "Relationship",  
        "value": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
    },  
    "energyPrice": {  
        "value": 0.8  
    },  
    "energyPattern": {  
        "type": "Relationship",  
        "value": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
    }  
}  
```  
#### Pompe NGSI-LD valeurs clés Exemple  
Voici un exemple d'une pompe au format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:Pump:85zhnf58-0d4c-h4g854g-b7d0-3310klm",  
  "type": "Pump",  
  "createdAt": "2020-03-02T15:42:00Z",  
  "modifiedAt": "2020-03-02T15:45:00Z",  
  "initialStatus": "OPEN",  
  "status": "OPEN",  
  "power": 100,  
  "speed": 1.2,  
  "startsAt": "urn:ngsi-ld:Junction:63fe7d79-0d4c-4da9-b7d0-3340efa0656a",  
  "endsAt": "urn:ngsi-ld:Reservoir:1863179e-3768-4480-9167-ff21f870dd19",  
  "tag": "DMA1",  
  "pumpPattern": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
  "efficCurve": "urn:ngsi-ld:Curve:fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
  "energyPrice": 0.8,  
  "energyPattern": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/data-models/master/context.jsonld"  
  ]  
}  
```  
#### Pompe NGSI-LD normalisée Exemple  
Voici un exemple d'une pompe au format JSON-LD telle que normalisée. Il est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "urn:ngsi-ld:Pump:85zhnf58-0d4c-h4g854g-b7d0-3310klm",  
    "type": "Pump",  
    "createdAt": "2020-03-02T15:42:00Z",  
    "modifiedAt": "2020-03-02T15:45:00Z",  
    "initialStatus": {  
        "type": "Property",  
        "value": "OPEN"  
    },  
    "status": {  
        "type": "Property",  
        "value": "OPEN"  
    },  
    "power": {  
        "type": "Property",  
        "value": 100,  
        "unitCode": "KWT"  
    },  
    "speed": {  
        "type": "Property",  
        "value": 1.2,  
        "unitCode": "MTS"  
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
    "tag": {  
        "type": "Property",  
        "value": "DMA1"  
    },  
    "pumpPattern":{  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
    },  
    "efficCurve":{  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Curve:fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
    },  
    "energyPrice":{  
        "type": "Property",  
        "value": 0.8,  
        "unitCode": "C62"  
    },  
    "energyPattern":{  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context"  
    ]  
}  
```  
