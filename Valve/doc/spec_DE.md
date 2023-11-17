<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: Ventil    
===============<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.WaterDistributionManagementEPANET/blob/master/Valve/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Globale Beschreibung: **Diese Einheit enthält eine harmonisierte Beschreibung eines generischen Ventils für die Wassernetzverwaltung. Diese Entität ist in erster Linie mit der vertikalen Wasserwirtschaft und damit verbundenen IoT-Anwendungen verbunden.**    
Version: 0.1.0    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste der Eigenschaften    
<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.    
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel, Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Land liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.      
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `diameter[number]`: Der Ventildurchmesser. Alle Einheiten werden im Code [CEFACT](https://www.unece.org/cefact.html) akzeptiert.  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `endsAt[uri]`: Die ID des Knotens auf der nominalen stromabwärts gelegenen oder druckseitigen Seite des Ventils  - `flow[object]`: Durchflussmenge vom Knoten `startsAt` zum Knoten `endsAt`, gemessen von einem Gerät an der Verbindung (Rohr, Ventil oder Pumpe)  	- `observedBy`:       
- `id[*]`: Eindeutiger Bezeichner der Entität  - `initialStatus[string]`: Der Verbindungsstatus zu Beginn der Simulation. Enum:'OPEN, CLOSED, CV'  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `minorLoss[number]`: Einheitsloser kleiner Verlustkoeffizient, der gilt, wenn das Ventil vollständig geöffnet ist. Alle Einheiten werden im Code [CEFACT](https://www.unece.org/cefact.html) akzeptiert.  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: Der Name dieses Artikels  - `openStatus[number]`: Status eines Ventils in Form eines numerischen Prozentwerts, der angibt, wie offen oder geschlossen das Ventil ist. 0% - vollständig geschlossen, 100% - vollständig geöffnet  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `quality[object]`: Beobachtete Qualität in der Netzkomponente  	- `observedBy`:       
- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `setting[number]`: Ein Parameter, der die Betriebseinstellung des Ventils beschreibt. Alle Einheiten werden im Code [CEFACT](https://www.unece.org/cefact.html) akzeptiert.  . Model: [https://schema.org/Number](https://schema.org/Number)- `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `startsAt[uri]`: Die ID des Knotens auf der nominalen Anströmseite des Ventils  - `status[string]`: Der dynamische Zustand des Knotens. Enum:'OPEN, CLOSED, CV'  . Model: [https://schema.org/Text](https://schema.org/Text)- `tag[string]`: Eine optionale Textzeichenfolge, die verwendet wird, um das Rohr einer Kategorie zuzuordnen, z. B. auf der Grundlage von Alter oder Material  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI-LD Entitätstyp. Er muss gleich Ventil sein  - `valveCurve[uri]`: Eine Beziehung zur Kurve der Einstellungseigenschaft. Nur erforderlich, wenn valveType GPV ist  - `valveType[string]`: Der Ventiltyp des Elements. enum:'FCV, GPV, PBV, PRV, PSV, TCV'  . Model: [https://schema.org/Text](https://schema.org/Text)- `velocity[object]`: Beobachtete Geschwindigkeit in der Verbindung (Rohr, Ventil oder Pumpe)  	- `observedBy[uri]`: Wenn die Geschwindigkeit beobachtet wurde      
- `vertices[*]`: Geoproperty. Koordinaten aller Scheitelpunkte im Ventil, geordnet vom startsAt-Knoten zum endsAt-Knoten und kodiert als GeoJSON  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Erforderliche Eigenschaften    
- `endsAt`  - `id`  - `startsAt`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Datenmodell Beschreibung der Eigenschaften    
Alphabetisch sortiert (für Details anklicken)    
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
## Beispiel-Nutzlasten    
#### Ventil NGSI-v2 Schlüsselwerte Beispiel    
Hier ist ein Beispiel für ein Ventil im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
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
#### Ventil NGSI-v2 normalisiert Beispiel    
Hier ist ein Beispiel für ein Ventil im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
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
#### Ventil NGSI-LD Schlüsselwerte Beispiel    
Hier ist ein Beispiel für ein Ventil im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
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
#### Ventil NGSI-LD normalisiert Beispiel    
Hier ist ein Beispiel für ein Ventil im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
