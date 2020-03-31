# Pattern

## Description
This entity contains an harmonised description of a generic pattern made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.

## Data Model

A JSON Schema corresponding to this data model can be found [here](../schema.json).

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

 ### Pattern Entity Properties
-   `tag` : {{Description of the Attribute}}
    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Property`.Text
    -   Optional

-   `description` : A free text description
    -   Optional

-   `multipliers` : Multipliers define how some base quantity (e.g., demand) is adjusted for each time period

    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Property`. {{Add here the attribute data type}}
    -   Attribute metadata Properties:
        -   `Enumeration` : {{Metadata Property Description}}
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
