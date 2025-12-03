-- SQL Updates for Similar Names (REQUIRES REVIEW)
-- Generated from name_comparison_report.json
-- Total records: 21

BEGIN;

-- Similarity: 93.8% | DB: 'DefensivelstTeam' -> CSV: 'Defensive1stTeam'
UPDATE players SET gamertag = 'Defensive1stTeam' WHERE LOWER(gamertag) = LOWER('DefensivelstTeam');

-- Similarity: 91.7% | DB: 'DynastyxTay2k' -> CSV: 'DynastyxTay'
UPDATE players SET gamertag = 'DynastyxTay' WHERE LOWER(gamertag) = LOWER('DynastyxTay2k');


-- Similarity: 92.3% | DB: 'TonyFrmTheSix' -> CSV: 'Tonyfrmthe6ix'
UPDATE players SET gamertag = 'Tonyfrmthe6ix' WHERE LOWER(gamertag) = LOWER('TonyFrmTheSix');

-- Similarity: 94.1% | DB: 'Alsmoove' -> CSV: 'Alsmoovee'
UPDATE players SET gamertag = 'Alsmoovee' WHERE LOWER(gamertag) = LOWER('Alsmoove');

-- Similarity: 94.7% | DB: 'outyxshyne' -> CSV: 'outxshyne'
UPDATE players SET gamertag = 'outxshyne' WHERE LOWER(gamertag) = LOWER('outyxshyne');



COMMIT;
