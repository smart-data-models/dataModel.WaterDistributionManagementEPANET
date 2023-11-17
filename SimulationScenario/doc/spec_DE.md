<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: SimulationScenario    
===========================<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.WaterDistributionManagementEPANET/blob/master/SimulationScenario/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Globale Beschreibung: **Diese Einheit enthält eine harmonisierte Beschreibung eines generischen Simulationsszenarios für den Bereich der Wassernetzverwaltung. Diese Entität ist in erster Linie mit der vertikalen Wassernetzverwaltung und damit verbundenen IoT-Anwendungen verbunden.**    
Version: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste der Eigenschaften    
<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.    
- `accuracy[number]`: Konvergenzkriterium für die gesamte normalisierte Durchflussänderung zur Bestimmung, wann eine hydraulische Lösung erreicht ist  . Model: [https://schema.org/Number](https://schema.org/Number)- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel, Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Land liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.      
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `bulkOrder[number]`: Reaktionsauftrag für Rohre in loser Schüttung  . Model: [https://schema.org/Number](https://schema.org/Number)- `checkFrequency[number]`: Häufigkeit der Kontrollen des hydraulischen Zustands  . Model: [https://schema.org/Number](https://schema.org/Number)- `chemicalName[string]`: Name der modellierten Chemikalie. Nur verwendet, wenn "qualityType" CHEM ist  . Model: [https://schema.org/Text](https://schema.org/Text)- `chemicalUnits[string]`: Einheiten der modellierten Chemikalie. Nur verwendet, wenn 'qualityType' CHEM ist  . Model: [https://schema.org/Text](https://schema.org/Text)- `concentrationLimit[number]`: Grenzkonzentration für Wachstumsreaktionen  . Model: [https://schema.org/Number](https://schema.org/Number)- `createdBy[*]`: Die ID desjenigen, der die Simulation erstellt/ausgelöst hat. Verweis auf eine Entität des Typs "Benutzer".  . Model: [https://schema.org/URL](https://schema.org/URL)- `dampLimit[number]`: Genauigkeitswert, bei dem die Lösungsdämpfung und die Statusprüfungen für PRVs und PSVs beginnen  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `demandCategory[object]`: Ermöglicht die Zuordnung von Basisanforderungen und Zeitmustern zu anderen Nutzerkategorien  . Model: [https://schema.org/Text](https://schema.org/Text)	- `baseDemand[string]`: Grundlegende oder durchschnittliche Nachfrage für die Kategorie. Eine Untereigenschaft der Eigenschaft demandCategory  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `demandPattern[*]`: Eine Beziehung zu dem Muster der Eigenschaft "demandCategory".      
- `demandCharge[number]`: Energiekosten pro maximalem kW Verbrauch  . Model: [https://schema.org/Number](https://schema.org/Number)- `demandModel[string]`: Gibt an, ob die Analyse druckgesteuert (PDA) oder bedarfsgesteuert (DDA) ist. Enum:'DDA, PDA'  . Model: [https://schema.org/Text](https://schema.org/Text)- `description[string]`: Eine Beschreibung dieses Artikels  - `diffusivity[number]`: Molekulare Diffusivität der in einer Qualitätsanalyse analysierten Chemikalie, bezogen auf die Diffusivität von Chlor in Wasser  . Model: [https://schema.org/Number](https://schema.org/Number)- `duration[number]`: Dauer der Simulation, angegeben in Sekunden  . Model: [https://schema.org/Number](https://schema.org/Number)- `emitterExponent[number]`: Leistung, um die der Druck an einer Verbindungsstelle erhöht wird, wenn von einem Emitter aus gerechnet wird  . Model: [https://schema.org/Number](https://schema.org/Number)- `energyUse[object]`: Beobachteter Energieverbrauch durch das Element des Netzes  	- `observedBy`:       
- `flow[object]`: Durchflussmenge vom Knoten `startsAt` zum Knoten `endsAt`, gemessen von einem Gerät an der Verbindung (Rohr, Ventil oder Pumpe)  	- `observedBy`:       
- `flowChange[number]`: Konvergenzkriterium der maximalen Durchflussänderung zur Bestimmung, wann eine hydraulische Lösung erreicht ist  . Model: [https://schema.org/Number](https://schema.org/Number)- `flowUnits[string]`: Einheiten, in denen die Durchflussmengen in der Simulation ausgedrückt werden. Zulässige Optionen sind CFS (Kubikfuß pro Sekunde), GPM (Gallonen pro Minute), MGD (Millionen Gallonen pro Tag), IMGD (Imperial MGD), AFD (Acre-feet pro Tag), LPS (Liter pro Sekunde), LPM (Liter pro Minute), MLD (Millionen Liter pro Tag), CMH (Kubikmeter pro Stunde) und CMD (Kubikmeter pro Tag). Enum:'AFD, CFS, CMD, CMH, GPM, IMGD, LPS, LPM, MLD, MGD'  . Model: [https://schema.org/Text](https://schema.org/Text)- `hasInputNetwork[*]`: Die ID des in der Simulation verwendeten Netzes  . Model: [https://schema.org/URL](https://schema.org/URL)- `hasSimulationResult[*]`: Die ID des zugehörigen Simulationsergebnisses. Verweis auf eine Entität des Typs "SimulationResult".  . Model: [https://schema.org/URL](https://schema.org/URL)- `head[object]`: Beobachtete Förderhöhe am Knotenpunkt (Kreuzung, Tank oder Reservoir)  	- `observedBy`:       
- `headError[number]`: Konvergenzkriterium für den maximalen Druckverlust zur Bestimmung, wann eine hydraulische Lösung erreicht ist  . Model: [https://schema.org/Number](https://schema.org/Number)- `headlossFormula[string]`: Formel zur Berechnung des Druckverlustes beim Durchfluss durch ein Rohr. Zur Auswahl stehen die Formeln Hazen-Williams (H-W), Darcy-Weisbach (D-W) oder Chezy-Manning (C-M). Zulässige Optionen sind 'H-W', 'D-W', 'C-M'. Enum:'C-M, D-W, H-W'  . Model: [https://schema.org/Text](https://schema.org/Text)- `hydraulicTimeStep[number]`: Legt fest, wie oft der hydraulische Zustand des Netzes berechnet wird. Angabe in Sekunden  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Eindeutiger Bezeichner der Entität  - `initialQuality[object]`: Anfangsqualität der Netzkomponente  	- `observedBy`:       
- `initialStatus[string]`: Der Verbindungsstatus zu Beginn der Simulation. Enum:'OPEN, CLOSED, CV'  . Model: [https://schema.org/Text](https://schema.org/Text)- `inputParameter[array]`: Beschreibung der für die Simulation am Netz vorzunehmenden Änderungen  . Model: [https://Text](https://Text)- `level[object]`: Beobachteter Pegel in dem Element des Netzes  	- `observedBy`:       
- `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `maxCheck[number]`: Anzahl der Versuche, nach denen die Statusprüfungen eingestellt werden  . Model: [https://schema.org/Number](https://schema.org/Number)- `minimumPressure[number]`: Druck, unter dem im Rahmen einer Drucklenkungsanalyse keine Leistung erbracht werden kann. Wird nur verwendet, wenn demandModel 'PDA' ist.  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: Der Name dieses Artikels  - `operationalControl[array]`: Die operative Kontrolle von de item  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `patternStart[date-time]`: Startzeitpunkt der Simulation  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `patternStep[number]`: Musterschritt der Simulation  . Model: [https://schema.org/Number](https://schema.org/Number)- `pressure[object]`: Beobachteter Druck am Knotenpunkt (Verbindungsstelle, Tank oder Reservoir)  	- `observedBy`:       
- `pressureExponent[number]`: Leistung, auf die der Druck bei der Berechnung des gelieferten Bedarfs im Rahmen einer druckabhängigen Analyse erhöht wird. Nur verwendet, wenn demandModel 'PDA' ist  . Model: [https://schema.org/Number](https://schema.org/Number)- `quality[object]`: Beobachtete Qualität in der Netzkomponente  	- `observedBy`:       
- `qualityTimeStep[number]`: Der Zeitschritt, der verwendet wird, um Änderungen der Wasserqualität im Netz zu verfolgen. Angegeben in Sekunden  . Model: [https://schema.org/Number](https://schema.org/Number)- `qualityType[string]`: Art der Wasserqualitätsanalyse. Enum:'chem, Alter, Spur, keine'  . Model: [https://schema.org/Text](https://schema.org/Text)- `reportStart[number]`: Simulationszeitpunkt, ab dem die Ergebnisse gemeldet werden sollen. Angabe in Sekunden ab Beginn der Simulation  . Model: [https://schema.org/Number](https://schema.org/Number)- `reportStep[number]`: Intervall, in dem die Ausgabeergebnisse gemeldet werden, angegeben in Sekunden  . Model: [https://schema.org/Number](https://schema.org/Number)- `requiredPressure[number]`: Druck, der erforderlich ist, um den vollen Bedarf eines Knotens im Rahmen einer druckgesteuerten Analyse zu decken. Wird nur verwendet, wenn demandModel 'PDA' ist.  . Model: [https://schema.org/Number](https://schema.org/Number)- `ruleTimeStep[number]`: Zeitschritt, der verwendet wird, um Änderungen des Systemstatus aufgrund von regelbasierten Kontrollen zu überprüfen. Angabe in Sekunden  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `sourceCategory[object]`: Beschreibung der Qualität des Quellstroms, der an einem bestimmten Knoten in das Netz eintritt  . Model: [https://schema.org/Text](https://schema.org/Text)	- `sourcePattern[*]`: Eine Beziehung zu dem Muster der Eigenschaft sourceCategory      
	- `sourceQuality[number]`: Ausgangs- oder Durchschnittskonzentration (oder Massendurchsatz) der Quelle. Eine Untereigenschaft der Eigenschaft "sourceCategory". Alle Einheiten werden im [CEFACT](https://www.unece.org/cefact.html)-Code akzeptiert  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `sourceType[string]`: Eine Untereigenschaft der Eigenschaft sourceCategory  . Model: [https://schema.org/Text](https://schema.org/Text)    
- `sourceMassInflow[object]`: Beobachteter Massezufluss der Quelle am Knotenpunkt (Knotenpunkt, Tank oder Reservoir)  	- `observedBy`:       
- `specificGravity[number]`: Das Verhältnis der Dichte der zu modellierenden Flüssigkeit zu der von Wasser bei 4 Grad Celsius. C  . Model: [https://schema.org/Number](https://schema.org/Number)- `startClockTime[number]`: Tageszeit, zu der die Simulation beginnt. Angegeben in Sekunden vom Tagesbeginn an  . Model: [https://schema.org/Number](https://schema.org/Number)- `statistic[string]`: Die Art der statistischen Nachbearbeitung, die für die erzeugten Zeitreihen der Simulationsergebnisse durchgeführt wird. Die Optionen sind AVERAGED (Bericht über die über die Zeit gemittelten Ergebnisse), MINIMUM (Bericht nur über die Minimalwerte), MAXIMUM (Bericht nur über die Maximalwerte), RANGE (Bericht über die Differenz zwischen Minimal- und Maximalwerten) und NONE (Bericht über die gesamte Zeitreihe). Enum:'gemittelt, minimal, maximal, Bereich, keine'  . Model: [https://schema.org/string](https://schema.org/string)- `status[string]`: Der dynamische Zustand des Knotens. Enum:'OPEN, CLOSED, CV'  . Model: [https://schema.org/Text](https://schema.org/Text)- `supply[object]`: Beobachtete Versorgung am Knotenpunkt (Anschlussstelle, Tank oder Reservoir)  	- `observedBy`:       
- `tag[string]`: Eine optionale Textzeichenfolge, die verwendet wird, um das Rohr einer Kategorie zuzuordnen, z. B. auf der Grundlage von Alter oder Material  . Model: [https://schema.org/Text](https://schema.org/Text)- `tankOrder[number]`: Schüttgutreaktionsauftrag für Tanks  . Model: [https://schema.org/Number](https://schema.org/Number)- `tolerance[number]`: Toleranz der Wasserqualität  . Model: [https://schema.org/Number](https://schema.org/Number)- `traceNodeID[*]`: URI des Knotens, der in der Qualitätsanalyse nachverfolgt wird. Obligatorisch, wenn "qualityType" TRACE ist, sonst nicht erforderlich  . Model: [https://schema.org/URL](https://schema.org/URL)- `trials[number]`: Die maximale Anzahl von Versuchen, die zur Lösung der Netzhydraulik bei jedem hydraulischen Zeitschritt einer Simulation verwendet werden  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI-LD-Entitätstyp. Es muss SimulationScenario sein  - `unbalanced[string]`: Legt fest, was geschieht, wenn eine hydraulische Lösung nicht innerhalb der zulässigen Anzahl von Versuchen erreicht werden kann. Zulässige Optionen sind STOP (Anhalten der Analyse), CONTINUE (Fortsetzung der Analyse mit einer Warnmeldung) und CONTINUE_N (Fortsetzung für weitere N Versuche, wobei der Wert von N durch 'unbalancedN' gegeben ist). Enum:'stop, continue, continue_N'  . Model: [https://schema.org/Text](https://schema.org/Text)- `unbalancedN[number]`: Anzahl der zulässigen zusätzlichen Versuche, wenn 'unbalanced' auf continue_N gesetzt ist. Obligatorisch, wenn "unbalanced" auf continue_N gesetzt ist, sonst nicht erforderlich  . Model: [https://schema.org/Number](https://schema.org/Number)- `valveCurve[*]`: Hinweis auf die Kurve, in der sich das Ventil befindet  - `valveType[string]`: Typ des Ventils nach Ventilkategorien. Enum:'FCV, GPV, PBV, PRV, PSV, TCV'  - `velocity[object]`: Beobachtete Geschwindigkeit in der Verbindung (Rohr, Ventil oder Pumpe)  	- `observedBy[uri]`: Wenn die Geschwindigkeit beobachtet wurde      
- `viscosity[number]`: Die kinematische Viskosität der zu modellierenden Flüssigkeit im Verhältnis zu der von Wasser bei 20 Grad Celsius. C  . Model: [https://schema.org/Number](https://schema.org/Number)- `wallOrder[number]`: Wandreaktionsordnung für Rohre  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Erforderliche Eigenschaften    
- `hasInputNetwork`  - `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Datenmodell Beschreibung der Eigenschaften    
Alphabetisch sortiert (für Details anklicken)    
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
## Beispiel-Nutzlasten    
#### SimulationScenario NGSI-v2 Schlüsselwerte Beispiel    
Hier ist ein Beispiel für ein SimulationScenario im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
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
#### SimulationsSzenario NGSI-v2 normalisiert Beispiel    
Hier ist ein Beispiel für ein SimulationScenario im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
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
#### SimulationsSzenario NGSI-LD Schlüsselwerte Beispiel    
Hier ist ein Beispiel für ein SimulationScenario im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
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
#### SimulationSzenario NGSI-LD normalisiert Beispiel    
Hier ist ein Beispiel für ein SimulationScenario im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
