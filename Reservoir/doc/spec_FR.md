Entité : Réservoir  
==================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.WaterNetworkManagement/blob/master/Reservoir/LICENSE.md)  
Description globale : **Cette entité contient une description harmonisée d'un réservoir générique fait pour le domaine de la gestion des réseaux d'eau. Cette entité est principalement associée aux applications verticales de gestion de l'eau et aux applications IdO connexes.**  

## Liste des biens  

- `address`: L'adresse postale.  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `description`: Un texte optionnel qui décrit d'autres informations importantes sur la jonction  - `elevation`: L'élévation au-dessus d'une référence commune du réservoir. Toutes les unités sont acceptées en code [CEFACT](https://www.unece.org/cefact.html).  - `hasInlet`: Une relation indiquant les points d'entrée d'eau du réservoir  - `hasOutlet`: Une relation indiquant les points de sortie d'eau du réservoir  - `headPattern`: L'étiquette d'identification d'un modèle temporel utilisé pour modéliser la variation temporelle de la hauteur de chute totale du réservoir  - `initialQuality`: Niveau de qualité de l'eau au réservoir. Toutes les unités sont acceptées en code [CEFACT](https://www.unece.org/cefact.html).  - `location`:   - `reservoirHead`: La hauteur hydraulique (élévation + hauteur de pression) de l'eau dans le réservoir. Toutes les unités sont acceptées en code [CEFACT](https://www.unece.org/cefact.html).  - `sourceCategory`: Description de la qualité du flux de sources entrant dans le réseau à un nœud spécifique.  - `tag`: Une chaîne de texte facultative utilisée pour classer la pipe dans une catégorie, peut-être en fonction de l'âge ou du matériau  - `type`: Type d'entité NGSI-LD. Il doit être égal à Réservoir.    
Propriétés requises  
- `id`  - `location`  - `reservoirHead`  - `type`  ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Reservoir:    
  description: 'This entity contains a harmonised description of a generic Reservoir made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.'    
  properties:    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/Text'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/Text'''    
          type: string    
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/Text'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/Text'''    
          type: string    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    description:    
      description: 'An optional text that describes other significant information about the junction'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    elevation:    
      description: 'The elevation above some common reference of the Reservoir. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: Metre    
    hasInlet:    
      description: 'A relationship indicating the water inlet points of the Reservoir'    
      format: uri    
      type: Relationship    
    hasOutlet:    
      description: 'A relationship indicating the water outlet points of the Reservoir'    
      format: uri    
      type: Relationship    
    headPattern:    
      description: 'The ID label of a time pattern used to model time variation in the reservoir''s total head'    
      format: uri    
      type: Relationship    
    initialQuality:    
      description: 'Water quality level at the Reservoir. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: mg/L    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      title: 'GeoJSON Geometry'    
    reservoirHead:    
      description: 'The hydraulic head (elevation + pressure head) of water in the Reservoir. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: Metre    
    sourceCategory:    
      description: 'Description of the quality of source flow entering the network at a specific node.'    
      properties:    
        sourcePattern:    
          description: 'Relationship. A relationship to the pattern pf the sourceCategory property'    
          format: uri    
          type: string    
        sourceQuality:    
          description: 'Property. Model:''https://schema.org/Number''. Units: ''mg/L''. Baseline or average concentration (or mass flow rate) of source. A sub-property of the Property ''sourceCategory''. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
          type: number    
        sourceType:    
          description: 'Property. Model:''https://schema.org/Text''. A sub-property of the Property ''sourceCategory'''    
          enum:    
            - CONCEN    
            - MASS    
            - FLOWPACED    
            - SETPOINT    
          type: string    
      required:    
        - type    
        - value    
        - sourceType    
        - sourceQuality    
        - sourcePattern    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    tag:    
      description: 'An optional text string used to assign the pipe to a category, perhaps one based on age or material'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    type:    
      description: 'NGSI-LD Entity Type. It must be equal to Reservoir.'    
      enum:    
        - Reservoir    
      type: Property    
  required:    
    - id    
    - type    
    - location    
    - reservoirHead    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### Réservoir NGSI V2 valeurs clés Exemple  
Voici un exemple de réservoir au format JSON en tant que valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "1863179e-3768-4480-9167-ff21f870dd19",  
    "type": "Reservoir",  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            24.30623,  
            60.07966  
        ]  
    },  
    "reservoirHead": 59.00,  
    "headPattern": "fbcb5fc8-8ca3-4533",  
    "elevation": 105.8,  
    "description": "This entity contains a harmonised description of a Reservoir",  
    "initialQuality": 0.5,  
    "sourceCategory": {  
        "value": "CategroyX",  
        "sourceType": "MASS",  
        "sourceQuality": 1.2,  
        "sourcePattern": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
    },  
    "tag": "DMA1"  
}  
```  
#### Réservoir NGSI V2 normalisé Exemple  
Voici un exemple de réservoir au format JSON tel que normalisé. Ce format est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "1863179e-3768-4480-9167-ff21f870dd19",  
    "type": "Reservoir",  
    "location": {  
        "type": "geo:json",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                24.30623,  
                60.07966  
            ]  
        }  
    },  
    "reservoirHead": {  
        "value": 59.00  
    },  
    "headPattern": {  
        "type": "Relationship",  
        "value": "fbcb5fc8-8ca3-4533"  
    },  
    "elevation": {  
        "value": 105.8  
    },  
    "description": {  
        "value": "This entity contains a harmonised description of a Reservoir"  
    },  
    "initialQuality": {  
        "value": 0.5  
    },  
    "sourceCategory": {  
        "value": {  
            "value": "CategroyX",  
            "sourceType": {  
                "value": "MASS"  
            },  
            "sourceQuality": {  
                "value": 1.2  
            },  
            "sourcePattern": {  
                "type": "Relationship",  
                "value": "fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
            }  
        }  
    },  
    "tag": {  
        "value": "DMA1"  
    }  
}  
```  
#### Réservoir NGSI-LD valeurs clés Exemple  
Voici un exemple de réservoir au format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context"],  
 "createdAt": "2020-03-02T15:42:00Z",  
 "description": "This entity contains a harmonised description of a Reservoir",  
 "elevation": 105.8,  
 "headPattern": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533",  
 "id": "urn:ngsi-ld:Reservoir:1863179e-3768-4480-9167-ff21f870dd19",  
 "initialQuality": 0.5,  
 "location": {"coordinates": [24.30623, 60.07966], "type": "Point"},  
 "modifiedAt": "2020-03-02T15:45:00Z",  
 "reservoirHead": 59.0,  
 "sourceCategory": "CategroyX",  
 "tag": "DMA1",  
 "type": "Reservoir"}  
