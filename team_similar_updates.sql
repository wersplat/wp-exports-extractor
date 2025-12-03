-- SQL Updates for Similar Team Names (REQUIRES REVIEW)
-- Generated from team_comparison_report.json
-- Total records: 118

BEGIN;

-- Similarity: 97.3% | DB: 'My Brothers Keeper' -> CSV: 'My Brother's Keeper'
UPDATE teams SET name = 'My Brother''s Keeper' WHERE LOWER(name) = LOWER('My Brothers Keeper');


-- Similarity: 90.9% | DB: 'Unorthodox 5' -> CSV: 'Unorthodox'
UPDATE teams SET name = 'Unorthodox' WHERE LOWER(name) = LOWER('Unorthodox 5');


-- Similarity: 90.0% | DB: 'La Montana' -> CSV: 'La Montaña'
UPDATE teams SET name = 'La Montaña' WHERE LOWER(name) = LOWER('La Montana');

-- Similarity: 92.9% | DB: 'Ships n Salsa' -> CSV: 'Ships and Salsa'
UPDATE teams SET name = 'Ships and Salsa' WHERE LOWER(name) = LOWER('Ships n Salsa');


-- Similarity: 95.7% | DB: 'Omnipresent' -> CSV: 'Omni Present'
UPDATE teams SET name = 'Omni Present' WHERE LOWER(name) = LOWER('Omnipresent');



-- Similarity: 92.9% | DB: 'Move in Silence' -> CSV: 'MoveinSilence'
UPDATE teams SET name = 'MoveinSilence' WHERE LOWER(name) = LOWER('Move in Silence');

-- Similarity: 96.6% | DB: 'Bench All Stars' -> CSV: 'Bench Allstars'
UPDATE teams SET name = 'Bench Allstars' WHERE LOWER(name) = LOWER('Bench All Stars');

-- Similarity: 88.9% | DB: 'First Degree 2K' -> CSV: 'FIRST DEGREE'
UPDATE teams SET name = 'FIRST DEGREE' WHERE LOWER(name) = LOWER('First Degree 2K');


-- Similarity: 88.9% | DB: 'Why Not Us' -> CSV: 'WHYNOTUS'
UPDATE teams SET name = 'WHYNOTUS' WHERE LOWER(name) = LOWER('Why Not Us');


-- Similarity: 90.0% | DB: 'Throwdown' -> CSV: 'Throwdown2k'
UPDATE teams SET name = 'Throwdown2k' WHERE LOWER(name) = LOWER('Throwdown');


-- Similarity: 88.9% | DB: 'No Tolerance' -> CSV: 'No Tolerance 2K'
UPDATE teams SET name = 'No Tolerance 2K' WHERE LOWER(name) = LOWER('No Tolerance');


-- Similarity: 97.1% | DB: 'Fire Sticks Gaming' -> CSV: 'Firesticks Gaming'
UPDATE teams SET name = 'Firesticks Gaming' WHERE LOWER(name) = LOWER('Fire Sticks Gaming');


-- Similarity: 82.4% | DB: 'Rebirth 2K' -> CSV: 'REBIRTH'
UPDATE teams SET name = 'REBIRTH' WHERE LOWER(name) = LOWER('Rebirth 2K');

-- Similarity: 95.7% | DB: 'Quit Playin' -> CSV: 'Quit Playing'
UPDATE teams SET name = 'Quit Playing' WHERE LOWER(name) = LOWER('Quit Playin');

-- Similarity: 87.0% | DB: 'Redefining Greatness (RDG)' -> CSV: 'ReDeFininG GreaTnesS'
UPDATE teams SET name = 'ReDeFininG GreaTnesS' WHERE LOWER(name) = LOWER('Redefining Greatness (RDG)');

-- Similarity: 81.2% | DB: 'Tunnel Vision' -> CSV: 'Tunnel Vision x H20'
UPDATE teams SET name = 'Tunnel Vision x H20' WHERE LOWER(name) = LOWER('Tunnel Vision');


