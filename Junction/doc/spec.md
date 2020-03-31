# Junction

## Description
This entity contains an harmonised description of a generic junction made for the Water Network Management domain. This entity is primarily associated with the water network management vertical and related IoT applications.

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
-   `elevation` : The elevation above some common reference of the junction
    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Property`.Text
    -   Attribute unit: All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code
    -   Attribute unit Example: `Metre`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `MTR`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Mondatory

-   `tag` : An optional text string used to assign the junction to a category, such as a pressure zone
    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Property`.Text
    -   Optional

-   `description` : An optional text that describes other significant information about the junction
    -   Optional

-   `initialQuality` : Water quality level at the junction at the start of the simulation
    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Property`.Text
    -   Attribute unit: All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code
    -   Attribute unit Example: `mg/L`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `M1`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Optional

-   `emitterCoefficient` : Discharge coefficient for emitter (sprinkler or nozzle) placed at junction
    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Property`.Text
    -   Attribute unit: All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code
    -   Attribute unit Example: `square metre per second`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `S4`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Optional

-   `demandCategory` : Allows base demands and time patterns to be assigned to other categories of users at the junction
    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Property`.Text
    -   `baseDemand`: A sub-property.
    -   `demandPattern`: A sub-Relationship
    -   Optional

-   `base demande` : Baseline or average demand for the category. A sub-property of the Property `demandCategory`
    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Property`.Text
    -   Attribute unit: All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code
    -   Attribute unit Example: `cubic metre per second`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `MQS`
    -   Optional

-   `sourceCategory` : Description of the quality of source flow entering the network at a specific node

    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Property`.Text
    -   `sourceType`: A sub-property.
    -   `sourceQuality`:A sub-property.
    -   `sourcePattern`: A sub-Relationship.
    -   Optional

-   `sourceType` : A sub-property of the Property `sourceCategory`
    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Property`.Text
    -  Values Restricted to : "CONCEN", "MASS", "FLOWPACED" and "SETPOINT"
    -   Optional

-   `sourceQuality` : Baseline or average concentration (or mass flow rate) of source. A sub-property of the Property `sourceCategory`
    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Property`.Text
    -   Attribute unit: All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code
    -   Attribute unit Example: `mg/L`
    -   [CEFACT](https://www.unece.org/cefact.html) unitCode: `M1`
    -   Optional

### Junction Entity Relationships


-   `demandPattern`: A relationship to the pattern pf the `demandCategory` property
    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Relationship`.
        {{Add here the description of the target relationship object}}
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Optional

-   `sourcePattern` : A relationship to the pattern pf the `sourceCategory` property
    -   Normative References: {{Add a normative reference}}
    -   Attribute type: `Relationship`.
        {{Add here the description of the target relationship object}}
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Optional

**Note**: JSON Schemas are intended to capture the data type and associated
constraints of the different Attributes, regardless their final representation
format in NGS-LD.


### LD Example

A full example is presented [here](../example-normalized-ld.jsonld).

## Use it with a real service

T.B.D.

## Open Issues