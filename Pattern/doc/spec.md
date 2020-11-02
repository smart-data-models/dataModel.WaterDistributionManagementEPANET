# Pattern

## Description
This entity contains an harmonised description of a generic pattern made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.

## Data Model

A JSON Schema corresponding to this data model can be found [here](../schema.json).

### NGSI-LD common Properties

-   `id`: Unique identifier.

-   `type`: Entity type. It must be equal to `Pattern`.

-   `modifiedAt`: Last update timestamp of this
    entity.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Read-Only. Automatically generated.

-   `createdAt`: Entity's creation timestamp.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Read-Only. Automatically generated.

 ### Pattern Entity Properties
-   `tag` : An optional text string used to assign the pattern to a category, such as a pressure zone
    -   Attribute type: `Property`.Text
    -   Optional

-   `description` : A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   `multipliers` : Multipliers define how some base quantity (e.g., demand) is adjusted for each time period

    -   Attribute type: `Property`. List of Number
    -   Attribute metadata Properties:
        -   `Enumeration` : {{Metadata Property Description}}
    -   Mandatory

-   `timeStep` : The time step used for the multipliers
    -   Attribute type: `Property`. Number
    -   Attribute unit: All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code
    -   Attribute unit Example: `Second`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `SEC`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Mandatory

-   `startTime` : The time at which the pattern starts
    -   Attribute type: `Property`. [Time](https://schema.org/Time)
    -   Mandatory

### Pattern Entity Relationships
No defined Relationships for this Entity.


**Note**: JSON Schemas are intended to capture the data type and associated
constraints of the different Attributes, regardless their final representation
format in NGSI-LD.

### LD Example

A full example is presented [here](../example-normalized-ld.jsonld).

## Use it with a real service

T.B.D.

## Open Issues