-- Similarity: 90.9% | DB: 'Fade 5' -> CSV: 'Fade5'
UPDATE teams SET name = 'Fade5' WHERE LOWER(name) = LOWER('Fade 5');

-- Similarity: 90.9% | DB: 'Alwayz Open' -> CSV: 'Always Open'
UPDATE teams SET name = 'Always Open' WHERE LOWER(name) = LOWER('Alwayz Open');

-- Similarity: 80.0% | DB: 'What is Comp (WIC)' -> CSV: 'What Is Comp'
UPDATE teams SET name = 'What Is Comp' WHERE LOWER(name) = LOWER('What is Comp (WIC)');


-- Similarity: 96.6% | DB: 'InFuria Esport' -> CSV: 'InFuria E-sport'
UPDATE teams SET name = 'InFuria E-sport' WHERE LOWER(name) = LOWER('InFuria Esport');


-- Similarity: 96.3% | DB: 'Zero Tolerance' -> CSV: 'ZeroTolerance'
UPDATE teams SET name = 'ZeroTolerance' WHERE LOWER(name) = LOWER('Zero Tolerance');

-- Similarity: 95.7% | DB: 'Revenge Tour' -> CSV: 'RevengeTour'
UPDATE teams SET name = 'RevengeTour' WHERE LOWER(name) = LOWER('Revenge Tour');


-- Similarity: 94.7% | DB: 'Five Star' -> CSV: 'Five Stars'
UPDATE teams SET name = 'Five Stars' WHERE LOWER(name) = LOWER('Five Star');

-- Similarity: 90.9% | DB: 'Bxrn Notice' -> CSV: 'Burn Notice'
UPDATE teams SET name = 'Burn Notice' WHERE LOWER(name) = LOWER('Bxrn Notice');

-- Similarity: 90.0% | DB: 'Nastyworks' -> CSV: 'Nastyworkz'
UPDATE teams SET name = 'Nastyworkz' WHERE LOWER(name) = LOWER('Nastyworks');

-- Similarity: 85.7% | DB: 'Glaciers of Ice' -> CSV: 'Siba Glaciers of Ice'
UPDATE teams SET name = 'Siba Glaciers of Ice' WHERE LOWER(name) = LOWER('Glaciers of Ice');


-- Similarity: 86.4% | DB: 'Nobody Plays Harder (NPH)' -> CSV: 'Nobody Plays Harder'
UPDATE teams SET name = 'Nobody Plays Harder' WHERE LOWER(name) = LOWER('Nobody Plays Harder (NPH)');

-- Similarity: 80.0% | DB: 'Akatsuki' -> CSV: 'The Akatsuki'
UPDATE teams SET name = 'The Akatsuki' WHERE LOWER(name) = LOWER('Akatsuki');

-- Similarity: 97.1% | DB: 'Team Always Hungry' -> CSV: 'Team AlwaysHungry'
UPDATE teams SET name = 'Team AlwaysHungry' WHERE LOWER(name) = LOWER('Team Always Hungry');

-- Similarity: 96.0% | DB: 'AlwaysLurkin' -> CSV: 'Always Lurkin'
UPDATE teams SET name = 'Always Lurkin' WHERE LOWER(name) = LOWER('AlwaysLurkin');

-- Similarity: 97.4% | DB: 'Twenty Stars eSports' -> CSV: 'TwentyStars eSports'
UPDATE teams SET name = 'TwentyStars eSports' WHERE LOWER(name) = LOWER('Twenty Stars eSports');

-- Similarity: 94.7% | DB: 'Orgless 2K' -> CSV: 'Orgless2K'
UPDATE teams SET name = 'Orgless2K' WHERE LOWER(name) = LOWER('Orgless 2K');


-- Similarity: 95.2% | DB: 'MadVillanz' -> CSV: 'Madvillainz'
UPDATE teams SET name = 'Madvillainz' WHERE LOWER(name) = LOWER('MadVillanz');


