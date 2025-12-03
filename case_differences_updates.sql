-- SQL Updates for Case Differences
-- Generated from name_comparison_report.json
-- Total records: 1

BEGIN;

UPDATE players SET gamertag = 'Mercypeaks' WHERE LOWER(gamertag) = LOWER('MercyPeaks');

COMMIT;
