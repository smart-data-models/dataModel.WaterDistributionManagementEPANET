<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
单位：Tank坦克    
=========<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.WaterDistributionManagementEPANET/blob/master/Tank/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全局描述：**该实体包含对水网管理领域通用水箱的统一描述。该实体主要与水管理垂直领域和相关物联网应用有关。    
版本： 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 属性列表    
<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。    
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理      
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `bulkReactionCoefficient[number]`: 用于模拟罐内反应的体积反应系数。所有单位均接受 [CEFACT](https://www.unece.org/cefact.html) 代码  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `elevation[number]`: Tank 的某个共同参考点之上的标高。所有单位均接受 [CEFACT](https://www.unece.org/cefact.html) 代码。  . Model: [https://schema.org/Number](https://schema.org/Number)- `hasInlet[uri]`: 标明水库进水点的关系图  - `hasOutlet[uri]`: 标明水库出水点的关系图  - `head[object]`: 节点（路口、水箱或水库）的观测水头  	- `observedBy`:       
- `id[*]`: 实体的唯一标识符  - `initLevel[number]`: 模拟开始时水面高于水箱底部标高的高度。所有单位均以 [CEFACT](https://www.unece.org/cefact.html) 代码表示  . Model: [https://schema.org/Number](https://schema.org/Number)- `initialQuality[number]`: 模拟开始时水箱中的水质水平。所有单位均接受 [CEFACT](https://www.unece.org/cefact.html) 代码  . Model: [https://schema.org/Number](https://schema.org/Number)- `level[object]`: 网络元素中的观测值  	- `observedBy`:       
- `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `maxLevel[number]`: 模拟开始时水面高于水箱底部标高的高度。所有单位均以 [CEFACT](https://www.unece.org/cefact.html) 代码表示  . Model: [https://schema.org/Number](https://schema.org/Number)- `minLevel[number]`: 水箱中的水可下降到的最低水位。所有单位都接受 [CEFACT](https://www.unece.org/cefact.html) 代码  . Model: [https://schema.org/Number](https://schema.org/Number)- `minVolume[number]`: 水箱处于最低水位时的水量。所有单位都接受 [CEFACT](https://www.unece.org/cefact.html) 代码  . Model: [https://schema.org/Number](https://schema.org/Number)- `mixingFraction[number]`: 双隔室 (2COMP) 混合模型中入口-出口隔室在罐体总容积中所占的比例。所有单位均接受 [CEFACT](https://www.unece.org/cefact.html) 代码  . Model: [https://schema.org/Number](https://schema.org/Number)- `mixingModel[string]`: 源类别属性的子属性。枚举：'2COMP、FIFO、LIFO、MIXED'。  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: 该项目的名称  - `nominalDiameter[number]`: 罐体直径。所有单位均接受 [CEFACT](https://www.unece.org/cefact.html) 代码  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `pressure[object]`: 节点（连接点、储罐或水库）处的观测压力  	- `observedBy`:       
- `quality[object]`: 网络组件的观测质量  	- `observedBy`:       
- `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `sourceCategory[object]`: 描述在特定节点进入网络的源流质量  . Model: [https://schema.org/Text](https://schema.org/Text)	- `sourcePattern[*]`: 与源类别属性模式的关系      
	- `sourceQuality[number]`: 源的基准或平均浓度（或质量流量）。源类别 "属性的子属性。[CEFACT](https://www.unece.org/cefact.html)代码中接受所有单位。  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `sourceType[string]`: 源类别属性的子属性  . Model: [https://schema.org/Text](https://schema.org/Text)    
- `sourceMassInflow[object]`: 节点（路口、水槽或水库）处观测到的源质量流入量  	- `observedBy`:       
- `supply[object]`: 在节点（连接点、水箱或蓄水池）观察到的供水量  	- `observedBy`:       
- `tag[string]`: 一个可选的文本字符串，用于将管道归入一个类别，可能是基于管龄或材料的类别  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI-LD 实体类型。必须是 Tank  - `volumeCurve[*]`: 用于描述水箱容积与水位关系的曲线的 ID 标签  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
所需属性    
- `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 属性的数据模型描述    
按字母顺序排列（点击查看详情）    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
Tank:      
  description: This entity contains a harmonised description of a generic tank made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.      
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
    bulkReactionCoefficient:      
      description: 'The bulk reaction coefficient used for modelling reactions in the tank. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code'      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: 1/day      
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
    elevation:      
      description: 'The elevation above some common reference of the Tank. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code'      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: metre      
    hasInlet:      
      description: A relationship indicating the water inlet points of the Reservoir      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    hasOutlet:      
      description: A relationship indicating the water outlet points of the Reservoir      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    head:      
      description: 'Observed head at the node (junction, tank or reservoir)'      
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
          description: Value of the head      
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
    initLevel:      
      description: 'The height of the water surface above the bottom elevation of the tank at the start of the simulation. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code'      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: metre      
    initialQuality:      
      description: 'Water quality level in the tank at the start of the simulation. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code'      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: mg/L      
    level:      
      description: Observed level in the element of the network      
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
          description: Numerical value of the level      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
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
    maxLevel:      
      description: 'The height of the water surface above the bottom elevation of the tank at the start of the simulation. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code'      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: metre      
    minLevel:      
      description: 'The minimum level that water in the tank can drop to. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code'      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: metre      
    minVolume:      
      description: 'The volume of water in the tank when it is at its minimum level. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code'      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: cubic metre      
    mixingFraction:      
      description: 'The fraction of the tank''s total volume that comprises the inlet-outlet compartment of the two-compartment (2COMP) mixing model. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code'      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: No unit      
    mixingModel:      
      description: 'A sub-property of the Property sourceCategory. Enum:''2COMP, FIFO, LIFO, MIXED'''      
      enum:      
        - 2COMP      
        - FIFO      
        - LIFO      
        - MIXED      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    nominalDiameter:      
      description: 'The diameter of the tank. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code'      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: Metre      
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
    pressure:      
      description: 'Observed pressure at the node (junction, tank or reservoir)'      
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
          description: Numerical value of the pressure      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
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
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    sourceCategory:      
      description: Description of the quality of source flow entering the network at a specific node      
      properties:      
        sourcePattern:      
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
          description: A relationship to the pattern pf the sourceCategory property      
          x-ngsi:      
            type: Relationship      
        sourceQuality:      
          description: 'Baseline or average concentration (or mass flow rate) of source. A sub-property of the Property ''sourceCategory''. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code'      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
            units: ' mg/L'      
        sourceType:      
          description: A sub-property of the Property sourceCategory      
          enum:      
            - CONCEN      
            - MASS      
            - FLOWPACED      
            - SETPOINT      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        value:      
          description: Value of the source category      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    sourceMassInflow:      
      description: 'Observed source mass inflow at the node (junction, tank or reservoir)'      
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
          description: Numerical value of the source mass at the inflow      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
    supply:      
      description: 'Observed supply at the node (junction, tank or reservoir)'      
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
          description: Numerical value of the supply      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
    tag:      
      description: 'An optional text string used to assign the pipe to a category, perhaps one based on age or material'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    type:      
      description: NGSI-LD Entity Type. It has to be Tank      
      enum:      
        - Tank      
      type: string      
      x-ngsi:      
        type: Property      
    volumeCurve:      
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
      description: The ID label of a curve used to describe the relation between tank volume and water level      
      x-ngsi:      
        type: Relationship      
  required:      
    - id      
    - type      
    - location      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.WaterDistributionManagementEPANET/blob/master/Tank/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.WaterDistributionManagementEPANET/Tank/schema.json      
  x-model-tags: FIWARE4WATER      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 有效载荷示例    
#### 坦克 NGSI-v2 键值示例    
下面是一个以 JSON-LD 格式作为键值的 Tank 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "1863179e-3968-4493-9167-ee21f880cc02",  
  "type": "Tank",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      24.30623,  
      60.07966  
    ]  
  },  
  "elevation": 112.9,  
  "initLevel": 3,  
  "minLevel": 0,  
  "maxLevel": 6.75,  
  "minVolume": 0,  
  "nominalDiameter": 13.73,  
  "description": "Free Text",  
  "initialQuality": 0.5,  
  "sourceCategory": {  
    "value": "category1",  
    "sourceType": "MASS",  
    "sourceQuality": 1.2,  
    "sourcePattern": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
  },  
  "mixingModel": "MIXED",  
  "volumeCurve": "fAM-8ca3-4533-a2eb-12015",  
  "mixingFraction": 0.7,  
  "bulkReactionCoefficient": 0.7,  
  "tag": "DMA1"  
}  
```  
</details>    
#### 储罐 NGSI-v2 标准化示例    
下面是一个规范化 JSON-LD 格式 Tank 的示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "1863179e-3968-4493-9167-ee21f880cc02",  
  "type": "Tank",  
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
  "elevation": {  
    "type": "Number",  
    "value": 112.9  
  },  
  "initLevel": {  
    "type": "Number",  
    "value": 3  
  },  
  "minLevel": {  
    "type": "Boolean",  
    "value": false  
  },  
  "maxLevel": {  
    "type": "Number",  
    "value": 6.75  
  },  
  "minVolume": {  
    "type": "Boolean",  
    "value": false  
  },  
  "nominalDiameter": {  
    "type": "Number",  
    "value": 13.73  
  },  
  "description": {  
    "type": "Text",  
    "value": "Free Text"  
  },  
  "initialQuality": {  
    "type": "Number",  
    "value": 0.5  
  },  
  "sourceCategory": {  
    "type": "StructuredValue",  
    "value": {  
      "value": "category1",  
      "sourceType": "MASS",  
      "sourceQuality": 1.2,  
      "sourcePattern": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
    }  
  },  
  "mixingModel": {  
    "type": "Text",  
    "value": "MIXED"  
  },  
  "volumeCurve": {  
    "type": "Text",  
    "value": "fAM-8ca3-4533-a2eb-12015"  
  },  
  "mixingFraction": {  
    "type": "Number",  
    "value": 0.7  
  },  
  "bulkReactionCoefficient": {  
    "type": "Number",  
    "value": 0.7  
  },  
  "tag": {  
    "type": "Text",  
    "value": "DMA1"  
  },  
  "level": {  
    "type": "StructuredValue",  
    "value": {  
      "value": 20,  
      "observedBy": "device-9845A"  
    }  
  },  
  "pressure": {  
    "type": "StructuredValue",  
    "value": {  
      "value": 20,  
      "observedBy": "device-9845A"  
    }  
  },  
  "supply": {  
    "type": "StructuredValue",  
    "value": {  
      "value": 150,  
      "observedBy": "device-9845A"  
    }  
  },  
  "head": {  
    "type": "StructuredValue",  
    "value": {  
      "value": 20,  
      "observedBy": "device-9845A"  
    }  
  },  
  "quality": {  
    "type": "StructuredValue",  
    "value": {  
      "value": 0.5,  
      "observedBy": "device-9845A"  
    }  
  },  
  "sourceMassInflow": {  
    "type": "StructuredValue",  
    "value": {  
      "value": 100,  
      "observedBy": "device-9845A"  
    }  
  }  
}  
```  
</details>    
#### 储罐 NGSI-LD 键值示例    
下面是一个以 JSON-LD 格式作为键值的 Tank 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Tank:1863179e-3968-4493-9167-ee21f880cc02",  
  "type": "Tank",  
  "bulkReactionCoefficient": 0.7,  
  "createdAt": "2020-03-13T15:42:00Z",  
  "description": "Free Text",  
  "elevation": 112.9,  
  "initLevel": 3,  
  "initialQuality": 0.5,  
  "location": {  
    "coordinates": [  
      24.30623,  
      60.07966  
    ],  
    "type": "Point"  
  },  
  "maxLevel": 6.75,  
  "minLevel": 0,  
  "minVolume": 0,  
  "mixingFraction": 0.7,  
  "mixingModel": "MIXED",  
  "modifiedAt": "2020-03-13T15:45:00Z",  
  "nominalDiameter": 13.73,  
  "sourceCategory": {  
    "value": "category1",  
    "sourceType": "MASS",  
    "sourceQuality": 1.2,  
    "sourcePattern": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
  },  
  "tag": "DMA1",  
  "volumeCurve": "urn:ngsi-ld:Curve:fAM-8ca3-4533-a2eb-12015",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.WaterDistributionManagementEPANET/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### 储罐 NGSI-LD 标准化示例    
下面是一个规范化 JSON-LD 格式 Tank 的示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:Tank:1863179e-3968-4493-9167-ee21f880cc02",  
    "type": "Tank",  
    "bulkReactionCoefficient": {  
        "type": "Property",  
        "value": 0.7,  
        "unitCode": "E91"  
    },  
    "description": {  
        "type": "Property",  
        "value": "Free Text"  
    },  
    "elevation": {  
        "type": "Property",  
        "value": 112.9,  
        "unitCode": "MTR"  
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
    "initLevel": {  
        "type": "Property",  
        "value": 3,  
        "unitCode": "MTR"  
    },  
    "initialQuality": {  
        "type": "Property",  
        "value": 0.5,  
        "unitCode": "M1"  
    },  
    "level": {  
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
    "maxLevel": {  
        "type": "Property",  
        "value": 6.75,  
        "unitCode": "MTR"  
    },  
    "minLevel": {  
        "type": "Property",  
        "value": 0,  
        "unitCode": "MTR"  
    },  
    "minVolume": {  
        "type": "Property",  
        "value": 0,  
        "unitCode": "MTQ"  
    },  
    "mixingFraction": {  
        "type": "Property",  
        "value": 0.7,  
        "unitCode": "C62"  
    },  
    "mixingModel": {  
        "type": "Property",  
        "value": "MIXED"  
    },  
    "nominalDiameter": {  
        "type": "Property",  
        "value": 13.73,  
        "unitCode": "MTR"  
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
    "sourceCategory": {  
        "type": "Property",  
        "value": {  
            "type": "Property",  
            "value": "category1"  
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
    "tag": {  
        "type": "Property",  
        "value": "DMA1"  
    },  
    "volumeCurve": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Curve:fAM-8ca3-4533-a2eb-12015"  
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
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
