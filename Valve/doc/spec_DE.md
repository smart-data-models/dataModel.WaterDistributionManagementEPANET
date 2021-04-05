Entität: Ventil  
===============  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.WaterDistributionManagementEPANET/blob/master/Valve/LICENSE.md)  
Globale Beschreibung: **Diese Entität enthält eine harmonisierte Beschreibung eines generischen Ventils, das für die Domäne Wassernetzmanagement gemacht wurde. Diese Entität ist in erster Linie mit der vertikalen Wasserwirtschaft und damit verbundenen IoT-Anwendungen verbunden.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `diameter`: Der Ventildurchmesser. Alle Einheiten werden im [CEFACT](https://www.unece.org/cefact.html) Code akzeptiert.  - `endsAt`: Die ID des Knotens auf der nominalen Nach- oder Druckseite des Ventils  - `flow`: Durchflussrate vom `startsAt`-Knoten zum `endsAt`-Knoten, gemessen von einem Gerät an der Verbindung (Rohr, Ventil oder Pumpe)  - `id`: Eindeutiger Bezeichner der Entität  - `initialStatus`: Der Link-Status beim Start der Simulation. Enum:'OPEN, CLOSED, CV'  - `location`:   - `minorLoss`: Einheitenloser Kleinverlustkoeffizient, der gilt, wenn das Ventil vollständig geöffnet ist. Alle Einheiten werden im [CEFACT](https://www.unece.org/cefact.html) Code akzeptiert.  - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `quality`: Beobachtete Qualität in der Netzwerkkomponente  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `setting`: Ein Parameter, der die Betriebseinstellung des Ventils beschreibt. Alle Einheiten werden im Code [CEFACT](https://www.unece.org/cefact.html) akzeptiert.  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `startsAt`: Die ID des Knotens auf der nominalen Vorlauf- oder Zulaufseite des Ventils  - `status`: Der dynamische Zustand des Knotens. Enum:'OPEN, CLOSED, CV'  - `tag`: Eine optionale Textzeichenkette, die dazu dient, das Rohr einer Kategorie zuzuordnen, z. B. basierend auf Alter oder Material  - `type`: NGSI-LD Entity Type. Er muss gleich Ventil sein.  - `valveCurve`: Eine Beziehung zur Kurve der Einstelleigenschaft. Nur erforderlich, wenn valveType GPV ist  - `valveType`: Der Ventiltyp des Elements. enum:'FCV, GPV, PBV, PRV, PSV, TCV'  - `velocity`: Beobachtete Geschwindigkeit in der Verbindung (Rohr, Ventil oder Pumpe)  - `vertices`: Koordinaten aller Scheitelpunkte im Ventil, geordnet vom startsAt-Knoten zum endsAt-Knoten und kodiert als GeoJSON    
Erforderliche Eigenschaften  
- `endsAt`  - `id`  - `startsAt`  - `type`  ## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Valve:    
  description: 'This entity contains a harmonised description of a generic Valve made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.'    
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
      description: 'The valve diameter. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        units: millimetre    
    endsAt:    
      description: 'The ID of the node on the nominal downstream or discharge side of the valve'    
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
      anyOf: &valve_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Unitless minor loss coefficient that applies when the valve is completely opened. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
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
        anyOf: *valve_-_properties_-_owner_-_items_-_anyof    
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
    setting:    
      description: 'A parameter that describes the valve''s operational setting. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'No unit'    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    startsAt:    
      description: 'The ID of the node on the nominal upstream or inflow side of the valve'    
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
      description: 'NGSI-LD Entity Type. It must be equal to Valve.'    
      enum:    
        - Valve    
      type: Property    
    valveCurve:    
      description: 'A relationship to the curve of the setting property. Only required when valveType is GPV'    
      format: uri    
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
      description: 'Coordinates of all vertices in the valve, ordered from the startsAt node to the endsAt node and encoded as a GeoJSON '    
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
    - startsAt    
    - endsAt    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
#### Ventil NGSI-v2-Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein Ventil im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
    "id": "87fe7d79-0d4c-4da9-b7d0-3340efa0656awytsd",  
    "type": "Valve",  
    "initiaStatus": "OPEN",  
    "status": "OPEN",  
    "diameter": 203.20,  
    "valveType": "PRV",  
    "setting": 40.00,  
    "minorLoss": 0.00,  
    "tag": "DMA1",  
    "startsAt": "uri:63fe7d79.0d4c-4da9-b7d0-3340efa0656a",  
    "endsAt": "uri:1863179e-3768-4480-9167-ff21f870dd19",  
    "initialStatus":"OPEN"  
}  
```  
#### Ventil NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein Ventil im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und gibt die Kontextdaten einer einzelnen Entität zurück.  
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
    "diameter": {  
        "type": "Number",  
        "value": 203.20  
    },  
    "valveType": {  
        "type": "Text",  
        "value": "PRV"  
    },  
    "setting": {  
        "type": "Number",  
        "value": 40.00  
    },  
    "minorLoss": {  
        "type": "Number",  
        "value": 0.00  
    },  
    "tag": {  
        "type": "Text",  
        "value": "DMA1"  
    },  
    "startsAt": {  
        "type": "Relationship",  
        "value": "63fe7d79-0d4c-4da9-b7d0-3340efa0656a"  
    },  
    "endsAt": {  
        "type": "Relationship",  
        "value": "1863179e-3768-4480-9167-ff21f870dd19"  
    },  
    "flow": {  
        "type": "object",  
        "value": {  
            "value": 20,  
            "observedBy": "device-9845A"  
        }  
    },  
    "velocity": {  
        "type": "object",  
        "value": {  
            "value": 2,  
            "observedBy": "device-9845A"  
        }  
    },  
    "quality": {  
        "type": "object",  
        "value": {  
            "value": 0.5,  
            "observedBy": "device-9845A"  
        }  
    }  
}  
```  
#### Ventil NGSI-LD-Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein Ventil im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ],  
  "id": "87fe7d79-0d4c-4da9-b7d0-3340efa0656awytsd",  
  "type": "Valve",  
  "initiaStatus": "OPEN",  
  "status": "OPEN",  
  "diameter": 203.2,  
  "valveType": "PRV",  
  "setting": 40.0,  
  "minorLoss": 0.0,  
  "tag": "DMA1",  
  "startsAt": "uri:63fe7d79.0d4c-4da9-b7d0-3340efa0656a",  
  "endsAt": "uri:1863179e-3768-4480-9167-ff21f870dd19",  
  "initialStatus": "OPEN"  
}  
```  
#### Ventil NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein Ventil im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:Valve:87fe7d79-0d4c-4da9-b7d0-3340efa0656awytsd",  
  "type": "Valve",  
  "createdAt": "2020-03-02T15:42:00Z",  
  "modifiedAt": "2020-03-02T15:45:00Z",  
  "initiaStatus": {  
    "type": "Property",  
    "value": "OPEN"  
  },  
  "status": {  
    "type": "Property",  
    "value": "OPEN"  
  },  
  "diameter": {  
    "type": "Property",  
    "value": 203.2,  
    "unitCode": "MMT"  
  },  
  "valveType": {  
    "type": "Property",  
    "value": "PRV"  
  },  
  "setting": {  
    "type": "Property",  
    "value": 40.0,  
    "unitCode": "C62"  
  },  
  "minorLoss": {  
    "type": "Property",  
    "value": 0.0,  
    "unitCode": "C62"  
  },  
  "tag": {  
    "type": "Property",  
    "value": "DMA1"  
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
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