-- Similarity: 95.2% | DB: 'Generation of Miracles' -> CSV: 'generationofmiracles'
UPDATE teams SET name = 'generationofmiracles' WHERE LOWER(name) = LOWER('Generation of Miracles');

-- Similarity: 80.0% | DB: 'Most Hated (MH)' -> CSV: 'Most Hated'
UPDATE teams SET name = 'Most Hated' WHERE LOWER(name) = LOWER('Most Hated (MH)');

-- Similarity: 96.0% | DB: 'Galia Esport' -> CSV: 'Galia Esports'
UPDATE teams SET name = 'Galia Esports' WHERE LOWER(name) = LOWER('Galia Esport');


-- Similarity: 96.0% | DB: 'No Hesitation' -> CSV: 'NoHesitation'
UPDATE teams SET name = 'NoHesitation' WHERE LOWER(name) = LOWER('No Hesitation');


-- Similarity: 97.0% | DB: 'One Ball One Team' -> CSV: 'one Ballone Team'
UPDATE teams SET name = 'one Ballone Team' WHERE LOWER(name) = LOWER('One Ball One Team');

-- Similarity: 88.0% | DB: '3 The Hard Way' -> CSV: '3TheHardWay'
UPDATE teams SET name = '3TheHardWay' WHERE LOWER(name) = LOWER('3 The Hard Way');

-- Similarity: 84.2% | DB: 'Earned Not Given (ENG)' -> CSV: 'Earned Not Given'
UPDATE teams SET name = 'Earned Not Given' WHERE LOWER(name) = LOWER('Earned Not Given (ENG)');

-- Similarity: 96.3% | DB: 'Elusive Pro Am' -> CSV: 'Elusive ProAm'
UPDATE teams SET name = 'Elusive ProAm' WHERE LOWER(name) = LOWER('Elusive Pro Am');

-- Similarity: 84.2% | DB: 'Fearless' -> CSV: 'Fearless 2k'
UPDATE teams SET name = 'Fearless 2k' WHERE LOWER(name) = LOWER('Fearless');

-- Similarity: 80.0% | DB: 'Hooligans' -> CSV: 'Hooligan 2K'
UPDATE teams SET name = 'Hooligan 2K' WHERE LOWER(name) = LOWER('Hooligans');

-- Similarity: 81.2% | DB: 'Kiss My Timbs (KMT)' -> CSV: 'Kiss My Timbs'
UPDATE teams SET name = 'Kiss My Timbs' WHERE LOWER(name) = LOWER('Kiss My Timbs (KMT)');

-- Similarity: 94.7% | DB: 'Lights Out' -> CSV: 'Lightsout'
UPDATE teams SET name = 'Lightsout' WHERE LOWER(name) = LOWER('Lights Out');

-- Similarity: 83.3% | DB: 'New Vision' -> CSV: 'New vision hof'
UPDATE teams SET name = 'New vision hof' WHERE LOWER(name) = LOWER('New Vision');

-- Similarity: 93.8% | DB: 'Only The Greatest' -> CSV: 'OnlyTheGreatest'
UPDATE teams SET name = 'OnlyTheGreatest' WHERE LOWER(name) = LOWER('Only The Greatest');

-- Similarity: 95.2% | DB: 'Quit Playin' -> CSV: 'QuitPlayin'
UPDATE teams SET name = 'QuitPlayin' WHERE LOWER(name) = LOWER('Quit Playin');

-- Similarity: 92.3% | DB: 'Self Made Gang' -> CSV: 'SelfMadeGang'
UPDATE teams SET name = 'SelfMadeGang' WHERE LOWER(name) = LOWER('Self Made Gang');

-- Similarity: 93.3% | DB: 'The 6IXX' -> CSV: 'The 6ix'
UPDATE teams SET name = 'The 6ix' WHERE LOWER(name) = LOWER('The 6IXX');

-- Similarity: 92.9% | DB: 'They Doubt Us' -> CSV: 'They Doubted Us'
UPDATE teams SET name = 'They Doubted Us' WHERE LOWER(name) = LOWER('They Doubt Us');

