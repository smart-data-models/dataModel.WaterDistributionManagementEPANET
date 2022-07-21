[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティSimulationScenario  
========================  
[オープンライセンス](https://github.com/smart-data-models//dataModel.WaterDistributionManagementEPANET/blob/master/SimulationScenario/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述。**このエンティティは、水域ネットワーク管理領域のために作られた汎用シミュレーションシナリオの調和された記述を含んでいます。このエンティティは、主に水ネットワーク管理の垂直方向と関連するIoTアプリケーションに関連しています。  
バージョン: 0.0.1  

## プロパティ一覧  

- `accuracy`: 水力学的な解決に到達したことを判断するための、総正規化流量変化収束基準。  - `address`: 郵送先住所  - `alternateName`: この項目の別称  - `areaServed`: サービスまたは提供品が提供される地理的な地域  - `bulkOrder`: 配管のバルク水反応順序  - `checkFrequency`: 油圧の状態チェックの頻度  - `chemicalName`: モデル化された化学物質の名前。qualityType'がCHEMの場合のみ使用されます。  - `chemicalUnits`: モデル化された化学物質の単位。qualityType'がCHEMの場合のみ使用されます。  - `concentrationLimit`: 成長反応の限界濃度  - `createdBy`: シミュレーションを作成/起動した人のID。User' タイプのエンティティへの参照。  - `dampLimit`: PRVおよびPSVのソリューションダンピングとステータスチェックが開始される精度値。  - `dataProvider`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `demandCharge`: 最大使用電力量（kW）あたりのエネルギー料金。  - `demandModel`: 解析が圧力駆動（PDA）か需要駆動（DDA）かを指定する。Enum:'DDA, PDA'  - `description`: このアイテムの説明  - `diffusivity`: 品質分析で分析される化学物質の分子拡散率で、水中の塩素の拡散率に対する相対値。  - `duration`: シミュレーションの継続時間（単位：秒  - `emitterExponent`: エミッタから演算するときに、接合部の圧力が上昇する力。  - `flowChange`: 水力学的な解決に到達したことを判断するための最大流量変化収束基準。  - `flowUnits`: シミュレーションで流量を表現する単位。CFS（立方フィート/秒）、GPM（ガロン/分）、MGD（百万ガロン/日）、IMGD（インペリアルMGD）、AFD（エーカーフィート/日）、LPS（リットル/秒）、LPM（リットル/分）、MLD（百万リットル/日）、CMH（立法メートル/時）およびCMD（立法メートル/日）が利用可能なオプションとして使用できます。Enum:'AFD, CFS, CMD, CMH, GPM, IMGD, LPS, LPM, MLD, MGD'.  - `hasInputNetwork`: シミュレーションに使用したネットワークのID  - `hasSimulationResult`: 関連するシミュレーション結果のIDです。SimulationResult' タイプのエンティティへの参照。  - `headError`: 水力学的な解決に到達したことを判断するための最大ヘッドロス収束基準。  - `headlossFormula`: 配管を流れる流量のヘッドロスを計算するための式。Hazen-Williams (H-W), Darcy-Weisbach (D-W) または Chezy-Manning (C-M) 式から選択します。許容される選択肢は、'H-W'、'D-W'、'C-M'である。Enum:'C-M, D-W, H-W'.  - `hydraulicTimeStep`: ネットワークの水力状態が計算される頻度を決定する。秒単位で指定  - `id`: エンティティの一意な識別子  - `inputParameter`: シミュレーションのためにネットワークに適用される一連の修正内容の説明  - `location`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `maxCheck`: ステータスチェックが終了するまでの試行回数  - `minimumPressure`: 圧力ダーベン分析で、これより低い圧力では需要が供給されない圧力。demandModelが'PDA'の場合のみ使用される。  - `name`: このアイテムの名称です。  - `operationalControl`: デアイテムの運用管理  - `owner`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリストです。  - `patternStart`: シミュレーションの開始時刻です。  - `patternStep`: シミュレーションのパターンステップ。  - `pressureExponent`: 圧力駆動解析のもとで配信される需要を計算する際に、圧力を上げる電力。demandModelが'PDA'の場合のみ使用される。  - `qualityTimeStep`: ネットワーク内の水質の変化を追跡するために使用されるタイムステップ。秒単位で指定  - `qualityType`: 水質分析の種類。Enum:'chem, age, trace, none'.  - `reportStart`: 結果を報告し始めるシミュレーション時間。シミュレーション開始からの秒数で指定  - `reportStep`: 出力結果を報告する間隔（秒）。  - `requiredPressure`: 圧力駆動解析でノードの全需要を供給するために必要な圧力。demandModelが'PDA'の場合のみ使用されます。  - `ruleTimeStep`: ルールベースの制御によるシステム状態の変化を確認するために使用される時間ステップ。秒単位で指定  - `seeAlso`: 項目に関する追加リソースを指すURIのリスト。  - `source`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `specificGravity`: モデル化された流体の密度と4℃の水の密度との比。C  - `startClockTime`: シミュレーションを開始する時刻。開始時刻からの秒数で指定  - `statistic`: 生成されたシミュレーション結果の時系列に対して行われる統計的な後処理の種類。オプションは、AVERAGED（時間平均した結果を報告）、MINIMUM（最小値のみを報告）、MAXIMUM（最大値のみを報告）、RANGE（最小値と最大値の差を報告）、NONE（全時間系列を報告）です。Enum:'averaged, minimum, maximum, range, none' （平均値、最小値、最大値、範囲、なし  - `tankOrder`: タンク用バルク水の反応順序  - `tolerance`: 水質許容度  - `traceNodeID`: 品質解析でトレースされるノードのURI。qualityType' が TRACE の場合は必須、それ以外の場合は不要。  - `trials`: シミュレーションの各水力学的時間ステップでネットワーク水理学を解くために使用される最大試行回数  - `type`: NGSI-LD Entity Type。SimulationScenarioでなければならない。  - `unbalanced`: 許容された試行回数内に水力学的解決に到達できなかった場合にどうするかを決定する。可能なオプションは STOP (解析停止)、CONTINUE (解析継続、ただし警告メッセージあり)、CONTINUE_N (さらに N 試行、ここで N の値は 'unbalancedN' で与えられる) である。Enum:'stop, continue, continue_N'.  - `unbalancedN`: unbalanced' が continue_N に設定されている場合に許可される追加試行回数。unbalanced' が continue_N に設定されている場合は必須、そうでない場合は不要。  - `viscosity`: 20℃における水の動粘度に対するモデル流体の動粘度。C  - `wallOrder`: パイプの壁面反応順序    
必要なプロパティ  
- `hasInputNetwork`  - `id`  - `type`  ## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
SimulationScenario:    
  description: 'This entity contains a harmonised description of a generic simulation scenario made for the Water Network Management domain. This entity is primarily associated with the water network management vertical and related IoT applications.'    
  properties:    
    accuracy:    
      description: 'Total normalized flow change convergence criterion for determining when a hydraulic solution has been reached.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
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
    bulkOrder:    
      description: 'Bulk water reaction order for pipes'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    checkFrequency:    
      description: 'Frequency of hydraulic status checks'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    chemicalName:    
      description: 'Name of the chemical modelled. Only used if ''qualityType'' is CHEM'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    chemicalUnits:    
      description: 'Units of the chemical modelled. Only used if ''qualityType'' is CHEM'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    concentrationLimit:    
      description: 'Limiting concentration for growth reactions'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    createdBy:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]'|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: 'The ID of who created/triggered the simulation. Reference to an entity of type ''User'''    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    dampLimit:    
      description: 'Accuracy value at which solution damping and status checks begin for PRVs and PSVs.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    demandCharge:    
      description: 'Energy charge per maximum kW usage.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    demandModel:    
      description: 'Specifies whether the analysis is pressure driven (PDA) or demand driven (DDA). Enum:''DDA, PDA'''    
      enum:    
        - DDA    
        - PDA    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    diffusivity:    
      description: 'Molecular diffusivity of the chemical analysed in a quality analysis, relative to diffusivity of chlorine in water.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    duration:    
      description: 'Duration of the simulation, given in seconds'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: seconds    
    emitterExponent:    
      description: 'Power to which pressure at a junction is raised when computing from an emitter.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    flowChange:    
      description: 'Maximum flow change convergence criterion for determining when a hydraulic solution has been reached.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    flowUnits:    
      description: 'Units in which flow rates are expressed in the simulation. Allowable options are CFS (cubic feet per second), GPM (gallons per minute), MGD (million gallons per day), IMGD (imperial MGD), AFD (acre-feet per day), LPS (litres pre second), LPM (litres per minute), MLD (million litres per day), CMH (cubic metres per hour) and CMD (cubic metres per day). Enum:''AFD, CFS, CMD, CMH, GPM, IMGD, LPS, LPM, MLD, MGD'''    
      enum:    
        - AFD    
        - CFS    
        - CMD    
        - CMH    
        - GPM    
        - IMGD    
        - LPS    
        - LPM    
        - MLD    
        - MGD    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    hasInputNetwork:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]'|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: 'The ID of the network used in the simulation'    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    hasSimulationResult:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]'|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: 'The ID of the related simulation result. Reference to an entity of type ''SimulationResult'''    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    headError:    
      description: 'Maximum headloss convergence criterion for determining when a hydraulic solution has been reached.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    headlossFormula:    
      description: 'Formula used for computing head loss for flow through a pipe. The choices are the Hazen-Williams (H-W), Darcy-Weisbach (D-W) or Chezy-Manning (C-M) formulas. Allowable options are ''H-W'', ''D-W'', ''C-M''. Enum:''C-M, D-W, H-W'''    
      enum:    
        - H-W    
        - D-W    
        - C-M    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    hydraulicTimeStep:    
      description: 'Determines how often the hydraulic state of the network is calculated. Given in seconds'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: seconds    
    id:    
      anyOf: &simulationscenario_-_properties_-_owner_-_items_-_anyof    
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
    inputParameter:    
      description: 'Description of the set of modifications to be applied to the network for the simulation'    
      items:    
        properties:    
          parameterName:    
            type: string    
          targetURI:    
            anyOf:    
              - maxLength: 256    
                minLength: 1    
                pattern: ^[\w\-\.\{\}\$\+\*\[\]'|~^@!,:\\]+$    
                type: string    
              - format: uri    
                type: string    
            description: 'Relationship. Model:''https://schema.org/URL''. URI of network component with property modified in simulation. A sub-relationship of the Property water attribute.'    
          value:    
            anyOf:    
              - type: string    
              - type: number    
              - type: boolean    
        type: object    
      type: array    
      x-ngsi:    
        model: https://Text    
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
    maxCheck:    
      description: 'Number of trials after which status checks are discontinued'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    minimumPressure:    
      description: 'Pressure below which no demand can be delivered under a pressure dirven analysis. Only used if demandModel is ''PDA'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    operationalControl:    
      description: 'The operational control of de item'    
      items:    
        properties:    
          controlType:    
            description: 'Property. Model:''https://schema.org/Text''. Type of trigger for the control. A sub-property of the Property ''control''. Enum:''HILEVEL, LOWLEVEL, TIMEOFDAY, TIMER'''    
            enum:    
              - HILEVEL    
              - LOWLEVEL    
              - TIMEOFDAY    
              - TIMER    
            type: string    
          controlledLink:    
            anyOf:    
              - maxLength: 256    
                minLength: 1    
                pattern: ^[\w\-\.\{\}\$\+\*\[\]'|~^@!,:\\]+$    
                type: string    
              - format: uri    
                type: string    
            description: 'Relationship. Model:''https://schema.org/URL''. Link controlled. A sub-relationship of the Property ''control''. Reference to an entity of type ''Pipe'', ''Pump'' or ''Valve'''    
          monitoredNode:    
            anyOf:    
              - maxLength: 256    
                minLength: 1    
                pattern: ^[\w\-\.\{\}\$\+\*\[\]'|~^@!,:\\]+$    
                type: string    
              - format: uri    
                type: string    
            description: 'Relationship. Model:''https://schema.org/URL''. Node which is monitored for control trigger level. A sub-relationship of the Property ''control''.  Reference to an entity of type ''Junction'', ''Tank'' or ''Reservoir'''    
          setting:    
            description: 'Property. Model:''https://schema.org/Number''. Setting applied in the to the controlled link when trigger level is reached. A sub-property of the Property ''control'''    
            type: number    
          triggerLevel:    
            description: 'Property. Model:''https://schema.org/Number''. Level at which control is activated. A sub-property of the Property ''control'''    
            type: number    
          type:    
            description: 'Property. Model:''https://schema.org/Text''. Description of a control applied to the network for the simulation. Enum:''controlledLink, controlType, monitoredNode, setting, triggerLevel'''    
            type: string    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *simulationscenario_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    patternStart:    
      description: 'Start time of the  the simulation.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    patternStep:    
      description: 'Pattern step of the simulation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    pressureExponent:    
      description: 'Power to which pressure is raised when calculating the demand delivered under a pressure driven analysis. Only used if demandModel is ''PDA'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    qualityTimeStep:    
      description: 'The timestep used to track changes in water quality in the network. Given in seconds'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: seconds    
    qualityType:    
      description: 'Type of water quality analysis. Enum:''chem, age, trace, none'''    
      enum:    
        - age    
        - chem    
        - none    
        - trace    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    reportStart:    
      description: 'Simulation time at which results start to be reported. Given in seconds from start of simulation'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: seconds    
    reportStep:    
      description: 'Interval at which output results are reported. given in seconds'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: seconds    
    requiredPressure:    
      description: 'Pressure required to supply a node''s full demand under a pressure driven analysis. Only used if demandModel is ''PDA'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ruleTimeStep:    
      description: 'Time step used to check for changes in system status due to rule-based controls. Given in seconds'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: seconds    
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
    specificGravity:    
      description: 'The ratio of the density of the fluid being modeled to that of water at 4 deg. C'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    startClockTime:    
      description: 'Time of day at which the simulation begins. Given as seconds from start of day'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: seconds    
    statistic:    
      description: 'The type of statistical post-processing that is done on the time series of simulation results generated. Options are AVERAGED (report time-averaged results), MINIMUM (report only minimum values), MAXIMUM (report only maximum values), RANGE (report difference between minimum and maximum values) and NONE (report full time series). Enum:''averaged, minimum, maximum, range, none'''    
      enum:    
        - averaged    
        - maximum    
        - minimum    
        - none    
        - range    
      type: string    
      x-ngsi:    
        model: https://schema.org/string    
        type: Property    
    tankOrder:    
      description: 'Bulk water reaction order for tanks'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    tolerance:    
      description: 'Water quality tolerance'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    traceNodeID:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]'|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: 'URI of node being traced in the quality analysis. Mandatory if ''qualityType'' is TRACE, otherwise not required'    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    trials:    
      description: 'The maximum number of trials used to solve network hydraulics at each hydraulic time step of a simulation'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI-LD Entity Type. It has to be SimulationScenario'    
      enum:    
        - SimulationScenario    
      type: string    
      x-ngsi:    
        type: Property    
    unbalanced:    
      description: 'Determines what happens if a hydraulic solution cannot be reached within the allowed number of trials. Allowable options are STOP (halt analysis), CONTINUE (continue analysis but with a warning message) and CONTINUE_N (continue for another N trials, where the value of N is given by ''unbalancedN''). Enum:''stop, continue, continue_N'''    
      enum:    
        - stop    
        - continue    
        - continue_N    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    unbalancedN:    
      description: 'Number of additional trials allowed if ''unbalanced'' is set to continue_N. Mandatory if ''unbalanced'' is set to continue_N, else not required.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    viscosity:    
      description: 'The kinematic viscosity of the fluid being modeled relative to that of water at 20 deg. C'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    wallOrder:    
      description: 'Wall reaction order for pipes'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required:    
    - id    
    - type    
    - hasInputNetwork    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.WaterDistributionManagementEPANET/blob/master/SimulationScenario/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-model.WaterNetworkManagementEPANET/Simulation/schema.json    
  x-model-tags: FIWARE4WATER    
  x-version: 0.0.1    
```  
</details>    
## ペイロードの例  
#### SimulationScenario NGSI-v2 key-values の例。  
SimulationScenarioをJSON-LD形式でkey-valuesにした例です。これは `options=keyValues` を使用した場合に NGSI-v2 と互換性があり、個々のエンティティのコンテキストデータが返されます。  
```json  
{  
  "id": "urn:ngsi-ld:SimulationScenario:01",  
  "type": "SimulationScenario",  
  "description": "Free Text",  
  "createdBy": "urn:ngsi-ld:User:u1",  
  "hasInputNetwork": "urn:ngsi-ld:WaterNetwork:01",  
  "hasSimulationResult": "urn:ngsi-ld:SimulationResult:01",  
  "duration": 86400,  
  "hydraulicTimeStep": 3600,  
  "flowUnits": "LPS",  
  "headlossFormula": "H-W",  
  "startClockTime": 0,  
  "reportStep": 3600,  
  "reportStart": 0,  
  "ruleTimeStep": 900,  
  "statistic": "none",  
  "trials": 40,  
  "accuracy": 0.001,  
  "tolerance": 0.01,  
  "emitterExponent": 0.5,  
  "headError": 0,  
  "flowChange": 0.01,  
  "demandCharge": 2,  
  "demandModel": "PDA",  
  "minimumPressure": 0,  
  "requiredPressure": 20,  
  "pressureExponent": 0.5,  
  "viscosity": 1,  
  "unbalanced": "continue_N",  
  "unbalancedN": 20,  
  "checkFrequency": 2,  
  "maxCheck": 10,  
  "dampLimit": 0,  
  "diffusivity": 1,  
  "bulkOrder": 1,  
  "wallOrder": 1,  
  "tankOrder": 1,  
  "concentrationLimit": 0,  
  "qualityType": "chem",  
  "chemicalName": "Chlorine",  
  "chemicalUnits": "mg/l",  
  "specificGravity": 1,  
  "qualityTimeStep": 60,  
  "operationalControl": [  
    {  
      "type": "Operational Control 1",  
      "setting": 0,  
      "triggerLevel": 30,  
      "controlType": "HILEVEL",  
      "controlledLink": "urn:ngsi-ld:Tank:T1",  
      "monitoredNode": "urn:ngsi-ld:Pump:P1"  
    },  
    {  
      "type": "Operational Control 2",  
      "triggerLevel": 10,  
      "setting": 1,  
      "controlType": "LOWLEVEL",  
      "monitoredNode": "urn:ngsi-ld:Tank:T1",  
      "controlledLink": "urn:ngsi-ld:Pump:P1"  
    }  
  ],  
  "inputParameters": [  
    {  
      "type": "Property 1",  
      "setting": 50,  
      "targetURI": "urn:ngsi-ld:Valve:V1"  
    },  
    {  
      "type": "Property 2",  
      "initialQuality": 2,  
      "targetURI": "urn:ngsi-ld:Tank:T1"  
    },  
    {  
      "type": "Property 1",  
      "efficCurve": "urn:ngsi-ld:Curve:C1",  
      "targetURI": "urn:ngsi-ld:Pump:P1"  
    },  
    {  
      "type": "demand Category 1",  
      "demandCategory": "agriculture demand",  
      "baseDemand": 1.1,  
      "demandPattern": "urn:ngsi-ld:Pattern:Agriculture",  
      "targetURI": "urn:ngsi-ld:Junction:J1"  
    },  
    {  
      "type": "demand Category 2",  
      "demandCategory": "residential demand",  
      "baseDemand": 1.7,  
      "demandPattern": "urn:ngsi-ld:Pattern:Residential",  
      "targetURI": "urn:ngsi-ld:Junction:J1"  
    }  
  ]  
}  
```  
#### SimulationScenario NGSI-v2 正規化例  
SimulationScenarioをJSON-LDフォーマットで正規化した例です。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキスト・データを返します。  
```json  
{  
  "id": "urn:ngsi-ld:SimulationScenario:01",  
  "type": "SimulationScenario",  
  "description": {  
    "type": "Property",  
    "value": "Free Text"  
  },  
  "createdBy": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:User:u1"  
  },  
  "hasInputNetwork": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:WaterNetwork:01"  
  },  
  "hasSimulationResult": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:SimulationResult:01"  
  },  
  "duration": {  
    "type": "Property",  
    "value": 86400  
  },  
  "hydraulicTimeStep": {  
    "type": "Property",  
    "value": 3600  
  },  
  "flowUnits": {  
    "type": "Property",  
    "value": "LPS"  
  },  
  "headlossFormula": {  
    "type": "Property",  
    "value": "H-W"  
  },  
  "startClockTime": {  
    "type": "Property",  
    "value": 0  
  },  
  "reportStep": {  
    "type": "Property",  
    "value": 3600  
  },  
  "reportStart": {  
    "type": "Property",  
    "value": 0  
  },  
  "ruleTimeStep": {  
    "type": "Property",  
    "value": 900  
  },  
  "statistic": {  
    "type": "Property",  
    "value": "NONE"  
  },  
  "trials": {  
    "type": "Property",  
    "value": 40  
  },  
  "accuracy": {  
    "type": "Property",  
    "value": 0.001  
  },  
  "tolerance": {  
    "type": "Property",  
    "value": 0.01  
  },  
  "emitterExponent": {  
    "type": "Property",  
    "value": 0.5  
  },  
  "headError": {  
    "type": "Property",  
    "value": 0  
  },  
  "flowChange": {  
    "type": "Property",  
    "value": 0.01  
  },  
  "demandCharge": {  
    "type": "Property",  
    "value": 2  
  },  
  "demandModel": {  
    "type": "Property",  
    "value": "PDA"  
  },  
  "minimumPressure": {  
    "type": "Property",  
    "value": 0  
  },  
  "requiredPressure": {  
    "type": "Property",  
    "value": 20  
  },  
  "pressureExponent": {  
    "type": "Property",  
    "value": 0.5  
  },  
  "viscosity": {  
    "type": "Property",  
    "value": 1  
  },  
  "unbalanced": {  
    "type": "Property",  
    "value": "continue_N"  
  },  
  "unbalancedN": {  
    "type": "Property",  
    "value": 20  
  },  
  "checkFrequency": {  
    "type": "Property",  
    "value": 2  
  },  
  "maxCheck": {  
    "type": "Property",  
    "value": 10,  
    "unitCode": "C62"  
  },  
  "dampLimit": {  
    "type": "Property",  
    "value": 0  
  },  
  "diffusivity": {  
    "type": "Property",  
    "value": 1  
  },  
  "bulkOrder": {  
    "type": "Property",  
    "value": 1  
  },  
  "wallOrder": {  
    "type": "Property",  
    "value": 1  
  },  
  "tankOrder": {  
    "type": "Property",  
    "value": 1  
  },  
  "concentrationLimit": {  
    "type": "Property",  
    "value": 0  
  },  
  "qualityType": {  
    "type": "Property",  
    "value": "chem"  
  },  
  "chemicalName": {  
    "type": "Property",  
    "value": "Chlorine"  
  },  
  "chemicalUnits": {  
    "type": "Property",  
    "value": "mg/l"  
  },  
  "specificGravity": {  
    "type": "Property",  
    "value": 1  
  },  
  "qualityTimeStep": {  
    "type": "Property",  
    "value": 60  
  },  
  "operationalControl": [  
    {  
      "type": "Property",  
      "value": "Operational Control 1",  
      "setting": {  
        "type": "Property",  
        "value": 0  
      },  
      "triggerLevel": {  
        "type": "Property",  
        "value": 30  
      },  
      "controlType": {  
        "type": "Property",  
        "value": "HILEVEL"  
      },  
      "controlledLink": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Tank:T1"  
      },  
      "monitoredNode": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Pump:P1"  
      }  
    },  
    {  
      "type": "Property",  
      "value": "Operational Control 2",  
      "triggerLevel": {  
        "type": "Property",  
        "value": 10  
      },  
      "setting": {  
        "type": "Property",  
        "value": 1  
      },  
      "controlType": {  
        "type": "Property",  
        "value": "LOWLEVEL"  
      },  
      "monitoredNode": {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:Tank:T1"  
      },  
      "controlledLink": {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:Pump:P1"  
      }  
    }  
  ],  
  "inputParameters": [  
    {  
      "type": "Property",  
      "value": "Property 1",  
      "setting": {  
        "type": "Property",  
        "value": 50,  
        "targetURI": {  
          "type": "Property",  
          "value": "urn:ngsi-ld:Valve:V1"  
        }  
      }  
    },  
    {  
      "type": "Property",  
      "value": "Property 2",  
      "initialQuality": {  
        "type": "Property",  
        "value": 2,  
        "targetURI": {  
          "type": "Relationship",  
          "value": "urn:ngsi-ld:Tank:T1"  
        }  
      }  
    },  
    {  
      "type": "Property",  
      "value": "Property 1",  
      "efficCurve": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Curve:C1",  
        "targetURI": {  
          "type": "Relationship",  
          "value": "urn:ngsi-ld:Pump:P1"  
        }  
      }  
    },  
    {  
      "type": "Property",  
      "value": "demand Category 1",  
      "demandCategory": {  
        "type": "Property",  
        "value": "agriculture demand",  
        "baseDemand": {  
          "type": "Property",  
          "value": 1.1  
        },  
        "demandPattern": {  
          "type": "Relationship",  
          "value": "urn:ngsi-ld:Pattern:Agriculture"  
        },  
        "targetURI": {  
          "type": "Relationship",  
          "object": "urn:ngsi-ld:Junction:J1"  
        }  
      }  
    },  
    {  
      "type": "Property",  
      "value": "demand Category 2",  
      "demandCategory": {  
        "type": "Property",  
        "value": "residential demand",  
        "baseDemand": {  
          "type": "Property",  
          "value": 1.7  
        },  
        "demandPattern": {  
          "type": "Relationship",  
          "value": "urn:ngsi-ld:Pattern:Residential"  
        },  
        "targetURI": {  
          "type": "Relationship",  
          "value": "urn:ngsi-ld:Junction:J1"  
        }  
      }  
    }  
  ]  
}  
```  
#### SimulationScenario NGSI-LD key-value Example  
SimulationScenarioをJSON-LD形式でkey-valuesにした例です。これは `options=keyValues` を使用した場合に NGSI-LD と互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
    "id": "urn:ngsi-ld:SimulationScenario:01",  
    "type": "SimulationScenario",  
    "accuracy": 0.001,  
    "bulkOrder": 1,  
    "checkFrequency": 2,  
    "chemicalName": "Chlorine",  
    "chemicalUnits": "mg/l",  
    "concentrationLimit": 0,  
    "createdBy": "urn:ngsi-ld:User:u1",  
    "dampLimit": 0,  
    "demandCharge": 2,  
    "demandModel": "PDA",  
    "description": "Free Text",  
    "diffusivity": 1,  
    "duration": 86400,  
    "emitterExponent": 0.5,  
    "flowChange": 0.01,  
    "flowUnits": "LPS",  
    "hasInputNetwork": "urn:ngsi-ld:WaterNetwork:01",  
    "hasSimulationResult": "urn:ngsi-ld:SimulationResult:01",  
    "headError": 0,  
    "headlossFormula": "H-W",  
    "hydraulicTimeStep": 3600,  
    "inputParameters": [  
        {  
            "type": "Property 1",  
            "setting": 50,  
            "targetURI": "urn:ngsi-ld:Valve:V1"  
        },  
        {  
            "type": "Property 2",  
            "initialQuality": 2,  
            "targetURI": "urn:ngsi-ld:Tank:T1"  
        },  
        {  
            "type": "Property 1",  
            "efficCurve": "urn:ngsi-ld:Curve:C1",  
            "targetURI": "urn:ngsi-ld:Pump:P1"  
        },  
        {  
            "type": "demand Category 1",  
            "demandCategory": "agriculture demand",  
            "baseDemand": 1.1,  
            "demandPattern": "urn:ngsi-ld:Pattern:Agriculture",  
            "targetURI": "urn:ngsi-ld:Junction:J1"  
        },  
        {  
            "type": "demand Category 2",  
            "demandCategory": "residential demand",  
            "baseDemand": 1.7,  
            "demandPattern": "urn:ngsi-ld:Pattern:Residential",  
            "targetURI": "urn:ngsi-ld:Junction:J1"  
        }  
    ],  
    "maxCheck": 10,  
    "minimumPressure": 0,  
    "operationalControl": [  
        {  
            "type": "Operational Control 1",  
            "setting": 0,  
            "triggerLevel": 30,  
            "controlType": "HILEVEL",  
            "controlledLink": "urn:ngsi-ld:Tank:T1",  
            "monitoredNode": "urn:ngsi-ld:Pump:P1"  
        },  
        {  
            "type": "Operational Control 2",  
            "triggerLevel": 10,  
            "setting": 1,  
            "controlType": "LOWLEVEL",  
            "monitoredNode": "urn:ngsi-ld:Tank:T1",  
            "controlledLink": "urn:ngsi-ld:Pump:P1"  
        }  
    ],  
    "pressureExponent": 0.5,  
    "qualityTimeStep": 60,  
    "qualityType": "chem",  
    "reportStart": 0,  
    "reportStep": 3600,  
    "requiredPressure": 20,  
    "ruleTimeStep": 900,  
    "specificGravity": 1,  
    "startClockTime": 0,  
    "statistic": "none",  
    "tankOrder": 1,  
    "tolerance": 0.01,  
    "trials": 40,  
    "unbalanced": "continue_N",  
    "unbalancedN": 20,  
    "viscosity": 1,  
    "wallOrder": 1,  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.WaterDistributionManagementEPANET/master/context.jsonld"  
    ]  
}  
```  
#### SimulationScenario NGSI-LD 正規化例  
SimulationScenarioをJSON-LDフォーマットで正規化した例です。これは、オプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
    "id": "urn:ngsi-ld:SimulationScenario:01",  
    "type": "SimulationScenario",  
    "accuracy": {  
        "type": "Property",  
        "value": 0.001,  
        "unitCode": "C62"  
    },  
    "bulkOrder": {  
        "type": "Property",  
        "value": 1,  
        "unitCode": "C62"  
    },  
    "checkFrequency": {  
        "type": "Property",  
        "value": 2,  
        "unitCode": "C62"  
    },  
    "chemicalName": {  
        "type": "Property",  
        "value": "Chlorine"  
    },  
    "chemicalUnits": {  
        "type": "Property",  
        "value": "mg/l"  
    },  
    "concentrationLimit": {  
        "type": "Property",  
        "value": 0,  
        "unitCode": "C62"  
    },  
    "createdBy": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:User:u1"  
    },  
    "dampLimit": {  
        "type": "Property",  
        "value": 0,  
        "unitCode": "C62"  
    },  
    "demandCharge": {  
        "type": "Property",  
        "value": 2  
    },  
    "demandModel": {  
        "type": "Property",  
        "value": "PDA"  
    },  
    "description": {  
        "type": "Property",  
        "value": "Free Text"  
    },  
    "diffusivity": {  
        "type": "Property",  
        "value": 1,  
        "unitCode": "C62"  
    },  
    "duration": {  
        "type": "Property",  
        "value": 86400,  
        "unitCode": "SEC"  
    },  
    "emitterExponent": {  
        "type": "Property",  
        "value": 0.5,  
        "unitCode": "C62"  
    },  
    "flowChange": {  
        "type": "Property",  
        "value": 0.01,  
        "unitCode": "MQS"  
    },  
    "flowUnits": {  
        "type": "Property",  
        "value": "LPS"  
    },  
    "hasInputNetwork": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:WaterNetwork:01"  
    },  
    "hasSimulationResult": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:SimulationResult:01"  
    },  
    "headError": {  
        "type": "Property",  
        "value": 0,  
        "unitCode": "MTR"  
    },  
    "headlossFormula": {  
        "type": "Property",  
        "value": "H-W"  
    },  
    "hydraulicTimeStep": {  
        "type": "Property",  
        "value": 3600,  
        "unitCode": "SEC"  
    },  
    "inputParameters": [  
        {  
            "type": "Property",  
            "value": "Property 1",  
            "setting": {  
                "type": "Property",  
                "value": 50,  
                "targetURI": {  
                    "type": "Property",  
                    "value": "urn:ngsi-ld:Valve:V1"  
                }  
            },  
            "datasetId": "urn:ngsi-ld:Dataset:ValveSetting"  
        },  
        {  
            "type": "Property",  
            "value": "Property 2",  
            "initialQuality": {  
                "type": "Property",  
                "value": 2,  
                "targetURI": {  
                    "type": "Relationship",  
                    "value": "urn:ngsi-ld:Tank:T1"  
                }  
            },  
            "datasetId": "urn:ngsi-ld:Dataset:TankInitialQuality"  
        },  
        {  
            "type": "Property",  
            "value": "Property 1",  
            "efficCurve": {  
                "type": "Relationship",  
                "object": "urn:ngsi-ld:Curve:C1",  
                "targetURI": {  
                    "type": "Relationship",  
                    "object": "urn:ngsi-ld:Pump:P1"  
                }  
            },  
            "datasetId": "urn:ngsi-ld:Dataset:PumpCurve"  
        },  
        {  
            "type": "Property",  
            "value": "demand Category 1",  
            "demandCategory": {  
                "type": "Property",  
                "value": "agriculture demand",  
                "baseDemand": {  
                    "type": "Property",  
                    "value": 1.1  
                },  
                "demandPattern": {  
                    "type": "Relationship",  
                    "value": "urn:ngsi-ld:Pattern:Agriculture"  
                },  
                "targetURI": {  
                    "type": "Relationship",  
                    "object": "urn:ngsi-ld:Junction:J1"  
                }  
            },  
            "datasetId": "urn:ngsi-ld:Dataset:Demand1"  
        },  
        {  
            "type": "Property",  
            "value": "demand Category 2",  
            "demandCategory": {  
                "type": "Property",  
                "value": "residential demand",  
                "baseDemand": {  
                    "type": "Property",  
                    "value": 1.7  
                },  
                "demandPattern": {  
                    "type": "Relationship",  
                    "value": "urn:ngsi-ld:Pattern:Residential"  
                },  
                "targetURI": {  
                    "type": "Relationship",  
                    "object": "urn:ngsi-ld:Junction:J1"  
                }  
            },  
            "datasetId": "urn:ngsi-ld:Dataset:Demand2"  
        }  
    ],  
    "maxCheck": {  
        "type": "Property",  
        "value": 10,  
        "unitCode": "C62"  
    },  
    "minimumPressure": {  
        "type": "Property",  
        "value": 0,  
        "unitCode": "MTR"  
    },  
    "operationalControl": [  
        {  
            "type": "Property",  
            "value": "Operational Control 1",  
            "setting": {  
                "type": "Property",  
                "value": 0  
            },  
            "triggerLevel": {  
                "type": "Property",  
                "value": 30  
            },  
            "controlType": {  
                "type": "Property",  
                "value": "HILEVEL"  
            },  
            "controlledLink": {  
                "type": "Relationship",  
                "object": "urn:ngsi-ld:Tank:T1",  
                "datasetId": "urn:ngsi-ld:Dataset:Control01:Node01"  
            },  
            "monitoredNode": {  
                "type": "Relationship",  
                "object": "urn:ngsi-ld:Pump:P1",  
                "datasetId": "urn:ngsi-ld:Dataset:Control01:Link01"  
            },  
            "datasetId": "urn:ngsi-ld:Dataset:HiLevel"  
        },  
        {  
            "type": "Property",  
            "value": "Operational Control 2",  
            "triggerLevel": {  
                "type": "Property",  
                "value": 10  
            },  
            "setting": {  
                "type": "Property",  
                "value": 1  
            },  
            "controlType": {  
                "type": "Property",  
                "value": "LOWLEVEL"  
            },  
            "monitoredNode": {  
                "type": "Relationship",  
                "object": "urn:ngsi-ld:Tank:T1"  
            },  
            "controlledLink": {  
                "type": "Relationship",  
                "object": "urn:ngsi-ld:Pump:P1"  
            },  
            "datasetId": "urn:ngsi-ld:Dataset:LowLevel"  
        }  
    ],  
    "pressureExponent": {  
        "type": "Property",  
        "value": 0.5,  
        "unitCode": "C62"  
    },  
    "qualityTimeStep": {  
        "type": "Property",  
        "value": 60,  
        "unitCode": "SEC"  
    },  
    "qualityType": {  
        "type": "Property",  
        "value": "CHEM"  
    },  
    "reportStart": {  
        "type": "Property",  
        "value": 0,  
        "unitCode": "SEC"  
    },  
    "reportStep": {  
        "type": "Property",  
        "value": 3600,  
        "unitCode": "SEC"  
    },  
    "requiredPressure": {  
        "type": "Property",  
        "value": 20,  
        "unitCode": "MTR"  
    },  
    "ruleTimeStep": {  
        "type": "Property",  
        "value": 900,  
        "unitCode": "SEC"  
    },  
    "specificGravity": {  
        "type": "Property",  
        "value": 1,  
        "unitCode": "C62"  
    },  
    "startClockTime": {  
        "type": "Property",  
        "value": 0,  
        "unitCode": "SEC"  
    },  
    "statistic": {  
        "type": "Property",  
        "value": "NONE"  
    },  
    "tankOrder": {  
        "type": "Property",  
        "value": 1,  
        "unitCode": "C62"  
    },  
    "tolerance": {  
        "type": "Property",  
        "value": 0.01,  
        "unitCode": "C62"  
    },  
    "trials": {  
        "type": "Property",  
        "value": 40,  
        "unitCode": "C62"  
    },  
    "unbalanced": {  
        "type": "Property",  
        "value": "CONTINUE_N"  
    },  
    "unbalancedN": {  
        "type": "Property",  
        "value": 20,  
        "unitCode": "C62"  
    },  
    "viscosity": {  
        "type": "Property",  
        "value": 1,  
        "unitCode": "C62"  
    },  
    "wallOrder": {  
        "type": "Property",  
        "value": 1,  
        "unitCode": "C62"  
    },  
    "@context": []  
}  
```  
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
