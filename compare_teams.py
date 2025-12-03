#!/usr/bin/env python3
"""
Compare team names from WordPress XML export against database teams.
"""

import csv
import json
from pathlib import Path
from collections import defaultdict
from difflib import SequenceMatcher


def similarity(a, b):
    """Calculate similarity ratio between two strings."""
    if not a or not b:
        return 0
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def normalize_name(name):
    """Normalize name for comparison (lowercase, strip whitespace)."""
    if not name:
        return ""
    return name.strip().lower()


def compare_teams(csv_file, db_teams):
    """Compare CSV team names with database teams."""
    
    # Read CSV teams
    csv_teams = {}
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            slug = row.get('slug', '')
            # Skip teams with slugs containing "__trashed"
            if '__trashed' in slug:
                continue
                
            name = row.get('name', '').strip()
            if name:
                csv_teams[name] = {
                    'slug': slug,
                    'post_id': row.get('post_id', ''),
                    'status': row.get('status', ''),
                    'twitter': row.get('twitter', ''),
                }
    
    # Normalize DB teams for comparison
    # db_teams is a list of dicts: [{'name': 'Team Name', 'team_twitter': 'handle'}, ...]
    db_normalized = {}
    for team in db_teams:
        name = team.get('name', '')
        if name:
            db_normalized[normalize_name(name)] = team
            
    csv_normalized = {normalize_name(k): v for k, v in csv_teams.items()}
    
    # Find matches and differences
    exact_matches = []
    case_differences = []
    csv_only = []
    db_only = []
    similar_names = []
    
    # Check CSV names against DB
    for csv_name, csv_data in csv_teams.items():
        csv_norm = normalize_name(csv_name)
        
        if csv_norm in db_normalized:
            db_team = db_normalized[csv_norm]
            db_name = db_team['name']
            
            if csv_name == db_name:
                exact_matches.append({
                    'csv_name': csv_name,
                    'db_name': db_name,
                    'slug': csv_data['slug'],
                    'post_id': csv_data['post_id'],
                    'csv_twitter': csv_data['twitter'],
                    'db_twitter': db_team.get('team_twitter'),
                })
            else:
                case_differences.append({
                    'csv_name': csv_name,
                    'db_name': db_name,
                    'slug': csv_data['slug'],
                    'post_id': csv_data['post_id'],
                })
        else:
            # Check for similar names (fuzzy matching)
            best_match = None
            best_similarity = 0
            
            for db_team in db_teams:
                db_name = db_team.get('name', '')
                sim = similarity(csv_name, db_name)
                if sim > best_similarity and sim >= 0.8:  # 80% similarity threshold
                    best_similarity = sim
                    best_match = db_name
            
            if best_match:
                similar_names.append({
                    'csv_name': csv_name,
                    'db_name': best_match,
                    'similarity': round(best_similarity * 100, 1),
                    'slug': csv_data['slug'],
                    'post_id': csv_data['post_id'],
                })
            else:
                csv_only.append({
                    'csv_name': csv_name,
                    'slug': csv_data['slug'],
                    'post_id': csv_data['post_id'],
                    'status': csv_data['status'],
                    'twitter': csv_data['twitter'],
                })
    
    # Find DB-only names
    for db_team in db_teams:
        db_name = db_team.get('name', '')
        db_norm = normalize_name(db_name)
        if db_norm not in csv_normalized:
            db_only.append({
                'db_name': db_name,
                'twitter': db_team.get('team_twitter'),
            })
    
    return {
        'exact_matches': exact_matches,
        'case_differences': case_differences,
        'csv_only': csv_only,
        'db_only': db_only,
        'similar_names': similar_names,
    }


def print_report(results):
    """Print comparison report."""
    print("=" * 80)
    print("TEAM NAME COMPARISON REPORT")
    print("=" * 80)
    print()
    
    print(f"📊 SUMMARY")
    print(f"   Exact matches: {len(results['exact_matches'])}")
    print(f"   Case differences: {len(results['case_differences'])}")
    print(f"   CSV only (not in DB): {len(results['csv_only'])}")
    print(f"   DB only (not in CSV): {len(results['db_only'])}")
    print(f"   Similar names (potential matches): {len(results['similar_names'])}")
    print()
    
    if results['case_differences']:
        print("=" * 80)
        print("🔤 CASE DIFFERENCES")
        print("=" * 80)
        for item in sorted(results['case_differences'], key=lambda x: x['csv_name'].lower()):
            print(f"   CSV: '{item['csv_name']}'")
            print(f"   DB:  '{item['db_name']}'")
            print(f"   Slug: {item['slug']}")
            print()
    
    if results['similar_names']:
        print("=" * 80)
        print("🔍 SIMILAR NAMES (Potential Matches)")
        print("=" * 80)
        for item in sorted(results['similar_names'], key=lambda x: x['similarity'], reverse=True)[:50]:
            print(f"   CSV: '{item['csv_name']}'")
            print(f"   DB:  '{item['db_name']}'")
            print(f"   Similarity: {item['similarity']}%")
            print(f"   Slug: {item['slug']}")
            print()
        if len(results['similar_names']) > 50:
            print(f"   ... and {len(results['similar_names']) - 50} more")
    
    if results['csv_only']:
        print("=" * 80)
        print("📝 CSV ONLY (Not found in database)")
        print("=" * 80)
        # Group by status
        by_status = defaultdict(list)
        for item in results['csv_only']:
            by_status[item['status']].append(item)
        
        for status in sorted(by_status.keys()):
            print(f"\n   Status: {status} ({len(by_status[status])} teams)")
            for item in sorted(by_status[status], key=lambda x: x['csv_name'].lower())[:20]:
                print(f"      '{item['csv_name']}' (slug: {item['slug']})")
            if len(by_status[status]) > 20:
                print(f"      ... and {len(by_status[status]) - 20} more")
        print()


def save_report(results, output_file):
    """Save detailed report to JSON file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"📄 Detailed report saved to {output_file}")


def main():
    csv_file = Path('teams.csv')
    db_file = Path('db_teams.json')
    
    if not csv_file.exists():
        print(f"Error: {csv_file} not found!")
        return
        
    if not db_file.exists():
        print(f"Error: {db_file} not found!")
        return
    
    # Load database teams
    with open(db_file, 'r', encoding='utf-8') as f:
        db_teams = json.load(f)
    
    print(f"Loaded {len(db_teams)} teams from database file")
    print("Comparing with CSV file...")
    
    # Compare
    results = compare_teams(csv_file, db_teams)
    
    # Print report
    print_report(results)
    
    # Save detailed report
    report_file = Path('team_comparison_report.json')
    save_report(results, report_file)


if __name__ == '__main__':
    main()

