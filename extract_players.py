#!/usr/bin/env python3
"""
Extract player information from WordPress XML export file.
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


def extract_player_data(xml_file):
    """Extract all player data from WordPress XML export."""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # Define namespaces
    namespaces = {
        'wp': 'http://wordpress.org/export/1.2/',
        'content': 'http://purl.org/rss/1.0/modules/content/',
        'dc': 'http://purl.org/dc/elements/1.1/',
    }
    
    players = []
    
    # Find all items
    for item in root.findall('.//item'):
        # Check if this is a player post type
        post_type = item.find('wp:post_type', namespaces)
        if post_type is None or post_type.text != 'sp_player':
            continue
        
        player = {}
        
        # Basic information
        title = item.find('title')
        player['name'] = parse_cdata(title.text) if title is not None else ""
        
        link = item.find('link')
        player['url'] = link.text if link is not None else ""
        
        post_id = item.find('wp:post_id', namespaces)
        player['post_id'] = post_id.text if post_id is not None else ""
        
        post_date = item.find('wp:post_date', namespaces)
        player['post_date'] = post_date.text if post_date is not None else ""
        
        post_modified = item.find('wp:post_modified', namespaces)
        player['post_modified'] = post_modified.text if post_modified is not None else ""
        
        post_name = item.find('wp:post_name', namespaces)
        player['slug'] = post_name.text if post_name is not None else ""
        
        status = item.find('wp:status', namespaces)
        player['status'] = status.text if status is not None else ""
        
        # Categories (positions, leagues, seasons)
        positions = []
        leagues = []
        seasons = []
        
        for category in item.findall('category'):
            domain = category.get('domain', '')
            nicename = category.get('nicename', '')
            text = parse_cdata(category.text) if category.text else ""
            
            if domain == 'sp_position':
                positions.append({'nicename': nicename, 'name': text})
            elif domain == 'sp_league':
                leagues.append({'nicename': nicename, 'name': text})
            elif domain == 'sp_season':
                seasons.append({'nicename': nicename, 'name': text})
        
        player['positions'] = positions
        player['leagues'] = leagues
        player['seasons'] = seasons
        
        # Meta fields
        meta_fields = defaultdict(list)
        
        for postmeta in item.findall('wp:postmeta', namespaces):
            meta_key = postmeta.find('wp:meta_key', namespaces)
            meta_value = postmeta.find('wp:meta_value', namespaces)
            
            if meta_key is not None and meta_value is not None:
                key = parse_cdata(meta_key.text)
                value = parse_cdata(meta_value.text)
                
                # Skip WordPress internal meta fields (starting with _)
                if not key.startswith('_') or key in ['_sp_import']:
                    meta_fields[key].append(value)
        
        # Extract specific meta fields
        player['jersey_number'] = meta_fields.get('sp_number', [''])[0]
        player['current_team_id'] = meta_fields.get('sp_current_team', [''])[0]
        player['nationality'] = meta_fields.get('sp_nationality', [''])[0]
        player['twitter'] = meta_fields.get('sp_twitter', [''])[0]
        
        # Team IDs (can be multiple)
        player['team_ids'] = meta_fields.get('sp_team', [])
        
        # Complex fields (may contain serialized data)
        player['metrics'] = meta_fields.get('sp_metrics', [''])[0]
        player['leagues_meta'] = meta_fields.get('sp_leagues', [''])[0]
        player['statistics'] = meta_fields.get('sp_statistics', [''])[0]
        player['assignments'] = meta_fields.get('sp_assignments', [''])[0]
        
        # Store all meta fields
        player['all_meta'] = dict(meta_fields)
        
        players.append(player)
    
    return players


def save_json(players, output_file):
    """Save players data to JSON file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(players, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(players)} players to {output_file}")


def save_csv(players, output_file):
    """Save players data to CSV file."""
    if not players:
        print("No players to save.")
        return
    
    # Flatten the data for CSV
    fieldnames = [
        'post_id', 'name', 'slug', 'url', 'status', 'post_date', 'post_modified',
        'jersey_number', 'current_team_id', 'nationality', 'twitter',
        'positions', 'leagues', 'seasons', 'team_ids', 'metrics', 
        'leagues_meta', 'statistics', 'assignments'
    ]
    
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for player in players:
            row = {
                'post_id': player.get('post_id', ''),
                'name': player.get('name', ''),
                'slug': player.get('slug', ''),
                'url': player.get('url', ''),
                'status': player.get('status', ''),
                'post_date': player.get('post_date', ''),
                'post_modified': player.get('post_modified', ''),
                'jersey_number': player.get('jersey_number', ''),
                'current_team_id': player.get('current_team_id', ''),
                'nationality': player.get('nationality', ''),
                'twitter': player.get('twitter', ''),
                'positions': '; '.join([p['name'] for p in player.get('positions', [])]),
                'leagues': '; '.join([l['name'] for l in player.get('leagues', [])]),
                'seasons': '; '.join([s['name'] for s in player.get('seasons', [])]),
                'team_ids': '; '.join(player.get('team_ids', [])),
                'metrics': player.get('metrics', ''),
                'leagues_meta': player.get('leagues_meta', ''),
                'statistics': player.get('statistics', ''),
                'assignments': player.get('assignments', ''),
            }
            writer.writerow(row)
    
    print(f"Saved {len(players)} players to {output_file}")


def main():
    xml_file = Path('hofleague.WordPress.2025-12-03.xml')
    
    if not xml_file.exists():
        print(f"Error: {xml_file} not found!")
        return
    
    print(f"Extracting player data from {xml_file}...")
    players = extract_player_data(xml_file)
    
    print(f"Found {len(players)} players")
    
    # Save to JSON
    json_file = Path('players.json')
    save_json(players, json_file)
    
    # Save to CSV
    csv_file = Path('players.csv')
    save_csv(players, csv_file)
    
    # Print summary
    print("\nSummary:")
    print(f"  Total players: {len(players)}")
    print(f"  Published players: {sum(1 for p in players if p.get('status') == 'publish')}")
    print(f"  Players with positions: {sum(1 for p in players if p.get('positions'))}")
    print(f"  Players with teams: {sum(1 for p in players if p.get('team_ids'))}")


if __name__ == '__main__':
    main()

