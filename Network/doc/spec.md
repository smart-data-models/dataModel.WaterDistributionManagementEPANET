# Network

## Description
This entity contains an harmonised description of a generic network made for the Water Network Management domain. This entity is primarily associated with the water network management vertical and related IoT applications.

## Data Model

A JSON Schema corresponding to this data model can be found [here](../schema.json)

### NGSI-LD common Properties
-   `id`: Unique identifier.

-   `type`: Entity type. It must be equal to `Network`.

### Network Entity Properties

-   `description` : A free text description
    -   Attribute type: `Property`.Text
    -   Optional

### Network Entity Relationships

-   isComposedOf: The ID of water component of the network

    -   Attribute type: `Relationship`. Reference to an entity of type `Node (Reservoir, Junction, Tank)` or `Link (Pipe, Valve, Pump)`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Optional

-   `hasSubNetwork` : The ID of the sub-network, considered as a Network.

    -   Attribute type: `Relationship`. Reference to an entity of type `Network`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Optional

**Note**: JSON Schemas are intended to capture the data type and associated
constraints of the different Attributes, regardless their final representation
format in NGSI-LD.


### LD Example

A full example is presented [here](../example-normalized-ld.jsonld).

## Use it with a real service

T.B.D.

## Open Issues