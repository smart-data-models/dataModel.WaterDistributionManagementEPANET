from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import (
    AnyUrl,
    AwareDatetime,
    BaseModel,
    Field,
    RootModel,
    confloat,
    constr,
)


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


class InitialStatus(Enum):
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'
    CV = 'CV'


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


class Status(Enum):
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'
    CV = 'CV'


class Type6(Enum):
    Valve = 'Valve'


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


class Type7(Enum):
    MultiPoint = 'MultiPoint'


class Vertices(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type7


class Type8(Enum):
    Point = 'Point'


class Vertices1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type8


class Valve(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
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
    diameter: Optional[float] = Field(
        None,
        description='The valve diameter. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code',
    )
    endsAt: Optional[AnyUrl] = Field(
        None,
        description='The ID of the node on the nominal downstream or discharge side of the valve',
    )
    flow: Optional[Flow] = Field(
        None,
        description='Rate of flow from `startsAt` node to `endsAt` node, measured by a device at the link (pipe, valve or pump)',
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
    initialStatus: Optional[InitialStatus] = Field(
        None,
        description="The link status at the start of the simulation. Enum:'OPEN, CLOSED, CV'",
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    minorLoss: Optional[float] = Field(
        None,
        description='Unitless minor loss coefficient that applies when the valve is completely opened. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    openStatus: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None,
        description='Status of a valve as a numeric percentage value representing how open or close the valve is. 0% - completely closed, 100% - fully open',
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
    quality: Optional[Quality] = Field(
        None, description='Observed quality in the network component'
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    setting: Optional[float] = Field(
        None,
        description="A parameter that describes the valve's operational setting. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code",
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    startsAt: Optional[AnyUrl] = Field(
        None,
        description='The ID of the node on the nominal upstream or inflow side of the valve',
    )
    status: Optional[Status] = Field(
        None, description="The dynamic state of the node. Enum:'OPEN, CLOSED, CV'"
    )
    tag: Optional[str] = Field(
        None,
        description='An optional text string used to assign the pipe to a category, perhaps one based on age or material',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI-LD Entity Type. It must be equal to Valve'
    )
    valveCurve: Optional[AnyUrl] = Field(
        None,
        description='A relationship to the curve of the setting property. Only required when valveType is GPV',
    )
    valveType: Optional[ValveType] = Field(
        None,
        description="The valve type of the element. enum:'FCV, GPV, PBV, PRV, PSV, TCV'",
    )
    velocity: Optional[Velocity] = Field(
        None, description='Observed velocity in the link (pipe, valve or pump)'
    )
    vertices: Optional[Union[Vertices, Vertices1]] = Field(
        None,
        description='Geoproperty. Coordinates of all vertices in the valve, ordered from the startsAt node to the endsAt node and encoded as a GeoJSON ',
    )
