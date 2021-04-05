Entité : Pipe  
=============  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.WaterDistributionManagementEPANET/blob/master/Pipe/LICENSE.md)  
Description globale : **Cette entité contient une description harmonisée d'un tuyau générique fabriqué pour le domaine de la gestion des réseaux d'eau. Cette entité est principalement associée à la gestion verticale de l'eau et aux applications IoT connexes.**  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `bulkCoeff`: Utilisez une valeur positive pour la croissance et une valeur négative pour la décroissance. Toutes les unités sont acceptées en code [CEFACT](https://www.unece.org/cefact.html).  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `diameter`: Le diamètre du tuyau  - `endsAt`: L'ID du nœud où le tuyau se termine  - `flow`: Taux d'écoulement du nœud `startsAt` au nœud `endsAt`, mesuré par un dispositif au niveau du lien (tuyau, vanne ou pompe).  - `id`: Identifiant unique de l'entité  - `initialStatus`: L'état de la liaison au début de la simulation. Enum : 'OUVERT, FERMÉ, CV'.  - `length`: La longueur réelle du tuyau. Toutes les unités sont acceptées en code [CEFACT] (https://www.unece.org/cefact.html).  - `location`:   - `minorLoss`: Coefficient de perte mineur sans unité associé aux coudes, aux raccords, etc.  - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `quality`: Qualité observée dans la composante réseau  - `roughness`: Le coefficient de rugosité de la conduite.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `startsAt`: L'ID du noeud où le tuyau commence  - `status`: L'état dynamique du noeud. Enum : 'OUVERT, FERME, CV  - `tag`: Une chaîne de texte facultative utilisée pour affecter le tuyau à une catégorie, peut-être basée sur l'âge ou le matériau.  - `type`: Type d'entité NGSI-LD. Il doit s'agir de Pipe  - `velocity`: Vitesse observée dans la liaison (tuyau, vanne ou pompe)  - `vertices`: Coordonnées de tous les sommets du tuyau, ordonnées du nœud startsAt au nœud endsAt et encodées sous forme de GeoJSON.  - `wallCoeff`: Le coefficient de réaction de la paroi pour le tuyau. Utilisez une valeur positive pour la croissance et une valeur négative pour la décroissance. Toutes les unités sont acceptées en code [CEFACT](https://www.unece.org/cefact.html).    
Propriétés requises  
- `id`  - `type`  ## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Pipe:    
  description: 'This entity contains a harmonised description of a generic pipe made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.'    
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
        model: https://schema.org/address    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    bulkCoeff:    
      description: 'Use a positive value for growth and a negative value for decay. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'reciprocal day The bulk reaction coefficient for the pipe'    
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
    flow:    
      description: 'Rate of flow from `startsAt` node to `endsAt` node, measured by a device at the link (pipe, valve or pump)'    
      properties:    
        observedBy:    
          anyOf:    
            - description: 'Property. Identifier format of any NGSI entity'    
              maxLength: 256    
              minLength: 1    
              pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
              type: string    
            - description: 'Property. Identifier format of any NGSI entity'    
              format: uri    
              type: string    
        value:    
          type: number    
      type: Property    
    id:    
      anyOf: &pipe_-_properties_-_owner_-_items_-_anyof    
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
    initialStatus:    
      description: 'The link status at the start of the simulation. Enum:''OPEN, CLOSED, CV'''    
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
    minorLoss:    
      description: 'Unitless minor loss coefficient associated with bends, fittings, etc'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'No unit'    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *pipe_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    quality:    
      description: 'Observed quality in the network component'    
      properties:    
        observedBy:    
          anyOf:    
            - description: 'Property. Identifier format of any NGSI entity'    
              maxLength: 256    
              minLength: 1    
              pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
              type: string    
            - description: 'Property. Identifier format of any NGSI entity'    
              format: uri    
              type: string    
        value:    
          type: number    
      type: Property    
    roughness:    
      description: 'The roughness coefficient of the Pipe.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'No unit'    
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
    startsAt:    
      description: 'The ID of the node where the pipe begins'    
      format: uri    
      type: Relationship    
    status:    
      description: 'The dynamic state of the node. Enum:''OPEN, CLOSED, CV'''    
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
    velocity:    
      description: 'Observed velocity in the link (pipe, valve or pump)'    
      properties:    
        observedBy:    
          format: uri    
          type: string    
        value:    
          type: number    
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
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### Pipe NGSI-v2 key-values Exemple  
Voici un exemple de Pipe au format JSON-LD en tant que key-values. Ceci est compatible avec NGSI-v2 lorsque vous utilisez `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
    "startsAt": "ngsi:63fe7d79-0d4c-4da9-b7d0-3340efa0656a",  
    "endsAt": "ngsi:1863179e-3768-4480-9167-ff21f870dd19",  
    "bulkCoeff": 72.4549,  
    "wallCoeff": 72.4549  
}  
```  
#### Tuyau NGSI-v2 normalisé Exemple  
Voici un exemple d'un Pipe au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "74azsty-70d4l-4da9-b7d0-3340ef655nnb",  
  "type": "Pipe",  
  "initialStatus": {  
    "type": "text",  
    "value": "OPEN"  
  },  
  "status": {  
    "type": "text",  
    "value": "OPEN"  
  },  
  "length": {  
    "type": "number",  
    "value": 52.90  
  },  
  "diameter": {  
    "type": "number",  
    "value": 203.00  
  },  
  "roughness": {  
    "type": "number",  
    "value": 72.4549  
  },  
  "minorLoss": {  
    "type": "number",  
    "value": 72.4549  
  },  
  "tag": {  
    "type": "text",  
    "value": "DMA1"  
  },  
  "description": {  
    "type": "text",  
    "value": "Free Text"  
  },  
  "startsAt": {  
    "type": "object",  
    "value": "63fe7d79-0d4c-4da9-b7d0-3340efa0656a"  
  },  
  "endsAt": {  
    "type": "object",  
    "value": "1863179e-3768-4480-9167-ff21f870dd19"  
  },  
  "bulkCoeff": {  
    "type": "number",  
    "value": 72.4549  
  },  
  "wallCoeff": {  
    "type": "number",  
    "value": 72.4549  
  },  
  "flow": {  
    "type": "structuredValue",  
    "value": {  
      "value": 20,  
      "observedBy": "device-9845A"  
    }  
  },  
  "velocity": {  
    "type": "structuredValue",  
    "value": {  
      "value": 2,  
      "observedBy": "device-9845A"  
    }  
  },  
  "quality": {  
    "type": "structuredValue",  
    "value": {  
      "value": 0.5,  
      "observedBy": "device-9845A"  
    }  
  }  
}  
```  
#### Pipe NGSI-LD key-values Exemple  
Voici un exemple de Pipe au format JSON-LD en tant que key-values. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ],  
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
  "wallCoeff": 72.4549  
}  
```  
#### Tuyau NGSI-LD normalisé Exemple  
Voici un exemple de Pipe au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:Pipe:74azsty-70d4l-4da9-b7d0-3340ef655nnb",  
  "type": "Pipe",  
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
    "value": 203.0,  
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
        [  
          24.40623,  
          60.17966  
        ],  
        [  
          24.50623,  
          60.27966  
        ]  
      ]  
    }  
  },  
  "bulkCoeff": {  
    "type": "Property",  
    "value": 72.4549,  
    "unitCode": "E91"  
  },  
  "wallCoeff": {  
    "type": "Property",  
    "value": 72.4549,  
    "unitCode": "RRC"  
  },  
  "flow": {  
    "type": "Property",  
    "value": {  
      "type": "Property",  
      "value": 20,  
      "unitCode": "G51"  
    },  
    "observedBy": {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:Device:device-9845A"  
    }  
  },  
  "velocity": {  
    "type": "Property",  
    "value": {  
      "type": "Property",  
      "value": 2,  
      "unitCode": "MTS"  
    },  
    "observedBy": {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:Device:device-9845A"  
    }  
  },  
  "quality": {  
    "type": "Property",  
    "value": {  
      "type": "Property",  
      "value": 0.5,  
      "unitCode": "F27"  
    },  
    "observedBy": {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:Device:device-9845A"  
    }  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
