# Pipe

## Description
This entity contains a harmonised description of a generic pipe made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications. 

	
## Data Model

A JSON Schema corresponding to this data model can be found [here](../schema.json).

### NGSI-LD common Properties
-   `id`: Unique identifier.

-   `type`: Entity type. It must be equal to `PIPE`.

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


### Pipe Entity Properties

-   `initialStatus` : Determines whether the pipe is initially open, closed, or contains a check valve
    -   Attribute type: `Property`.Text.
    -   Attribute metadata Properties:
        -   Values are resrtricted to: "OPEN","CLOSED","CV"
    -   Mandatory

-   `status` : Dynamic state of the pipe
    -   Attribute type: `Property`.Text.
    -   Attribute metadata Properties:
        -   Values are resrtricted to: "OPEN","CLOSED","CV"
    -   Mandatory

-   `length` : The actual length of the pipe
    -   Attribute type: `Property`.Number
    -   Attribute unit: `Metre`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `MTR`
    -   Optional

-   `diameter` : The pipe diameter
    -   Attribute type: `Property`.Number
    -   Attribute unit: `millimetre`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `MMT`
    -   Optional

-   `roughness` : The roughness coefficient of the pipe. It is unitless for Hazen-Williams or Chezy-Manning roughness and has units of millifeet (mm) for Darcy-Weisbach roughness.
    -   Attribute type: `Property`.Number
    -  Attribute unit: `No unit`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `C62`
    -   Optional

-   `minorLoss` : Unitless minor loss coefficient associated with bends, fittings, etc.
    -   Attribute type: `Property`.Number
    -   Attribute unit: `No unit`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `C62`
    -   Optional

-   `tag` : An optional text string used to assign the pipe to a category, perhaps one based on age or material
    -   Attribute type: `Property`.Text
    -   Optional

-   `description` : A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   `bulkCoeff` : The bulk reaction coefficient for the pipe. Use a positive value for growth and a negative value for decay
    -   Attribute type: `Property`.Number
    -   Attribute unit: `reciprocal day`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `E91`
    -   Optional

-   `wallCoeff` : The wall reaction coefficient for the pipe. Use a positive value for growth and a negative value for decay.
    -   Attribute type: `Property`.Number
    -   Attribute unit: `mg/m²/day`
    -   Proposed unitCode: `RRC`
    -   Optional

### Pipe Entity Relationships

-   `startsAt` : The ID of the node where the pipe begins
    -   Attribute type: `Relationship`. Reference to an entity of type `Node (Reservoir, Junction, Tank)`
    -   Mandatory

-   `endsAt` : The ID of the node where the pipe ends

    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Relationship`. Reference to an entity of type `Node (Reservoir, Junction, Tank)
    -   Mandatory

**Note**: JSON Schemas are intended to capture the data type and associated
constraints of the different Attributes, regardless their final representation
format in NGSI-LD.

### LD Example

A full example is presented [here](../example-normalized-ld.jsonld).

## Use it with a real service

T.B.D.

## Open Issues
