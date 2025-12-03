#!/usr/bin/env python3
"""
Save database gamertags from Supabase query result to JSON file.
This script processes the raw query output.
"""

import json
import re

# The query result data (from Supabase MCP execute_sql)
# This would normally come from the MCP tool, but we'll parse it here
query_result_text = """
[{"gamertag":"|-Dreadz-|"},{"gamertag":"|GodSent|-"},{"gamertag":"a little to alot"},...]
"""

def extract_gamertags_from_query_result():
    """Extract gamertags from the Supabase query result."""
    # Since we can't directly access MCP tools from Python,
    # we'll need to manually paste the query result or load from a file
    print("To use this script:")
    print("1. Run: SELECT gamertag FROM players ORDER BY gamertag;")
    print("2. Copy the JSON result")
    print("3. Paste it into a file called 'query_result.json'")
    print("4. Run this script again")
    
    query_file = Path('query_result.json')
    if query_file.exists():
        with open(query_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Extract gamertags
        gamertags = [item['gamertag'] for item in data if 'gamertag' in item]
        
        # Save to db_gamertags.json
        output_data = [{'gamertag': gt} for gt in gamertags]
        with open('db_gamertags.json', 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        
        print(f"Saved {len(gamertags)} gamertags to db_gamertags.json")
    else:
        print(f"{query_file} not found. Please create it with the query results.")

if __name__ == '__main__':
    from pathlib import Path
    extract_gamertags_from_query_result()

