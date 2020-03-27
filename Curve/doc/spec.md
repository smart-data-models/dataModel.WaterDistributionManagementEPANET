# Curve

## Description
This entity contains a harmonised description of a generic curve made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.

## Data Model

A JSON Schema corresponding to this data model can be found [here](../schema.json).

### NGSI-LD common Properties

-   `id` : Unique identifier.

-   `type`: Entity type. It must be equal to `Curve`.

-   `modifiedAt`: Last update timestamp of this entity.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Read-Only. Automatically generated.

-   `createdAt`: Entity's creation timestamp.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Read-Only. Automatically generated.

### Curve Entity Properties
-   `curveType` : Entity's curve type.

    -   Attribute type: `Property`.
    -   Accepted Values:`FLOW-HEAD`,
                        `FLOW-EFFICIANCY`,
                        `FLOW-HEADLOSS`,
                        `LEVEL-VOLUME`
    -   Required

-   `xData` : {{Description of the Attribute}}

    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Property`. {{Add here the attribute data type}}
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   {{Optional/Mandatory}}

-   `yData` : {{Description of the Attribute}}

    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Property`. {{Add here the attribute data type}}
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   {{Optional/Mandatory}}

### Junction Entity Relationships

No Relationhips defined for this entity
### NGSI-LD Example

A full example is presented [here](../example-normalized-ld.jsonld).

## Use it with a real service

T.B.D.

## Open Issues
