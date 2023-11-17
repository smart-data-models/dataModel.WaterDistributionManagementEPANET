<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entidad: SimulationScenario    
===========================<!-- /10-Header -->    
<!-- 15-License -->    
[Licencia abierta](https://github.com/smart-data-models//dataModel.WaterDistributionManagementEPANET/blob/master/SimulationScenario/LICENSE.md)    
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descripción global: **Esta entidad contiene una descripción armonizada de un escenario de simulación genérico realizado para el dominio de Gestión de Redes de Agua. Esta entidad se asocia principalmente con el vertical de gestión de redes de agua y las aplicaciones IoT relacionadas.**.    
versión: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Lista de propiedades    
<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.    
- `accuracy[number]`: Criterio de convergencia del cambio de caudal total normalizado para determinar cuándo se ha alcanzado una solución hidráulica.  . Model: [https://schema.org/Number](https://schema.org/Number)- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: El país. Por ejemplo, España  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La localidad en la que se encuentra la dirección postal, y que está en la región  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La región en la que se encuentra la localidad, y que está en el país  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distrito es un tipo de división administrativa que, en algunos países, gestiona el gobierno local      
	- `postOfficeBoxNumber[string]`: El número del apartado de correos para las direcciones de apartados postales. Por ejemplo, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: El código postal. Por ejemplo, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: La dirección  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `bulkOrder[number]`: Orden de reacción del agua a granel para tuberías  . Model: [https://schema.org/Number](https://schema.org/Number)- `checkFrequency[number]`: Frecuencia de los controles del estado hidráulico  . Model: [https://schema.org/Number](https://schema.org/Number)- `chemicalName[string]`: Nombre de la sustancia química modelizada. Sólo se utiliza si 'qualityType' es CHEM  . Model: [https://schema.org/Text](https://schema.org/Text)- `chemicalUnits[string]`: Unidades de la sustancia química modelada. Sólo se utiliza si 'qualityType' es CHEM  . Model: [https://schema.org/Text](https://schema.org/Text)- `concentrationLimit[number]`: Concentración límite para las reacciones de crecimiento  . Model: [https://schema.org/Number](https://schema.org/Number)- `createdBy[*]`: El ID de quien creó/desencadenó la simulación. Referencia a una entidad de tipo "Usuario".  . Model: [https://schema.org/URL](https://schema.org/URL)- `dampLimit[number]`: Valor de precisión a partir del cual se inicia la amortiguación de la solución y las comprobaciones de estado para PRV y PSV.  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `demandCategory[object]`: Permite asignar demandas básicas y patrones horarios a otras categorías de usuarios  . Model: [https://schema.org/Text](https://schema.org/Text)	- `baseDemand[string]`: Demanda base o media de la categoría. Subpropiedad de la propiedad demandCategory  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `demandPattern[*]`: Una relación con el patrón de la propiedad "demandCategory      
- `demandCharge[number]`: Tasa energética por consumo máximo de kW  . Model: [https://schema.org/Number](https://schema.org/Number)- `demandModel[string]`: Especifica si el análisis se basa en la presión (PDA) o en la demanda (DDA). Enum:'DDA, PDA'  . Model: [https://schema.org/Text](https://schema.org/Text)- `description[string]`: Descripción de este artículo  - `diffusivity[number]`: Difusividad molecular de la sustancia química analizada en un análisis de calidad, en relación con la difusividad del cloro en el agua.  . Model: [https://schema.org/Number](https://schema.org/Number)- `duration[number]`: Duración de la simulación, en segundos  . Model: [https://schema.org/Number](https://schema.org/Number)- `emitterExponent[number]`: Potencia a la que se eleva la presión en una unión al computar desde un emisor.  . Model: [https://schema.org/Number](https://schema.org/Number)- `energyUse[object]`: Uso de energía observado por el elemento de la red  	- `observedBy`:       
- `flow[object]`: Caudal desde el nodo "inicio" hasta el nodo "fin", medido por un dispositivo situado en el enlace (tubería, válvula o bomba).  	- `observedBy`:       
- `flowChange[number]`: Criterio de convergencia del cambio máximo de caudal para determinar cuándo se ha alcanzado una solución hidráulica  . Model: [https://schema.org/Number](https://schema.org/Number)- `flowUnits[string]`: Unidades en las que se expresan los caudales en la simulación. Las opciones permitidas son CFS (pies cúbicos por segundo), GPM (galones por minuto), MGD (millones de galones por día), IMGD (imperial MGD), AFD (acres-pies por día), LPS (litros por segundo), LPM (litros por minuto), MLD (millones de litros por día), CMH (metros cúbicos por hora) y CMD (metros cúbicos por día). Enum:'AFD, CFS, CMD, CMH, GPM, IMGD, LPS, LPM, MLD, MGD'  . Model: [https://schema.org/Text](https://schema.org/Text)- `hasInputNetwork[*]`: ID de la red utilizada en la simulación  . Model: [https://schema.org/URL](https://schema.org/URL)- `hasSimulationResult[*]`: El ID del resultado de simulación relacionado. Referencia a una entidad de tipo "SimulationResult".  . Model: [https://schema.org/URL](https://schema.org/URL)- `head[object]`: Altura observada en el nodo (cruce, depósito o embalse)  	- `observedBy`:       
- `headError[number]`: Criterio de convergencia de la pérdida de carga máxima para determinar cuándo se ha alcanzado una solución hidráulica  . Model: [https://schema.org/Number](https://schema.org/Number)- `headlossFormula[string]`: Fórmula utilizada para calcular la pérdida de carga para el flujo a través de una tubería. Se puede elegir entre las fórmulas Hazen-Williams (H-W), Darcy-Weisbach (D-W) o Chezy-Manning (C-M). Las opciones permitidas son 'H-W', 'D-W', 'C-M'. Enum:'C-M, D-W, H-W'  . Model: [https://schema.org/Text](https://schema.org/Text)- `hydraulicTimeStep[number]`: Determina la frecuencia con la que se calcula el estado hidráulico de la red. Indicado en segundos  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Identificador único de la entidad  - `initialQuality[object]`: Calidad inicial del componente de red  	- `observedBy`:       
- `initialStatus[string]`: Estado del enlace al inicio de la simulación. Enum:'ABIERTO, CERRADO, CV'  . Model: [https://schema.org/Text](https://schema.org/Text)- `inputParameter[array]`: Descripción del conjunto de modificaciones que se aplicarán a la red para la simulación  . Model: [https://Text](https://Text)- `level[object]`: Nivel observado en el elemento de la red  	- `observedBy`:       
- `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `maxCheck[number]`: Número de pruebas tras las cuales se interrumpen las comprobaciones de estado  . Model: [https://schema.org/Number](https://schema.org/Number)- `minimumPressure[number]`: Presión por debajo de la cual no puede suministrarse ninguna demanda en un análisis de presión dirven. Sólo se utiliza si demandModel es 'PDA'.  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: El nombre de este artículo  - `operationalControl[array]`: El control operativo de de item  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `patternStart[date-time]`: Hora de inicio de la simulación  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `patternStep[number]`: Paso de la simulación  . Model: [https://schema.org/Number](https://schema.org/Number)- `pressure[object]`: Presión observada en el nodo (empalme, depósito o tanque)  	- `observedBy`:       
- `pressureExponent[number]`: Potencia a la que se eleva la presión al calcular la demanda suministrada en un análisis basado en la presión. Sólo se utiliza si demandModel es 'PDA'.  . Model: [https://schema.org/Number](https://schema.org/Number)- `quality[object]`: Calidad observada en el componente de red  	- `observedBy`:       
- `qualityTimeStep[number]`: El paso de tiempo utilizado para seguir los cambios en la calidad del agua en la red. En segundos  . Model: [https://schema.org/Number](https://schema.org/Number)- `qualityType[string]`: Tipo de análisis de la calidad del agua. Enum:'chem, age, trace, none'  . Model: [https://schema.org/Text](https://schema.org/Text)- `reportStart[number]`: Tiempo de simulación a partir del cual se empiezan a notificar los resultados. En segundos desde el inicio de la simulación  . Model: [https://schema.org/Number](https://schema.org/Number)- `reportStep[number]`: Intervalo en el que se informa de los resultados de salida. dado en segundos.  . Model: [https://schema.org/Number](https://schema.org/Number)- `requiredPressure[number]`: Presión necesaria para suministrar toda la demanda de un nodo en un análisis basado en la presión. Sólo se utiliza si demandModel es 'PDA'.  . Model: [https://schema.org/Number](https://schema.org/Number)- `ruleTimeStep[number]`: Paso de tiempo utilizado para comprobar los cambios en el estado del sistema debidos a controles basados en reglas. En segundos  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `sourceCategory[object]`: Descripción de la calidad del flujo de origen que entra en la red en un nodo específico  . Model: [https://schema.org/Text](https://schema.org/Text)	- `sourcePattern[*]`: Una relación con el patrón de la propiedad sourceCategory      
	- `sourceQuality[number]`: Concentración de referencia o media (o caudal másico) de la fuente. Subpropiedad de la propiedad "sourceCategory". Se aceptan todas las unidades en código [CEFACT](https://www.unece.org/cefact.html)  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `sourceType[string]`: Subpropiedad de la propiedad sourceCategory  . Model: [https://schema.org/Text](https://schema.org/Text)    
- `sourceMassInflow[object]`: Entrada de masa de la fuente observada en el nodo (cruce, depósito o embalse)  	- `observedBy`:       
- `specificGravity[number]`: La relación entre la densidad del fluido modelizado y la del agua a 4 deg. C  . Model: [https://schema.org/Number](https://schema.org/Number)- `startClockTime[number]`: Hora del día a la que comienza la simulación. Se indica en segundos a partir del inicio del día  . Model: [https://schema.org/Number](https://schema.org/Number)- `statistic[string]`: Tipo de postprocesamiento estadístico que se realiza sobre las series temporales de resultados de simulación generados. Las opciones son PROMEDIO (resultados promediados en el tiempo), MÍNIMO (sólo valores mínimos), MÁXIMO (sólo valores máximos), RANGO (diferencia entre valores mínimos y máximos) y NINGUNO (serie temporal completa). Enum:'promediado, mínimo, máximo, rango, ninguno'  . Model: [https://schema.org/string](https://schema.org/string)- `status[string]`: Estado dinámico del nodo. Enum:'ABIERTO, CERRADO, CV'  . Model: [https://schema.org/Text](https://schema.org/Text)- `supply[object]`: Suministro observado en el nudo (empalme, depósito o tanque)  	- `observedBy`:       
- `tag[string]`: Cadena de texto opcional utilizada para asignar la tubería a una categoría, quizás una basada en la edad o el material.  . Model: [https://schema.org/Text](https://schema.org/Text)- `tankOrder[number]`: Pedido de reacción de agua a granel para cisternas  . Model: [https://schema.org/Number](https://schema.org/Number)- `tolerance[number]`: Tolerancia de la calidad del agua  . Model: [https://schema.org/Number](https://schema.org/Number)- `traceNodeID[*]`: URI del nodo que se está rastreando en el análisis de calidad. Obligatorio si "qualityType" es TRACE; en caso contrario, no es necesario.  . Model: [https://schema.org/URL](https://schema.org/URL)- `trials[number]`: Número máximo de ensayos utilizados para resolver la hidráulica de red en cada paso de tiempo hidráulico de una simulación.  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Tipo de entidad NGSI-LD. Tiene que ser SimulationScenario  - `unbalanced[string]`: Determina qué ocurre si no se puede alcanzar una solución hidráulica en el número de ensayos permitido. Las opciones permitidas son STOP (detener el análisis), CONTINUE (continuar el análisis pero con un mensaje de advertencia) y CONTINUE_N (continuar durante otros N ensayos, donde el valor de N viene dado por 'unbalancedN'). Enum:'detener, continuar, continuar_N'  . Model: [https://schema.org/Text](https://schema.org/Text)- `unbalancedN[number]`: Número de pruebas adicionales permitidas si "desequilibrado" se establece en continue_N. Obligatorio si 'unbalanced' se establece en continue_N, de lo contrario no es necesario.  . Model: [https://schema.org/Number](https://schema.org/Number)- `valveCurve[*]`: Referencia a la curva donde se encuentra la válvula  - `valveType[string]`: Tipo de válvula según las categorías de válvulas. Enum:'FCV, GPV, PBV, PRV, PSV, TCV'  - `velocity[object]`: Velocidad observada en el enlace (tubería, válvula o bomba)  	- `observedBy[uri]`: Donde se ha observado la velocidad      
- `viscosity[number]`: La viscosidad cinemática del fluido que se está modelando en relación con la del agua a 20 deg. C  . Model: [https://schema.org/Number](https://schema.org/Number)- `wallOrder[number]`: Orden de reacción en pared para tuberías  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propiedades requeridas    
- `hasInputNetwork`  - `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Descripción de las propiedades del modelo de datos    
Ordenados alfabéticamente (pulse para más detalles)    
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
## Ejemplo de carga útil    
#### SimulationScenario NGSI-v2 key-values Ejemplo    
Aquí hay un ejemplo de un SimulationScenario en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
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
#### SimulationScenario NGSI-v2 normalizado Ejemplo    
He aquí un ejemplo de un SimulationScenario en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
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
#### SimulationScenario NGSI-LD key-values Ejemplo    
Aquí hay un ejemplo de un SimulationScenario en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
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
#### SimulationScenario NGSI-LD normalizado Ejemplo    
He aquí un ejemplo de un SimulationScenario en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
