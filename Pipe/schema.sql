/* (Beta) Export of data model Pipe of the subject dataModel.WaterDistributionManagementEPANET for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Pipe_initialStatus_type AS ENUM ('OPEN', 'CLOSED', 'CV');
CREATE TYPE Pipe_status_type AS ENUM ('OPEN', 'CLOSED', 'CV');
CREATE TYPE Pipe_type AS ENUM ('Pipe');
CREATE TABLE Pipe (
  "address" JSON,
  "alternateName" TEXT,
  "areaServed" TEXT,
  "bulkCoeff" NUMERIC,
  "dataProvider" TEXT,
  "dateCreated" TIMESTAMP,
  "dateModified" TIMESTAMP,
  "description" TEXT,
  "diameter" NUMERIC,
  "endsAt" TEXT,
  "flow" JSON,
  "id" TEXT PRIMARY KEY,
  "initialStatus" Pipe_initialStatus_type,
  "length" NUMERIC,
  "location" JSON,
  "minorLoss" NUMERIC,
  "name" TEXT,
  "owner" JSON,
  "quality" JSON,
  "roughness" NUMERIC,
  "seeAlso" JSON,
  "source" TEXT,
  "startsAt" TEXT,
  "status" Pipe_status_type,
  "tag" TEXT,
  "type" Pipe_type,
  "velocity" JSON,
  "vertices" JSON,
  "wallCoeff" NUMERIC
);