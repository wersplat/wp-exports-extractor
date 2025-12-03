# Player Gamertag Comparison and Update Tool

This set of scripts helps you compare player names from a WordPress XML export (converted to CSV) against the current `gamertag` values in your Supabase database. It identifies discrepancies in spelling and casing, and generates SQL scripts to update the database to match the XML source.

## Prerequisites

1.  **`players.csv`**: This file contains the player data extracted from the WordPress XML export. It should be in the root directory.
2.  **`db_gamertags.json`**: This file contains the current list of gamertags from your database.

### How to refresh `db_gamertags.json`

If you need to fetch the latest data from the database:

1.  Run the following SQL query in your Supabase SQL Editor:
    ```sql
    SELECT gamertag FROM players ORDER BY gamertag;
    ```
2.  Copy the resulting JSON output.
3.  Paste it into `db_gamertags.json`.
    *   *Note: Ensure the file contains a valid JSON array of objects, e.g., `[{"gamertag": "Name1"}, {"gamertag": "Name2"}]`.*

## 1. Run the Comparison

Execute the comparison script to analyze differences between the CSV and the database:

```bash
python3 do_comparison.py
```

This script will:
*   Load gamertags from `players.csv` and `db_gamertags.json`.
*   Compare names to find:
    *   **Exact matches**: Names that are identical.
    *   **Case differences**: Names that match but have different capitalization (e.g., "PlayerOne" vs "playerone").
    *   **Similar names**: Names that are close but not identical (potential typos or slight variations).
    *   **Missing names**: Names present in one source but not the other.
*   Generate a detailed report in `name_comparison_report.json`.
*   Print a summary to the console.

## 2. Generate Update Scripts

Once the comparison is complete, run the update script to generate SQL files for fixing the discrepancies:

```bash
python3 update_gamertags.py
```

This will create three files:

1.  **`case_differences_updates.sql`**: Contains SQL `UPDATE` statements for records where the name matches exactly but the casing is different. **These are generally safe to run immediately.**
2.  **`similar_names_updates.sql`**: Contains SQL `UPDATE` statements for names that are similar but not identical. **Review this file carefully before running.**
3.  **`similar_names_review.json`**: A JSON file listing the similar matches for easier programmatic review if needed.

## 3. Apply Updates

### Case Differences
Run the generated SQL file against your database to fix capitalization issues:

```bash
# You can run this via the Supabase Dashboard SQL Editor
# Open case_differences_updates.sql, copy the content, and execute it.
```

### Similar Names
1.  Open `similar_names_updates.sql`.
2.  Review each update. Comments in the file show the similarity score and the old vs. new values.
3.  Remove or comment out any updates you do **not** want to apply.
4.  Execute the remaining SQL commands in your database.

## Files Overview

*   `do_comparison.py`: Main script to perform the comparison.
*   `update_gamertags.py`: Generates SQL update scripts based on the comparison report.
*   `compare_names.py`: Contains the logic for fuzzy matching and name normalization.
*   `fix_json.py`: Utility script to fix common JSON formatting errors in the `db_gamertags.json` file if manual pasting introduced issues.
*   `name_comparison_report.json`: The output of the comparison, containing all categorized matches.

