#!/usr/bin/env python3
"""
Extract team information from WordPress XML export file.
"""

import xml.etree.ElementTree as ET
import json
import csv
from collections import defaultdict
from pathlib import Path


def parse_cdata(text):
    """Extract text from CDATA sections."""
    if text:
        return text.strip()
    return ""


def extract_team_data(xml_file):
    """Extract all team data from WordPress XML export."""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # Define namespaces
    namespaces = {
        'wp': 'http://wordpress.org/export/1.2/',
        'content': 'http://purl.org/rss/1.0/modules/content/',
        'dc': 'http://purl.org/dc/elements/1.1/',
    }
    
    teams = []
    
    # Find all item elements
    for item in root.findall('.//item'):
        # Check if this is a team post type
        post_type = item.find('wp:post_type', namespaces)
        if post_type is None or post_type.text != 'sp_team':
            continue
        
        team = {}
        
        # Basic information
        title = item.find('title')
        team['name'] = parse_cdata(title.text) if title is not None else ""
        
        link = item.find('link')
        team['url'] = link.text if link is not None else ""
        
        post_id = item.find('wp:post_id', namespaces)
        team['post_id'] = post_id.text if post_id is not None else ""
        
        post_date = item.find('wp:post_date', namespaces)
        team['post_date'] = post_date.text if post_date is not None else ""
        
        post_modified = item.find('wp:post_modified', namespaces)
        team['post_modified'] = post_modified.text if post_modified is not None else ""
        
        post_name = item.find('wp:post_name', namespaces)
        team['slug'] = post_name.text if post_name is not None else ""
        
        status = item.find('wp:status', namespaces)
        team['status'] = status.text if status is not None else ""
        
        # Categories (leagues, seasons)
        leagues = []
        seasons = []
        
        for category in item.findall('category'):
            domain = category.get('domain', '')
            nicename = category.get('nicename', '')
            text = parse_cdata(category.text) if category.text else ""
            
            if domain == 'sp_league':
                leagues.append({'nicename': nicename, 'name': text})
            elif domain == 'sp_season':
                seasons.append({'nicename': nicename, 'name': text})
        
        team['leagues'] = leagues
        team['seasons'] = seasons
        
        # Meta fields
        meta_fields = defaultdict(list)
        
        for postmeta in item.findall('wp:postmeta', namespaces):
            meta_key = postmeta.find('wp:meta_key', namespaces)
            meta_value = postmeta.find('wp:meta_value', namespaces)
            
            if meta_key is not None and meta_value is not None:
                key = parse_cdata(meta_key.text)
                value = parse_cdata(meta_value.text)
                
                # Skip WordPress internal meta fields (starting with _) except _sp_import
                if not key.startswith('_') or key in ['_sp_import']:
                    meta_fields[key].append(value)
        
        # Extract specific meta fields for teams
        team['abbreviation'] = meta_fields.get('sp_abbreviation', [''])[0]
        team['short_name'] = meta_fields.get('sp_short_name', [''])[0]
        team['twitter'] = meta_fields.get('sp_twitter', [''])[0]
        team['facebook'] = meta_fields.get('sp_facebook', [''])[0]
        team['url_meta'] = meta_fields.get('sp_url', [''])[0]
        
        # Store all meta fields
        team['all_meta'] = dict(meta_fields)
        
        teams.append(team)
    
    return teams


def save_json(teams, output_file):
    """Save teams data to JSON file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(teams, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(teams)} teams to {output_file}")


def save_csv(teams, output_file):
    """Save teams data to CSV file."""
    if not teams:
        print("No teams to save.")
        return
    
    # Flatten the data for CSV
    fieldnames = [
        'post_id', 'name', 'slug', 'url', 'status', 'post_date', 'post_modified',
        'abbreviation', 'short_name', 'twitter', 'facebook', 'url_meta',
        'leagues', 'seasons'
    ]
    
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for team in teams:
            row = {
                'post_id': team.get('post_id', ''),
                'name': team.get('name', ''),
                'slug': team.get('slug', ''),
                'url': team.get('url', ''),
                'status': team.get('status', ''),
                'post_date': team.get('post_date', ''),
                'post_modified': team.get('post_modified', ''),
                'abbreviation': team.get('abbreviation', ''),
                'short_name': team.get('short_name', ''),
                'twitter': team.get('twitter', ''),
                'facebook': team.get('facebook', ''),
                'url_meta': team.get('url_meta', ''),
                'leagues': '; '.join([l['name'] for l in team.get('leagues', [])]),
                'seasons': '; '.join([s['name'] for s in team.get('seasons', [])]),
            }
            writer.writerow(row)
    
    print(f"Saved {len(teams)} teams to {output_file}")


def main():
    # XML file provided in the prompt
    xml_file = Path('teams-hofleague.WordPress.2025-12-03 (1).xml')
    
    if not xml_file.exists():
        print(f"Error: {xml_file} not found!")
        return
    
    print(f"Extracting team data from {xml_file}...")
    teams = extract_team_data(xml_file)
    
    print(f"Found {len(teams)} teams")
    
    # Save to JSON
    json_file = Path('teams.json')
    save_json(teams, json_file)
    
    # Save to CSV
    csv_file = Path('teams.csv')
    save_csv(teams, csv_file)
    
    # Print summary
    print("\nSummary:")
    print(f"  Total teams: {len(teams)}")
    print(f"  Published teams: {sum(1 for t in teams if t.get('status') == 'publish')}")
    print(f"  Teams with Twitter: {sum(1 for t in teams if t.get('twitter'))}")


if __name__ == '__main__':
    main()

