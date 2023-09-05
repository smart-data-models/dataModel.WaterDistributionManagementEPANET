/* (Beta) Export of data model SimulationScenario of the subject dataModel.WaterDistributionManagementEPANET for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE demandModel_type AS ENUM ('DDA', 'PDA');CREATE TYPE flowUnits_type AS ENUM ('AFD', 'CFS', 'CMD', 'CMH', 'GPM', 'IMGD', 'LPS', 'LPM', 'MLD', 'MGD');CREATE TYPE headlossFormula_type AS ENUM ('H-W', 'D-W', 'C-M');CREATE TYPE qualityType_type AS ENUM ('age', 'chem', 'none', 'trace');CREATE TYPE statistic_type AS ENUM ('averaged', 'maximum', 'minimum', 'none', 'range');CREATE TYPE SimulationScenario_type AS ENUM ('SimulationScenario');CREATE TYPE unbalanced_type AS ENUM ('stop', 'continue', 'continue_N');
CREATE TABLE SimulationScenario (accuracy text, address json, alternateName text, areaServed text, bulkOrder text, checkFrequency text, chemicalName text, chemicalUnits text, concentrationLimit text, createdBy text, dampLimit text, dataProvider text, dateCreated timestamp, dateModified timestamp, demandCharge text, demandModel demandModel_type, description text, diffusivity text, duration text, emitterExponent text, flowChange text, flowUnits flowUnits_type, hasInputNetwork text, hasSimulationResult text, headError text, headlossFormula headlossFormula_type, hydraulicTimeStep text, id text, inputParameter json, location json, maxCheck text, minimumPressure text, name text, operationalControl json, owner json, patternStart timestamp, patternStep text, pressureExponent text, qualityTimeStep text, qualityType qualityType_type, reportStart text, reportStep text, requiredPressure text, ruleTimeStep text, seeAlso json, source text, specificGravity text, startClockTime text, statistic statistic_type, tankOrder text, tolerance text, traceNodeID text, trials text, type SimulationScenario_type, unbalanced unbalanced_type, unbalancedN text, viscosity text, wallOrder text);