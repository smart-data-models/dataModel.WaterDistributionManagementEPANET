エンティティパイプ  
=========  
[オープンライセンス](https://github.com/smart-data-models//dataModel.WaterDistributionManagementEPANET/blob/master/Pipe/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述。**このエンティティは、Water Network Managementドメインのために作られた一般的なパイプの調和された記述を含む。このエンティティは、主に水管理の垂直方向と関連するIoTアプリケーションに関連付けられています。  

## プロパティのリスト  

- `address`: 郵送先住所  - `alternateName`: このアイテムの別称  - `areaServed`: サービスや提供されるアイテムが提供される地理的なエリア  - `bulkCoeff`: 成長には正の値を、減衰には負の値を使用してください。すべての単位は[CEFACT](https://www.unece.org/cefact.html)コードで受け付けています。  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `description`: このアイテムの説明  - `diameter`: パイプの直径  - `endsAt`: パイプが終了するノードのID  - `flow`: リンク先のデバイス（パイプ、バルブ、ポンプ）によって測定された、`startsAt`ノードから`endsAt`ノードへの流れの速度  - `id`: エンティティのユニークな識別子  - `initialStatus`: シミュレーション開始時のリンクの状態。Enum:'OPEN, CLOSED, CV'  - `length`: パイプの実際の長さです。すべての単位は[CEFACT](https://www.unece.org/cefact.html)コードで受け付けます。  - `location`: アイテムへのGeojson参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygonのいずれかです。  - `minorLoss`: ベンド、フィッティングなどに伴う単位のないマイナーロス係数  - `name`: このアイテムの名前です。  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `quality`: ネットワークコンポーネントの品質を確認  - `roughness`: パイプの粗さ係数です。  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `startsAt`: パイプの始点となるノードのID  - `status`: ノードの動的な状態。列挙:'OPEN, CLOSED, CV'  - `tag`: パイプをカテゴリー別に分類するための任意のテキスト文字列です。  - `type`: NGSI-LD エンティティタイプ。パイプでなければならない  - `velocity`: リンク（パイプ、バルブ、ポンプ）で観測された速度  - `vertices`: パイプ内のすべての頂点の座標を、startsAtノードからendsAtノードまで順番に並べ、GeoJSONでエンコードしたもの。  - `wallCoeff`: パイプの壁反応係数です。成長には正の値を、崩壊には負の値を使用する。単位はすべて[CEFACT](https://www.unece.org/cefact.html)コードで受け付けます。    
必須項目  
- `id`  - `type`  ## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます）  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Pipe:    
  description: 'This entity contains a harmonised description of a generic pipe made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.'    
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
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    bulkCoeff:    
      description: 'Use a positive value for growth and a negative value for decay. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'reciprocal day The bulk reaction coefficient for the pipe'    
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
    diameter:    
      description: 'The pipe diameter'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Millimetre    
    endsAt:    
      description: 'The ID of the node where the pipe ends'    
      format: uri    
      type: string    
      x-ngsi:    
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
      type: object    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &pipe_-_properties_-_owner_-_items_-_anyof    
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
    length:    
      description: 'The actual length of the pipe. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Metre    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
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
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
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
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
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
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiPolygon'    
          type: object    
      x-ngsi:    
        type: Geoproperty    
    minorLoss:    
      description: 'Unitless minor loss coefficient associated with bends, fittings, etc'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'No unit'    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *pipe_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
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
      type: object    
      x-ngsi:    
        type: Property    
    roughness:    
      description: 'The roughness coefficient of the Pipe.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'No unit'    
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
    startsAt:    
      description: 'The ID of the node where the pipe begins'    
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
      description: 'NGSI-LD Entity Type. It has to be Pipe'    
      enum:    
        - Pipe    
      type: string    
      x-ngsi:    
        type: Property    
    velocity:    
      description: 'Observed velocity in the link (pipe, valve or pump)'    
      properties:    
        observedBy:    
          format: uri    
          type: string    
        value:    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    vertices:    
      description: 'Coordinates of all vertices in the pipe, ordered from the startsAt node to the endsAt node and encoded as a GeoJSON '    
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
      x-ngsi:    
        type: Geoproperty    
    wallCoeff:    
      description: 'The wall reaction coefficient for the pipe. Use a positive value for growth and a negative value for decay. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: mg/m²/day    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.WaterDistributionManagementEPANET/blob/master/Pipe/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.WaterDistributionManagementEPANET/Pipe/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## ペイロードの例  
#### パイプNGSI-v2のキーバリューの例  
ここでは、Pipeをkey-valuesとしてJSON-LD形式にした例を紹介します。これは`options=keyValues`を使った場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
    "id": "74azsty-70d4l-4da9-b7d0-3340ef655nnb",  
    "type": "Pipe",  
    "initialStatus": "OPEN",  
    "status": "OPEN",  
    "length": 52.90,  
    "diameter": 203.00,  
    "roughness": 72.4549,  
    "minorLoss": 72.4549,  
    "tag": "DMA1",  
    "description": "Free Text",  
    "startsAt": "ngsi:63fe7d79-0d4c-4da9-b7d0-3340efa0656a",  
    "endsAt": "ngsi:1863179e-3768-4480-9167-ff21f870dd19",  
    "bulkCoeff": 72.4549,  
    "wallCoeff": 72.4549  
}  
```  
#### パイプNGSI-v2規格化例  
ここでは、JSON-LD形式のPipeを正規化した例を示します。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "74azsty-70d4l-4da9-b7d0-3340ef655nnb",  
  "type": "Pipe",  
  "initialStatus": {  
    "type": "text",  
    "value": "OPEN"  
  },  
  "status": {  
    "type": "text",  
    "value": "OPEN"  
  },  
  "length": {  
    "type": "number",  
    "value": 52.90  
  },  
  "diameter": {  
    "type": "number",  
    "value": 203.00  
  },  
  "roughness": {  
    "type": "number",  
    "value": 72.4549  
  },  
  "minorLoss": {  
    "type": "number",  
    "value": 72.4549  
  },  
  "tag": {  
    "type": "text",  
    "value": "DMA1"  
  },  
  "description": {  
    "type": "text",  
    "value": "Free Text"  
  },  
  "startsAt": {  
    "type": "object",  
    "value": "63fe7d79-0d4c-4da9-b7d0-3340efa0656a"  
  },  
  "endsAt": {  
    "type": "object",  
    "value": "1863179e-3768-4480-9167-ff21f870dd19"  
  },  
  "bulkCoeff": {  
    "type": "number",  
    "value": 72.4549  
  },  
  "wallCoeff": {  
    "type": "number",  
    "value": 72.4549  
  },  
  "flow": {  
    "type": "structuredValue",  
    "value": {  
      "value": 20,  
      "observedBy": "device-9845A"  
    }  
  },  
  "velocity": {  
    "type": "structuredValue",  
    "value": {  
      "value": 2,  
      "observedBy": "device-9845A"  
    }  
  },  
  "quality": {  
    "type": "structuredValue",  
    "value": {  
      "value": 0.5,  
      "observedBy": "device-9845A"  
    }  
  }  
}  
```  
#### パイプNGSI-LDのキーバリューの例  
ここでは、Pipeをkey-valuesとしてJSON-LD形式にした例を紹介します。これは、`options=keyValues`を使った場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ],  
  "bulkCoeff": 72.4549,  
  "createdAt": "2020-02-20T15:42:00Z",  
  "description": "Free Text",  
  "diameter": 203.0,  
  "endsAt": "urn:ngsi-ld:Reservoir:1863179e-3768-4480-9167-ff21f870dd19",  
  "id": "urn:ngsi-ld:Pipe:74azsty-70d4l-4da9-b7d0-3340ef655nnb",  
  "initialStatus": "OPEN",  
  "length": 52.9,  
  "minorLoss": 72.4549,  
  "modifiedAt": "2020-02-20T15:45:00Z",  
  "roughness": 72.4549,  
  "startsAt": "urn:ngsi-ld:Junction:63fe7d79-0d4c-4da9-b7d0-3340efa0656a",  
  "status": "OPEN",  
  "tag": "DMA1",  
  "type": "Pipe",  
  "wallCoeff": 72.4549  
}  
```  
#### パイプ NGSI-LD 正規化例  
ここでは、JSON-LD形式のPipeを正規化した例を示します。これは、オプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:Pipe:74azsty-70d4l-4da9-b7d0-3340ef655nnb",  
  "type": "Pipe",  
  "initialStatus": {  
    "type": "Property",  
    "value": "OPEN"  
  },  
  "status": {  
    "type": "Property",  
    "value": "OPEN"  
  },  
  "length": {  
    "type": "Property",  
    "value": 52.90,  
    "unitCode": "MTR"  
  },  
  "diameter": {  
    "type": "Property",  
    "value": 203.0,  
    "unitCode": "MMT"  
  },  
  "roughness": {  
    "type": "Property",  
    "value": 72.4549,  
    "unitCode": "C62"  
  },  
  "minorLoss": {  
    "type": "Property",  
    "value": 72.4549,  
    "unitCode": "C62"  
  },  
  "tag": {  
    "type": "Property",  
    "value": "DMA1"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Free Text"  
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
  "bulkCoeff": {  
    "type": "Property",  
    "value": 72.4549,  
    "unitCode": "E91"  
  },  
  "wallCoeff": {  
    "type": "Property",  
    "value": 72.4549,  
    "unitCode": "RRC"  
  },  
  "flow": {  
    "type": "Property",  
    "value": {  
      "type": "Property",  
      "value": 20,  
      "unitCode": "G51"  
    },  
    "observedBy": {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:Device:device-9845A"  
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
      "object": "urn:ngsi-ld:Device:device-9845A"  
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
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  

マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。
