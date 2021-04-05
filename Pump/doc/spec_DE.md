Entität: Pumpe  
==============  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.WaterDistributionManagementEPANET/blob/master/Pump/LICENSE.md)  
Globale Beschreibung: **Diese Entität enthält eine harmonisierte Beschreibung einer generischen Pumpe, die für die Domäne Wassernetzmanagement hergestellt wurde. Diese Entität ist in erster Linie mit der vertikalen Wasserwirtschaft und damit verbundenen IoT-Anwendungen verbunden.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `efficCurve`: Die ID-Kennzeichnung der Kurve, die den Wirkungsgrad der Pumpe in Abhängigkeit von der Durchflussrate darstellt.  - `endsAt`: Die ID des Knotens auf der Druckseite der Pumpe  - `energyPattern`: Die ID-Kennzeichnung des Zeitmusters, das verwendet wird, um die Variation des Energiepreises im Laufe des Tages zu beschreiben.  - `energyPrice`: Der durchschnittliche oder nominale Preis von Energie in Geldeinheiten. Alle Einheiten werden im [CEFACT](https://www.unece.org/cefact.html)-Code akzeptiert.  - `energyUse`: Beobachtete Energienutzung durch das Element des Netzwerks  - `flow`: Durchflussrate vom `startsAt`-Knoten zum `endsAt`-Knoten, gemessen von einem Gerät an der Verbindung (Rohr, Ventil oder Pumpe)  - `headCurve`: Die ID-Kennzeichnung der Pumpenkurve, die verwendet wird, um das Verhältnis zwischen der von der Pumpe gelieferten Förderhöhe und dem Durchfluss durch die Pumpe zu beschreiben.  - `id`: Eindeutiger Bezeichner der Entität  - `initialStatus`: Der Link-Status beim Start der Simulation. Enum:'OPEN, CLOSED, CV'  - `location`:   - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `power`: Die von der Pumpe gelieferte Leistung. Alle Einheiten werden im Code [CEFACT](https://www.unece.org/cefact.html) akzeptiert.  - `pumpPattern`: Die ID-Kennzeichnung eines Zeitmusters, das zur Steuerung des Pumpenbetriebs verwendet wird. Die Multiplikatoren des Musters entsprechen den Geschwindigkeitseinstellungen. Ein Multiplikator von Null bedeutet, dass die Pumpe während des entsprechenden Zeitraums abgeschaltet wird  - `quality`: Beobachtete Qualität in der Netzwerkkomponente  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `speed`: Die relative Geschwindigkeitseinstellung der Pumpe. Alle Einheiten werden im Code [CEFACT](https://www.unece.org/cefact.html) akzeptiert.  - `startsAt`: Die ID des Knotens auf der Saugseite der Pumpe  - `status`: Der dynamische Zustand des Knotens. Enum:'OPEN, CLOSED, CV'  - `tag`: Eine optionale Textzeichenkette, die dazu dient, das Rohr einer Kategorie zuzuordnen, z. B. basierend auf Alter oder Material  - `type`: NGSI-LD Entity Type. Er muss gleich "Pump" sein.  - `velocity`: Beobachtete Geschwindigkeit in der Verbindung (Rohr, Ventil oder Pumpe)  - `vertices`: Koordinaten aller Scheitelpunkte in der Pumpe, geordnet vom startsAt-Knoten zum endsAt-Knoten und kodiert als GeoJSON    
Erforderliche Eigenschaften  
- `endsAt`  - `id`  - `initialStatus`  - `startsAt`  - `type`  ## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Pump:    
  description: 'This entity contains a harmonised description of a generic pump made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.'    
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
    efficCurve:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'The ID label of the curve that represents the pump''s wire-to-water efficiency as a function of flow rate.'    
      type: Relationship    
    endsAt:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'The ID of the node on the discharge side of the pump'    
      type: Relationship    
    energyPattern:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'The ID label of the time pattern used to describe the variation in energy price throughout the day.'    
      type: Relationship    
    energyPrice:    
      description: 'The average or nominal price of energy in monetary units. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        units: 'No unit'    
    energyUse:    
      description: 'Observed energy use by the element of the network'    
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
    headCurve:    
      description: 'The ID label of the pump curve used to describe the relationship between the head delivered by the pump and the flow through the Pump.'    
      format: uri    
      type: Relationship    
    id:    
      anyOf: &pump_-_properties_-_owner_-_items_-_anyof    
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
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *pump_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    power:    
      description: 'The power supplied by the pump. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: KiloWatt    
    pumpPattern:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'The ID label of a time pattern used to control the pump''s operation. The multipliers of the pattern are equivalent to speed settings. A multiplier of zero implies that the pump will be shut off during the corresponding time period'    
      type: Relationship    
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
    speed:    
      description: 'The relative speed setting of the Pump. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'Metre per Second'    
    startsAt:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'The ID of the node on the suction side of the pump'    
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
      description: 'NGSI-LD Entity Type. It must be equal to Pump.'    
      enum:    
        - Pump    
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
## Beispiel-Nutzlasten  
#### Pumpe NGSI-v2-Schlüsselwerte Beispiel  
Hier ist ein Beispiel für eine Pumpe im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und gibt die Kontextdaten einer einzelnen Entität zurück.  
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
#### Pumpe NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für eine Pumpe im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und gibt die Kontextdaten einer einzelnen Entität zurück.  
```json  
{  
  "id": "85zhnf58-0d4c-h4g854g-b7d0-3310klm",  
  "type": "Pump",  
  "initialStatus": {  
    "type": "text",  
    "value": "OPEN"  
  },  
  "status": {  
    "type": "text",  
    "value": "OPEN"  
  },  
  "power": {  
    "type": "number",  
    "value": 100  
  },  
  "speed": {  
    "type": "number",  
    "value": 1.2  
  },  
  "startsAt": {  
    "type": "object",  
    "value": "63fe7d79-0d4c-4da9-b7d0-3340efa0656a"  
  },  
  "endsAt": {  
    "type": "object",  
    "value": "1863179e-3768-4480-9167-ff21f870dd19"  
  },  
  "tag": {  
    "type": "text",  
    "value": "DMA1"  
  },  
  "pumpPattern": {  
    "type": "Relationship",  
    "object": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
  },  
  "efficCurve": {  
    "type": "Relationship",  
    "object": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
  },  
  "energyPrice": {  
    "type": "number",  
    "value": 0.8  
  },  
  "energyPattern": {  
    "type": "Relationship",  
    "object": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
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
  },  
  "energyUse": {  
    "type": "object",  
    "value": {  
      "value": 50,  
      "observedBy": "device-9845A"  
    }  
  }  
}  
```  
#### Pumpe NGSI-LD-Schlüsselwerte Beispiel  
Hier ist ein Beispiel für eine Pumpe im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und gibt die Kontextdaten einer einzelnen Entität zurück.  
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
#### Pumpe NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine Pumpe im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und gibt die Kontextdaten einer einzelnen Entität zurück.  
```json  
{  
  "id": "urn:ngsi-ld:Pump:85zhnf58-0d4c-h4g854g-b7d0-3310klm",  
  "type": "Pump",  
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
  "tag": {  
    "type": "Property",  
    "value": "DMA1"  
  },  
  "pumpPattern": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
  },  
  "efficCurve": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Curve:fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
  },  
  "energyPrice": {  
    "type": "Property",  
    "value": 0.8,  
    "unitCode": "C62"  
  },  
  "energyPattern": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
  },  
  "flow": {  
    "type": "Property",  
    "value": {  
      "value": 20,  
      "unitCode": "G51"  
    },  
    "observedBy": {  
      "value": "urn:ngsi-ld:Device:device-9845A",  
      "type": "Relationship"  
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
      "value": "urn:ngsi-ld:Device:device-9845A"  
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
  "energyUse": {  
    "type": "Property",  
    "value": {  
      "type": "Property",  
      "value": 50,  
      "unitCode": "KWT"  
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
