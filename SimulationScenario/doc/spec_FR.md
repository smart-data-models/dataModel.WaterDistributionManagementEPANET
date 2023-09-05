<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : SimulationScenario  
===========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.WaterDistributionManagementEPANET/blob/master/SimulationScenario/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Cette entité contient une description harmonisée d'un scénario de simulation générique réalisé pour le domaine de la gestion des réseaux d'eau. Cette entité est principalement associée à la verticale de la gestion des réseaux d'eau et aux applications IoT associées.**  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `accuracy[number]`: Critère de convergence de la variation du débit total normalisé pour déterminer si une solution hydraulique a été atteinte  . Model: [https://schema.org/Number](https://schema.org/Number)- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse postale et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La région dans laquelle se trouve la localité et qui se trouve dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local.    
	- `postOfficeBoxNumber[string]`: Le numéro de la boîte postale pour les adresses de boîtes postales. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `bulkOrder[number]`: Ordre de réaction de l'eau en vrac pour les tuyaux  . Model: [https://schema.org/Number](https://schema.org/Number)- `checkFrequency[number]`: Fréquence des contrôles de l'état hydraulique  . Model: [https://schema.org/Number](https://schema.org/Number)- `chemicalName[string]`: Nom du produit chimique modélisé. Utilisé uniquement si "qualityType" est CHEM  . Model: [https://schema.org/Text](https://schema.org/Text)- `chemicalUnits[string]`: Unités du produit chimique modélisé. Utilisé uniquement si "qualityType" est CHEM  . Model: [https://schema.org/Text](https://schema.org/Text)- `concentrationLimit[number]`: Concentration limite pour les réactions de croissance  . Model: [https://schema.org/Number](https://schema.org/Number)- `createdBy[*]`: L'ID de la personne qui a créé/déclenché la simulation. Référence à une entité de type "Utilisateur  . Model: [https://schema.org/URL](https://schema.org/URL)- `dampLimit[number]`: Valeur de précision à partir de laquelle l'amortissement de la solution et les contrôles d'état commencent pour les PRV et PSV  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `demandCategory[object]`: Permet d'attribuer les demandes de base et les modèles horaires à d'autres catégories d'utilisateurs.  . Model: [https://schema.org/Text](https://schema.org/Text)	- `baseDemand[string]`: Demande de base ou moyenne pour la catégorie. Une sous-propriété de la propriété demandCategory  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `demandPattern[*]`: Une relation avec le modèle de la propriété "demandCategory".    
- `demandCharge[number]`: Frais d'énergie par kW maximum d'utilisation  . Model: [https://schema.org/Number](https://schema.org/Number)- `demandModel[string]`: Précise si l'analyse est axée sur la pression (PDA) ou sur la demande (DDA). Enum : "DDA, PDA  . Model: [https://schema.org/Text](https://schema.org/Text)- `description[string]`: Une description de l'article  - `diffusivity[number]`: Diffusion moléculaire de la substance chimique analysée dans le cadre d'une analyse de qualité, par rapport à la diffusion du chlore dans l'eau  . Model: [https://schema.org/Number](https://schema.org/Number)- `duration[number]`: Durée de la simulation, exprimée en secondes  . Model: [https://schema.org/Number](https://schema.org/Number)- `emitterExponent[number]`: Puissance à laquelle la pression à un point de jonction est augmentée lorsque l'on calcule à partir d'un émetteur  . Model: [https://schema.org/Number](https://schema.org/Number)- `energyUse[object]`: Consommation d'énergie observée par l'élément du réseau  	- `observedBy`:     
- `flow[object]`: Débit du nœud `startsAt` au nœud `endsAt`, mesuré par un dispositif au niveau de la liaison (tuyau, vanne ou pompe).  	- `observedBy`:     
- `flowChange[number]`: Critère de convergence de la variation maximale du débit pour déterminer si une solution hydraulique a été atteinte  . Model: [https://schema.org/Number](https://schema.org/Number)- `flowUnits[string]`: Unités dans lesquelles les débits sont exprimés dans la simulation. Les options autorisées sont les suivantes : CFS (pieds cubes par seconde), GPM (gallons par minute), MGD (millions de gallons par jour), IMGD (MGD impérial), AFD (acre-feet par jour), LPS (litres par seconde), LPM (litres par minute), MLD (millions de litres par jour), CMH (mètres cubes par heure) et CMD (mètres cubes par jour). Enum : "AFD, CFS, CMD, CMH, GPM, IMGD, LPS, LPM, MLD, MGD".  . Model: [https://schema.org/Text](https://schema.org/Text)- `hasInputNetwork[*]`: L'ID du réseau utilisé dans la simulation  . Model: [https://schema.org/URL](https://schema.org/URL)- `hasSimulationResult[*]`: L'identifiant du résultat de simulation concerné. Référence à une entité de type "SimulationResult".  . Model: [https://schema.org/URL](https://schema.org/URL)- `head[object]`: Hauteur de chute observée au nœud (jonction, réservoir)  	- `observedBy`:     
- `headError[number]`: Critère de convergence de perte de charge maximale pour déterminer quand une solution hydraulique a été atteinte  . Model: [https://schema.org/Number](https://schema.org/Number)- `headlossFormula[string]`: Formule utilisée pour calculer la perte de charge pour l'écoulement dans une conduite. Les choix possibles sont les formules Hazen-Williams (H-W), Darcy-Weisbach (D-W) ou Chezy-Manning (C-M). Les options autorisées sont 'H-W', 'D-W', 'C-M'. Enum : 'C-M, D-W, H-W'  . Model: [https://schema.org/Text](https://schema.org/Text)- `hydraulicTimeStep[number]`: Détermine la fréquence de calcul de l'état hydraulique du réseau. Exprimé en secondes  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Identifiant unique de l'entité  - `initialQuality[object]`: Qualité initiale de la composante réseau  	- `observedBy`:     
- `initialStatus[string]`: État de la liaison au début de la simulation. Enum : "OUVERT, FERMÉ, CV  . Model: [https://schema.org/Text](https://schema.org/Text)- `inputParameter[array]`: Description de l'ensemble des modifications à appliquer au réseau pour la simulation  . Model: [https://Text](https://Text)- `level[object]`: Niveau observé dans l'élément du réseau  	- `observedBy`:     
- `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `maxCheck[number]`: Nombre d'essais après lesquels les contrôles d'état sont interrompus  . Model: [https://schema.org/Number](https://schema.org/Number)- `minimumPressure[number]`: Pression en dessous de laquelle aucune demande ne peut être satisfaite dans le cadre d'une analyse des pertes de charge. Uniquement utilisé si demandModel est 'PDA'.  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: Le nom de cet élément  - `operationalControl[array]`: Le contrôle opérationnel du poste  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `patternStart[date-time]`: Heure de début de la simulation  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `patternStep[number]`: Étape de la simulation  . Model: [https://schema.org/Number](https://schema.org/Number)- `pressure[object]`: Pression observée au point nodal (jonction, cuve ou réservoir)  	- `observedBy`:     
- `pressureExponent[number]`: Puissance à laquelle la pression est augmentée lors du calcul de la demande fournie dans le cadre d'une analyse basée sur la pression. Uniquement utilisé si demandModel est "PDA".  . Model: [https://schema.org/Number](https://schema.org/Number)- `quality[object]`: Qualité observée dans la composante réseau  	- `observedBy`:     
- `qualityTimeStep[number]`: Le pas de temps utilisé pour suivre les changements de la qualité de l'eau dans le réseau. Exprimé en secondes  . Model: [https://schema.org/Number](https://schema.org/Number)- `qualityType[string]`: Type d'analyse de la qualité de l'eau. Enum : "chem, age, trace, none" (chimie, âge, traces, aucune)  . Model: [https://schema.org/Text](https://schema.org/Text)- `reportStart[number]`: Heure de simulation à laquelle les résultats commencent à être rapportés. Indiqué en secondes à partir du début de la simulation  . Model: [https://schema.org/Number](https://schema.org/Number)- `reportStep[number]`: Intervalle auquel les résultats de la sortie sont rapportés, en secondes  . Model: [https://schema.org/Number](https://schema.org/Number)- `requiredPressure[number]`: Pression nécessaire pour répondre à la totalité de la demande d'un nœud dans le cadre d'une analyse pilotée par la pression. Uniquement utilisé si demandModel est "PDA".  . Model: [https://schema.org/Number](https://schema.org/Number)- `ruleTimeStep[number]`: Pas de temps utilisé pour vérifier les changements d'état du système dus aux contrôles basés sur des règles. Exprimé en secondes  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `sourceCategory[object]`: Description de la qualité du flux source entrant dans le réseau à un nœud spécifique  . Model: [https://schema.org/Text](https://schema.org/Text)	- `sourcePattern[*]`: Une relation avec le modèle de la propriété sourceCategory    
	- `sourceQuality[number]`: Concentration de base ou moyenne (ou débit massique) de la source. Une sous-propriété de la propriété "sourceCategory". Toutes les unités sont acceptées dans le code [CEFACT] (https://www.unece.org/cefact.html).  . Model: [https://schema.org/Number](https://schema.org/Number)  
	- `sourceType[string]`: Une sous-propriété de la propriété sourceCategory  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `sourceMassInflow[object]`: Débit massique de la source observée au nœud (jonction, cuve ou réservoir)  	- `observedBy`:     
- `specificGravity[number]`: Le rapport entre la densité du fluide modélisé et celle de l'eau à 4 deg. C  . Model: [https://schema.org/Number](https://schema.org/Number)- `startClockTime[number]`: Heure du jour à laquelle la simulation commence. Exprimée en secondes à partir du début de la journée  . Model: [https://schema.org/Number](https://schema.org/Number)- `statistic[string]`: Le type de post-traitement statistique effectué sur la série temporelle des résultats de simulation générés. Les options sont AVERAGED (rapport sur les résultats moyennés dans le temps), MINIMUM (rapport sur les valeurs minimales uniquement), MAXIMUM (rapport sur les valeurs maximales uniquement), RANGE (rapport sur la différence entre les valeurs minimales et maximales) et NONE (rapport sur l'ensemble de la série temporelle). Enum : "average, minimum, maximum, range, none" (moyenne, minimum, maximum, intervalle, aucun)  . Model: [https://schema.org/string](https://schema.org/string)- `status[string]`: État dynamique du nœud. Enum : "OUVERT, FERMÉ, CV  . Model: [https://schema.org/Text](https://schema.org/Text)- `supply[object]`: Approvisionnement observé au nœud (jonction, réservoir ou citerne)  	- `observedBy`:     
- `tag[string]`: Une chaîne de texte facultative utilisée pour classer le tuyau dans une catégorie, par exemple en fonction de l'âge ou du matériau.  . Model: [https://schema.org/Text](https://schema.org/Text)- `tankOrder[number]`: Ordre de réaction de l'eau en vrac pour les réservoirs  . Model: [https://schema.org/Number](https://schema.org/Number)- `tolerance[number]`: Tolérance de la qualité de l'eau  . Model: [https://schema.org/Number](https://schema.org/Number)- `traceNodeID[*]`: URI du nœud faisant l'objet d'un suivi dans le cadre de l'analyse de la qualité. Obligatoire si "qualityType" est TRACE, sinon non requis.  . Model: [https://schema.org/URL](https://schema.org/URL)- `trials[number]`: Le nombre maximum d'essais utilisés pour résoudre l'hydraulique du réseau à chaque pas de temps hydraulique d'une simulation.  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Type d'entité NGSI-LD. Il doit s'agir de SimulationScenario  - `unbalanced[string]`: Détermine ce qui se passe si une solution hydraulique ne peut être atteinte dans le nombre d'essais autorisé. Les options autorisées sont STOP (arrêt de l'analyse), CONTINUE (poursuite de l'analyse mais avec un message d'avertissement) et CONTINUE_N (poursuite pour N essais supplémentaires, où la valeur de N est donnée par 'unbalancedN'). Enum : 'stop, continue, continue_N'  . Model: [https://schema.org/Text](https://schema.org/Text)- `unbalancedN[number]`: Nombre d'essais supplémentaires autorisés si la valeur "unbalanced" est fixée à continue_N. Obligatoire si "unbalanced" est défini sur continue_N, sinon non requis.  . Model: [https://schema.org/Number](https://schema.org/Number)- `valveCurve[*]`: Référence à la courbe où se trouve la vanne  - `valveType[string]`: Type de vanne selon les catégories de vannes. Enum : "FCV, GPV, PBV, PRV, PSV, TCV  - `velocity[object]`: Vitesse observée dans la liaison (tuyau, vanne ou pompe)  	- `observedBy[uri]`: Où la vitesse a été observée    
- `viscosity[number]`: La viscosité cinématique du fluide modélisé par rapport à celle de l'eau à 20 deg. C  . Model: [https://schema.org/Number](https://schema.org/Number)- `wallOrder[number]`: Ordre de réaction des parois pour les tuyaux  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `hasInputNetwork`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modèle de données description des propriétés  
Classés par ordre alphabétique (cliquez pour plus de détails)  
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
## Exemples de charges utiles  
#### SimulationScénario Valeurs clés de l'INSG-v2 Exemple  
Voici un exemple de SimulationScenario au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
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
#### SimulationScénario NGSI-v2 normalisé Exemple  
Voici un exemple de SimulationScenario au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### SimulationScénario Valeurs clés NGSI-LD Exemple  
Voici un exemple de SimulationScenario au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
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
#### SimulationScénario NGSI-LD normalisé Exemple  
Voici un exemple de SimulationScenario au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
