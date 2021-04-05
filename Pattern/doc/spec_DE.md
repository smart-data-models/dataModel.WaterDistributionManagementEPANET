Entität: Muster  
===============  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.WaterDistributionManagementEPANET/blob/master/Pattern/LICENSE.md)  
Globale Beschreibung: **Diese Entität enthält eine harmonisierte Beschreibung eines generischen Musters, das für die Domäne Wassernetzmanagement erstellt wurde. Diese Entität ist in erster Linie mit der vertikalen Wasserwirtschaft und damit verbundenen IoT-Anwendungen verbunden.**  

## Liste der Eigenschaften  

- `alternateName`: Ein alternativer Name für diesen Artikel  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `id`: Eindeutiger Bezeichner der Entität  - `multipliers`: Multiplikatoren definieren, wie eine bestimmte Basismenge (z. B. die Nachfrage) für jede Zeitperiode angepasst wird  - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `startTime`: Die Zeit, zu der das Muster beginnt  - `tag`: Eine optionale Textzeichenkette, die dazu dient, das Rohr einer Kategorie zuzuordnen, z. B. basierend auf Alter oder Material  - `timeStep`: Der Zeitschritt, der für die Multiplikatoren verwendet wird. Alle Einheiten werden im Code [CEFACT](https://www.unece.org/cefact.html) akzeptiert.  - `type`: NGSI-LD Entity Type. Es muss Pattern sein    
Erforderliche Eigenschaften  
- `id`  - `multipliers`  - `startTime`  - `timeStep`  - `type`  ## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Pattern:    
  description: 'This entity contains a harmonised description of a generic pattern made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
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
    id:    
      anyOf: &pattern_-_properties_-_owner_-_items_-_anyof    
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
    multipliers:    
      description: 'Multipliers define how some base quantity (e.g., demand) is adjusted for each time period'    
      items:    
        type: number    
      type: Property    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *pattern_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
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
    startTime:    
      description: 'The time at which the pattern starts'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Time    
    tag:    
      description: 'An optional text string used to assign the pipe to a category, perhaps one based on age or material'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    timeStep:    
      description: 'The time step used for the multipliers. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        units: Second    
    type:    
      description: 'NGSI-LD Entity Type. It has to be Pattern'    
      enum:    
        - Pattern    
      type: Property    
  required:    
    - id    
    - type    
    - multipliers    
    - timeStep    
    - startTime    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
#### Pattern NGSI-v2 Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein Pattern im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
  "type": "Pattern",  
  "multipliers": [  
    0.5692,  
    0.4647,  
    0.4385,  
    0.3604,  
    0.3098,  
    0.3345  
  ],  
  "timeStep": 3600,  
  "description": "Open Text",  
  "tag": "DMA1",  
  "startTime": "2020-02-20T17:43:00Z"  
}  
```  
#### Pattern NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein Pattern im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
    "id": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
    "type": "Pattern",  
    "multipliers": {  
        "value": [  
            0.5692,  
            0.4647,  
            0.4385,  
            0.3604,  
            0.3098,  
            0.3345  
        ]  
    },  
    "timeStep": {  
        "value": 3600  
    },  
    "description": {  
        "value": "Open Text"  
    },  
    "tag": {  
        "value": "DMA1"  
    }  
}  
```  
#### Muster NGSI-LD-Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein Pattern im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ],  
  "createdAt": "2020-02-20T17:43:00Z",  
  "description": "Open Text",  
  "id": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
  "modifiedAt": "2020-02-20T17:43:00Z",  
  "multipliers": [  
    0.5692,  
    0.4647,  
    0.4385,  
    0.3604,  
    0.3098,  
    0.3345  
  ],  
  "tag": "DMA1",  
  "timeStep": 3600,  
  "startTime": "2020-02-20T17:43:00Z",  
  "type": "Pattern"  
}  
```  
#### Muster NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein Pattern im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
  "type": "Pattern",  
  "createdAt": "2020-02-20T17:43:00Z",  
  "modifiedAt": "2020-02-20T17:43:00Z",  
  "multipliers": {  
    "type": "Property",  
    "value": [  
      0.5692,  
      0.4647,  
      0.4385,  
      0.3604,  
      0.3098,  
      0.3345  
    ],  
    "unitCode": "C62"  
  },  
  "timeStep": {  
    "type": "Property",  
    "value": 3600,  
    "unitCode": "SEC"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Open Text"  
  },  
  "startTime": {  
    "type": "Property",  
    "value": "00:00"  
  },  
  "tag": {  
    "type": "Property",  
    "value": "DMA1"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
