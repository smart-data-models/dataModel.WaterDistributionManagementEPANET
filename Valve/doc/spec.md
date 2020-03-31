# Valve

## Description
This entity contains a harmonised description of a generic Valve made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.

	
## Data Model

A JSON Schema corresponding to this data model can be found [here](../schema.json)
### NGSI-LD common Properties
-   `id`: Unique identifier.

-   `type`: Entity type. It must be equal to `Junction`.

-   `modifiedAt`: Last update timestamp of this
    entity.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Read-Only. Automatically generated.

-   `createdAt`: Entity's creation timestamp.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Read-Only. Automatically generated.

-   `location` : Location of Junction represented by a GeoJSON geometry.

    -   Attribute type: `GeoProperty`
    -   Normative References:
        [https://tools.ietf.org/html/rfc7946](https://tools.ietf.org/html/rfc7946)
    -   Mandatory.

### Valve Entity Properties

-   `tag` : An optional text string used to assign the valve to a category, perhaps based on type or location
    -   Attribute type: `Property`.Text
    -   Optional

-   `description` : A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   `initialStatus` : Valve status at the start of the simulation. If set to OPEN or CLOSED then the control setting of the valve is ignored and the valve behaves as an open or closed link, respectively. If set to NONE, then the valve will behave as intended
    -   Attribute type: `Property`.Text
    -   Accepted Values : "OPEN","CLOSED","NONE"
    -   Mandatory

-   `status` : Dynamic state of the valve
    -   Attribute type: `Property`.Text
    -   Accepted Values : "OPEN","CLOSED","NONE"
    -   Mandatory

-   `diameter` : The valve diameter
    -   Attribute type: `Property`.Number
    -   Attribute unit: `millimetre`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `MMT`
    -   Optional

-   `valveType` : The valve type
    -   Attribute type: `Property`.Text
    -   Accepted Values: "PRV", "PSV","PBV","FCV","TCV" and"GPV"
    -   Mandatory

-   `setting` : A parameter that describes the valve's operational setting
    -   Attribute type: `Property`.Number
    -   Attribute unit: `No unit`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `C62`
    -   Optional

-   `minorLoss` : Unitless minor loss coefficient that applies when the valve is completely opened
    -   Attribute type: `Property`.Number
    -   Attribute unit: `No unit`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `C62`
    -   Optional
### Valve Entity Relationships

-   `startsAt` : The ID of the node on the nominal upstream or inflow side of the valve
    -   Attribute type: `Relationship`. Reference to an entity of type `Node (Reservoir, Junction, Tank)`
    -   Mandatory

-   `endsAt` : The ID of the node on the nominal downstream or discharge side of the valve
    -   Attribute type: `Relationship`. Reference to an entity of type `Node (Reservoir, Junction, Tank)`
    -   Mandatory


**Note**: JSON Schemas are intended to capture the data type and associated
constraints of the different Attributes, regardless their final representation
format in NGSI(v2, LD).

### LD Example

A full example is presented [here](../example-normalized-ld.jsonld).

## Use it with a real service

T.B.D.

## Open Issues