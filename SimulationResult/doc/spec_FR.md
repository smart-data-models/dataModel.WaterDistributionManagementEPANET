Entité : SimulationResult  
=========================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.WaterNetworkManagement/blob/master/SimulationResult/LICENSE.md)  
Description globale : **Cette entité contient une description harmonisée d'un résultat de simulation générique réalisé pour le domaine de la gestion des réseaux d'eau. Cette entité est principalement associée à la gestion verticale des réseaux d'eau et aux applications IdO connexes.**  

## Liste des biens  

- `address`: L'adresse postale  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `hasInputNetwork`: L'identifiant du réseau utilisé dans la simulation  - `id`: Identifiant unique de l'entité  - `location`:   - `name`: Le nom de cet article.  - `outputParameters`: Description de l'ensemble des résultats de la simulation appliquée au réseau.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `refSimulationScenario`: L'ID du scénario de simulation  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `type`: Type d'entité NGSI-LD. Il doit s'agir de SimulationResult    
Propriétés requises  
- `id`  - `refSimulationScenario`  - `type`  ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
SimulationResult:    
  description: 'This entity contains a harmonised description of a generic simulation result made for the Water Network Management domain. This entity is primarily associated with the water network management vertical and related IoT applications.'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/areaServed'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/adddress    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
    hasInputNetwork:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: 'The ID of the network used in the simulation'    
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
    id:    
      anyOf: &simulationresult_-_properties_-_owner_-_items_-_anyof    
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
    name:    
      description: 'The name of this item.'    
      type: Property    
    outputParameters:    
      description: 'Description of the set of results of applied simulation to the network.'    
      items:    
        properties:    
          parameter:    
            enum:    
              - demand    
              - energyUse    
              - flow    
              - head    
              - initialQuality    
              - level    
              - pressure    
              - quality    
              - sourceMassInflow    
              - supply    
              - velocity    
              - waterLevel    
            type: string    
          targetURI:    
            anyOf:    
              - maxLength: 256    
                minLength: 1    
                pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
                type: string    
              - format: uri    
                type: string    
          value:    
            anyOf:    
              - type: string    
              - type: number    
              - type: boolean    
        type: object    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *simulationresult_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    refSimulationScenario:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: 'The ID of the simulation scenario'    
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
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
    type:    
      description: 'NGSI-LD Entity Type. It has to be SimulationResult'    
      enum:    
        - SimulationResult    
      type: Property    
  required:    
    - id    
    - type    
    - refSimulationScenario    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### SimulationResult NGSI V2 key-values Exemple  
Voici un exemple de résultat de simulation au format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsque l'on utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:SimulationResult:01",  
  "type": "SimulationResult",  
  "description": "Free Text",  
  "hasInputNetwork": "urn:ngsi-ld:WaterNetwork:01",  
  "refSimulationScenario": "urn:ngsi-ld:Simulation:01",  
  "outputParameters": [  
    {  
      "parameter": "waterLevel",  
      "value": 50,  
      "targetURI": "urn:ngsi-ld:Valve:V1"  
    },  
    {  
      "parameter": "initialQuality",  
      "value": 2,  
      "targetURI": "urn:ngsi-ld:Tank:T1"  
    }  
  ]  
}  
```  
#### SimulationResult NGSI V2 normalisé Exemple  
Voici un exemple de résultat de simulation au format JSON tel que normalisé. Ce format est compatible avec la version 2 du NGSI lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:SimulationResult:01",  
  "type": "SimulationResult",  
  "description": {  
    "type": "Property",  
    "value": "Free Text"  
  },  
  "hasInputNetwork": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:WaterNetwork:01"  
  },  
  "refSimulationScenario": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Simulation:01"  
  },  
  "outputParameters": [  
    {  
      "type": "Property",  
      "value": "output parameter 1",  
      "waterLevel": {  
        "type": "Property",  
        "value": 50,  
        "targetURI": {  
          "type": "Property",  
          "value": "urn:ngsi-ld:Valve:V1"  
        }  
      }  
    },  
    {  
      "type": "Property",  
      "value": "output parameter 2",  
      "initialQuality": {  
        "type": "Property",  
        "value": 2,  
        "targetURI": {  
          "type": "Relationship",  
          "value": "urn:ngsi-ld:Tank:T1"  
        }  
      }  
    }  
  ]  
}  
```  
#### SimulationResult NGSI-LD key-values Exemple  
Voici un exemple de résultat de simulation au format JSON-LD en tant que valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:SimulationResult:01",  
  "type": "SimulationResult",  
  "description": "Free Text",  
  "hasInputNetwork": "urn:ngsi-ld:WaterNetwork:01",  
  "refSimulationScenario": "urn:ngsi-ld:Simulation:01",  
  "outputParameters": [  
    {  
      "parameter": "waterLevel",  
      "value": 50,  
      "targetURI": "urn:ngsi-ld:Valve:V1"  
    },  
    {  
      "parameter": "initialQuality",  
      "value": 2,  
      "targetURI": "urn:ngsi-ld:Tank:T1"  
    }  
  ],  
  "@context": [  
    "https://schema.lab.fiware.org/ld/context"  
  ]  
}  
```  
#### SimulationResult NGSI-LD normalisé Exemple  
Voici un exemple de résultat de simulation au format JSON-LD tel que normalisé. Il est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "urn:ngsi-ld:SimulationResult:01",  
    "type": "SimulationResult",  
    "description": {  
        "type": "Property",  
        "value": "Free Text"  
    },  
    "hasInputNetwork": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:WaterNetwork:01"  
    },  
    "refSimulationScenario": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Simulation:01"  
    },  
    "outputParameters": [  
        {  
            "type": "Property",  
            "value": "output parameter 1",  
            "waterLevel": {  
                "type": "Property",  
                "value": 50,  
                "targetURI": {  
                    "type": "Property",  
                    "value": "urn:ngsi-ld:Valve:V1"  
                }  
            },  
            "datasetId": "urn:ngsi-ld:Dataset:ValveSetting"  
        },  
        {  
            "type": "Property",  
            "value": "output parameter 2",  
            "initialQuality": {  
                "type": "Property",  
                "value": 2,  
                "targetURI": {  
                    "type": "Relationship",  
                    "value": "urn:ngsi-ld:Tank:T1"  
                }  
            },  
            "datasetId": "urn:ngsi-ld:Dataset:TankInitialQuality"  
        }  
    ],  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context"  
    ]  
}  
```  
