#!/usr/bin/env python3
"""
Generate SQL updates to fix gamertag spellings in the database.
Reads from name_comparison_report.json.
"""

import json
import os
from pathlib import Path

def escape_sql_string(s):
    """Escape single quotes in SQL strings."""
    if s is None:
        return ''
    return s.replace("'", "''")

def generate_update_sql(table, set_field, set_value, where_field, where_value):
    """Generate a single SQL UPDATE statement."""
    safe_set_value = escape_sql_string(set_value)
    safe_where_value = escape_sql_string(where_value)
    
    # Using LOWER() for case-insensitive matching on the WHERE clause to be safe,
    # although for case differences, exact string match might fail if DB collation is case-sensitive.
    # The plan specified: WHERE LOWER(gamertag) = LOWER('current_db_name')
    return f"UPDATE {table} SET {set_field} = '{safe_set_value}' WHERE LOWER({where_field}) = LOWER('{safe_where_value}');"

def main():
    report_file = Path('name_comparison_report.json')
    
    if not report_file.exists():
        print(f"Error: {report_file} not found!")
        return

    print(f"Loading report from {report_file}...")
    with open(report_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    case_differences = data.get('case_differences', [])
    similar_names = data.get('similar_names', [])

    print(f"Found {len(case_differences)} case differences.")
    print(f"Found {len(similar_names)} similar names.")

    # 1. Handle Case Differences (Safe Updates)
    case_diff_sql_file = Path('case_differences_updates.sql')
    print(f"\nGenerating SQL for case differences -> {case_diff_sql_file}")
    
    with open(case_diff_sql_file, 'w', encoding='utf-8') as f:
        f.write("-- SQL Updates for Case Differences\n")
        f.write(f"-- Generated from {report_file}\n")
        f.write(f"-- Total records: {len(case_differences)}\n\n")
        f.write("BEGIN;\n\n")
        
        for item in case_differences:
            db_val = item['db_gamertag']
            csv_val = item['csv_name']
            sql = generate_update_sql('players', 'gamertag', csv_val, 'gamertag', db_val)
            f.write(f"{sql}\n")
            
        f.write("\nCOMMIT;\n")

    # 2. Handle Similar Names (Review Required)
    similar_sql_file = Path('similar_names_updates.sql')
    similar_review_file = Path('similar_names_review.json')
    
    print(f"Generating SQL for similar names -> {similar_sql_file}")
    print(f"Generating review JSON -> {similar_review_file}")
    
    # Generate Review JSON
    with open(similar_review_file, 'w', encoding='utf-8') as f:
        json.dump(similar_names, f, indent=2, ensure_ascii=False)

    # Generate SQL
    with open(similar_sql_file, 'w', encoding='utf-8') as f:
        f.write("-- SQL Updates for Similar Names (REQUIRES REVIEW)\n")
        f.write(f"-- Generated from {report_file}\n")
        f.write(f"-- Total records: {len(similar_names)}\n\n")
        f.write("BEGIN;\n\n")
        
        for item in similar_names:
            db_val = item['db_gamertag']
            csv_val = item['csv_name']
            similarity = item.get('similarity', 'N/A')
            
            f.write(f"-- Similarity: {similarity}% | DB: '{db_val}' -> CSV: '{csv_val}'\n")
            sql = generate_update_sql('players', 'gamertag', csv_val, 'gamertag', db_val)
            f.write(f"{sql}\n\n")
            
        f.write("\nCOMMIT;\n")

    print("\nSummary:")
    print(f"  - {case_diff_sql_file}: {len(case_differences)} updates (Ready to run)")
    print(f"  - {similar_sql_file}: {len(similar_names)} updates (Review recommended)")
    print(f"  - {similar_review_file}: JSON data for review")

if __name__ == '__main__':
    main()