```  
#### Réservoir NGSI-LD normalisé Exemple  
Voici un exemple de réservoir au format JSON-LD tel que normalisé. Ce format est compatible avec JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "urn:ngsi-ld:Reservoir:1863179e-3768-4480-9167-ff21f870dd19",  
    "type": "Reservoir",  
    "createdAt": "2020-03-02T15:42:00Z",  
    "modifiedAt": "2020-03-02T15:45:00Z",  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                24.30623,  
                60.07966  
            ]  
        }  
    },  
    "reservoirHead": {  
        "type": "Property",  
        "value": 59.00,  
        "unitCode": "MTR"  
    },  
    "headPattern": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533"  
    },  
    "elevation": {  
        "type": "Property",  
        "value": 105.8,  
        "unitCode": "MTR"  
    },  
    "description": {  
        "type": "Property",  
        "value": "This entity contains a harmonised description of a Reservoir"  
    },  
    "initialQuality": {  
        "type": "Property",  
        "value": 0.5,  
        "unitCode":"M1"  
    },  
    "sourceCategory": {  
        "type": "Property",  
        "value": "CategroyX",  
        "sourceType": {  
            "type": "Property",  
            "value": "MASS"  
        },  
        "sourceQuality": {  
            "type": "Property",  
            "value": 1.2,  
            "unitCode": "M1"  
        },  
        "sourcePattern": {  
            "type": "Relationship",  
            "object": "urn:ngsi-ld:Pattern:fbcb5fc8-8ca3-4533-a2eb-34bc89262190"  
        }  
    },  
    "tag": {  
        "type": "Property",  
        "value": "DMA1"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context"  
    ]  
}  
```  
