# Tank

## Description
This entity contains a harmonised description of a generic Tank made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.

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


### Tank Enity Properties

-   `tag` : An optional text string used to assign the tank to a category, such as a pressure zone
    -   Attribute type: `Property`.Text
    -   Optional

-   `description` : A free text description
    -   Attribute type: `Property`.Text
    -   Optional
-   `demandCategory` : Allows base demands and time patterns to be assigned to other categories of users at the junction
    -   Attribute type: `Property`.Text
    -   `baseDemand`: A sub-property.
    -   `demandPattern`: A sub-Relationship
    -   Optional

-   `elevation` : The elevation above some common reference of the tank
    -   Attribute type: `Property`.Number
    -   Attribute unit: `Metre`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `MTR`
    -   Optional

-   `sourceCategory` : Description of the quality of source flow entering the network at a specific node
    -   Attribute type: `Property`.Text
    -   `sourceType`: A sub-property.
    -   `sourceQuality`:A sub-property.
    -   `sourcePattern`: A sub-Relationship.

-   `sourceType` : A sub-property of the Property `sourceCategory`
    -   Attribute type: `Property`.Text
    -   Accepted Values : "CONCEN", "MASS", "FLOWPACED" and "SETPOINT"
    -   Mandatory

-   `sourceQuality` : Baseline or average concentration (or mass flow rate) of source. A sub-property of the Property `sourceCategory`
    -   Attribute type: `Property`. Number
    Attribute unit: `Mg/L`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `M1`
    -   Mandatory

-   `initLevel` : The height of the water surface above the bottom elevation of the tank at the start of the simulation
    -   Attribute type: `Property`. Number
    -   Attribute unit: `Metre`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `MTR`
    -   Optional

-   `minLevel` : The height of the water surface above the bottom elevation of the tank at the start of the simulation
    -   Attribute type: `Property`. Number
    -   Attribute unit: `Metre`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `MTR`
    -   Optional

-   `maxLevel` : The height of the water surface above the bottom elevation of the tank at the start of the simulation
    -   Attribute type: `Property`. Number
    -   Attribute unit: `Metre`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `MTR`
    -   Optional

-   `minVolume` : The volume of water in the tank when it is at its minimum level
    -   Attribute type: `Property`. Number
    -   Attribute unit: `cubic metre`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `MTQ`
    -   Optional

-   `nominalDiameter` : The diameter of the tank
    -   Attribute type: `Property`. Number
    -   Attribute unit: `Metre`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `MTR`
    -   Optional

-   `mixingModel` : A sub-property of the Property `sourceCategory`
    -   Attribute type: `Property`. Text
    -   Accepted Values :  "MIXED", "2COMP", "FIFO" and "LIFO"
    -   Mandatory

-   `volumCurve` : The ID label of a curve used to describe the relation between tank volume and water level
    -   Attribute type: `Property`. Number
    -   Attribute unit: `cubic metre`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `MTQ`
    -   Optional

-   `mixingFraction` : The fraction of the tank's total volume that comprises the inlet-outlet compartment of the two-compartment (2COMP) mixing model
    -   Attribute type: `Property`. Number
    -   Attribute unit: `No unit`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `C62`
    -   Optional

### Tank Enity Relationships

-   `demandPattern`: A relationship to the pattern of the `demandCategory` property
    -   Attribute type: `Relationship`. Reference to an entity of type `Pattern`
    -   Mandatory

-   `sourcePattern` : A relationship to the pattern of the `sourceCategory` property
    -   Attribute type: `Relationship`. Reference to an entity of type `Pattern`
    -   Mandatory

**Note**: JSON Schemas are intended to capture the data type and associated
constraints of the different Attributes, regardless their final representation
format in NGSI(v2, LD).

### LD Example

A full example is presented [here](../example-normalized-ld.jsonld).

## Use it with a real service

T.B.D.

## Open Issues

