[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティポンプ  
=========  
[オープンライセンス](https://github.com/smart-data-models//dataModel.WaterDistributionManagementEPANET/blob/master/Pump/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述。**このエンティティは、水ネットワーク管理領域のために作られた汎用ポンプの調和された記述を含む。このエンティティは、主に水管理の垂直方向と関連する IoT アプリケーションに関連するものである**。  
バージョン: 0.0.1  

## プロパティ一覧  

- `address`: 郵送先住所  - `alternateName`: この項目の別称  - `areaServed`: サービスまたは提供品が提供される地理的な地域  - `dataProvider`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description`: このアイテムの説明  - `efficCurve`: ポンプの電線対水効率を流量の関数として表した曲線のIDラベルです。  - `endsAt`: ポンプ吐出側のノードのID  - `energyPattern`: 一日のエネルギー価格の変動を表現するために使用されるタイムパターンのIDラベル。  - `energyPrice`: エネルギーの平均価格または名目価格を貨幣単位で表したもの。すべての単位は[CEFACT](https://www.unece.org/cefact.html)コードで受け付けています。  - `energyUse`: ネットワークの要素によるエネルギー使用量の観測値  - `flow`: リンク先の装置（パイプ、バルブ、ポンプ）で測定された、`startAt`ノードから`endsAt`ノードへの流速  - `headCurve`: ポンプが送り出す揚程とポンプを通過する流量の関係を説明するために使用されるポンプ曲線のIDラベルです。  - `id`: エンティティの一意な識別子  - `initialStatus`: シミュレーション開始時のリンク状態。Enum:'OPEN, CLOSED, CV' です。  - `location`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `name`: このアイテムの名称です。  - `owner`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリストです。  - `power`: ポンプから供給される電力。単位はすべて[CEFACT](https://www.unece.org/cefact.html)コードで受け付けます。  - `pumpPattern`: ポンプの運転制御に使用するタイムパターンのIDラベルです。パターンの倍率は、速度設定に相当する。倍率が0の場合、該当する時間帯はポンプが停止することを意味する。  - `quality`: ネットワークコンポーネントで観測された品質  - `seeAlso`: 項目に関する追加リソースを指すURIのリスト。  - `source`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `speed`: ポンプの相対速度設定。単位はすべて[CEFACT](https://www.unece.org/cefact.html)コードで受け付けます。  - `startsAt`: ポンプ吸込側のノードのID  - `status`: ノードの動的状態。Enum:'OPEN, CLOSED, CV'.  - `tag`: パイプをカテゴリに割り当てるためのオプションのテキスト文字列、おそらく年齢や素材に基づいたもの  - `type`: NGSI-LD Entity Type。Pump と等しくなければならない。  - `velocity`: リンク（パイプ、バルブ、ポンプ）内の観測された流速  - `vertices`: ポンプ内のすべての頂点の座標を、startsAtノードからendsAtノードに並べて、GeoJSONとしてエンコードしたもの。    
必要なプロパティ  
- `endsAt`  - `id`  - `initialStatus`  - `startsAt`  - `type`  ## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
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
      x-ngsi:    
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
      x-ngsi:    
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
      x-ngsi:    
        type: Relationship    
    energyPrice:    
      description: 'The average or nominal price of energy in monetary units. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: number    
      x-ngsi:    
        type: Property    
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
      type: object    
      x-ngsi:    
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
      type: object    
      x-ngsi:    
        type: Property    
    headCurve:    
      description: 'The ID label of the pump curve used to describe the relationship between the head delivered by the pump and the flow through the Pump.'    
      format: uri    
      type: string    
      x-ngsi:    
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
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *pump_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    power:    
      description: 'The power supplied by the pump. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
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
      x-ngsi:    
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
      type: object    
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
    speed:    
      description: 'The relative speed setting of the Pump. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
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
      description: 'NGSI-LD Entity Type. It must be equal to Pump.'    
      enum:    
        - Pump    
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
      x-ngsi:    
        type: Geoproperty    
  required:    
    - id    
    - type    
    - initialStatus    
    - startsAt    
    - endsAt    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.WaterDistributionManagementEPANET/blob/master/Pump/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.WaterDistributionManagementEPANET/Pump/schema.json    
  x-model-tags: FIWARE4WATER    
  x-version: 0.0.1    
```  
</details>    
## ペイロードの例  
#### ポンプNGSI-v2鍵盤の例  
ここでは、PumpをJSON-LD形式でkey-valuesとした場合の例を示す。これは `options=keyValues` を使用した場合に NGSI-v2 と互換性があり、個々のエンティティのコンテキストデータが返される。  
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
#### ポンプ NGSI-v2 正規化例  
以下は、PumpをJSON-LD形式で正規化した例である。これはオプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### ポンプ NGSI-LD キー値例  
ここでは、PumpをJSON-LD形式でkey-valuesにした例を示します。これは `options=keyValues` を使用した場合に NGSI-LD と互換性があり、個々のエンティティのコンテキストデータが返される。  
```json  
{  
    "id": "urn:ngsi-ld:Pump:85zhnf58-0d4c-h4g854g-b7d0-3310klm",  
    "type": "Pump",  
    "createdAt": "2020-03-02T15:42:00Z",  
    "efficCurve": "urn:ngsi-ld:Curve:fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
    "endsAt": "urn:ngsi-ld:Reservoir:1863179e-3768-4480-9167-ff21f870dd19",  
    "energyPattern": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
    "energyPrice": 0.8,  
    "initialStatus": "OPEN",  
    "modifiedAt": "2020-03-02T15:45:00Z",  
    "power": 100,  
    "pumpPattern": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533-a2eb-34bc89262190",  
    "speed": 1.2,  
    "startsAt": "urn:ngsi-ld:Junction:63fe7d79-0d4c-4da9-b7d0-3340efa0656a",  
    "status": "OPEN",  
    "tag": "DMA1",  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/data-models/master/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.WaterDistributionManagementEPANET/master/context.jsonld"  
    ]  
}  
```  
#### ポンプ NGSI-LD 正規化例  
以下は、PumpをJSON-LD形式で正規化した例である。これはオプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
    "id": "urn:ngsi-ld:Pump:85zhnf58-0d4c-h4g854g-b7d0-3310klm",  
    "type": "Pump",  
    "efficCurve": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Curve:fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
    },  
    "endsAt": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Reservoir:1863179e-3768-4480-9167-ff21f870dd19"  
    },  
    "energyPattern": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
    },  
    "energyPrice": {  
        "type": "Property",  
        "value": 0.8,  
        "unitCode": "C62"  
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
    "initialStatus": {  
        "type": "Property",  
        "value": "OPEN"  
    },  
    "power": {  
        "type": "Property",  
        "value": 100,  
        "unitCode": "KWT"  
    },  
    "pumpPattern": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
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
    "speed": {  
        "type": "Property",  
        "value": 1.2,  
        "unitCode": "MTS"  
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
    "@context": []  
}  
```  
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
