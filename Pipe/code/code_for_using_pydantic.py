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
    Pipe = 'Pipe'


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


class Pipe(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    bulkCoeff: Optional[float] = Field(
        None,
        description='Use a positive value for growth and a negative value for decay. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code',
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
    diameter: Optional[float] = Field(None, description='The pipe diameter')
    endsAt: Optional[AnyUrl] = Field(
        None, description='The ID of the node where the pipe ends'
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
    length: Optional[float] = Field(
        None,
        description='The actual length of the pipe. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code',
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    minorLoss: Optional[float] = Field(
        None,
        description='Unitless minor loss coefficient associated with bends, fittings, etc',
    )
    name: Optional[str] = Field(None, description='The name of this item')
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
    roughness: Optional[float] = Field(
        None, description='The roughness coefficient of the Pipe'
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    startsAt: Optional[AnyUrl] = Field(
        None, description='The ID of the node where the pipe begins'
    )
    status: Optional[Status] = Field(
        None, description="The dynamic state of the node. Enum:'OPEN, CLOSED, CV'"
    )
    tag: Optional[str] = Field(
        None,
        description='An optional text string used to assign the pipe to a category, perhaps one based on age or material',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI-LD Entity Type. It has to be Pipe'
    )
    velocity: Optional[Velocity] = Field(
        None, description='Observed velocity in the link (pipe, valve or pump)'
    )
    vertices: Optional[Union[Vertices, Vertices1]] = Field(
        None,
        description='Geoproperty. Coordinates of all vertices in the pipe, ordered from the startsAt node to the endsAt node and encoded as a GeoJSON ',
    )
    wallCoeff: Optional[float] = Field(
        None,
        description='The wall reaction coefficient for the pipe. Use a positive value for growth and a negative value for decay. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code',
    )
