Entité : Scénario de simulation  
===============================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.WaterNetworkManagement/blob/master/SimulationScenario/LICENSE.md)  
Description globale : **Cette entité contient une description harmonisée d'un scénario de simulation générique réalisé pour le domaine de la gestion des réseaux d'eau. Cette entité est principalement associée à la gestion verticale des réseaux d'eau et aux applications IdO connexes.**  

## Liste des biens  

- `accuracy`: Critère de convergence de la variation du débit total normalisé pour déterminer quand une solution hydraulique a été atteinte.  - `address`: L'adresse postale  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `bulkOrder`: Ordre de réaction de l'eau en vrac pour les tuyaux  - `checkFrequency`: Fréquence des contrôles de l'état hydraulique  - `chemicalName`: Nom du produit chimique modélisé. Utilisé uniquement si "qualityType" est CHEM  - `chemicalUnits`: Modélisation des unités de la substance chimique. Utilisé uniquement si le "qualityType" est CHEM  - `concentrationLimit`: Limitation de la concentration pour les réactions de croissance  - `createdBy`: L'identifiant de la personne qui a créé/déclenché la simulation. La référence à une entité de type "utilisateur".  - `dampLimit`: Valeur de précision à laquelle l'amortissement de la solution et les contrôles d'état commencent pour les PRV et les PSV.  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `demandCharge`: Charge d'énergie par utilisation maximale de kW.  - `demandModel`: Précise si l'analyse est axée sur la pression (PDA) ou sur la demande (DDA). Enum : "DDA, PDA".  - `description`: Une description de cet article  - `diffusivity`: Diffusion moléculaire du produit chimique analysé dans une analyse de qualité, par rapport à la diffusivité du chlore dans l'eau.  - `duration`: Durée de la simulation, exprimée en secondes  - `emitterExponent`: Puissance à laquelle la pression à une jonction est augmentée lors du calcul à partir d'un émetteur.  - `flowChange`: Critère de convergence de la variation maximale du débit pour déterminer quand une solution hydraulique a été atteinte.  - `flowUnits`: Unités dans lesquelles les débits sont exprimés dans la simulation. Les options autorisées sont CFS (pieds cubes par seconde), GPM (gallons par minute), MGD (million de gallons par jour), IMGD (MGD impérial), AFD (acre-pieds par jour), LPS (litres avant seconde), LPM (litres par minute), MLD (million de litres par jour), CMH (mètres cubes par heure) et CMD (mètres cubes par jour). Enum : "AFD, CFS, CMD, CMH, GPM, IMGD, LPS, LPM, MLD, MGD".  - `hasInputNetwork`: L'identifiant du réseau utilisé dans la simulation  - `hasSimulationResult`: L'ID du résultat de la simulation correspondante. Référence à une entité de type "SimulationResult".  - `headError`: Critère de convergence de la perte de charge maximale pour déterminer quand une solution hydraulique a été atteinte.  - `headlossFormula`: Formule utilisée pour calculer la perte de charge pour un écoulement dans un tuyau. Les choix sont les formules de Hazen-Williams (H-W), Darcy-Weisbach (D-W) ou Chezy-Manning (C-M). Les options autorisées sont "H-W", "D-W", "C-M". Enumération : "C-M, D-W, H-W".  - `hydraulicTimeStep`: Détermine la fréquence à laquelle l'état hydraulique du réseau est calculé. Donné en secondes  - `id`: Identifiant unique de l'entité  - `inputParameter`: Description de l'ensemble des modifications à appliquer au réseau pour la simulation  - `location`:   - `maxCheck`: Nombre d'essais après lesquels les contrôles de statut sont interrompus  - `minimumPressure`: Pression en dessous de laquelle aucune demande ne peut être satisfaite selon une analyse de la pression. Utilisé uniquement si le modèle de demande est un "PDA".  - `name`: Le nom de cet article.  - `operationalControl`: Le contrôle opérationnel de l'article  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `patternStart`: Heure de début de la simulation.  - `patternStep`: Pas de modèle de la simulation.  - `pressureExponent`: Puissance à laquelle la pression est augmentée lors du calcul de la demande fournie dans le cadre d'une analyse axée sur la pression. Utilisé uniquement si le modèle de demande est un "PDA".  - `qualityTimeStep`: Le pas de temps utilisé pour suivre l'évolution de la qualité de l'eau dans le réseau. Donné en secondes  - `qualityType`: Type d'analyse de la qualité de l'eau. Enum : "chimie, âge, trace, aucune".  - `reportStart`: Moment de la simulation où les résultats commencent à être communiqués. Donné en secondes à partir du début de la simulation  - `reportStep`: Intervalle auquel les résultats de la production sont communiqués. donné en secondes  - `requiredPressure`: Pression requise pour satisfaire la demande totale d'un nœud dans le cadre d'une analyse axée sur la pression. Utilisé uniquement si le modèle de demande est un "PDA".  - `ruleTimeStep`: Pas de temps utilisé pour vérifier les changements de statut du système dus aux contrôles basés sur des règles. Donné en secondes  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `specificGravity`: Le rapport entre la densité du fluide modélisé et celle de l'eau à 4 degrés. C  - `startClockTime`: Heure à laquelle la simulation commence. Indiquée en secondes à partir du début de la journée  - `statistic`: Le type de post-traitement statistique qui est effectué sur les séries chronologiques des résultats de simulation générés. Les options sont les suivantes : MOYENNE (déclarer les résultats moyens sur une période donnée), MINIMALE (déclarer uniquement les valeurs minimales), MAXIMALE (déclarer uniquement les valeurs maximales), GAMME (déclarer la différence entre les valeurs minimales et maximales) et AUCUNE (déclarer les séries chronologiques complètes). Enum : "moyenné, minimum, maximum, plage, aucun".  - `tankOrder`: Ordre de réaction à l'eau en vrac pour les réservoirs  - `tolerance`: Tolérance de la qualité de l'eau  - `traceNodeID`: URI du nœud en cours de traçage dans l'analyse de la qualité. Obligatoire si "qualityType" est TRACE, sinon pas nécessaire  - `trials`: Le nombre maximum d'essais utilisés pour résoudre l'hydraulique de réseau à chaque pas de temps hydraulique d'une simulation  - `type`: Type d'entité NGSI-LD. Il doit s'agir de SimulationScenario  - `unbalanced`: Détermine ce qui se passe si une solution hydraulique ne peut être obtenue dans le cadre du nombre d'essais autorisés. Les options autorisées sont STOP (arrêter l'analyse), CONTINUE (continuer l'analyse mais avec un message d'avertissement) et CONTINUE_N (continuer pour un autre essai N, où la valeur de N est donnée par "unbalancedN"). Enumération : "stop, continue, continue_N  - `unbalancedN`: Nombre d'essais supplémentaires autorisés si "déséquilibré" est défini comme suit : continue_N. Obligatoire si "unbalanced" est défini sur continue_N, sinon pas nécessaire.  - `viscosity`: La viscosité cinématique du fluide modélisé par rapport à celle de l'eau à 20 degrés. C  - `wallOrder`: Ordre de réaction des murs pour les tuyaux    
Propriétés requises  
- `hasInputNetwork`  - `id`  - `type`  ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
SimulationScenario:    
  description: 'This entity contains a harmonised description of a generic simulation scenario made for the Water Network Management domain. This entity is primarily associated with the water network management vertical and related IoT applications.'    
  properties:    
    accuracy:    
      description: 'Total normalized flow change convergence criterion for determining when a hydraulic solution has been reached.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
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
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/areaServed'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/adddress    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    bulkOrder:    
      description: 'Bulk water reaction order for pipes'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    checkFrequency:    
      description: 'Frequency of hydraulic status checks'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    chemicalName:    
      description: 'Name of the chemical modelled. Only used if ''qualityType'' is CHEM'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    chemicalUnits:    
      description: 'Units of the chemical modelled. Only used if ''qualityType'' is CHEM'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    concentrationLimit:    
      description: 'Limiting concentration for growth reactions'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    createdBy:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]'|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: 'The ID of who created/triggered the simulation. Reference to an entity of type ''User'''    
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
    dampLimit:    
      description: 'Accuracy value at which solution damping and status checks begin for PRVs and PSVs.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    demandCharge:    
      description: 'Energy charge per maximum kW usage.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    demandModel:    
      description: 'Specifies whether the analysis is pressure driven (PDA) or demand driven (DDA). Enum:''DDA, PDA'''    
      enum:    
        - DDA    
        - PDA    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    description:    
      description: 'A description of this item'    
      type: Property    
    diffusivity:    
      description: 'Molecular diffusivity of the chemical analysed in a quality analysis, relative to diffusivity of chlorine in water.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    duration:    
      description: 'Duration of the simulation, given in seconds'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: seconds    
    emitterExponent:    
      description: 'Power to which pressure at a junction is raised when computing from an emitter.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    flowChange:    
      description: 'Maximum flow change convergence criterion for determining when a hydraulic solution has been reached.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    hasInputNetwork:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]'|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: 'The ID of the network used in the simulation'    
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
    hasSimulationResult:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]'|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: 'The ID of the related simulation result. Reference to an entity of type ''SimulationResult'''    
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
    headError:    
      description: 'Maximum headloss convergence criterion for determining when a hydraulic solution has been reached.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    headlossFormula:    
      description: 'Formula used for computing head loss for flow through a pipe. The choices are the Hazen-Williams (H-W), Darcy-Weisbach (D-W) or Chezy-Manning (C-M) formulas. Allowable options are ''H-W'', ''D-W'', ''C-M''. Enum:''C-M, D-W, H-W'''    
      enum:    
        - H-W    
        - D-W    
        - C-M    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    hydraulicTimeStep:    
      description: 'Determines how often the hydraulic state of the network is calculated. Given in seconds'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
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
      type: Property    
      x-ngsi:    
        model: https://Text    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
      title: 'GeoJSON Geometry'    
    maxCheck:    
      description: 'Number of trials after which status checks are discontinued'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    minimumPressure:    
      description: 'Pressure below which no demand can be delivered under a pressure dirven analysis. Only used if demandModel is ''PDA'''    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    name:    
      description: 'The name of this item.'    
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
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *simulationscenario_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    patternStart:    
      description: 'Start time of the  the simulation.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    patternStep:    
      description: 'Pattern step of the simulation.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    pressureExponent:    
      description: 'Power to which pressure is raised when calculating the demand delivered under a pressure driven analysis. Only used if demandModel is ''PDA'''    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    qualityTimeStep:    
      description: 'The timestep used to track changes in water quality in the network. Given in seconds'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: seconds    
    qualityType:    
      description: 'Type of water quality analysis. Enum:''chem, age, trace, none'''    
      enum:    
        - age    
        - chem    
        - none    
        - trace    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    reportStart:    
      description: 'Simulation time at which results start to be reported. Given in seconds from start of simulation'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: seconds    
    reportStep:    
      description: 'Interval at which output results are reported. given in seconds'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: seconds    
    requiredPressure:    
      description: 'Pressure required to supply a node''s full demand under a pressure driven analysis. Only used if demandModel is ''PDA'''    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    ruleTimeStep:    
      description: 'Time step used to check for changes in system status due to rule-based controls. Given in seconds'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: seconds    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    specificGravity:    
      description: 'The ratio of the density of the fluid being modeled to that of water at 4 deg. C'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    startClockTime:    
      description: 'Time of day at which the simulation begins. Given as seconds from start of day'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: seconds    
    statistic:    
      description: 'The type of statistical post-processing that is done on the time series of simulation results generated. Options are AVERAGED (report time-averaged results), MINIMUM (report only minimum values), MAXIMUM (report only maximum values), RANGE (report difference between minimum and maximum values) and NONE (report full time series). Enum:''averaged, minimum, maximum, range, none'''    
      enum:    
        - averaged    
        - maximum    
        - minimum    
        - none    
        - range    
      type: Property    
      x-ngsi:    
        model: https://schema.org/string    
    tankOrder:    
      description: 'Bulk water reaction order for tanks'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    tolerance:    
      description: 'Water quality tolerance'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    traceNodeID:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]'|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: 'URI of node being traced in the quality analysis. Mandatory if ''qualityType'' is TRACE, otherwise not required'    
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
    trials:    
      description: 'The maximum number of trials used to solve network hydraulics at each hydraulic time step of a simulation'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI-LD Entity Type. It has to be SimulationScenario'    
      enum:    
        - SimulationScenario    
      type: Property    
    unbalanced:    
      description: 'Determines what happens if a hydraulic solution cannot be reached within the allowed number of trials. Allowable options are STOP (halt analysis), CONTINUE (continue analysis but with a warning message) and CONTINUE_N (continue for another N trials, where the value of N is given by ''unbalancedN''). Enum:''stop, continue, continue_N'''    
      enum:    
        - stop    
        - continue    
        - continue_N    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    unbalancedN:    
      description: 'Number of additional trials allowed if ''unbalanced'' is set to continue_N. Mandatory if ''unbalanced'' is set to continue_N, else not required.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    viscosity:    
      description: 'The kinematic viscosity of the fluid being modeled relative to that of water at 20 deg. C'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    wallOrder:    
      description: 'Wall reaction order for pipes'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
  required:    
    - id    
    - type    
    - hasInputNetwork    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### Scénario de simulation NGSI V2 - Exemple de valeurs clés  
