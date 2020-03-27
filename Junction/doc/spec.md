# Junction

## Description
This entity contains a harmonised description of a generic junction made for the Water Network Management domain. This entity is primarily associated with the water network management vertical and related IoT applications.

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

### Junction Entity Properties
-   `elevation` : {{Description of the Attribute}}
    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Property`.Text
    -   Attribute unit: `Metre`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `MTR`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Optional

-   `tag` : {{Description of the Attribute}}
    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Property`.Text
    -   Optional

-   `description` : A free text description
    -   Optional

-   `initialQuality` : {{Description of the Attribute}}
    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Property`.Text
    -   Attribute unit: `Mg/L`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `M1`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Optional

-   `emitterCoefficient` : {{Description of the Attribute}}
    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Property`.Text
    -   Attribute unit: `square metre per second`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `S4`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Optional

-   `demandCategory` : {{Description of the Attribute}}
    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Property`.Text
    -   `baseDemand`: A sub-property.
    -   `demandPattern`: A sub-Relationship
    -   Mondatory

-   `base demande` : {{A sub-property of the Property `demandCategory`}}
    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Property`.Text
    Attribute unit: `cubic metre per second`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `MQS`
    -   Mandatory

-   `sourceCategory` : {{Description of the Attribute}}

    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Property`.Text
    -   `sourceType`: A sub-property.
    -   `sourceQuality`:A sub-property.
    -   `sourcePattern`: A sub-Relationship.

-   `sourceType` : A sub-property of the Property `sourceCategory`
    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Property`.Text
    -  Values Restricted to : "CONCEN", "MASS", "FLOWPACED" and "SETPOINT"
    -   Mandatory

-   `sourceQuality` : {{A sub-property of the Property `sourceCategory`}}
    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Property`.Text
    Attribute unit: `Mg/L`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `M1`
    -   Mandatory

### Junction Entity Relationships


-   `demandPattern`: A relationship to the pattern pf the `demandCategory` property
    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Relationship`.
        {{Add here the description of the target relationship object}}
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Mandatory

-   `sourcePattern` : A relationship to the pattern pf the `sourceCategory` property
    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Relationship`.
        {{Add here the description of the target relationship object}}
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Mandatory

**Note**: JSON Schemas are intended to capture the data type and associated
constraints of the different Attributes, regardless their final representation
format in NGS-LD.


### LD Example

A full example is presented [here](../example-normalized-ld.jsonld).

## Use it with a real service

T.B.D.

## Open Issues