<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entité : Valve    
==============<!-- /10-Header -->    
<!-- 15-License -->    
[Licence ouverte] (https://github.com/smart-data-models//dataModel.WaterDistributionManagementEPANET/blob/master/Valve/LICENSE.md)    
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Description globale : **Cette entité contient une description harmonisée d'une vanne générique réalisée pour le domaine de la gestion des réseaux d'eau. Cette entité est principalement associée au domaine vertical de la gestion de l'eau et aux applications IoT connexes.**    
version : 0.1.0    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste des propriétés    
<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.    
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse postale et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La région dans laquelle se trouve la localité et qui se trouve dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local.      
	- `postOfficeBoxNumber[string]`: Le numéro de la boîte postale pour les adresses de boîtes postales. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `diameter[number]`: Le diamètre de la valve. Toutes les unités sont acceptées dans le code [CEFACT] (https://www.unece.org/cefact.html).  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `endsAt[uri]`: L'ID du nœud sur le côté nominal aval ou de décharge de la vanne  - `flow[object]`: Débit du nœud `startsAt` au nœud `endsAt`, mesuré par un dispositif au niveau de la liaison (tuyau, vanne ou pompe).  	- `observedBy`:       
- `id[*]`: Identifiant unique de l'entité  - `initialStatus[string]`: État de la liaison au début de la simulation. Enum : "OUVERT, FERMÉ, CV  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `minorLoss[number]`: Coefficient de perte mineure sans unité qui s'applique lorsque la vanne est complètement ouverte. Toutes les unités sont acceptées dans le code [CEFACT] (https://www.unece.org/cefact.html).  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: Le nom de cet élément  - `openStatus[number]`: État d'une vanne sous la forme d'un pourcentage numérique représentant le degré d'ouverture ou de fermeture de la vanne. 0% - complètement fermée, 100% - complètement ouverte  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `quality[object]`: Qualité observée dans la composante réseau  	- `observedBy`:       
- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `setting[number]`: Paramètre décrivant le réglage opérationnel de la vanne. Toutes les unités sont acceptées dans le code [CEFACT] (https://www.unece.org/cefact.html).  . Model: [https://schema.org/Number](https://schema.org/Number)- `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `startsAt[uri]`: L'ID du nœud sur le côté amont nominal ou côté débit d'entrée de la vanne  - `status[string]`: État dynamique du nœud. Enum : "OUVERT, FERMÉ, CV  . Model: [https://schema.org/Text](https://schema.org/Text)- `tag[string]`: Une chaîne de texte facultative utilisée pour classer le tuyau dans une catégorie, par exemple en fonction de l'âge ou du matériau.  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: Type d'entité NGSI-LD. Il doit être égal à Valve  - `valveCurve[uri]`: Une relation avec la courbe de la propriété de réglage. Nécessaire uniquement lorsque valveType est GPV  - `valveType[string]`: Le type de vanne de l'élément. enum : "FCV, GPV, PBV, PRV, PSV, TCV  . Model: [https://schema.org/Text](https://schema.org/Text)- `velocity[object]`: Vitesse observée dans la liaison (tuyau, vanne ou pompe)  	- `observedBy[uri]`: Où la vitesse a été observée      
- `vertices[*]`: Géopropriété. Coordonnées de tous les sommets de la vanne, ordonnées du nœud startsAt au nœud endsAt et encodées sous forme de GeoJSON.  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propriétés requises    
- `endsAt`  - `id`  - `startsAt`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modèle de données description des propriétés    
Classés par ordre alphabétique (cliquez pour plus de détails)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
Valve:      
  description: This entity contains a harmonised description of a generic Valve made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.      
  properties:      
    address:      
      description: The mailing address      
      properties:      
        addressCountry:      
          description: 'The country. For example, Spain'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressCountry      
            type: Property      
        addressLocality:      
          description: 'The locality in which the street address is, and which is in the region'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressLocality      
            type: Property      
        addressRegion:      
          description: 'The region in which the locality is, and which is in the country'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressRegion      
            type: Property      
        district:      
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'      
          type: string      
          x-ngsi:      
            type: Property      
        postOfficeBoxNumber:      
          description: 'The post office box number for PO box addresses. For example, 03578'      
          type: string      
          x-ngsi:      
            model: https://schema.org/postOfficeBoxNumber      
            type: Property      
        postalCode:      
          description: 'The postal code. For example, 24004'      
          type: string      
          x-ngsi:      
            model: https://schema.org/https://schema.org/postalCode      
            type: Property      
        streetAddress:      
          description: The street address      
          type: string      
          x-ngsi:      
            model: https://schema.org/streetAddress      
            type: Property      
        streetNr:      
          description: Number identifying a specific property on a public street      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/address      
        type: Property      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    areaServed:      
      description: The geographic area where a service or offered item is provided      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
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
    diameter:      
      description: 'The valve diameter. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code'      
      type: number      
      x-ngsi:      
        model: ' https://schema.org/Number'      
        type: Property      
        units: millimetre      
    endsAt:      
      description: The ID of the node on the nominal downstream or discharge side of the valve      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    flow:      
      description: 'Rate of flow from `startsAt` node to `endsAt` node, measured by a device at the link (pipe, valve or pump)'      
      properties:      
        observedBy:      
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
        value:      
          description: Value of the flow      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
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
    initialStatus:      
      description: 'The link status at the start of the simulation. Enum:''OPEN, CLOSED, CV'''      
      enum:      
        - OPEN      
        - CLOSED      
        - CV      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    location:      
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
      oneOf:      
        - description: Geojson reference to the item. Point      
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
          title: GeoJSON Point      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. LineString      
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
              minItems: 2      
              type: array      
            type:      
              enum:      
                - LineString      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON LineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. Polygon      
          properties:      
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
          title: GeoJSON Polygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiPoint      
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
          title: GeoJSON MultiPoint      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
          properties:      
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
          title: GeoJSON MultiLineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
          properties:      
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
          title: GeoJSON MultiPolygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
      x-ngsi:      
        type: GeoProperty      
    minorLoss:      
      description: 'Unitless minor loss coefficient that applies when the valve is completely opened. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code'      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: No unit      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    openStatus:      
      description: 'Status of a valve as a numeric percentage value representing how open or close the valve is. 0% - completely closed, 100% - fully open'      
      maximum: 1      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: ' https://schema.org/Number'      
        type: Property      
        units: ' %'      
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
    quality:      
      description: Observed quality in the network component      
      properties:      
        observedBy:      
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
        value:      
          description: Numerical value of the quality      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
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
    setting:      
      description: 'A parameter that describes the valve''s operational setting. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code'      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: No unit      
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    startsAt:      
      description: The ID of the node on the nominal upstream or inflow side of the valve      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    status:      
      description: 'The dynamic state of the node. Enum:''OPEN, CLOSED, CV'''      
      enum:      
        - OPEN      
        - CLOSED      
        - CV      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    tag:      
      description: 'An optional text string used to assign the pipe to a category, perhaps one based on age or material'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    type:      
      description: NGSI-LD Entity Type. It must be equal to Valve      
      enum:      
        - Valve      
      type: string      
      x-ngsi:      
        type: Property      
    valveCurve:      
      description: A relationship to the curve of the setting property. Only required when valveType is GPV      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    valveType:      
      description: 'The valve type of the element. enum:''FCV, GPV, PBV, PRV, PSV, TCV'''      
      enum:      
        - FCV      
        - GPV      
        - PBV      
        - PRV      
        - PSV      
        - TCV      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    velocity:      
      description: 'Observed velocity in the link (pipe, valve or pump)'      
      properties:      
        observedBy:      
          description: Where the velocity has been observed      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
        value:      
          description: Value of the velocity      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
    vertices:      
      description: 'Geoproperty. Coordinates of all vertices in the valve, ordered from the startsAt node to the endsAt node and encoded as a GeoJSON '      
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
          title: GeoJSON MultiPoint      
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
          title: GeoJSON Point      
          type: object      
  required:      
    - id      
    - type      
    - startsAt      
    - endsAt      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.WaterDistributionManagementEPANET/blob/master/Valve/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModels/WaterNetworkManagementEPANET/Valve/schema.json      
  x-model-tags: FIWARE4WATER      
  x-version: 0.1.0      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Exemples de charges utiles    
#### Valve NGSI-v2 key-values Exemple    
Voici un exemple d'une vanne au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "87fe7d79-0d4c-4da9-b7d0-3340efa0656awytsd",  
  "type": "Valve",  
  "initialStatus": "OPEN",  
  "openStatus": 0.3,  
  "status": "OPEN",  
  "diameter": 203.2,  
  "valveType": "PRV",  
  "setting": 40.0,  
  "minorLoss": 0.0,  
  "tag": "DMA1",  
  "startsAt": "uri:63fe7d79.0d4c-4da9-b7d0-3340efa0656a",  
  "endsAt": "uri:1863179e-3768-4480-9167-ff21f870dd19"  
}  
```  
</details>    
#### Valve NGSI-v2 normalisée Exemple    
Voici un exemple d'une vanne au format JSON-LD normalisé. Ce format est compatible avec la norme NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "87fe7d79-0d4c-4da9-b7d0-3340efa0656awytsd",  
  "type": "Valve",  
  "initialStatus": {  
    "type": "Text",  
    "value": "OPEN"  
  },  
  "status": {  
    "type": "Text",  
    "value": "OPEN"  
  },  
  "openStatus": {  
    "type": "Number",  
    "value": 0.3  
  },  
  "diameter": {  
    "type": "Number",  
    "value": 203.2  
  },  
  "valveType": {  
    "type": "Text",  
    "value": "PRV"  
  },  
  "setting": {  
    "type": "Number",  
    "value": 40.0  
  },  
  "minorLoss": {  
    "type": "Boolean",  
    "value": false  
  },  
  "tag": {  
    "type": "Text",  
    "value": "DMA1"  
  },  
  "startsAt": {  
    "type": "Text",  
    "value": "63fe7d79-0d4c-4da9-b7d0-3340efa0656a"  
  },  
  "endsAt": {  
    "type": "Text",  
    "value": "1863179e-3768-4480-9167-ff21f870dd19"  
  },  
  "flow": {  
    "type": "StructuredValue",  
    "value": {  
      "value": 20,  
      "observedBy": "device-9845A"  
    }  
  },  
  "velocity": {  
    "type": "StructuredValue",  
    "value": {  
      "value": 2,  
      "observedBy": "device-9845A"  
    }  
  },  
  "quality": {  
    "type": "StructuredValue",  
    "value": {  
      "value": 0.5,  
      "observedBy": "device-9845A"  
    }  
  }  
}  
```  
</details>    
#### Valve NGSI-LD key-values Exemple    
Voici un exemple d'une vanne au format JSON-LD en tant que valeurs-clés. Ce format est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "87fe7d79-0d4c-4da9-b7d0-3340efa0656awytsd",  
  "type": "Valve",  
  "diameter": 203.2,  
  "endsAt": "uri:1863179e-3768-4480-9167-ff21f870dd19",  
  "initialStatus": "OPEN",  
  "minorLoss": 0.0,  
  "openStatus": 0.3,  
  "setting": 40.0,  
  "startsAt": "uri:63fe7d79.0d4c-4da9-b7d0-3340efa0656a",  
  "status": "OPEN",  
  "tag": "DMA1",  
  "valveType": "PRV",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.WaterDistributionManagementEPANET/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### Valve NGSI-LD normalisée Exemple    
Voici un exemple d'une vanne au format JSON-LD normalisé. Ce format est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:Valve:87fe7d79-0d4c-4da9-b7d0-3340efa0656awytsd",  
    "type": "Valve",  
    "createdAt": "2020-03-02T15:42:00Z",  
    "diameter": {  
        "type": "Property",  
        "value": 203.2,  
        "unitCode": "MMT"  
    },  
    "endsAt": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Reservoir:1863179e-3768-4480-9167-ff21f870dd19"  
    },  
    "initiaStatus": {  
        "type": "Property",  
        "value": "OPEN"  
    },  
    "minorLoss": {  
        "type": "Property",  
        "value": 0.0,  
        "unitCode": "C62"  
    },  
    "modifiedAt": "2020-03-02T15:45:00Z",  
    "openStatus": {  
        "type": "Property",  
        "value": 0.3  
    },  
    "setting": {  
        "type": "Property",  
        "value": 40.0,  
        "unitCode": "C62"  
    },  
    "startsAt": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Junction:63fe7d79-0d4c-4da9-b7d0-3340efa0656a"  
    },  
    "status": {  
        "type": "Property",  
        "value": "OPEN"  
    },  
    "tag": {  
        "type": "Property",  
        "value": "DMA1"  
    },  
    "valveType": {  
        "type": "Property",  
        "value": "PRV"  
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