-- Similarity: 96.0% | DB: 'UNT Assasins' -> CSV: 'UNT Assassins'
UPDATE teams SET name = 'UNT Assassins' WHERE LOWER(name) = LOWER('UNT Assasins');

-- Similarity: 96.8% | DB: 'BESIKTAS ESPORT' -> CSV: 'Besiktas Esports'
UPDATE teams SET name = 'Besiktas Esports' WHERE LOWER(name) = LOWER('BESIKTAS ESPORT');

-- Similarity: 87.5% | DB: 'Opulance' -> CSV: 'Opulence'
UPDATE teams SET name = 'Opulence' WHERE LOWER(name) = LOWER('Opulance');

-- Similarity: 89.7% | DB: 'The Blueprint 4L' -> CSV: 'The Blueprint'
UPDATE teams SET name = 'The Blueprint' WHERE LOWER(name) = LOWER('The Blueprint 4L');

-- Similarity: 92.9% | DB: 'Ruska Roma Prep' -> CSV: 'RuskaRomaPrep'
UPDATE teams SET name = 'RuskaRomaPrep' WHERE LOWER(name) = LOWER('Ruska Roma Prep');

-- Similarity: 96.3% | DB: 'Trained to Go' -> CSV: 'TARAINED TO GO'
UPDATE teams SET name = 'TARAINED TO GO' WHERE LOWER(name) = LOWER('Trained to Go');

-- Similarity: 97.0% | DB: 'Hoopers Next Door' -> CSV: 'Hoopers NXT Door'
UPDATE teams SET name = 'Hoopers NXT Door' WHERE LOWER(name) = LOWER('Hoopers Next Door');

-- Similarity: 85.7% | DB: 'Boomerz' -> CSV: 'BOOM3Rz'
UPDATE teams SET name = 'BOOM3Rz' WHERE LOWER(name) = LOWER('Boomerz');

-- Similarity: 95.2% | DB: 'Zentastic 5' -> CSV: 'Zentastic5'
UPDATE teams SET name = 'Zentastic5' WHERE LOWER(name) = LOWER('Zentastic 5');

-- Similarity: 88.9% | DB: '6ix Fatals' -> CSV: '6ixFatal'
UPDATE teams SET name = '6ixFatal' WHERE LOWER(name) = LOWER('6ix Fatals');

-- Similarity: 95.2% | DB: 'Kill Switch' -> CSV: 'KillSwitch'
UPDATE teams SET name = 'KillSwitch' WHERE LOWER(name) = LOWER('Kill Switch');

-- Similarity: 81.8% | DB: 'The Franchise' -> CSV: 'Franchise'
UPDATE teams SET name = 'Franchise' WHERE LOWER(name) = LOWER('The Franchise');

-- Similarity: 94.1% | DB: 'The Cabin' -> CSV: 'TheCabin'
UPDATE teams SET name = 'TheCabin' WHERE LOWER(name) = LOWER('The Cabin');

-- Similarity: 83.3% | DB: 'Spaced Out' -> CSV: 'Spaced Out SOE'
UPDATE teams SET name = 'Spaced Out SOE' WHERE LOWER(name) = LOWER('Spaced Out');

-- Similarity: 96.3% | DB: 'Nopressure 2k' -> CSV: 'No pressure 2k'
UPDATE teams SET name = 'No pressure 2k' WHERE LOWER(name) = LOWER('Nopressure 2k');

-- Similarity: 91.7% | DB: 'BC MOSKOWSKY' -> CSV: 'BC Moscowsky'
UPDATE teams SET name = 'BC Moscowsky' WHERE LOWER(name) = LOWER('BC MOSKOWSKY');

-- Similarity: 89.7% | DB: 'House Of H.O.P.E' -> CSV: 'House of Hope'
UPDATE teams SET name = 'House of Hope' WHERE LOWER(name) = LOWER('House Of H.O.P.E');


COMMIT;
