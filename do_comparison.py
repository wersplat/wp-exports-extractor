#!/usr/bin/env python3
"""Run the comparison using fetched database gamertags."""

import json
import sys
from pathlib import Path

# Import comparison functions
sys.path.insert(0, str(Path(__file__).parent))
from compare_names import compare_names, print_report, save_report

# Helper to load gamertags from file
def load_db_gamertags():
    db_file = Path('db_gamertags.json')
    if db_file.exists():
        with open(db_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [item['gamertag'] for item in data]
    return []

def main():
    csv_file = Path('players.csv')
    
    if not csv_file.exists():
        print(f"Error: {csv_file} not found!")
        return
    
    # Load database gamertags
    db_gamertags = load_db_gamertags()
    
    if not db_gamertags:
        print("Error: Could not load gamertags from db_gamertags.json")
        print("Please fetch fresh data from the database first.")
        return
    
    print(f"Loaded {len(db_gamertags)} gamertags from database file")
    print("Comparing with CSV file...")
    
    # Compare
    results = compare_names(csv_file, db_gamertags)
    
    # Print report
    print_report(results)
    
    # Save detailed report
    report_file = Path('name_comparison_report.json')
    save_report(results, report_file)

if __name__ == '__main__':
    main()
