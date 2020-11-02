# Reservoir

## Description
This entity contains an harmonised description of a generic Reservoir made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.
	
## Data Model

A JSON Schema corresponding to this data model can be found [here](../schema.json)

## NGSI-LD Common Properties
-   `id`: Unique identifier.

-   `type`: Entity type. It must be equal to `Reservoir`.

-   `modifiedAt`: Last update timestamp of this
    entity.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Read-Only. Automatically generated.

-   `createdAt`: Entity's creation timestamp.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Read-Only. Automatically generated.

-   `location` : Location of Reservoir represented by a GeoJSON geometry.

    -   Attribute type: `GeoProperty`
    -   Normative References:
        [https://tools.ietf.org/html/rfc7946](https://tools.ietf.org/html/rfc7946)
    -   Mandatory.

## Reservoir Entity Properties

-   `elevation` : The elevation above some common reference of the reservoir
    -   Attribute type: `Property`.Text
    -   Attribute unit: `Metre`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `MTR`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Mandatory

-   `tag` : An optional text string used to assign the reservoir to a category, such as a pressure zone
    -   Attribute type: `Property`.Text
    -   Optional

-   `description` : A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   `reservoirHead` : The hydraulic head (elevation + pressure head) of water in the reservoir
    -   Attribute type: `Property`. Number
    -   Attribute unit: All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code
    -   Attribute unit Example: `Metre`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `MTR`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Mandatory

-   `initialQuality` : Water quality level at the reservoir
    -   Attribute type: `Property`. Number
    -   Attribute unit: All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code
    -   Attribute unit Example: `mg/L`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `M1`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Optional

-   `sourceCategory` : Description of the quality of source flow entering the network at a specific node

    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Property`.Text
    -   `sourceType`: A sub-property.
    -   `sourceQuality`:A sub-property.
    -   `sourcePattern`: A sub-Relationship.
    -   Optional

-   `sourceType` : A sub-property of the Property `sourceCategory`
    -   Attribute type: `Property`.Text
    -   Values are Restricted to: "CONCEN", "MASS", "FLOWPACED" and "SETPOINT"
    -   Optional

-   `sourceQuality` : Baseline or average concentration (or mass flow rate) of source. A sub-property of the Property `sourceCategory`
    -   Attribute type: `Property`. Number
    -   Attribute unit: All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code
    -   Attribute unit Example: `mg/L`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `M1`
    -   Optional

## Reservoir Entity Relationships
-   `headPattern`: The ID label of a time pattern used to model time variation in the reservoir's total head

    -   Attribute type: `Relationship`. Reference to an entity of type `Pattern`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}`: {{Metadata Property Description}}
    -   Optional

-   `sourcePattern` : A relationship to the pattern pf the `sourceCategory` property
    -   Attribute type: `Relationship`. Reference to an entity of type `Pattern`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Optional
-   `hasInlet` :  A relationship indicating the water inlet points of the `Reservoir`. This relationhip is neither the inverse or the equivalent of `startsAt` or `endsAt` relationships of the `ARC(Pipe,Pump,Valve)` models. It depends on the water flow direction in the Water Network.
    -   Attribute type: `Relationship`. Reference to an entity of type `Pipe` or `Valve`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Optional
-   `hasOutlet` :  A relationship indicating the water outlet points of the `Reservoir`. This relationhip is neither the inverse or the equivalent of `startsAt` or `endsAt` relationships of the `ARC(Pipe,Pump,Valve)` models. It depends on the water flow direction in the Water Network.
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

