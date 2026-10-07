/* (Beta) Export of data model Valve of the subject dataModel.WaterDistributionManagementEPANET for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Valve_initialStatus_type AS ENUM ('OPEN', 'CLOSED', 'CV');
CREATE TYPE Valve_status_type AS ENUM ('OPEN', 'CLOSED', 'CV');
CREATE TYPE Valve_type AS ENUM ('Valve');
CREATE TYPE Valve_valveType_type AS ENUM ('FCV', 'GPV', 'PBV', 'PRV', 'PSV', 'TCV');
CREATE TABLE Valve (
  "address" JSON,
  "alternateName" TEXT,
  "areaServed" TEXT,
  "dataProvider" TEXT,
  "dateCreated" TIMESTAMP,
  "dateModified" TIMESTAMP,
  "description" TEXT,
  "diameter" NUMERIC,
  "endsAt" TEXT,
  "flow" JSON,
  "id" TEXT PRIMARY KEY,
  "initialStatus" Valve_initialStatus_type,
  "location" JSON,
  "minorLoss" NUMERIC,
  "name" TEXT,
  "openStatus" NUMERIC,
  "owner" JSON,
  "quality" JSON,
  "seeAlso" JSON,
  "setting" NUMERIC,
  "source" TEXT,
  "startsAt" TEXT,
  "status" Valve_status_type,
  "tag" TEXT,
  "type" Valve_type,
  "valveCurve" TEXT,
  "valveType" Valve_valveType_type,
  "velocity" JSON,
  "vertices" JSON
);