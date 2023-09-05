<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: Valvola  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.WaterDistributionManagementEPANET/blob/master/Valve/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Questa entità contiene una descrizione armonizzata di una valvola generica realizzata per il dominio della gestione della rete idrica. Questa entità è principalmente associata al verticale della gestione dell'acqua e alle relative applicazioni IoT.**  
versione: 0.1.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestita dal governo locale.    
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `diameter[number]`: Il diametro della valvola. Tutte le unità sono accettate in codice [CEFACT](https://www.unece.org/cefact.html).  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `endsAt[uri]`: L'ID del nodo sul lato nominale a valle o di scarico della valvola.  - `flow[object]`: Velocità di flusso dal nodo `inizioAt` al nodo `termineAt`, misurata da un dispositivo sul collegamento (tubo, valvola o pompa)  	- `observedBy`:     
- `id[*]`: Identificatore univoco dell'entità  - `initialStatus[string]`: Stato del collegamento all'inizio della simulazione. Enum:'APERTO, CHIUSO, CV'  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `minorLoss[number]`: Coefficiente di perdita minore senza unità che si applica quando la valvola è completamente aperta. Tutte le unità sono accettate in codice [CEFACT](https://www.unece.org/cefact.html).  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: Il nome di questo elemento  - `openStatus[number]`: Stato di una valvola come valore numerico percentuale che rappresenta l'apertura o la chiusura della valvola. 0% - completamente chiusa, 100% - completamente aperta  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `quality[object]`: Qualità osservata nel componente di rete  	- `observedBy`:     
- `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `setting[number]`: Un parametro che descrive l'impostazione operativa della valvola. Tutte le unità sono accettate in codice [CEFACT](https://www.unece.org/cefact.html).  . Model: [https://schema.org/Number](https://schema.org/Number)- `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `startsAt[uri]`: L'ID del nodo sul lato nominale a monte o di afflusso della valvola.  - `status[string]`: Stato dinamico del nodo. Enum:'APERTO, CHIUSO, CV'  . Model: [https://schema.org/Text](https://schema.org/Text)- `tag[string]`: Una stringa di testo opzionale utilizzata per assegnare il tubo a una categoria, magari basata sull'età o sul materiale.  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: Tipo di entità NGSI-LD. Deve essere uguale a Valve  - `valveCurve[uri]`: Una relazione con la curva della proprietà di regolazione. Richiesto solo quando valveType è GPV  - `valveType[string]`: Tipo di valvola dell'elemento enum:'FCV, GPV, PBV, PRV, PSV, TCV'.  . Model: [https://schema.org/Text](https://schema.org/Text)- `velocity[object]`: Velocità osservata nel collegamento (tubo, valvola o pompa)  	- `observedBy[uri]`: Dove è stata osservata la velocità    
- `vertices[*]`: Geoproprietà. Coordinate di tutti i vertici della valvola, ordinate dal nodo startsAt al nodo endsAt e codificate come GeoJSON.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `endsAt`  - `id`  - `startsAt`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
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
## Esempi di payload  
#### Valvola NGSI-v2 valori-chiave Esempio  
Ecco un esempio di Valve in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "87fe7d79-0d4c-4da9-b7d0-3340efa0656awytsd",  
    "type": "Valve",  
    "initialStatus": "OPEN",  
    "openStatus": 0.3,  
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
</details>  
#### Valvola NGSI-v2 normalizzata Esempio  
Ecco un esempio di Valve in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si usano le opzioni e restituisce i dati di contesto di una singola entità.  
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
</details>  
#### Valvola NGSI-LD valori-chiave Esempio  
Ecco un esempio di Valve in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### Valvola NGSI-LD normalizzata Esempio  
Ecco un esempio di Valve in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si usano le opzioni e restituisce i dati di contesto di una singola entità.  
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