Voici un exemple de scénario de simulation en format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
#### Scénario de simulation NGSI V2 normalisé Exemple  
Voici un exemple de scénario de simulation au format JSON tel que normalisé. Il est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
#### Scénario de simulation Valeurs clés de l'INSG-LD Exemple  
Voici un exemple de scénario de simulation en format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
  ],  
  "@context": [  
    "https://schema.lab.fiware.org/ld/context"  
  ]  
}  
```  
#### Scénario de simulation NGSI-LD normalisé Exemple  
Voici un exemple de scénario de simulation au format JSON-LD tel que normalisé. Il est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
        "object": "urn:ngsi-ld:User:u1"  
    },  
    "hasInputNetwork": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:WaterNetwork:01"  
    },  
    "hasSimulationResult": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:SimulationResult:01"  
    },  
    "duration": {  
        "type": "Property",  
        "value": 86400,  
        "unitCode": "SEC"  
    },  
    "hydraulicTimeStep": {  
        "type": "Property",  
        "value": 3600,  
        "unitCode": "SEC"  
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
        "value": 0,  
        "unitCode": "SEC"  
    },  
    "reportStep": {  
        "type": "Property",  
        "value": 3600,  
        "unitCode": "SEC"  
    },  
    "reportStart": {  
        "type": "Property",  
        "value": 0,  
        "unitCode": "SEC"  
    },  
    "ruleTimeStep": {  
        "type": "Property",  
        "value": 900,  
        "unitCode": "SEC"  
    },  
    "statistic": {  
        "type": "Property",  
        "value": "NONE"  
    },  
    "trials": {  
        "type": "Property",  
        "value": 40,  
        "unitCode": "C62"  
    },  
    "accuracy": {  
        "type": "Property",  
        "value": 0.001,  
        "unitCode": "C62"  
    },  
    "tolerance": {  
        "type": "Property",  
        "value": 0.01,  
        "unitCode": "C62"  
    },  
    "emitterExponent": {  
        "type": "Property",  
        "value": 0.5,  
        "unitCode": "C62"  
    },  
    "headError": {  
        "type": "Property",  
        "value": 0,  
        "unitCode": "MTR"  
    },  
    "flowChange": {  
        "type": "Property",  
        "value": 0.01,  
        "unitCode": "MQS"  
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
        "value": 0,  
        "unitCode": "MTR"  
    },  
    "requiredPressure": {  
        "type": "Property",  
        "value": 20,  
        "unitCode": "MTR"  
    },  
    "pressureExponent": {  
        "type": "Property",  
        "value": 0.5,  
        "unitCode": "C62"  
    },  
    "viscosity": {  
        "type": "Property",  
        "value": 1,  
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
    "checkFrequency": {  
        "type": "Property",  
        "value": 2,  
        "unitCode": "C62"  
    },  
    "maxCheck": {  
        "type": "Property",  
        "value": 10,  
        "unitCode": "C62"  
    },  
    "dampLimit": {  
        "type": "Property",  
        "value": 0,  
        "unitCode": "C62"  
    },  
    "diffusivity": {  
        "type": "Property",  
        "value": 1,  
        "unitCode": "C62"  
    },  
    "bulkOrder": {  
        "type": "Property",  
        "value": 1,  
        "unitCode": "C62"  
    },  
    "wallOrder": {  
        "type": "Property",  
        "value": 1,  
        "unitCode": "C62"  
    },  
    "tankOrder": {  
        "type": "Property",  
        "value": 1,  
        "unitCode": "C62"  
    },  
    "concentrationLimit": {  
        "type": "Property",  
        "value": 0,  
        "unitCode": "C62"  
    },  
    "qualityType": {  
        "type": "Property",  
        "value": "CHEM"  
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
        "value": 1,  
        "unitCode": "C62"  
    },  
    "qualityTimeStep": {  
        "type": "Property",  
        "value": 60,  
        "unitCode": "SEC"  
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
    "@context": [  
        "https://schema.lab.fiware.org/ld/context"  
    ]  
}  
```  
