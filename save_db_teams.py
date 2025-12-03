#!/usr/bin/env python3
"""
Save database teams from Supabase query result to JSON file.
This script helps fetch and save the team data for comparison.
"""

import json
from pathlib import Path

def main():
    print("Fetching teams from Supabase database...")
    print("(This requires Supabase MCP connection instructions)")
    print()
    print("Please run the following SQL query manually using the MCP tool:")
    print("  SELECT name, team_twitter FROM teams ORDER BY name;")
    print()
    print("Then save the results to 'db_teams.json' in this format:")
    print('  [{"name": "Team Name", "team_twitter": "handle"}, ...]')
    print()
    
    # Check if file already exists
    db_file = Path('db_teams.json')
    if db_file.exists():
        try:
            with open(db_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            print(f"Found existing db_teams.json with {len(data)} teams.")
        except json.JSONDecodeError:
            print("Found db_teams.json but it contains invalid JSON.")
    else:
        print(f"{db_file} not found. Please create it with the query results.")

if __name__ == '__main__':
    main()

