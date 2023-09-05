/* (Beta) Export of data model Valve of the subject dataModel.WaterDistributionManagementEPANET for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE initialStatus_type AS ENUM ('OPEN', 'CLOSED', 'CV');CREATE TYPE status_type AS ENUM ('OPEN', 'CLOSED', 'CV');CREATE TYPE Valve_type AS ENUM ('Valve');CREATE TYPE valveType_type AS ENUM ('FCV', 'GPV', 'PBV', 'PRV', 'PSV', 'TCV');
CREATE TABLE Valve (address json, alternateName text, areaServed text, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, diameter text, endsAt text, flow json, id text, initialStatus initialStatus_type, location json, minorLoss text, name text, openStatus text, owner json, quality json, seeAlso json, setting text, source text, startsAt text, status status_type, tag text, type Valve_type, valveCurve text, valveType valveType_type, velocity json, vertices json);