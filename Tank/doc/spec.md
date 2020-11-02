# Tank

## Description
This entity contains an harmonised description of a generic Tank made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.

## Data Model

A JSON Schema corresponding to this data model can be found [here](../schema.json)

### NGSI-LD common Properties
-   `id`: Unique identifier.

-   `type`: Entity type. It must be equal to `Tank`.

-   `modifiedAt`: Last update timestamp of this
    entity.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Read-Only. Automatically generated.

-   `createdAt`: Entity's creation timestamp.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Read-Only. Automatically generated.

-   `location` : Location of Tank represented by a GeoJSON geometry.

    -   Attribute type: `GeoProperty`
    -   Normative References:
        [https://tools.ietf.org/html/rfc7946](https://tools.ietf.org/html/rfc7946)
    -   Mandatory.


### Tank Enity Properties

-   `tag` : An optional text string used to assign the tank to a category, such as a pressure zone
    -   Attribute type: `Property`.Text
    -   Optional

-   `description` : A free text description
    -   Attribute type: `Property`.Text
    -   Optional


-   `elevation` : The elevation above some common reference of the tank
    -   Attribute type: `Property`. Number
    -   Attribute unit: All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code
    -   Attribute unit Example: `Metre`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `MTR`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Mandatory

-   `sourceCategory` : Description of the quality of source flow entering the network at a specific node
    -   Attribute type: `Property`.Text
    -   `sourceType`: A sub-property.
    -   `sourceQuality`:A sub-property.
    -   `sourcePattern`: A sub-Relationship.
    -   Optional

-   `sourceType` : A sub-property of the Property `sourceCategory`
    -   Attribute type: `Property`.Text
    -   Values Restricted to : "CONCEN", "MASS", "FLOWPACED" and "SETPOINT"
    -   Optional

-   `sourceQuality` : Baseline or average concentration (or mass flow rate) of source. A sub-property of the Property `sourceCategory`
    -   Attribute unit: All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code
    -   Attribute unit Example: `Property`. Number
    Attribute unit: `mg/L`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `M1`
    -   Optional

-   `initLevel` : The height of the water surface above the bottom elevation of the tank at the start of the simulation
    -   Attribute type: `Property`. Number
    -   Attribute unit: All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code
    -   Attribute unit Example: `Metre`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `MTR`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Mandatory

-   `maxLevel` : The height of the water surface above the bottom elevation of the tank at the start of the simulation
    -   Attribute type: `Property`. Number
    -   Attribute unit: All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code
    -   Attribute unit Example: `Metre`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `MTR`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Mandatory

-   `minLevel` : The minimum level that water in the tank can drop to
    -   Attribute type: `Property`. Number
    -   Attribute unit: All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code
    -   Attribute unit Example: `metre`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `MTR`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Mandatory

-   `minVolume` : The volume of water in the tank when it is at its minimum level
    -   Attribute type: `Property`. Number
    -   Attribute unit: All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code
    -   Attribute unit Example: `cubic metre`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `MTQ`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Mandatory

-   `nominalDiameter` : The diameter of the tank
    -   Attribute type: `Property`. Number
    -   Attribute unit: All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code
    -   Attribute unit Example: `Metre`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `MTR`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Mandatory

-   `mixingModel` : A sub-property of the Property `sourceCategory`
    -   Attribute type: `Property`.Text
    -   Values Restricted to :  "MIXED", "2COMP", "FIFO" and "LIFO"
    -   Mandatory

-   `volumeCurve` : The ID label of a curve used to describe the relation between tank volume and water level
    -   Attribute type: `Relationship`. Reference to an entity of type `Curve`
    -   Attribute unit: All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Optional

-   `mixingFraction` : The fraction of the tank's total volume that comprises the inlet-outlet compartment of the two-compartment (2COMP) mixing model
    -   Attribute type: `Property`. Number
    -   Attribute unit: All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code
    -   Attribute unit Example:: `No unit`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `C62`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Optional

-   `bulkReactionCoefficient` : The bulk reaction coefficient used for modelling reactions in the tank.
    -   Attribute type: `Property`. Number
    -   Attribute unit: All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code
    -   Attribute unit Example: `1/day`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `E91`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Mandatory

-   `initialQuality` : Water quality level int the tank at the start of the simulation
    -   Attribute type: `Property`. Number
    -   Attribute unit: All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code
    -   Attribute unit Example: `mg/L`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `M1`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Optional

### Tank Enity Relationships

-   `sourcePattern` : A relationship to the pattern of the `sourceCategory` property
    -   Attribute type: `Relationship`. Reference to an entity of type `Pattern`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Optional
-   `hasInlet` :  A relationship indicating the water inlet points of the `Tank`. This relationhip is neither the inverse or the equivalent of `startsAt` or `endsAt` relationships of the `ARC(Pipe,Pump,Valve)` models. It depends on the water flow direction in the Water Network.
    -   Attribute type: `Relationship`. Reference to an entity of type `Pipe` or `Valve`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Optional
-   `hasOutlet` :  A relationship indicating the water outlet points of the `Tank`. This relationhip is neither the inverse or the equivalent of `startsAt` or `endsAt` relationships of the `ARC(Pipe,Pump,Valve)` models. It depends on the water flow direction in the Water Network.
    -   Attribute type: `Relationship`. Reference to an entity of type `Pipe` or `Valve`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Optional

**Note**: JSON Schemas are intended to capture the data type and associated
constraints of the different Attributes, regardless their final representation
format in NGSI(v2, LD).

### LD Example

A full example is presented [here](../example-normalized-ld.jsonld).

## Use it with a real service

T.B.D.

## Open Issues

