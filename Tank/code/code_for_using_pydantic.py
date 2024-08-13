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


class MixingModel(Enum):
    field_2COMP = '2COMP'
    FIFO = 'FIFO'
    LIFO = 'LIFO'
    MIXED = 'MIXED'


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
    Tank = 'Tank'


class Tank(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    bulkReactionCoefficient: Optional[float] = Field(
        None,
        description='The bulk reaction coefficient used for modelling reactions in the tank. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code',
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
    description: Optional[str] = Field(None, description='A description of this item')
    elevation: Optional[float] = Field(
        None,
        description='The elevation above some common reference of the Tank. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code',
    )
    hasInlet: Optional[AnyUrl] = Field(
        None,
        description='A relationship indicating the water inlet points of the Reservoir',
    )
    hasOutlet: Optional[AnyUrl] = Field(
        None,
        description='A relationship indicating the water outlet points of the Reservoir',
    )
    head: Optional[Head] = Field(
        None, description='Observed head at the node (junction, tank or reservoir)'
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
    initLevel: Optional[float] = Field(
        None,
        description='The height of the water surface above the bottom elevation of the tank at the start of the simulation. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code',
    )
    initialQuality: Optional[float] = Field(
        None,
        description='Water quality level in the tank at the start of the simulation. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code',
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
    maxLevel: Optional[float] = Field(
        None,
        description='The height of the water surface above the bottom elevation of the tank at the start of the simulation. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code',
    )
    minLevel: Optional[float] = Field(
        None,
        description='The minimum level that water in the tank can drop to. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code',
    )
    minVolume: Optional[float] = Field(
        None,
        description='The volume of water in the tank when it is at its minimum level. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code',
    )
    mixingFraction: Optional[float] = Field(
        None,
        description="The fraction of the tank's total volume that comprises the inlet-outlet compartment of the two-compartment (2COMP) mixing model. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code",
    )
    mixingModel: Optional[MixingModel] = Field(
        None,
        description="A sub-property of the Property sourceCategory. Enum:'2COMP, FIFO, LIFO, MIXED'",
    )
    name: Optional[str] = Field(None, description='The name of this item')
    nominalDiameter: Optional[float] = Field(
        None,
        description='The diameter of the tank. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code',
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
    pressure: Optional[Pressure] = Field(
        None, description='Observed pressure at the node (junction, tank or reservoir)'
    )
    quality: Optional[Quality] = Field(
        None, description='Observed quality in the network component'
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
    supply: Optional[Supply] = Field(
        None, description='Observed supply at the node (junction, tank or reservoir)'
    )
    tag: Optional[str] = Field(
        None,
        description='An optional text string used to assign the pipe to a category, perhaps one based on age or material',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI-LD Entity Type. It has to be Tank'
    )
    volumeCurve: Optional[
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
        description='The ID label of a curve used to describe the relation between tank volume and water level',
    )
