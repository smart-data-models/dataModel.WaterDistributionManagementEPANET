/* (Beta) Export of data model Pattern of the subject dataModel.WaterDistributionManagementEPANET for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Pattern_type AS ENUM ('Pattern');
CREATE TABLE Pattern (alternateName TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, id TEXT PRIMARY KEY, multipliers JSON, name TEXT, owner JSON, seeAlso JSON, source TEXT, startTime TIMESTAMP, tag TEXT, timeStep NUMERIC, type Pattern_type);