/* (Beta) Export of data model Pump of the subject dataModel.WaterDistributionManagementEPANET for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Pump_initialStatus_type AS ENUM ('OPEN', 'CLOSED', 'CV');
CREATE TYPE Pump_status_type AS ENUM ('OPEN', 'CLOSED', 'CV');
CREATE TYPE Pump_type AS ENUM ('Pump');
CREATE TABLE Pump (
  "address" JSON,
  "alternateName" TEXT,
  "areaServed" TEXT,
  "dataProvider" TEXT,
  "dateCreated" TIMESTAMP,
  "dateModified" TIMESTAMP,
  "description" TEXT,
  "efficCurve" JSON,
  "endsAt" JSON,
  "energyPattern" JSON,
  "energyPrice" NUMERIC,
  "energyUse" JSON,
  "flow" JSON,
  "headCurve" TEXT,
  "id" TEXT PRIMARY KEY,
  "initialStatus" Pump_initialStatus_type,
  "location" JSON,
  "name" TEXT,
  "owner" JSON,
  "power" NUMERIC,
  "pumpPattern" JSON,
  "quality" JSON,
  "seeAlso" JSON,
  "source" TEXT,
  "speed" NUMERIC,
  "startsAt" JSON,
  "status" Pump_status_type,
  "tag" TEXT,
  "type" Pump_type,
  "velocity" JSON,
  "vertices" JSON
);