from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, RootModel, constr


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class DemandCategory(BaseModel):
    baseDemand: Optional[str] = Field(
        None,
        description='Baseline or average demand for the category. A sub-property of the Property demandCategory',
    )
    demandPattern: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description="A relationship to the pattern of the 'demandCategory' property",
    )
    value: Optional[float] = Field(None, description='Value of the demand category')


class DemandModel(Enum):
    DDA = 'DDA'
    PDA = 'PDA'


class EnergyUse(BaseModel):
    observedBy: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = None
    value: Optional[float] = Field(
        None, description='Numerical value of the use of Energy'
    )


class Flow(BaseModel):
    observedBy: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = None
    value: Optional[float] = Field(None, description='Value of the flow')


class FlowUnits(Enum):
    AFD = 'AFD'
    CFS = 'CFS'
    CMD = 'CMD'
    CMH = 'CMH'
    GPM = 'GPM'
    IMGD = 'IMGD'
    LPS = 'LPS'
    LPM = 'LPM'
    MLD = 'MLD'
    MGD = 'MGD'


class Head(BaseModel):
    observedBy: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = None
    value: Optional[float] = Field(None, description='Value of the head')


class HeadlossFormula(Enum):
    H_W = 'H-W'
    D_W = 'D-W'
    C_M = 'C-M'


class InitialQuality(BaseModel):
    observedBy: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = None
    value: Optional[float] = Field(
        None, description='Numerical value of the initial quality'
    )


class InitialStatus(Enum):
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'
    CV = 'CV'


