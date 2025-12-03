#!/usr/bin/env python3
"""
Run the player name comparison using Supabase MCP tools.
"""

import subprocess
import json
import sys
from pathlib import Path

# Import the comparison functions
from compare_names import compare_names, print_report, save_report

def main():
    csv_file = Path('players.csv')
    
    if not csv_file.exists():
        print(f"Error: {csv_file} not found!")
        return
    
    print("Fetching gamertags from Supabase database...")
    print("(This requires Supabase MCP connection)")
    print()
    print("Please run the following SQL query manually:")
    print("  SELECT gamertag FROM players ORDER BY gamertag;")
    print()
    print("Then save the results to 'db_gamertags.json' in this format:")
    print('  [{"gamertag": "Player1"}, {"gamertag": "Player2"}, ...]')
    print()
    print("Alternatively, you can use the MCP Supabase tools directly.")
    
    # Try to load from file
    db_file = Path('db_gamertags.json')
    if db_file.exists():
        with open(db_file, 'r', encoding='utf-8') as f:
            db_data = json.load(f)
            db_gamertags = [item['gamertag'] for item in db_data if 'gamertag' in item]
        print(f"Loaded {len(db_gamertags)} gamertags from {db_file}")
    else:
        print(f"\n{db_file} not found. Cannot proceed without database gamertags.")
        return
    
    print("Comparing names...")
    results = compare_names(csv_file, db_gamertags)
    
    print_report(results)
    
    report_file = Path('name_comparison_report.json')
    save_report(results, report_file)

if __name__ == '__main__':
    main()

