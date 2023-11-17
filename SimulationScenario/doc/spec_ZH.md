<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体：模拟场景    
=======<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.WaterDistributionManagementEPANET/blob/master/SimulationScenario/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全局描述：**该实体包含对水网管理领域通用模拟场景的统一描述。该实体主要与垂直水网管理和相关物联网应用有关。    
版本： 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 属性列表    
<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。    
- `accuracy[number]`: 用于确定何时达到水力解决方案的总归一化流量变化收敛标准  . Model: [https://schema.org/Number](https://schema.org/Number)- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理      
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `bulkOrder[number]`: 管道散装水反应顺序  . Model: [https://schema.org/Number](https://schema.org/Number)- `checkFrequency[number]`: 液压状态检查频率  . Model: [https://schema.org/Number](https://schema.org/Number)- `chemicalName[string]`: 建模化学品的名称。仅在 "质量类型 "为 CHEM 时使用  . Model: [https://schema.org/Text](https://schema.org/Text)- `chemicalUnits[string]`: 建模化学品的单位。仅在 "质量类型 "为 CHEM 时使用  . Model: [https://schema.org/Text](https://schema.org/Text)- `concentrationLimit[number]`: 生长反应的极限浓度  . Model: [https://schema.org/Number](https://schema.org/Number)- `createdBy[*]`: 创建/触发模拟的 ID。对 "用户 "类型实体的引用  . Model: [https://schema.org/URL](https://schema.org/URL)- `dampLimit[number]`: PRV 和 PSV 开始进行溶液阻尼和状态检查的精度值  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `demandCategory[object]`: 允许将基本需求和时间模式分配给其他类别的用户  . Model: [https://schema.org/Text](https://schema.org/Text)	- `baseDemand[string]`: 该类别的基准或平均需求量。需求类别属性的子属性  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `demandPattern[*]`: 与 "需求类别 "属性模式的关系      
- `demandCharge[number]`: 按最高千瓦使用量收取能源费用  . Model: [https://schema.org/Number](https://schema.org/Number)- `demandModel[string]`: 指定分析是压力驱动（PDA）还是需求驱动（DDA）。枚举:'DDA, PDA  . Model: [https://schema.org/Text](https://schema.org/Text)- `description[string]`: 项目描述  - `diffusivity[number]`: 相对于氯在水中的扩散率，质量分析中分析的化学品的分子扩散率  . Model: [https://schema.org/Number](https://schema.org/Number)- `duration[number]`: 模拟时间，以秒为单位  . Model: [https://schema.org/Number](https://schema.org/Number)- `emitterExponent[number]`: 从发射极计算时，交界处压力升高的功率  . Model: [https://schema.org/Number](https://schema.org/Number)- `energyUse[object]`: 观察网络元素的能源使用情况  	- `observedBy`:       
- `flow[object]`: 从 "起点 "节点到 "终点 "节点的流速，由链接处的设备（管道、阀门或泵）测量得出  	- `observedBy`:       
- `flowChange[number]`: 最大流量变化收敛标准，用于确定何时达到水力解决方案  . Model: [https://schema.org/Number](https://schema.org/Number)- `flowUnits[string]`: 模拟中表示流速的单位。允许的选项有 CFS（立方英尺/秒）、GPM（加仑/分钟）、MGD（百万加仑/天）、IMGD（英制百万加仑/天）、AFD（英亩-英尺/天）、LPS（升/秒）、LPM（升/分钟）、MLD（百万升/天）、CMH（立方米/小时）和 CMD（立方米/天）。枚举：'AFD、CFS、CMD、CMH、GPM、IMGD、LPS、LPM、MLD、MGD'。  . Model: [https://schema.org/Text](https://schema.org/Text)- `hasInputNetwork[*]`: 模拟中使用的网络 ID  . Model: [https://schema.org/URL](https://schema.org/URL)- `hasSimulationResult[*]`: 相关模拟结果的 ID。模拟结果 "类型实体的引用  . Model: [https://schema.org/URL](https://schema.org/URL)- `head[object]`: 节点（路口、水箱或水库）的观测水头  	- `observedBy`:       
- `headError[number]`: 最大水头损失收敛标准，用于确定何时达到水力解决方案  . Model: [https://schema.org/Number](https://schema.org/Number)- `headlossFormula[string]`: 用于计算流经管道的水头损失的公式。可选公式有 Hazen-Williams (H-W)、Darcy-Weisbach (D-W) 或 Chezy-Manning (C-M)。允许的选项有 "H-W"、"D-W"、"C-M"。枚举：'C-M、D-W、H-W  . Model: [https://schema.org/Text](https://schema.org/Text)- `hydraulicTimeStep[number]`: 决定计算网络水力状态的频率。以秒为单位  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: 实体的唯一标识符  - `initialQuality[object]`: 网络组件的初始质量  	- `observedBy`:       
- `initialStatus[string]`: 模拟开始时的链接状态。枚举："打开"、"关闭"、"CV  . Model: [https://schema.org/Text](https://schema.org/Text)- `inputParameter[array]`: 描述为模拟而对网络进行的一系列修改  . Model: [https://Text](https://Text)- `level[object]`: 网络元素中的观测值  	- `observedBy`:       
- `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `maxCheck[number]`: 停止状态检查的试验次数  . Model: [https://schema.org/Number](https://schema.org/Number)- `minimumPressure[number]`: 在压力曲线分析中，低于该压力时无法交付需求。仅在需求模型为 "PDA "时使用  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: 该项目的名称  - `operationalControl[array]`: 项目的运行控制  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `patternStart[date-time]`: 模拟开始时间  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `patternStep[number]`: 模拟的模式步骤  . Model: [https://schema.org/Number](https://schema.org/Number)- `pressure[object]`: 节点（连接点、储罐或水库）处的观测压力  	- `observedBy`:       
- `pressureExponent[number]`: 在压力驱动分析中计算输送需求时，压力升高到的功率。仅在需求模型为 "PDA "时使用  . Model: [https://schema.org/Number](https://schema.org/Number)- `quality[object]`: 网络组件的观测质量  	- `observedBy`:       
- `qualityTimeStep[number]`: 用于跟踪网络中水质变化的时间步长。单位为秒  . Model: [https://schema.org/Number](https://schema.org/Number)- `qualityType[string]`: 水质分析类型。枚举:'化学、年龄、痕量、无  . Model: [https://schema.org/Text](https://schema.org/Text)- `reportStart[number]`: 开始报告结果的模拟时间。以模拟开始后的秒数表示  . Model: [https://schema.org/Number](https://schema.org/Number)- `reportStep[number]`: 报告输出结果的时间间隔，以秒为单位  . Model: [https://schema.org/Number](https://schema.org/Number)- `requiredPressure[number]`: 在压力驱动分析下，满足节点全部需求所需的压力。仅在需求模型为 "PDA "时使用  . Model: [https://schema.org/Number](https://schema.org/Number)- `ruleTimeStep[number]`: 时间步长，用于检查基于规则的控制导致的系统状态变化。以秒为单位  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `sourceCategory[object]`: 描述在特定节点进入网络的源流质量  . Model: [https://schema.org/Text](https://schema.org/Text)	- `sourcePattern[*]`: 与源类别属性模式的关系      
	- `sourceQuality[number]`: 源的基准或平均浓度（或质量流量）。源类别 "属性的子属性。[CEFACT](https://www.unece.org/cefact.html)代码中接受所有单位。  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `sourceType[string]`: 源类别属性的子属性  . Model: [https://schema.org/Text](https://schema.org/Text)    
- `sourceMassInflow[object]`: 节点（路口、水槽或水库）处观测到的源质量流入量  	- `observedBy`:       
- `specificGravity[number]`: 被模拟流体的密度与 4 摄氏度时水的密度之比。C  . Model: [https://schema.org/Number](https://schema.org/Number)- `startClockTime[number]`: 模拟开始的时间。以从当天开始的秒数表示  . Model: [https://schema.org/Number](https://schema.org/Number)- `statistic[string]`: 对生成的模拟结果时间序列进行统计后处理的类型。选项包括平均值（报告时间平均结果）、最小值（仅报告最小值）、最大值（仅报告最大值）、范围（报告最小值和最大值之间的差值）和无（报告完整时间序列）。枚举："平均、最小、最大、范围、无"。  . Model: [https://schema.org/string](https://schema.org/string)- `status[string]`: 节点的动态状态。枚举："打开"、"关闭"、"CV  . Model: [https://schema.org/Text](https://schema.org/Text)- `supply[object]`: 在节点（连接点、水箱或蓄水池）观察到的供水量  	- `observedBy`:       
- `tag[string]`: 一个可选的文本字符串，用于将管道归入一个类别，可能是基于管龄或材料的类别  . Model: [https://schema.org/Text](https://schema.org/Text)- `tankOrder[number]`: 储罐散装水反应顺序  . Model: [https://schema.org/Number](https://schema.org/Number)- `tolerance[number]`: 水质容忍度  . Model: [https://schema.org/Number](https://schema.org/Number)- `traceNodeID[*]`: 质量分析中被跟踪节点的 URI。如果 "qualityType"（质量类型）为 TRACE，则为必填项，否则为非必填项  . Model: [https://schema.org/URL](https://schema.org/URL)- `trials[number]`: 在模拟的每个水力时间步进中，用于求解网络水力的最大试验次数  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI-LD 实体类型。必须是 SimulationScenario  - `unbalanced[string]`: 确定在允许的试验次数内无法得出水力解时的处理方式。允许的选项有 STOP（停止分析）、CONTINUE（继续分析，但有警告信息）和 CONTINUE_N（继续 N 次试验，N 的值由 "unbalancedN "给出）。枚举："停止、继续、继续_N  . Model: [https://schema.org/Text](https://schema.org/Text)- `unbalancedN[number]`: 如果 "不平衡 "设置为 continue_N，则允许的额外试验次数。如果 "不平衡 "设置为 continue_N，则为必填项，否则为非必填项  . Model: [https://schema.org/Number](https://schema.org/Number)- `valveCurve[*]`: 参考阀门所在的曲线  - `valveType[string]`: 根据阀门类别划分的阀门类型。枚举：'FCV、GPV、PBV、PRV、PSV、TCV  - `velocity[object]`: 在链接处（管道、阀门或泵）观察到的速度  	- `observedBy[uri]`: 观测到速度的地方      
- `viscosity[number]`: 模拟流体的运动粘度相对于 20 摄氏度时水的运动粘度。C  . Model: [https://schema.org/Number](https://schema.org/Number)- `wallOrder[number]`: 管壁反应顺序  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
所需属性    
- `hasInputNetwork`  - `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 属性的数据模型描述    
按字母顺序排列（点击查看详情）    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
SimulationScenario:      
  description: This entity contains a harmonised description of a generic simulation scenario made for the Water Network Management domain. This entity is primarily associated with the water network management vertical and related IoT applications.      
  properties:      
    accuracy:      
      description: Total normalized flow change convergence criterion for determining when a hydraulic solution has been reached      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
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
    bulkOrder:      
      description: Bulk water reaction order for pipes      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    checkFrequency:      
      description: Frequency of hydraulic status checks      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    chemicalName:      
      description: Name of the chemical modelled. Only used if 'qualityType' is CHEM      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    chemicalUnits:      
      description: Units of the chemical modelled. Only used if 'qualityType' is CHEM      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    concentrationLimit:      
      description: Limiting concentration for growth reactions      
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
      description: The ID of who created/triggered the simulation. Reference to an entity of type 'User'      
      x-ngsi:      
        model: https://schema.org/URL      
        type: Relationship      
    dampLimit:      
      description: Accuracy value at which solution damping and status checks begin for PRVs and PSVs      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
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
    demandCategory:      
      description: Allows base demands and time patterns to be assigned to other categories of users      
      properties:      
        baseDemand:      
          description: Baseline or average demand for the category. A sub-property of the Property demandCategory      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        demandPattern:      
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
          description: A relationship to the pattern of the 'demandCategory' property      
          x-ngsi:      
            type: Relationship      
        value:      
          description: Value of the demand category      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    demandCharge:      
      description: Energy charge per maximum kW usage      
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
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    diffusivity:      
      description: 'Molecular diffusivity of the chemical analysed in a quality analysis, relative to diffusivity of chlorine in water'      
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
      description: Power to which pressure at a junction is raised when computing from an emitter      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    energyUse:      
      description: Observed energy use by the element of the network      
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
          description: Numerical value of the use of Energy      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
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
    flowChange:      
      description: Maximum flow change convergence criterion for determining when a hydraulic solution has been reached      
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
      description: The ID of the network used in the simulation      
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
      description: The ID of the related simulation result. Reference to an entity of type 'SimulationResult'      
      x-ngsi:      
        model: https://schema.org/URL      
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
    headError:      
      description: Maximum headloss convergence criterion for determining when a hydraulic solution has been reached      
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
      description: Determines how often the hydraulic state of the network is calculated. Given in seconds      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: seconds      
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
    initialQuality:      
      description: Initial quality in the network component      
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
          description: Numerical value of the initial quality      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
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
    inputParameter:      
      description: Description of the set of modifications to be applied to the network for the simulation      
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
            description: URI of network component with property modified in simulation. A sub-relationship of the Property water attribute      
            x-ngsi:      
              model: https://schema.org/URL      
              type: Relationship      
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
    maxCheck:      
      description: Number of trials after which status checks are discontinued      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    minimumPressure:      
      description: Pressure below which no demand can be delivered under a pressure dirven analysis. Only used if demandModel is 'PDA'      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    operationalControl:      
      description: The operational control of de item      
      items:      
        properties:      
          controlType:      
            description: 'Type of trigger for the control. A sub-property of the Property ''control''. Enum:''HILEVEL, LOWLEVEL, TIMEOFDAY, TIMER'''      
            enum:      
              - HILEVEL      
              - LOWLEVEL      
              - TIMEOFDAY      
              - TIMER      
            type: string      
            x-ngsi:      
              model: https://schema.org/Text      
              type: Property      
          controlledLink:      
            anyOf:      
              - maxLength: 256      
                minLength: 1      
                pattern: ^[\w\-\.\{\}\$\+\*\[\]'|~^@!,:\\]+$      
                type: string      
              - format: uri      
                type: string      
            description: 'Link controlled. A sub-relationship of the Property ''control''. Reference to an entity of type ''Pipe'', ''Pump'' or ''Valve'''      
            x-ngsi:      
              model: https://schema.org/URL      
              type: Relationship      
          monitoredNode:      
            anyOf:      
              - maxLength: 256      
                minLength: 1      
                pattern: ^[\w\-\.\{\}\$\+\*\[\]'|~^@!,:\\]+$      
                type: string      
              - format: uri      
                type: string      
            description: 'Node which is monitored for control trigger level. A sub-relationship of the Property ''control''.  Reference to an entity of type ''Junction'', ''Tank'' or ''Reservoir'''      
            x-ngsi:      
              model: https://schema.org/URL      
              type: Relationship      
          setting:      
            description: Setting applied in the to the controlled link when trigger level is reached. A sub-property of the Property 'control'      
            type: number      
            x-ngsi:      
              model: https://schema.org/Number      
              type: Property      
          triggerLevel:      
            description: Level at which control is activated. A sub-property of the Property 'control'      
            type: number      
            x-ngsi:      
              model: https://schema.org/Number      
              type: Property      
          type:      
            description: 'Description of a control applied to the network for the simulation. Enum:''controlledLink, controlType, monitoredNode, setting, triggerLevel'''      
            type: string      
            x-ngsi:      
              model: https://schema.org/Text      
              type: Property      
        type: object      
      type: array      
      x-ngsi:      
        type: Property      
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
    patternStart:      
      description: Start time of the  the simulation      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    patternStep:      
      description: Pattern step of the simulation      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
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
    pressureExponent:      
      description: Power to which pressure is raised when calculating the demand delivered under a pressure driven analysis. Only used if demandModel is 'PDA'      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
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
    qualityTimeStep:      
      description: The timestep used to track changes in water quality in the network. Given in seconds      
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
      description: Simulation time at which results start to be reported. Given in seconds from start of simulation      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: seconds      
    reportStep:      
      description: Interval at which output results are reported. given in seconds      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: seconds      
    requiredPressure:      
      description: Pressure required to supply a node's full demand under a pressure driven analysis. Only used if demandModel is 'PDA'      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    ruleTimeStep:      
      description: Time step used to check for changes in system status due to rule-based controls. Given in seconds      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: seconds      
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
    specificGravity:      
      description: The ratio of the density of the fluid being modeled to that of water at 4 deg. C      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    startClockTime:      
      description: Time of day at which the simulation begins. Given as seconds from start of day      
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
    tankOrder:      
      description: Bulk water reaction order for tanks      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    tolerance:      
      description: Water quality tolerance      
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
      description: The maximum number of trials used to solve network hydraulics at each hydraulic time step of a simulation      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    type:      
      description: NGSI-LD Entity Type. It has to be SimulationScenario      
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
      description: 'Number of additional trials allowed if ''unbalanced'' is set to continue_N. Mandatory if ''unbalanced'' is set to continue_N, else not required'      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    valveCurve:      
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
      description: Reference to the Curve where the valve is located      
      x-ngsi:      
        type: Relationship      
    valveType:      
      description: 'Type of valve according to valve categories. Enum:''FCV, GPV, PBV, PRV, PSV, TCV'''      
      enum:      
        - FCV      
        - GPV      
        - PBV      
        - PRV      
        - PSV      
        - TCV      
      type: string      
      x-ngsi:      
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
    viscosity:      
      description: The kinematic viscosity of the fluid being modeled relative to that of water at 20 deg. C      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    wallOrder:      
      description: Wall reaction order for pipes      
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.WaterDistributionManagementEPANET/blob/master/SimulationScenario/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/data-model.WaterNetworkManagementEPANET/Simulation/schema.json      
  x-model-tags: FIWARE4WATER      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 有效载荷示例    
#### SimulationScenario NGSI-v2 key-values 示例    
下面是一个以 JSON-LD 格式作为键值的 SimulationScenario 示例。当使用 "options=keyValues "时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
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
</details>    
#### SimulationScenario NGSI-v2 normalized 示例    
下面是一个规范化 JSON-LD 格式的 SimulationScenario 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SimulationScenario:01",  
  "type": "SimulationScenario",  
  "description": {  
    "type": "Text",  
    "value": "Free Text"  
  },  
  "createdBy": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:User:u1"  
  },  
  "hasInputNetwork": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:WaterNetwork:01"  
  },  
  "hasSimulationResult": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SimulationResult:01"  
  },  
  "duration": {  
    "type": "Number",  
    "value": 86400  
  },  
  "hydraulicTimeStep": {  
    "type": "Number",  
    "value": 3600  
  },  
  "flowUnits": {  
    "type": "Text",  
    "value": "LPS"  
  },  
  "headlossFormula": {  
    "type": "Text",  
    "value": "H-W"  
  },  
  "startClockTime": {  
    "type": "Boolean",  
    "value": false  
  },  
  "reportStep": {  
    "type": "Number",  
    "value": 3600  
  },  
  "reportStart": {  
    "type": "Boolean",  
    "value": false  
  },  
  "ruleTimeStep": {  
    "type": "Number",  
    "value": 900  
  },  
  "statistic": {  
    "type": "Text",  
    "value": "none"  
  },  
  "trials": {  
    "type": "Number",  
    "value": 40  
  },  
  "accuracy": {  
    "type": "Number",  
    "value": 0.001  
  },  
  "tolerance": {  
    "type": "Number",  
    "value": 0.01  
  },  
  "emitterExponent": {  
    "type": "Number",  
    "value": 0.5  
  },  
  "headError": {  
    "type": "Boolean",  
    "value": false  
  },  
  "flowChange": {  
    "type": "Number",  
    "value": 0.01  
  },  
  "demandCharge": {  
    "type": "Number",  
    "value": 2  
  },  
  "demandModel": {  
    "type": "Text",  
    "value": "PDA"  
  },  
  "minimumPressure": {  
    "type": "Boolean",  
    "value": false  
  },  
  "requiredPressure": {  
    "type": "Number",  
    "value": 20  
  },  
  "pressureExponent": {  
    "type": "Number",  
    "value": 0.5  
  },  
  "viscosity": {  
    "type": "Boolean",  
    "value": true  
  },  
  "unbalanced": {  
    "type": "Text",  
    "value": "continue_N"  
  },  
  "unbalancedN": {  
    "type": "Number",  
    "value": 20  
  },  
  "checkFrequency": {  
    "type": "Number",  
    "value": 2  
  },  
  "maxCheck": {  
    "type": "Number",  
    "value": 10  
  },  
  "dampLimit": {  
    "type": "Boolean",  
    "value": false  
  },  
  "diffusivity": {  
    "type": "Boolean",  
    "value": true  
  },  
  "bulkOrder": {  
    "type": "Boolean",  
    "value": true  
  },  
  "wallOrder": {  
    "type": "Boolean",  
    "value": true  
  },  
  "tankOrder": {  
    "type": "Boolean",  
    "value": true  
  },  
  "concentrationLimit": {  
    "type": "Boolean",  
    "value": false  
  },  
  "qualityType": {  
    "type": "Text",  
    "value": "chem"  
  },  
  "chemicalName": {  
    "type": "Text",  
    "value": "Chlorine"  
  },  
  "chemicalUnits": {  
    "type": "Text",  
    "value": "mg/l"  
  },  
  "specificGravity": {  
    "type": "Boolean",  
    "value": true  
  },  
  "qualityTimeStep": {  
    "type": "Number",  
    "value": 60  
  },  
  "operationalControl": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "controlType": "HILEVEL",  
        "controlledLink": "urn:ngsi-ld:Tank:T1",  
        "monitoredNode": "urn:ngsi-ld:Pump:P1",  
        "setting": 0,  
        "triggerLevel": 30,  
        "type": "Operational Control 1"  
      },  
      {  
        "controlType": "LOWLEVEL",  
        "controlledLink": "urn:ngsi-ld:Pump:P1",  
        "monitoredNode": "urn:ngsi-ld:Tank:T1",  
        "setting": 1,  
        "triggerLevel": 10,  
        "type": "Operational Control 2"  
      }  
    ]  
  },  
  "inputParameters": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "setting": 50,  
        "targetURI": "urn:ngsi-ld:Valve:V1",  
        "type": "Property 1"  
      },  
      {  
        "initialQuality": 2,  
        "targetURI": "urn:ngsi-ld:Tank:T1",  
        "type": "Property 2"  
      },  
      {  
        "efficCurve": "urn:ngsi-ld:Curve:C1",  
        "targetURI": "urn:ngsi-ld:Pump:P1",  
        "type": "Property 1"  
      },  
      {  
        "baseDemand": 1.1,  
        "demandCategory": "agriculture demand",  
        "demandPattern": "urn:ngsi-ld:Pattern:Agriculture",  
        "targetURI": "urn:ngsi-ld:Junction:J1",  
        "type": "demand Category 1"  
      },  
      {  
        "baseDemand": 1.7,  
        "demandCategory": "residential demand",  
        "demandPattern": "urn:ngsi-ld:Pattern:Residential",  
        "targetURI": "urn:ngsi-ld:Junction:J1",  
        "type": "demand Category 2"  
      }  
    ]  
  }  
}  
```  
</details>    
#### SimulationScenario NGSI-LD key-values 示例    
下面是一个以 JSON-LD 格式作为键值的 SimulationScenario 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
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
</details>    
#### 模拟情景 NGSI-LD 标准化示例    
下面是一个规范化 JSON-LD 格式的 SimulationScenario 示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
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
          "object": "urn:ngsi-ld:Tank:T1"  
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
          "object": "urn:ngsi-ld:Pattern:Agriculture"  
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
          "object": "urn:ngsi-ld:Pattern:Residential"  
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
