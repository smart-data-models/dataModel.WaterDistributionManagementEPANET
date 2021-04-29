Entität: Stausee  
================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.WaterDistributionManagementEPANET/blob/master/Reservoir/LICENSE.md)  
Globale Beschreibung: **Diese Entität enthält eine harmonisierte Beschreibung eines generischen Reservoirs, die für die Wassernetzmanagement-Domäne erstellt wurde. Diese Entität ist in erster Linie mit der vertikalen Wasserwirtschaft und damit verbundenen IoT-Anwendungen verbunden.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `elevation`: Die Höhe über einer gemeinsamen Referenz des Stausees. Alle Einheiten werden im Code [CEFACT](https://www.unece.org/cefact.html) akzeptiert.  - `hasInlet`: Eine Beziehung, die die Wassereinlasspunkte des Reservoirs anzeigt  - `hasOutlet`: Eine Beziehung, die die Wasserauslasspunkte des Reservoirs anzeigt  - `head`: Beobachtete Förderhöhe am Knotenpunkt (Abzweigung, Tank oder Reservoir)  - `headPattern`: Die ID-Bezeichnung eines Zeitmusters, das zur Modellierung der zeitlichen Variation der Gesamtförderhöhe des Reservoirs verwendet wird  - `id`: Eindeutiger Bezeichner der Entität  - `initialQuality`: Anfangsqualität in der Netzwerkkomponente  - `location`:   - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `pressure`: Beobachteter Druck am Knotenpunkt (Verbindungsstelle, Tank oder Reservoir)  - `quality`: Beobachtete Qualität in der Netzwerkkomponente  - `reservoirHead`: Die hydraulische Höhe (Höhe + Druckhöhe) des Wassers im Reservoir. Alle Einheiten werden im Code [CEFACT](https://www.unece.org/cefact.html) akzeptiert.  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `sourceCategory`: Beschreibung der Qualität des Quellflusses, der an einem bestimmten Knoten in das Netzwerk eintritt.  - `sourceMassInflow`: Eigenschaft. Beobachteter Quell-Massenzufluss am Knoten (Knotenpunkt, Tank oder Reservoir)  - `supply`: Beobachtete Versorgung am Knoten (Abzweig, Tank oder Reservoir)  - `tag`: Eine optionale Textzeichenkette, die dazu dient, das Rohr einer Kategorie zuzuordnen, z. B. basierend auf Alter oder Material  - `type`: NGSI-LD Entity Type. Er muss gleich Reservoir sein.    
Erforderliche Eigenschaften  
- `id`  - `location`  - `reservoirHead`  - `type`  ## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Reservoir:    
  description: 'This entity contains a harmonised description of a generic Reservoir made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.'    
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
    elevation:    
      description: 'The elevation above some common reference of the Reservoir. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: Metre    
    hasInlet:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A relationship indicating the water inlet points of the Reservoir'    
      type: Relationship    
    hasOutlet:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A relationship indicating the water outlet points of the Reservoir'    
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
    headPattern:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'The ID label of a time pattern used to model time variation in the reservoir''s total head'    
      type: Relationship    
    id:    
      anyOf: &reservoir_-_properties_-_owner_-_items_-_anyof    
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
    initialQuality:    
      description: 'Initial quality in the network component'    
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
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *reservoir_-_properties_-_owner_-_items_-_anyof    
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
    reservoirHead:    
      description: 'The hydraulic head (elevation + pressure head) of water in the Reservoir. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: Metre    
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
      description: 'NGSI-LD Entity Type. It must be equal to Reservoir.'    
      enum:    
        - Reservoir    
      type: Property    
  required:    
    - id    
    - type    
    - location    
    - reservoirHead    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
#### Reservoir NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für ein Reservoir im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
    "value": "CategroyX",  
    "sourceType": "MASS",  
    "sourceQuality": 1.2,  
    "sourcePattern": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
  },  
  "tag": "DMA1"  
}  
```  
#### Reservoir NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein Reservoir im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
    "value": 0.5  
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
#### Reservoir NGSI-LD-Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein Reservoir im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ],  
  "createdAt": "2020-03-02T15:42:00Z",  
  "description": "This entity contains a harmonised description of a Reservoir",  
  "elevation": 105.8,  
  "headPattern": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533",  
  "id": "urn:ngsi-ld:Reservoir:1863179e-3768-4480-9167-ff21f870dd19",  
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
  "type": "Reservoir"  
}  
```  
#### Reservoir NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein Reservoir im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:Reservoir:1863179e-3768-4480-9167-ff21f870dd19",  
  "type": "Reservoir",  
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
  "reservoirHead": {  
    "type": "Property",  
    "value": 59.0,  
    "unitCode": "MTR"  
  },  
  "headPattern": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533"  
  },  
  "elevation": {  
    "type": "Property",  
    "value": 105.8,  
    "unitCode": "MTR"  
  },  
  "description": {  
    "type": "Property",  
    "value": "This entity contains a harmonised description of a Reservoir"  
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
  "tag": {  
    "type": "Property",  
    "value": "DMA1"  
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
