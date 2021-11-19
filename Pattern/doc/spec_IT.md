Entità: Modello  
===============  
[Licenza aperta](https://github.com/smart-data-models//dataModel.WaterDistributionManagementEPANET/blob/master/Pattern/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Questa entità contiene una descrizione armonizzata di un modello generico fatto per il dominio di gestione della rete idrica. Questa entità è principalmente associata alla gestione verticale dell'acqua e alle relative applicazioni IoT.  

## Elenco delle proprietà  

- `alternateName`: Un nome alternativo per questa voce  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `description`: Una descrizione di questo articolo  - `id`: Identificatore unico dell'entità  - `multipliers`: I moltiplicatori definiscono come una certa quantità di base (per esempio, la domanda) viene aggiustata per ogni periodo di tempo  - `name`: Il nome di questo articolo.  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio completamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `startTime`: Il tempo in cui il modello inizia  - `tag`: Una stringa di testo opzionale usata per assegnare il tubo a una categoria, forse una basata sull'età o sul materiale  - `timeStep`: Il passo temporale utilizzato per i moltiplicatori. Tutte le unità sono accettate in codice [CEFACT](https://www.unece.org/cefact.html).  - `type`: Tipo di entità NGSI-LD. Deve essere Pattern    
Proprietà richieste  
- `id`  - `multipliers`  - `startTime`  - `timeStep`  - `type`  ## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Pattern:    
  description: 'This entity contains a harmonised description of a generic pattern made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
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
      x-ngsi:    
        type: Property    
    multipliers:    
      description: 'Multipliers define how some base quantity (e.g., demand) is adjusted for each time period'    
      items:    
        type: number    
      type: array    
      x-ngsi:    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *pattern_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    startTime:    
      description: 'The time at which the pattern starts'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Time    
        type: Property    
    tag:    
      description: 'An optional text string used to assign the pipe to a category, perhaps one based on age or material'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    timeStep:    
      description: 'The time step used for the multipliers. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: number    
      x-ngsi:    
        type: Property    
        units: Second    
    type:    
      description: 'NGSI-LD Entity Type. It has to be Pattern'    
      enum:    
        - Pattern    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - multipliers    
    - timeStep    
    - startTime    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.WaterDistributionManagementEPANET/blob/master/Pattern/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.WaterDistributionManagementEPANET/Pattern/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## Esempio di payloads  
#### Schema valori chiave NGSI-v2 Esempio  
Ecco un esempio di uno schema in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### Modello NGSI-v2 normalizzato Esempio  
Ecco un esempio di uno schema in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
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
#### Schema valori chiave NGSI-LD Esempio  
Ecco un esempio di uno schema in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### Modello NGSI-LD normalizzato Esempio  
Ecco un esempio di uno schema in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
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
