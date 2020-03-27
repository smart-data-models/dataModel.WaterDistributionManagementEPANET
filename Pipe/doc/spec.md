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

-   `initialStatus` : {{Description of the Attribute}}
    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Property`.Text.
    -   Attribute metadata Properties:
        -   Values are resrtricted to: "OPEN","CLOSED","CV"
    -   Mandatory

-   `status` : {{Description of the Attribute}}
    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Property`.Text.
    -   Attribute metadata Properties:
        -   Values are resrtricted to: "OPEN","CLOSED","CV"
    -   Mandatory

-   `length` : {{Description of the Attribute}}
    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Property`.Text
    -   Attribute unit: `Metre`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `MTR`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Optional

-   `diameter` : {{Description of the Attribute}}
    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Property`.Text
    -   Attribute unit: `millimetre`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `MMT`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Optional

-   `roughness` : {{Description of the Attribute}}
    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Property`.Text
    -  Attribute unit: `No unit`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `C62`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Optional

-   `minorLoss` : {{Description of the Attribute}}
    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Property`.Text
    -   Attribute unit: `No unit`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `C62`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Optional

-   `tag` : {{Description of the Attribute}}
    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Property`.Text
    -   Optional

-   `description` : A free text description
    -   Optional

-   `bulkCoeff` : {{Description of the Attribute}}
    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Property`.Text
    -   Attribute unit: `reciprocal day`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `E91`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Optional

-   `wallCoeff` : {{Description of the Attribute}}
    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Property`.Text
    -   Attribute unit: `mg/m²/day`
    -   Proposed unitCode: `RRC`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Optional


### Pipe Entity Relationships

-   `startsAt` : {{Description of the Attribute}}

    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Relationship`.
        {{Add here the description of the target relationship object}}
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Mandatory

-   `endsAt` : {{Description of the Attribute}}

    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Relationship`.
        {{Add here the description of the target relationship object}}
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Mandatory

**Note**: JSON Schemas are intended to capture the data type and associated
constraints of the different Attributes, regardless their final representation
format in NGSI-LD.

### LD Example

A full example is presented [here](../example-normalized-ld.jsonld).

## Use it with a real service

T.B.D.

## Open Issues
