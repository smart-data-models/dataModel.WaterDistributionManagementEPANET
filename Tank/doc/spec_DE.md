Entität: Tank  
=============  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.WaterDistributionManagementEPANET/blob/master/Tank/LICENSE.md)  
Globale Beschreibung: **Diese Entität enthält eine harmonisierte Beschreibung eines generischen Tanks, der für die Domäne Wassernetzmanagement hergestellt wurde. Diese Entität ist in erster Linie mit der vertikalen Wasserwirtschaft und damit verbundenen IoT-Anwendungen verbunden.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `bulkReactionCoefficient`: Der Massenreaktionskoeffizient, der für die Modellierung von Reaktionen im Tank verwendet wird. Alle Einheiten werden im [CEFACT](https://www.unece.org/cefact.html)-Code akzeptiert.  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `elevation`: Die Höhe über einer gemeinsamen Referenz des Tanks. Alle Einheiten werden im Code [CEFACT](https://www.unece.org/cefact.html) akzeptiert.  - `hasInlet`: Eine Beziehung, die die Wassereinlasspunkte des Reservoirs anzeigt  - `hasOutlet`: Eine Beziehung, die die Wasserauslasspunkte des Reservoirs anzeigt  - `head`: Beobachtete Förderhöhe am Knotenpunkt (Abzweigung, Tank oder Reservoir)  - `id`: Eindeutiger Bezeichner der Entität  - `initLevel`: Die Höhe der Wasseroberfläche über der Bodenhöhe des Tanks zu Beginn der Simulation. Alle Einheiten werden im Code [CEFACT](https://www.unece.org/cefact.html) akzeptiert.  - `initialQuality`: Wasserqualitätsniveau im Tank zu Beginn der Simulation. Alle Einheiten werden im Code [CEFACT](https://www.unece.org/cefact.html) akzeptiert.  - `level`: Beobachteter Pegel im Element des Netzwerks  - `location`:   - `maxLevel`: Die Höhe der Wasseroberfläche über der Bodenhöhe des Tanks zu Beginn der Simulation. Alle Einheiten werden im Code [CEFACT](https://www.unece.org/cefact.html) akzeptiert.  - `minLevel`: Der Mindestpegel, auf den das Wasser im Tank sinken kann. Alle Einheiten werden im Code [CEFACT](https://www.unece.org/cefact.html) akzeptiert.  - `minVolume`: Das Wasservolumen im Tank, wenn dieser seinen minimalen Füllstand erreicht hat. Alle Einheiten werden im Code [CEFACT](https://www.unece.org/cefact.html) akzeptiert.  - `mixingFraction`: Der Anteil des Gesamtvolumens des Tanks, der das Einlass-Auslass-Kompartiment des Zwei-Kompartiment-Mischmodells (2COMP) umfasst. Alle Einheiten werden im [CEFACT](https://www.unece.org/cefact.html)-Code akzeptiert.  - `mixingModel`: Eine Untereigenschaft der Eigenschaft sourceCategory. Enum:'2COMP, FIFO, LIFO, MIXED'  - `name`: Der Name dieses Elements.  - `nominalDiameter`: Der Durchmesser des Tanks. Alle Einheiten werden im Code [CEFACT](https://www.unece.org/cefact.html) akzeptiert.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `pressure`: Beobachteter Druck am Knotenpunkt (Verbindungsstelle, Tank oder Reservoir)  - `quality`: Beobachtete Qualität in der Netzwerkkomponente  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `sourceCategory`: Beschreibung der Qualität des Quellstroms, der an einem bestimmten Knoten in das Netzwerk eintritt.  - `sourceMassInflow`: Eigenschaft. Beobachteter Quell-Massenzufluss am Knoten (Knotenpunkt, Tank oder Reservoir)  - `supply`: Beobachtete Versorgung am Knoten (Abzweig, Tank oder Reservoir)  - `tag`: Eine optionale Textzeichenkette, die dazu dient, das Rohr einer Kategorie zuzuordnen, z. B. basierend auf Alter oder Material  - `type`: NGSI-LD-Entitätstyp. Es muss Tank sein  - `volumeCurve`: Die ID-Kennzeichnung einer Kurve, die zur Beschreibung der Beziehung zwischen Tankvolumen und Wasserstand verwendet wird    
Erforderliche Eigenschaften  
- `id`  - `location`  - `type`  ## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Tank:    
  description: 'This entity contains a harmonised description of a generic tank made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.'    
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
    bulkReactionCoefficient:    
      description: 'The bulk reaction coefficient used for modelling reactions in the tank. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 1/day    
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
    elevation:    
      description: 'The elevation above some common reference of the Tank. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: metre    
    hasInlet:    
      description: 'A relationship indicating the water inlet points of the Reservoir'    
      format: uri    
      type: Relationship    
    hasOutlet:    
      description: 'A relationship indicating the water outlet points of the Reservoir'    
      format: uri    
      type: Relationship    
    head:    
      description: 'Observed head at the node (junction, tank or reservoir)'    
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
      anyOf: &tank_-_properties_-_owner_-_items_-_anyof    
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
    initLevel:    
      description: 'The height of the water surface above the bottom elevation of the tank at the start of the simulation. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: metre    
    initialQuality:    
      description: 'Water quality level in the tank at the start of the simulation. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: mg/L    
    level:    
      description: 'Observed level in the element of the network'    
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
    maxLevel:    
      description: 'The height of the water surface above the bottom elevation of the tank at the start of the simulation. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: metre    
    minLevel:    
      description: 'The minimum level that water in the tank can drop to. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: metre    
    minVolume:    
      description: 'The volume of water in the tank when it is at its minimum level. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'cubic metre'    
    mixingFraction:    
      description: 'The fraction of the tank''s total volume that comprises the inlet-outlet compartment of the two-compartment (2COMP) mixing model. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'No unit'    
    mixingModel:    
      description: 'A sub-property of the Property sourceCategory. Enum:''2COMP, FIFO, LIFO, MIXED'''    
      enum:    
        - 2COMP    
        - FIFO    
        - LIFO    
        - MIXED    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    name:    
      description: 'The name of this item.'    
      type: Property    
    nominalDiameter:    
      description: 'The diameter of the tank. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: Metre    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *tank_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    pressure:    
      description: 'Observed pressure at the node (junction, tank or reservoir)'    
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
    sourceCategory:    
      description: 'Description of the quality of source flow entering the network at a specific node.'    
      properties:    
        sourcePattern:    
          anyOf:    
            - description: 'Property. Identifier format of any NGSI entity'    
              maxLength: 256    
              minLength: 1    
              pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
              type: string    
            - description: 'Property. Identifier format of any NGSI entity'    
              format: uri    
              type: string    
          description: 'Relationship. A relationship to the pattern pf the sourceCategory property'    
        sourceQuality:    
          description: 'Property. Model:''https://schema.org/Number''. Units: ''mg/L''. Baseline or average concentration (or mass flow rate) of source. A sub-property of the Property ''sourceCategory''. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
          type: number    
        sourceType:    
          description: 'Property. Model:''https://schema.org/Text''. A sub-property of the Property ''sourceCategory'''    
          enum:    
            - CONCEN    
            - MASS    
            - FLOWPACED    
            - SETPOINT    
          type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    sourceMassInflow:    
      description: 'Property.. Observed source mass inflow at the node (junction, tank or reservoir)'    
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
      type: object    
    supply:    
      description: 'Observed supply at the node (junction, tank or reservoir)'    
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
    tag:    
      description: 'An optional text string used to assign the pipe to a category, perhaps one based on age or material'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    type:    
      description: 'NGSI-LD Entity Type. It has to be Tank'    
      enum:    
        - Tank    
      type: Property    
    volumeCurve:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'The ID label of a curve used to describe the relation between tank volume and water level'    
      type: Relationship    
  required:    
    - id    
    - type    
    - location    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
#### Tank NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen Tank im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
    "id": "1863179e-3968-4493-9167-ee21f880cc02",  
    "type": "Tank",  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            24.30623,  
            60.07966  
        ]  
    },  
    "elevation": 112.9,  
    "initLevel": 3,  
    "minLevel": 0,  
    "maxLevel": 6.75,  
    "minVolume": 0,  
    "nominalDiameter": 13.73,  
    "description": "Free Text",  
    "initialQuality": 0.5,  
    "sourceCategory": {  
        "value": "category1",  
        "sourceType": "MASS",  
        "sourceQuality": 1.2,  
        "sourcePattern": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
    },  
    "mixingModel": "MIXED",  
    "volumeCurve": "fAM-8ca3-4533-a2eb-12015",  
    "mixingFraction": 0.7,  
    "bulkReactionCoefficient": 0.7,  
    "tag": "DMA1"  
}  
```  
#### Tank NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen Tank im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und gibt die Kontextdaten einer einzelnen Entität zurück.  
```json  
{  
  "id": "1863179e-3968-4493-9167-ee21f880cc02",  
  "type": "Tank",  
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
    "type": "Number",  
    "value": 112.9  
  },  
  "initLevel": {  
    "type": "Number",  
    "value": 3  
  },  
  "minLevel": {  
    "type": "Number",  
    "value": 0  
  },  
  "maxLevel": {  
    "type": "Number",  
    "value": 6.75  
  },  
  "minVolume": {  
    "type": "Number",  
    "value": 0  
  },  
  "nominalDiameter": {  
    "type": "Number",  
    "value": 13.73  
  },  
  "description": {  
    "type": "Text",  
    "value": "Free Text"  
  },  
  "initialQuality": {  
    "type": "Number",  
    "value": 0.5  
  },  
  "sourceCategory": {  
    "type": "object",  
    "value": {  
      "value": "category1",  
      "sourceType": "MASS",  
      "sourceQuality": 1.2,  
      "sourcePattern": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
    }  
  },  
  "mixingModel": {  
    "type": "Text",  
    "value": "MIXED"  
  },  
  "volumeCurve": {  
    "type": "Relationship",  
    "value": "fAM-8ca3-4533-a2eb-12015"  
  },  
  "mixingFraction": {  
    "type": "Number",  
    "value": 0.7  
  },  
  "bulkReactionCoefficient": {  
    "type": "Number",  
    "value": 0.7  
  },  
  "tag": {  
    "type": "Text",  
    "value": "DMA1"  
  },  
  "level": {  
    "type": "object",  
    "value": {  
      "value": 20,  
      "observedBy": "device-9845A"  
    }  
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
#### Tank NGSI-LD-Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen Tank im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ],  
  "bulkReactionCoefficient": 0.7,  
  "createdAt": "2020-03-13T15:42:00Z",  
  "description": "Free Text",  
  "elevation": 112.9,  
  "id": "urn:ngsi-ld:Tank:1863179e-3968-4493-9167-ee21f880cc02",  
  "initLevel": 3,  
  "initialQuality": 0.5,  
  "location": {  
    "coordinates": [  
      24.30623,  
      60.07966  
    ],  
    "type": "Point"  
  },  
  "maxLevel": 6.75,  
  "minLevel": 0,  
  "minVolume": 0,  
  "mixingFraction": 0.7,  
  "mixingModel": "MIXED",  
  "modifiedAt": "2020-03-13T15:45:00Z",  
  "nominalDiameter": 13.73,  
  "sourceCategory": "category1",  
  "tag": "DMA1",  
  "type": "Tank",  
  "volumeCurve": "urn:ngsi-ld:Curve:fAM-8ca3-4533-a2eb-12015"  
}  
```  
#### Tank NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen Tank im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:Tank:1863179e-3968-4493-9167-ee21f880cc02",  
  "type": "Tank",  
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
    "value": 112.9,  
    "unitCode": "MTR"  
  },  
  "initLevel": {  
    "type": "Property",  
    "value": 3,  
    "unitCode": "MTR"  
  },  
  "minLevel": {  
    "type": "Property",  
    "value": 0,  
    "unitCode": "MTR"  
  },  
  "maxLevel": {  
    "type": "Property",  
    "value": 6.75,  
    "unitCode": "MTR"  
  },  
  "minVolume": {  
    "type": "Property",  
    "value": 0,  
    "unitCode": "MTQ"  
  },  
  "nominalDiameter": {  
    "type": "Property",  
    "value": 13.73,  
    "unitCode": "MTR"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Free Text"  
  },  
  "initialQuality": {  
    "type": "Property",  
    "value": 0.5,  
    "unitCode": "M1"  
  },  
  "sourceCategory": {  
    "type": "Property",  
    "value": {  
      "type": "Property",  
      "value": "category1"  
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
  "mixingModel": {  
    "type": "Property",  
    "value": "MIXED"  
  },  
  "volumeCurve": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Curve:fAM-8ca3-4533-a2eb-12015"  
  },  
  "mixingFraction": {  
    "type": "Property",  
    "value": 0.7,  
    "unitCode": "C62"  
  },  
  "bulkReactionCoefficient": {  
    "type": "Property",  
    "value": 0.7,  
    "unitCode": "E91"  
  },  
  "tag": {  
    "type": "Property",  
    "value": "DMA1"  
  },  
  "level": {  
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
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
