<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: Stausee  
================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.WaterDistributionManagementEPANET/blob/master/Reservoir/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Diese Entität enthält eine harmonisierte Beschreibung eines generischen Reservoirs für den Bereich Wassernetzmanagement. Diese Entität ist in erster Linie mit der vertikalen Wasserwirtschaft und damit verbundenen IoT-Anwendungen verbunden.**  
Version: 0.0.1  
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
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `elevation[number]`: Die Höhe über einer gemeinsamen Referenz des Stausees. Alle Einheiten werden im Code [CEFACT](https://www.unece.org/cefact.html) akzeptiert.  . Model: [https://schema.org/Number](https://schema.org/Number)- `hasInlet[*]`: Eine Beziehung, die die Wassereinlasspunkte des Stausees angibt  - `hasOutlet[*]`: Eine Beziehung, die die Wasseraustrittsstellen des Stausees angibt  - `head[object]`: Beobachtete Förderhöhe am Knotenpunkt (Kreuzung, Tank oder Reservoir)  	- `observedBy`:     
- `headPattern[*]`: Die ID-Bezeichnung eines Zeitmusters, das zur Modellierung der zeitlichen Variation der Gesamtförderhöhe des Reservoirs verwendet wird  - `id[*]`: Eindeutiger Bezeichner der Entität  - `initialQuality[object]`: Anfangsqualität der Netzkomponente  	- `observedBy`:     
- `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `pressure[object]`: Beobachteter Druck am Knotenpunkt (Verbindungsstelle, Tank oder Reservoir)  	- `observedBy`:     
- `quality[object]`: Beobachtete Qualität in der Netzkomponente  	- `observedBy`:     
- `reservoirHead[number]`: Die hydraulische Höhe (Höhe + Druckhöhe) des Wassers im Stausee. Alle Einheiten werden im Code [CEFACT](https://www.unece.org/cefact.html) akzeptiert.  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `sourceCategory[object]`: Beschreibung der Qualität des Quellstroms, der an einem bestimmten Knoten in das Netz eintritt  . Model: [https://schema.org/Text](https://schema.org/Text)	- `sourcePattern[*]`: Eine Beziehung zu dem Muster der Eigenschaft sourceCategory    
	- `sourceQuality[number]`: Ausgangs- oder Durchschnittskonzentration (oder Massendurchsatz) der Quelle. Eine Untereigenschaft der Eigenschaft "sourceCategory". Alle Einheiten werden im [CEFACT](https://www.unece.org/cefact.html)-Code akzeptiert  . Model: [https://schema.org/Number](https://schema.org/Number)  
	- `sourceType[string]`: Eine Untereigenschaft der Eigenschaft sourceCategory  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `sourceMassInflow[object]`: Beobachteter Massezufluss der Quelle am Knotenpunkt (Knotenpunkt, Tank oder Reservoir)  	- `observedBy`:     
- `supply[object]`: Beobachtete Versorgung am Knotenpunkt (Anschlussstelle, Tank oder Reservoir)  	- `observedBy`:     
- `tag[string]`: Eine optionale Textzeichenfolge, die dazu dient, das Rohr einer Kategorie zuzuordnen, z. B. einer Kategorie, die auf Alter oder Material basiert  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI-LD-Entitätstyp. Er muss gleich Reservoir sein  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `id`  - `location`  - `reservoirHead`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Reservoir:    
  description: This entity contains a harmonised description of a generic Reservoir made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.    
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
    elevation:    
      description: 'The elevation above some common reference of the Reservoir. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Metre    
    hasInlet:    
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
      description: A relationship indicating the water inlet points of the Reservoir    
      x-ngsi:    
        type: Relationship    
    hasOutlet:    
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
      description: A relationship indicating the water outlet points of the Reservoir    
      x-ngsi:    
        type: Relationship    
    head:    
      description: 'Observed head at the node (junction, tank or reservoir)'    
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
          description: Value of the head    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    headPattern:    
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
      description: The ID label of a time pattern used to model time variation in the reservoir's total head    
      x-ngsi:    
        type: Relationship    
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
    initialQuality:    
      description: Initial quality in the network component    
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
          description: Numerical value of the initial quality    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
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
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
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
    pressure:    
      description: 'Observed pressure at the node (junction, tank or reservoir)'    
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
          description: Numerical value of the pressure    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
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
    reservoirHead:    
      description: 'The hydraulic head (elevation + pressure head) of water in the Reservoir. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Metre    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    sourceCategory:    
      description: Description of the quality of source flow entering the network at a specific node    
      properties:    
        sourcePattern:    
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
          description: A relationship to the pattern pf the sourceCategory property    
          x-ngsi:    
            type: Relationship    
        sourceQuality:    
          description: 'Baseline or average concentration (or mass flow rate) of source. A sub-property of the Property ''sourceCategory''. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code'    
          type: number    
          x-ngsi:    
            model: https://schema.org/Number    
            type: Property    
            units: ' mg/L'    
        sourceType:    
          description: A sub-property of the Property sourceCategory    
          enum:    
            - CONCEN    
            - MASS    
            - FLOWPACED    
            - SETPOINT    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        value:    
          description: Value of the source category    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    sourceMassInflow:    
      description: 'Observed source mass inflow at the node (junction, tank or reservoir)'    
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
          description: Numerical value of the source mass at the inflow    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    supply:    
      description: 'Observed supply at the node (junction, tank or reservoir)'    
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
          description: Numerical value of the supply    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    tag:    
      description: 'An optional text string used to assign the pipe to a category, perhaps one based on age or material'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: NGSI-LD Entity Type. It must be equal to Reservoir    
      enum:    
        - Reservoir    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - location    
    - reservoirHead    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.WaterDistributionManagementEPANET/blob/master/Reservoir/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.WaterDistributionManagementEPANET/Reservoir/schema.json    
  x-model-tags: FIWARE4WATER    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### Reservoir NGSI-v2 Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein Reservoir im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
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
  "initialQuality": {  
    "value": 0.5  
  },  
  "sourceCategory": {  
    "value": "CategoryX",  
    "sourceType": "MASS",  
    "sourceQuality": 1.2,  
    "sourcePattern": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
  },  
  "tag": "DMA1"  
}  
```  
</details>  
#### Reservoir NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein Reservoir im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
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
    "type": "Number",  
    "value": 59.00  
  },  
  "headPattern": {  
    "type": "Relationship",  
    "object": "fbcb5fc8-8ca3-4533"  
  },  
  "elevation": {  
    "type": "Number",  
    "value": 105.8  
  },  
  "description": {  
    "type": "Text",  
    "value": "This entity contains a harmonised description of a Reservoir"  
  },  
  "initialQuality": {  
    "type": "Number",  
    "value": {  
      "observedBy": "device-9845A",  
      "value": 0.5  
    }  
  },  
  "sourceCategory": {  
    "type": "object",  
    "value": {  
      "value": "CategoryX",  
      "sourceType": "MASS",  
      "sourceQuality": 1.2,  
      "sourcePattern": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
    }  
  },  
  "tag": {  
    "type": "Text",  
    "value": "DMA1"  
  },  
  "pressure": {  
    "type": "object",  
    "value": {  
      "value": 20,  
      "observedBy": "device-9845A"  
    }  
  },  
  "supply": {  
    "type": "object",  
    "value": {  
      "value": 150,  
      "observedBy": "device-9845A"  
    }  
  },  
  "head": {  
    "type": "object",  
    "value": {  
      "value": 20,  
      "observedBy": "device-9845A"  
    }  
  },  
  "quality": {  
    "type": "object",  
    "value": {  
      "value": 0.5,  
      "observedBy": "device-9845A"  
    }  
  },  
  "sourceMassInflow": {  
    "type": "object",  
    "value": {  
      "value": 100,  
      "observedBy": "device-9845A"  
    }  
  }  
}  
```  
</details>  
#### Reservoir NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein Reservoir im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Reservoir:1863179e-3768-4480-9167-ff21f870dd19",  
    "type": "Reservoir",  
    "createdAt": "2020-03-02T15:42:00Z",  
    "description": "This entity contains a harmonised description of a Reservoir",  
    "elevation": 105.8,  
    "headPattern": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533",  
    "initialQuality": 0.5,  
    "location": {  
        "coordinates": [  
            24.30623,  
            60.07966  
        ],  
        "type": "Point"  
    },  
    "modifiedAt": "2020-03-02T15:45:00Z",  
    "reservoirHead": 59.0,  
    "sourceCategory": "CategroyX",  
    "tag": "DMA1",  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.WaterDistributionManagementEPANET/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### Reservoir NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein Reservoir im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Reservoir:1863179e-3768-4480-9167-ff21f870dd19",  
    "type": "Reservoir",  
    "description": {  
        "type": "Property",  
        "value": "This entity contains a harmonised description of a Reservoir"  
    },  
    "elevation": {  
        "type": "Property",  
        "value": 105.8,  
        "unitCode": "MTR"  
    },  
    "head": {  
        "type": "Property",  
        "value": {  
            "type": "Property",  
            "value": 20,  
            "unitCode": "MTR"  
        },  
        "observedBy": {  
            "type": "Relationship",  
            "object": "urn:ngsi-ld:Device:device-9845A"  
        }  
    },  
    "headPattern": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533"  
    },  
    "initialQuality": {  
        "type": "Property",  
        "value": 0.5,  
        "unitCode": "M1"  
    },  
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
    "pressure": {  
        "type": "Property",  
        "value": {  
            "type": "Property",  
            "value": 20,  
            "unitCode": "MTR"  
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
            "unitCode": "M1"  
        },  
        "observedBy": {  
            "type": "Relationship",  
            "object": "urn:ngsi-ld:Device:device-9845A"  
        }  
    },  
    "reservoirHead": {  
        "type": "Property",  
        "value": 59.0,  
        "unitCode": "MTR"  
    },  
    "sourceCategory": {  
        "type": "Property",  
        "value": {  
            "type": "Property",  
            "value": "CategoryX"  
        },  
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
    "sourceMassInflow": {  
        "type": "Property",  
        "value": {  
            "type": "Property",  
            "value": 100,  
            "unitCode": "F27"  
        },  
        "observedBy": {  
            "type": "Relationship",  
            "object": "urn:ngsi-ld:Device:device-9845A"  
        }  
    },  
    "supply": {  
        "type": "Property",  
        "value": {  
            "type": "Property",  
            "value": 150,  
            "unitCode": "LTR"  
        },  
        "observedBy": {  
            "type": "Relationship",  
            "object": "urn:ngsi-ld:Device:device-9845A"  
        }  
    },  
    "tag": {  
        "type": "Property",  
        "value": "DMA1"  
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
