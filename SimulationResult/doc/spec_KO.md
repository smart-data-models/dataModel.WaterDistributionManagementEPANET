<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: SimulationResult    
=====================<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.WaterDistributionManagementEPANET/blob/master/SimulationResult/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **이 엔티티에는 상수도망 관리 도메인에 대해 만들어진 일반 시뮬레이션 결과에 대한 조화로운 설명이 포함되어 있습니다. 이 엔티티는 주로 상수도망 관리 업종 및 관련 IoT 애플리케이션과 연관되어 있습니다.**    
버전: 0.0.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 속성 목록    
<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.    
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.      
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호      
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `demandCategory[object]`: 기본 수요 및 시간 패턴을 다른 사용자 범주에 할당할 수 있습니다.  . Model: [https://schema.org/Text](https://schema.org/Text)	- `baseDemand[string]`: 카테고리의 기준 또는 평균 수요입니다. 속성 수요 카테고리의 하위 속성입니다.  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `demandPattern[*]`: '수요 카테고리' 속성의 패턴과의 관계      
	- `value[number]`: 수요 카테고리의 가치      
- `description[string]`: 이 항목에 대한 설명  - `energyUse[object]`: 네트워크 요소에서 관찰된 에너지 사용량  	- `observedBy`:       
	- `value[number]`: 에너지 사용의 수치적 가치      
- `flow[object]`: 링크의 장치(파이프, 밸브 또는 펌프)에서 측정한 `startsAt` 노드에서 `endsAt` 노드까지의 유량 비율입니다.  	- `observedBy`:       
	- `value[number]`: 흐름의 가치      
- `hasInputNetwork[*]`: 시뮬레이션에 사용된 네트워크의 ID입니다.  . Model: [https://schema.org/URL](https://schema.org/URL)- `head[object]`: 노드에서 관찰된 헤드(정션, 탱크 또는 저수지)  	- `observedBy`:       
	- `value[number]`: 머리의 가치      
- `id[*]`: 엔티티의 고유 식별자  - `initialQuality[object]`: 네트워크 구성 요소의 초기 품질  	- `observedBy`:       
	- `value[number]`: 초기 품질의 수치 값      
- `initialStatus[string]`: 시뮬레이션 시작 시점의 링크 상태입니다. Enum:'OPEN, CLOSED, CV'  . Model: [https://schema.org/Text](https://schema.org/Text)- `level[object]`: 네트워크 요소에서 관찰된 레벨  	- `observedBy`:       
	- `value[number]`: 레벨의 수치 값      
- `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `outputFile[uri]`: 네트워크에 적용된 시뮬레이션 결과가 포함된 바이너리 파일 링크  - `outputParameters[array]`: 네트워크에 적용된 시뮬레이션 결과 집합에 대한 설명  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `pressure[object]`: 노드(접합부, 탱크 또는 저장소)에서 관측된 압력  	- `observedBy`:       
	- `value[number]`: 압력의 수치 값      
- `quality[object]`: 네트워크 구성 요소에서 관찰된 품질  	- `observedBy`:       
	- `value[number]`: 품질에 대한 수치적 가치      
- `refSimulationScenario[*]`: 시뮬레이션 시나리오의 ID  . Model: [https://schema.org/URL](https://schema.org/URL)- `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `sourceCategory[object]`: 특정 노드에서 네트워크에 유입되는 소스 흐름의 품질에 대한 설명  . Model: [https://schema.org/Text](https://schema.org/Text)	- `sourcePattern[*]`: sourceCategory 속성의 패턴에 대한 관계      
	- `sourceQuality[number]`: 소스의 기준선 또는 평균 농도(또는 질량 유량)입니다. 속성 'sourceCategory'의 하위 속성입니다. 모든 단위는 [CEFACT](https://www.unece.org/cefact.html) 코드에서 허용됩니다.  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `sourceType[string]`: Property sourceCategory의 하위 속성입니다.  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `value[string]`: 소스 카테고리의 값      
- `sourceMassInflow[object]`: 노드(정션, 탱크 또는 저수지)에서 관찰된 소스 질량 유입 관찰됨  	- `observedBy`:       
	- `value[number]`: 유입 시 소스 질량의 수치 값      
- `status[string]`: 노드의 동적 상태입니다. Enum:'OPEN, CLOSED, CV'  . Model: [https://schema.org/Text](https://schema.org/Text)- `supply[object]`: 노드(정션, 탱크 또는 저장소)에서 관찰된 공급량  	- `observedBy`:       
	- `value[number]`: 공급의 수치적 가치      
- `tag[string]`: 파이프를 카테고리(예: 연령 또는 재질에 따른 카테고리)에 할당하는 데 사용되는 선택적 텍스트 문자열입니다.  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI-LD 엔티티 유형. SimulationResult여야 합니다.  - `valveCurve[*]`: 밸브가 위치한 커브에 대한 참조  - `valveType[string]`: 밸브 카테고리에 따른 밸브 유형입니다. Enum:'FCV, GPV, PBV, PRV, PSV, TCV'  - `velocity[object]`: 링크(파이프, 밸브 또는 펌프)에서 관찰된 속도  	- `observedBy[uri]`: 속도가 관찰된 위치      
	- `value[number]`: 속도 값      
<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
필수 속성    
- `id`  - `refSimulationScenario`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 속성에 대한 데이터 모델 설명    
알파벳순으로 정렬(자세한 내용을 보려면 클릭)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
SimulationResult:      
  description: This entity contains a harmonised description of a generic simulation result made for the Water Network Management domain. This entity is primarily associated with the water network management vertical and related IoT applications.      
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
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
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
    hasInputNetwork:      
      anyOf:      
        - maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
        - format: uri      
          type: string      
      description: The ID of the network used in the simulation      
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
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    outputFile:      
      description: Link to binary file containing results of applied simulation to the network      
      format: uri      
      type: string      
      x-ngsi:      
        type: Property      
    outputParameters:      
      description: Description of the set of results of applied simulation to the network      
      items:      
        properties:      
          parameter:      
            enum:      
              - demand      
              - energyUse      
              - flow      
              - head      
              - initialQuality      
              - level      
              - pressure      
              - quality      
              - sourceMassInflow      
              - supply      
              - velocity      
              - waterLevel      
            type: string      
          targetURI:      
            anyOf:      
              - maxLength: 256      
                minLength: 1      
                pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
                type: string      
              - format: uri      
                type: string      
          value:      
            anyOf:      
              - type: string      
              - type: number      
              - type: boolean      
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
    refSimulationScenario:      
      anyOf:      
        - maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
        - format: uri      
          type: string      
      description: The ID of the simulation scenario      
      x-ngsi:      
        model: https://schema.org/URL      
        type: Relationship      
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
    type:      
      description: NGSI-LD Entity Type. It has to be SimulationResult      
      enum:      
        - SimulationResult      
      type: string      
      x-ngsi:      
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
  required:      
    - id      
    - type      
    - refSimulationScenario      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.WaterDistributionManagementEPANET/blob/master/SimulationResult/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.WaterDistributionManagementEPANET/Result/schema.json      
  x-model-tags: FIWARE4WATER      
  x-version: 0.0.2      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 페이로드 예시    
#### 시뮬레이션 결과 NGSI-v2 키-값 예시    
다음은 키-값으로 JSON-LD 형식의 SimulationResult의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SimulationResult:01",  
  "type": "SimulationResult",  
  "description": "Free Text",  
  "hasInputNetwork": "urn:ngsi-ld:WaterNetwork:01",  
  "refSimulationScenario": "urn:ngsi-ld:Simulation:01",  
  "outputParameters": [  
    {  
      "parameter": "waterLevel",  
      "value": 50,  
      "targetURI": "urn:ngsi-ld:Valve:V1"  
    },  
    {  
      "parameter": "initialQuality",  
      "value": 2,  
      "targetURI": "urn:ngsi-ld:Tank:T1"  
    }  
  ]  
}  
```  
</details>    
#### SimulationResult NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 SimulationResult의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SimulationResult:01",  
  "type": "SimulationResult",  
  "description": {  
    "type": "Text",  
    "value": "Free Text"  
  },  
  "hasInputNetwork": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:WaterNetwork:01"  
  },  
  "refSimulationScenario": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Simulation:01"  
  },  
  "outputParameters": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "parameter": "waterLevel",  
        "value": 50,  
        "targetURI": "urn:ngsi-ld:Valve:V1"  
      },  
      {  
        "parameter": "initialQuality",  
        "value": 2,  
        "targetURI": "urn:ngsi-ld:Tank:T1"  
      }  
    ]  
  }  
}  
```  
</details>    
#### SimulationResult NGSI-LD 키-값 예시    
다음은 키 값으로 JSON-LD 형식의 SimulationResult의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SimulationResult:01",  
  "type": "SimulationResult",  
  "description": "Free Text",  
  "hasInputNetwork": "urn:ngsi-ld:WaterNetwork:01",  
  "outputFile": "c://epanetsimulations/simulationResult.bin",  
  "outputParameters": [  
    {  
      "parameter": "waterLevel",  
      "value": 50,  
      "targetURI": "urn:ngsi-ld:Valve:V1"  
    },  
    {  
      "parameter": "initialQuality",  
      "value": 2,  
      "targetURI": "urn:ngsi-ld:Tank:T1"  
    }  
  ],  
  "refSimulationScenario": "urn:ngsi-ld:Simulation:01",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.WaterDistributionManagementEPANET/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### SimulationResult NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 SimulationResult의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:SimulationResult:01",  
    "type": "SimulationResult",  
    "description": {  
        "type": "Property",  
        "value": "Free Text"  
    },  
    "hasInputNetwork": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:WaterNetwork:01"  
    },  
    "outputFile": [  
        {  
            "type": "Relationship",  
            "object": "c://epanetsimulations/simulationResult.bin"  
        }  
    ],  
    "refSimulationScenario": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Simulation:01"  
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
