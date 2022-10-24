<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: Modello  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.WaterDistributionManagementEPANET/blob/master/Pattern/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Questa entità contiene una descrizione armonizzata di un modello generico realizzato per il dominio della gestione delle reti idriche. Questa entità è principalmente associata al verticale della gestione dell'acqua e alle relative applicazioni IoT.**  
versione: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `alternateName[string]`: Un nome alternativo per questa voce  - `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated[string]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateModified[string]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `description[string]`: Descrizione dell'articolo  - `id[*]`: Identificatore univoco dell'entità  - `multipliers[array]`: I moltiplicatori definiscono il modo in cui una quantità di base (ad esempio, la domanda) viene aggiustata per ogni periodo di tempo.  - `name[string]`: Il nome di questo elemento.  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `startTime[string]`: L'ora di inizio del modello  . Model: [https://schema.org/Time](https://schema.org/Time)- `tag[string]`: Una stringa di testo opzionale utilizzata per assegnare il tubo a una categoria, magari basata sull'età o sul materiale.  . Model: [https://schema.org/Text](https://schema.org/Text)- `timeStep[number]`: Il passo temporale utilizzato per i moltiplicatori. Tutte le unità sono accettate in codice [CEFACT](https://www.unece.org/cefact.html).  - `type[string]`: Tipo di entità NGSI-LD. Deve essere un modello  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `id`  - `multipliers`  - `startTime`  - `timeStep`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
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
  x-model-tags: FIWARE4WATER    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### Pattern NGSI-v2 valori-chiave Esempio  
Ecco un esempio di Pattern in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### Modello NGSI-v2 normalizzato Esempio  
Ecco un esempio di Pattern in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si usano le opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### Schema Valori chiave NGSI-LD Esempio  
Ecco un esempio di Pattern in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
    "type": "Pattern",  
    "createdAt": "2020-02-20T17:43:00Z",  
    "description": "Open Text",  
    "modifiedAt": "2020-02-20T17:43:00Z",  
    "multipliers": [  
        0.5692,  
        0.4647,  
        0.4385,  
        0.3604,  
        0.3098,  
        0.3345  
    ],  
    "startTime": "2020-02-20T17:43:00Z",  
    "tag": "DMA1",  
    "timeStep": 3600,  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.WaterDistributionManagementEPANET/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### Modello NGSI-LD normalizzato Esempio  
Ecco un esempio di Pattern in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si usano le opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
    "type": "Pattern",  
    "createdAt": "2020-02-20T17:43:00Z",  
    "description": {  
        "type": "Property",  
        "value": "Open Text"  
    },  
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
    "startTime": {  
        "type": "Property",  
        "value": "00:00"  
    },  
    "tag": {  
        "type": "Property",  
        "value": "DMA1"  
    },  
    "timeStep": {  
        "type": "Property",  
        "value": 3600,  
        "unitCode": "SEC"  
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
