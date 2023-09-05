/* (Beta) Export of data model Reservoir of the subject dataModel.WaterDistributionManagementEPANET for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Reservoir_type AS ENUM ('Reservoir');
CREATE TABLE Reservoir (address json, alternateName text, areaServed text, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, elevation text, hasInlet text, hasOutlet text, head json, headPattern text, id text, initialQuality json, location json, name text, owner json, pressure json, quality json, reservoirHead text, seeAlso json, source text, sourceCategory json, sourceMassInflow json, supply json, tag text, type Reservoir_type);