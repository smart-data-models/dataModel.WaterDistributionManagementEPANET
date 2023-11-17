<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: SimulationResult    
=========================<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.WaterDistributionManagementEPANET/blob/master/SimulationResult/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Globale Beschreibung: **Diese Einheit enthält eine harmonisierte Beschreibung eines generischen Simulationsergebnisses, das für den Bereich Wassernetzmanagement erstellt wurde. Diese Entität ist in erster Linie mit der vertikalen Wassernetzverwaltung und damit verbundenen IoT-Anwendungen verbunden.**    
Version: 0.0.2    
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
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `demandCategory[object]`: Ermöglicht die Zuordnung von Basisanforderungen und Zeitmustern zu anderen Nutzerkategorien  . Model: [https://schema.org/Text](https://schema.org/Text)	- `baseDemand[string]`: Grundlegende oder durchschnittliche Nachfrage für die Kategorie. Eine Untereigenschaft der Eigenschaft demandCategory  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `demandPattern[*]`: Eine Beziehung zu dem Muster der Eigenschaft "demandCategory".      
- `description[string]`: Eine Beschreibung dieses Artikels  - `energyUse[object]`: Beobachteter Energieverbrauch durch das Element des Netzes  	- `observedBy`:       
- `flow[object]`: Durchflussmenge vom Knoten `startsAt` zum Knoten `endsAt`, gemessen von einem Gerät an der Verbindung (Rohr, Ventil oder Pumpe)  	- `observedBy`:       
- `hasInputNetwork[*]`: Die ID des in der Simulation verwendeten Netzes  . Model: [https://schema.org/URL](https://schema.org/URL)- `head[object]`: Beobachtete Förderhöhe am Knotenpunkt (Kreuzung, Tank oder Reservoir)  	- `observedBy`:       
- `id[*]`: Eindeutiger Bezeichner der Entität  - `initialQuality[object]`: Anfangsqualität der Netzkomponente  	- `observedBy`:       
- `initialStatus[string]`: Der Verbindungsstatus zu Beginn der Simulation. Enum:'OPEN, CLOSED, CV'  . Model: [https://schema.org/Text](https://schema.org/Text)- `level[object]`: Beobachteter Pegel in dem Element des Netzes  	- `observedBy`:       
- `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels  - `outputFile[uri]`: Link zu einer Binärdatei mit den Ergebnissen der auf das Netz angewandten Simulation  - `outputParameters[array]`: Beschreibung der Ergebnismenge der auf das Netz angewandten Simulation  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `pressure[object]`: Beobachteter Druck am Knotenpunkt (Verbindungsstelle, Tank oder Reservoir)  	- `observedBy`:       
- `quality[object]`: Beobachtete Qualität in der Netzkomponente  	- `observedBy`:       
- `refSimulationScenario[*]`: Die ID des Simulationsszenarios  . Model: [https://schema.org/URL](https://schema.org/URL)- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `sourceCategory[object]`: Beschreibung der Qualität des Quellstroms, der an einem bestimmten Knoten in das Netz eintritt  . Model: [https://schema.org/Text](https://schema.org/Text)	- `sourcePattern[*]`: Eine Beziehung zu dem Muster der Eigenschaft sourceCategory      
	- `sourceQuality[number]`: Ausgangs- oder Durchschnittskonzentration (oder Massendurchsatz) der Quelle. Eine Untereigenschaft der Eigenschaft "sourceCategory". Alle Einheiten werden im [CEFACT](https://www.unece.org/cefact.html)-Code akzeptiert  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `sourceType[string]`: Eine Untereigenschaft der Eigenschaft sourceCategory  . Model: [https://schema.org/Text](https://schema.org/Text)    
- `sourceMassInflow[object]`: Beobachteter Massezufluss der Quelle am Knotenpunkt (Knotenpunkt, Tank oder Reservoir)  	- `observedBy`:       
- `status[string]`: Der dynamische Zustand des Knotens. Enum:'OPEN, CLOSED, CV'  . Model: [https://schema.org/Text](https://schema.org/Text)- `supply[object]`: Beobachtete Versorgung am Knotenpunkt (Anschlussstelle, Tank oder Reservoir)  	- `observedBy`:       
- `tag[string]`: Eine optionale Textzeichenfolge, die verwendet wird, um das Rohr einer Kategorie zuzuordnen, z. B. auf der Grundlage von Alter oder Material  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI-LD-Entitätstyp. Es muss SimulationResult sein  - `valveCurve[*]`: Hinweis auf die Kurve, in der sich das Ventil befindet  - `valveType[string]`: Typ des Ventils nach Ventilkategorien. Enum:'FCV, GPV, PBV, PRV, PSV, TCV'  - `velocity[object]`: Beobachtete Geschwindigkeit in der Verbindung (Rohr, Ventil oder Pumpe)  	- `observedBy[uri]`: Wenn die Geschwindigkeit beobachtet wurde      
<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Erforderliche Eigenschaften    
- `id`  - `refSimulationScenario`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Datenmodell Beschreibung der Eigenschaften    
Alphabetisch sortiert (für Details anklicken)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
SimulationResult:      
  description: This entity contains a harmonised description of a generic simulation result made for the Water Network Management domain. This entity is primarily associated with the water network management vertical and related IoT applications.      
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
    demandCategory:      
      description: Allows base demands and time patterns to be assigned to other categories of users      
      properties:      
        baseDemand:      
          description: Baseline or average demand for the category. A sub-property of the Property demandCategory      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        demandPattern:      
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
          description: A relationship to the pattern of the 'demandCategory' property      
          x-ngsi:      
            type: Relationship      
        value:      
          description: Value of the demand category      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    energyUse:      
      description: Observed energy use by the element of the network      
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
          description: Numerical value of the use of Energy      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
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
    hasInputNetwork:      
      anyOf:      
        - maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
        - format: uri      
          type: string      
      description: The ID of the network used in the simulation      
      x-ngsi:      
        model: https://schema.org/URL      
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
    level:      
      description: Observed level in the element of the network      
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
          description: Numerical value of the level      
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
    outputFile:      
      description: Link to binary file containing results of applied simulation to the network      
      format: uri      
      type: string      
      x-ngsi:      
        type: Property      
    outputParameters:      
      description: Description of the set of results of applied simulation to the network      
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
      type: array      
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
    refSimulationScenario:      
      anyOf:      
        - maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
        - format: uri      
          type: string      
      description: The ID of the simulation scenario      
      x-ngsi:      
        model: https://schema.org/URL      
        type: Relationship      
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
      description: NGSI-LD Entity Type. It has to be SimulationResult      
      enum:      
        - SimulationResult      
      type: string      
      x-ngsi:      
        type: Property      
    valveCurve:      
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
      description: Reference to the Curve where the valve is located      
      x-ngsi:      
        type: Relationship      
    valveType:      
      description: 'Type of valve according to valve categories. Enum:''FCV, GPV, PBV, PRV, PSV, TCV'''      
      enum:      
        - FCV      
        - GPV      
        - PBV      
        - PRV      
        - PSV      
        - TCV      
      type: string      
      x-ngsi:      
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
  required:      
    - id      
    - type      
    - refSimulationScenario      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.WaterDistributionManagementEPANET/blob/master/SimulationResult/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.WaterDistributionManagementEPANET/Result/schema.json      
  x-model-tags: FIWARE4WATER      
  x-version: 0.0.2      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Beispiel-Nutzlasten    
#### SimulationResult NGSI-v2 key-values Beispiel    
Hier ist ein Beispiel für ein SimulationResult im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
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
</details>    
#### SimulationResult NGSI-v2 normalisiert Beispiel    
Hier ist ein Beispiel für ein SimulationResult im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SimulationResult:01",  
  "type": "SimulationResult",  
  "description": {  
    "type": "Text",  
    "value": "Free Text"  
  },  
  "hasInputNetwork": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:WaterNetwork:01"  
  },  
  "refSimulationScenario": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Simulation:01"  
  },  
  "outputParameters": {  
    "type": "StructuredValue",  
    "value": [  
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
}  
```  
</details>    
#### SimulationResult NGSI-LD Schlüsselwerte Beispiel    
Hier ist ein Beispiel für ein SimulationResult im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SimulationResult:01",  
  "type": "SimulationResult",  
  "description": "Free Text",  
  "hasInputNetwork": "urn:ngsi-ld:WaterNetwork:01",  
  "outputFile": "c://epanetsimulations/simulationResult.bin",  
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
  "refSimulationScenario": "urn:ngsi-ld:Simulation:01",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.WaterDistributionManagementEPANET/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### SimulationResult NGSI-LD normalisiert Beispiel    
Hier ist ein Beispiel für ein SimulationResult im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
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
    "outputFile": [  
        {  
            "type": "Relationship",  
            "object": "c://epanetsimulations/simulationResult.bin"  
        }  
    ],  
    "refSimulationScenario": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Simulation:01"  
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
