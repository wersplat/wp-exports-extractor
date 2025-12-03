-- SQL Updates for Case Differences
-- Generated from name_comparison_report.json
-- Total records: 1

BEGIN;

UPDATE players SET gamertag = 'Reallytrxp' WHERE LOWER(gamertag) = LOWER('reallytrxp');

COMMIT;