class InputParameterItem(BaseModel):
    parameterName: Optional[str] = None
    targetURI: Optional[
        Union[
            constr(
                pattern=r'^[\w\-\.\{\}\$\+\*\[\]\'|~^@!, :\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description='URI of network component with property modified in simulation. A sub-relationship of the Property water attribute',
    )
    value: Optional[Union[str, float, bool]] = None


class Level(BaseModel):
    observedBy: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = None
    value: Optional[float] = Field(None, description='Numerical value of the level')


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class ControlType(Enum):
    HILEVEL = 'HILEVEL'
    LOWLEVEL = 'LOWLEVEL'
    TIMEOFDAY = 'TIMEOFDAY'
    TIMER = 'TIMER'


class OperationalControlItem(BaseModel):
    controlType: Optional[ControlType] = Field(
        None,
        description="Type of trigger for the control. A sub-property of the Property 'control'. Enum:'HILEVEL, LOWLEVEL, TIMEOFDAY, TIMER'",
    )
    controlledLink: Optional[
        Union[
            constr(
                pattern=r'^[\w\-\.\{\}\$\+\*\[\]\'|~^@!, :\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description="Link controlled. A sub-relationship of the Property 'control'. Reference to an entity of type 'Pipe', 'Pump' or 'Valve'",
    )
    monitoredNode: Optional[
        Union[
            constr(
                pattern=r'^[\w\-\.\{\}\$\+\*\[\]\'|~^@!, :\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description="Node which is monitored for control trigger level. A sub-relationship of the Property 'control'.  Reference to an entity of type 'Junction', 'Tank' or 'Reservoir'",
    )
    setting: Optional[float] = Field(
        None,
        description="Setting applied in the to the controlled link when trigger level is reached. A sub-property of the Property 'control'",
    )
    triggerLevel: Optional[float] = Field(
        None,
        description="Level at which control is activated. A sub-property of the Property 'control'",
    )
    type: Optional[str] = Field(
        None,
        description="Description of a control applied to the network for the simulation. Enum:'controlledLink, controlType, monitoredNode, setting, triggerLevel'",
    )


class Pressure(BaseModel):
    observedBy: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = None
    value: Optional[float] = Field(None, description='Numerical value of the pressure')


class Quality(BaseModel):
    observedBy: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = None
    value: Optional[float] = Field(None, description='Numerical value of the quality')


class QualityType(Enum):
    age = 'age'
    chem = 'chem'
    none = 'none'
    trace = 'trace'


class SourceType(Enum):
    CONCEN = 'CONCEN'
    MASS = 'MASS'
    FLOWPACED = 'FLOWPACED'
    SETPOINT = 'SETPOINT'


class SourceCategory(BaseModel):
    sourcePattern: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None, description='A relationship to the pattern pf the sourceCategory property'
    )
    sourceQuality: Optional[float] = Field(
        None,
        description="Baseline or average concentration (or mass flow rate) of source. A sub-property of the Property 'sourceCategory'. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code",
    )
    sourceType: Optional[SourceType] = Field(
        None, description='A sub-property of the Property sourceCategory'
    )
    value: Optional[str] = Field(None, description='Value of the source category')


class SourceMassInflow(BaseModel):
    observedBy: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = None
    value: Optional[float] = Field(
        None, description='Numerical value of the source mass at the inflow'
    )


class Statistic(Enum):
    averaged = 'averaged'
    maximum = 'maximum'
    minimum = 'minimum'
    none = 'none'
    range = 'range'


class Status(Enum):
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'
    CV = 'CV'


class Supply(BaseModel):
    observedBy: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = None
    value: Optional[float] = Field(None, description='Numerical value of the supply')


class Type6(Enum):
    SimulationScenario = 'SimulationScenario'


class Unbalanced(Enum):
    stop = 'stop'
    continue_ = 'continue'
    continue_N = 'continue_N'


class ValveType(Enum):
    FCV = 'FCV'
    GPV = 'GPV'
    PBV = 'PBV'
    PRV = 'PRV'
    PSV = 'PSV'
    TCV = 'TCV'


class Velocity(BaseModel):
    observedBy: Optional[AnyUrl] = Field(
        None, description='Where the velocity has been observed'
    )
    value: Optional[float] = Field(None, description='Value of the velocity')


class SimulationScenario(BaseModel):
    accuracy: Optional[float] = Field(
        None,
        description='Total normalized flow change convergence criterion for determining when a hydraulic solution has been reached',
    )
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    bulkOrder: Optional[float] = Field(
        None, description='Bulk water reaction order for pipes'
    )
    checkFrequency: Optional[float] = Field(
        None, description='Frequency of hydraulic status checks'
    )
    chemicalName: Optional[str] = Field(
        None,
        description="Name of the chemical modelled. Only used if 'qualityType' is CHEM",
    )
    chemicalUnits: Optional[str] = Field(
        None,
        description="Units of the chemical modelled. Only used if 'qualityType' is CHEM",
    )
    concentrationLimit: Optional[float] = Field(
        None, description='Limiting concentration for growth reactions'
    )
    createdBy: Optional[
        Union[
            constr(
                pattern=r'^[\w\-\.\{\}\$\+\*\[\]\'|~^@!, :\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description="The ID of who created/triggered the simulation. Reference to an entity of type 'User'",
    )
    dampLimit: Optional[float] = Field(
        None,
        description='Accuracy value at which solution damping and status checks begin for PRVs and PSVs',
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    demandCategory: Optional[DemandCategory] = Field(
        None,
        description='Allows base demands and time patterns to be assigned to other categories of users',
    )
    demandCharge: Optional[float] = Field(
        None, description='Energy charge per maximum kW usage'
    )
    demandModel: Optional[DemandModel] = Field(
        None,
        description="Specifies whether the analysis is pressure driven (PDA) or demand driven (DDA). Enum:'DDA, PDA'",
    )
    description: Optional[str] = Field(None, description='A description of this item')
    diffusivity: Optional[float] = Field(
        None,
        description='Molecular diffusivity of the chemical analysed in a quality analysis, relative to diffusivity of chlorine in water',
    )
    duration: Optional[float] = Field(
        None, description='Duration of the simulation, given in seconds'
    )
    emitterExponent: Optional[float] = Field(
        None,
        description='Power to which pressure at a junction is raised when computing from an emitter',
    )
    energyUse: Optional[EnergyUse] = Field(
        None, description='Observed energy use by the element of the network'
    )
    flow: Optional[Flow] = Field(
        None,
        description='Rate of flow from `startsAt` node to `endsAt` node, measured by a device at the link (pipe, valve or pump)',
    )
    flowChange: Optional[float] = Field(
        None,
        description='Maximum flow change convergence criterion for determining when a hydraulic solution has been reached',
    )
    flowUnits: Optional[FlowUnits] = Field(
        None,
        description="Units in which flow rates are expressed in the simulation. Allowable options are CFS (cubic feet per second), GPM (gallons per minute), MGD (million gallons per day), IMGD (imperial MGD), AFD (acre-feet per day), LPS (litres pre second), LPM (litres per minute), MLD (million litres per day), CMH (cubic metres per hour) and CMD (cubic metres per day). Enum:'AFD, CFS, CMD, CMH, GPM, IMGD, LPS, LPM, MLD, MGD'",
    )
    hasInputNetwork: Optional[
        Union[
            constr(
                pattern=r'^[\w\-\.\{\}\$\+\*\[\]\'|~^@!, :\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='The ID of the network used in the simulation')
    hasSimulationResult: Optional[
        Union[
            constr(
                pattern=r'^[\w\-\.\{\}\$\+\*\[\]\'|~^@!, :\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description="The ID of the related simulation result. Reference to an entity of type 'SimulationResult'",
    )
    head: Optional[Head] = Field(
        None, description='Observed head at the node (junction, tank or reservoir)'
    )
    headError: Optional[float] = Field(
        None,
        description='Maximum headloss convergence criterion for determining when a hydraulic solution has been reached',
    )
    headlossFormula: Optional[HeadlossFormula] = Field(
        None,
        description="Formula used for computing head loss for flow through a pipe. The choices are the Hazen-Williams (H-W), Darcy-Weisbach (D-W) or Chezy-Manning (C-M) formulas. Allowable options are 'H-W', 'D-W', 'C-M'. Enum:'C-M, D-W, H-W'",
    )
    hydraulicTimeStep: Optional[float] = Field(
        None,
        description='Determines how often the hydraulic state of the network is calculated. Given in seconds',
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    initialQuality: Optional[InitialQuality] = Field(
        None, description='Initial quality in the network component'
    )
    initialStatus: Optional[InitialStatus] = Field(
        None,
        description="The link status at the start of the simulation. Enum:'OPEN, CLOSED, CV'",
    )
    inputParameter: Optional[List[InputParameterItem]] = Field(
        None,
        description='Description of the set of modifications to be applied to the network for the simulation',
    )
    level: Optional[Level] = Field(
        None, description='Observed level in the element of the network'
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    maxCheck: Optional[float] = Field(
        None, description='Number of trials after which status checks are discontinued'
    )
    minimumPressure: Optional[float] = Field(
        None,
        description="Pressure below which no demand can be delivered under a pressure dirven analysis. Only used if demandModel is 'PDA'",
    )
    name: Optional[str] = Field(None, description='The name of this item')
    operationalControl: Optional[List[OperationalControlItem]] = Field(
        None, description='The operational control of de item'
    )
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    patternStart: Optional[AwareDatetime] = Field(
        None, description='Start time of the  the simulation'
    )
    patternStep: Optional[float] = Field(
        None, description='Pattern step of the simulation'
    )
    pressure: Optional[Pressure] = Field(
        None, description='Observed pressure at the node (junction, tank or reservoir)'
    )
    pressureExponent: Optional[float] = Field(
        None,
        description="Power to which pressure is raised when calculating the demand delivered under a pressure driven analysis. Only used if demandModel is 'PDA'",
    )
    quality: Optional[Quality] = Field(
        None, description='Observed quality in the network component'
    )
    qualityTimeStep: Optional[float] = Field(
        None,
        description='The timestep used to track changes in water quality in the network. Given in seconds',
    )
    qualityType: Optional[QualityType] = Field(
        None,
        description="Type of water quality analysis. Enum:'chem, age, trace, none'",
    )
    reportStart: Optional[float] = Field(
        None,
        description='Simulation time at which results start to be reported. Given in seconds from start of simulation',
    )
    reportStep: Optional[float] = Field(
        None,
        description='Interval at which output results are reported. given in seconds',
    )
    requiredPressure: Optional[float] = Field(
        None,
        description="Pressure required to supply a node's full demand under a pressure driven analysis. Only used if demandModel is 'PDA'",
    )
    ruleTimeStep: Optional[float] = Field(
        None,
        description='Time step used to check for changes in system status due to rule-based controls. Given in seconds',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    sourceCategory: Optional[SourceCategory] = Field(
        None,
        description='Description of the quality of source flow entering the network at a specific node',
    )
    sourceMassInflow: Optional[SourceMassInflow] = Field(
        None,
        description='Observed source mass inflow at the node (junction, tank or reservoir)',
    )
    specificGravity: Optional[float] = Field(
        None,
        description='The ratio of the density of the fluid being modeled to that of water at 4 deg. C',
    )
    startClockTime: Optional[float] = Field(
        None,
        description='Time of day at which the simulation begins. Given as seconds from start of day',
    )
    statistic: Optional[Statistic] = Field(
        None,
        description="The type of statistical post-processing that is done on the time series of simulation results generated. Options are AVERAGED (report time-averaged results), MINIMUM (report only minimum values), MAXIMUM (report only maximum values), RANGE (report difference between minimum and maximum values) and NONE (report full time series). Enum:'averaged, minimum, maximum, range, none'",
    )
    status: Optional[Status] = Field(
        None, description="The dynamic state of the node. Enum:'OPEN, CLOSED, CV'"
    )
    supply: Optional[Supply] = Field(
        None, description='Observed supply at the node (junction, tank or reservoir)'
    )
    tag: Optional[str] = Field(
        None,
        description='An optional text string used to assign the pipe to a category, perhaps one based on age or material',
    )
    tankOrder: Optional[float] = Field(
        None, description='Bulk water reaction order for tanks'
    )
    tolerance: Optional[float] = Field(None, description='Water quality tolerance')
    traceNodeID: Optional[
        Union[
            constr(
                pattern=r'^[\w\-\.\{\}\$\+\*\[\]\'|~^@!, :\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description="URI of node being traced in the quality analysis. Mandatory if 'qualityType' is TRACE, otherwise not required",
    )
    trials: Optional[float] = Field(
        None,
        description='The maximum number of trials used to solve network hydraulics at each hydraulic time step of a simulation',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI-LD Entity Type. It has to be SimulationScenario'
    )
    unbalanced: Optional[Unbalanced] = Field(
        None,
        description="Determines what happens if a hydraulic solution cannot be reached within the allowed number of trials. Allowable options are STOP (halt analysis), CONTINUE (continue analysis but with a warning message) and CONTINUE_N (continue for another N trials, where the value of N is given by 'unbalancedN'). Enum:'stop, continue, continue_N'",
    )
    unbalancedN: Optional[float] = Field(
        None,
        description="Number of additional trials allowed if 'unbalanced' is set to continue_N. Mandatory if 'unbalanced' is set to continue_N, else not required",
    )
    valveCurve: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Reference to the Curve where the valve is located')
    valveType: Optional[ValveType] = Field(
        None,
        description="Type of valve according to valve categories. Enum:'FCV, GPV, PBV, PRV, PSV, TCV'",
    )
    velocity: Optional[Velocity] = Field(
        None, description='Observed velocity in the link (pipe, valve or pump)'
    )
    viscosity: Optional[float] = Field(
        None,
        description='The kinematic viscosity of the fluid being modeled relative to that of water at 20 deg. C',
    )
    wallOrder: Optional[float] = Field(
        None, description='Wall reaction order for pipes'
    )
