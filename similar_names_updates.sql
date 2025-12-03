-- SQL Updates for Similar Names (REQUIRES REVIEW)
-- Generated from name_comparison_report.json
-- Total records: 13

BEGIN;

-- Similarity: 88.9% | DB: 'Repowrld_' -> CSV: 'Repowrld-'
UPDATE players SET gamertag = 'Repowrld-' WHERE LOWER(gamertag) = LOWER('Repowrld_');

-- Similarity: 92.3% | DB: 'Gohthum' -> CSV: 'Gothum'
UPDATE players SET gamertag = 'Gothum' WHERE LOWER(gamertag) = LOWER('Gohthum');

-- Similarity: 93.3% | DB: 'Jairo2k_' -> CSV: 'Jairo2k'
UPDATE players SET gamertag = 'Jairo2k' WHERE LOWER(gamertag) = LOWER('Jairo2k_');

-- Similarity: 95.2% | DB: 'Chris kickz' -> CSV: 'Chriskickz'
UPDATE players SET gamertag = 'Chriskickz' WHERE LOWER(gamertag) = LOWER('Chris kickz');


-- Similarity: 94.7% | DB: 'Manny Taft' -> CSV: 'MannyTAFT'
UPDATE players SET gamertag = 'MannyTAFT' WHERE LOWER(gamertag) = LOWER('Manny Taft');

-- Similarity: 80.0% | DB: 'TvcrZyIq' -> CSV: 'CrazyIQ'
UPDATE players SET gamertag = 'CrazyIQ' WHERE LOWER(gamertag) = LOWER('TvcrZyIq');

-- Similarity: 88.0% | DB: 'Llucciiferrr' -> CSV: 'Llucciffferrr'
UPDATE players SET gamertag = 'Llucciffferrr' WHERE LOWER(gamertag) = LOWER('Llucciiferrr');

-- Similarity: 85.7% | DB: 'Breezsh' -> CSV: 'BBreesh'
UPDATE players SET gamertag = 'BBreesh' WHERE LOWER(gamertag) = LOWER('Breezsh');

-- Similarity: 80.0% | DB: 'HeIIaBoots' -> CSV: 'HellaBoots'
UPDATE players SET gamertag = 'HellaBoots' WHERE LOWER(gamertag) = LOWER('HeIIaBoots');

-- Similarity: 81.8% | DB: 'HeIIaHeavys' -> CSV: 'HellaHeavys'
UPDATE players SET gamertag = 'HellaHeavys' WHERE LOWER(gamertag) = LOWER('HeIIaHeavys');

-- Similarity: 80.0% | DB: 'iiSellii' -> CSV: 'IIsebII'
UPDATE players SET gamertag = 'IIsebII' WHERE LOWER(gamertag) = LOWER('iiSellii');

-- Similarity: 80.0% | DB: 'Iuhlocks' -> CSV: 'ILocksy'
UPDATE players SET gamertag = 'ILocksy' WHERE LOWER(gamertag) = LOWER('Iuhlocks');


COMMIT;
