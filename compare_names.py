#!/usr/bin/env python3
"""
Compare player name spellings from WordPress XML export against database gamertags.
"""

import csv
import json
from pathlib import Path
from collections import defaultdict
from difflib import SequenceMatcher


def similarity(a, b):
    """Calculate similarity ratio between two strings."""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def normalize_name(name):
    """Normalize name for comparison (lowercase, remove all spaces and special formatting)."""
    if not name:
        return ""
    # Remove all spaces and convert to lowercase for comparison
    # This allows "lvlr Syn" to match "LVLrSyn" as a case difference
    return name.replace(' ', '').replace('-', '').replace('_', '').strip().lower()


def compare_names(csv_file, db_gamertags):
    """Compare CSV player names with database gamertags."""
    
    # Read CSV players
    csv_players = {}
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            slug = row.get('slug', '')
            # Skip players with slugs containing "__trashed"
            if '__trashed' in slug:
                continue
            name = row.get('name', '').strip()
            if name and name != '.':
                csv_players[name] = {
                    'slug': slug,
                    'post_id': row.get('post_id', ''),
                    'status': row.get('status', ''),
                }
    
    # Normalize for comparison
    csv_normalized = {normalize_name(k): v for k, v in csv_players.items()}
    db_normalized = {normalize_name(gt): gt for gt in db_gamertags}
    
    # Find matches and differences
    exact_matches = []
    case_differences = []
    csv_only = []
    db_only = []
    similar_names = []
    
    # Check CSV names against DB
    for csv_name, csv_data in csv_players.items():
        csv_norm = normalize_name(csv_name)
        
        if csv_norm in db_normalized:
            db_name = db_normalized[csv_norm]
            if csv_name == db_name:
                exact_matches.append({
                    'csv_name': csv_name,
                    'db_gamertag': db_name,
                    'slug': csv_data['slug'],
                    'post_id': csv_data['post_id'],
                })
            else:
                case_differences.append({
                    'csv_name': csv_name,
                    'db_gamertag': db_name,
                    'slug': csv_data['slug'],
                    'post_id': csv_data['post_id'],
                })
        else:
            # Check for similar names (fuzzy matching)
            best_match = None
            best_similarity = 0
            
            for db_gt in db_gamertags:
                sim = similarity(csv_name, db_gt)
                if sim > best_similarity and sim >= 0.8:  # 80% similarity threshold
                    best_similarity = sim
                    best_match = db_gt
            
            if best_match:
                # If similarity is 95% or higher, treat as case difference (safe to update)
                if best_similarity >= 0.95:
                    case_differences.append({
                        'csv_name': csv_name,
                        'db_gamertag': best_match,
                        'slug': csv_data['slug'],
                        'post_id': csv_data['post_id'],
                    })
                else:
                    # Lower similarity requires manual review
                    similar_names.append({
                        'csv_name': csv_name,
                        'db_gamertag': best_match,
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
                })
    
    # Find DB-only names
    for db_gt in db_gamertags:
        db_norm = normalize_name(db_gt)
        if db_norm not in csv_normalized:
            db_only.append({
                'db_gamertag': db_gt,
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
    print("PLAYER NAME COMPARISON REPORT")
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
            print(f"   DB:  '{item['db_gamertag']}'")
            print(f"   Slug: {item['slug']}")
            print()
    
    if results['similar_names']:
        print("=" * 80)
        print("🔍 SIMILAR NAMES (Potential Matches)")
        print("=" * 80)
        for item in sorted(results['similar_names'], key=lambda x: x['similarity'], reverse=True):
            print(f"   CSV: '{item['csv_name']}'")
            print(f"   DB:  '{item['db_gamertag']}'")
            print(f"   Similarity: {item['similarity']}%")
            print(f"   Slug: {item['slug']}")
            print()
    
    if results['csv_only']:
        print("=" * 80)
        print("📝 CSV ONLY (Not found in database)")
        print("=" * 80)
        # Group by status
        by_status = defaultdict(list)
        for item in results['csv_only']:
            by_status[item['status']].append(item)
        
        for status in sorted(by_status.keys()):
            print(f"\n   Status: {status} ({len(by_status[status])} players)")
            for item in sorted(by_status[status], key=lambda x: x['csv_name'].lower())[:50]:  # Show first 50
                print(f"      '{item['csv_name']}' (slug: {item['slug']})")
            if len(by_status[status]) > 50:
                print(f"      ... and {len(by_status[status]) - 50} more")
        print()
    
    if results['db_only']:
        print("=" * 80)
        print("💾 DB ONLY (Not found in CSV)")
        print("=" * 80)
        for item in sorted(results['db_only'], key=lambda x: x['db_gamertag'].lower())[:100]:  # Show first 100
            print(f"   '{item['db_gamertag']}'")
        if len(results['db_only']) > 100:
            print(f"   ... and {len(results['db_only']) - 100} more")
        print()


def save_report(results, output_file):
    """Save detailed report to JSON file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"📄 Detailed report saved to {output_file}")


def main():
    csv_file = Path('players.csv')
    
    if not csv_file.exists():
        print(f"Error: {csv_file} not found!")
        return
    
    # Load database gamertags from the fetched data
    # This is the data from the Supabase query
    db_gamertags_data = [
        {"gamertag": "|-Dreadz-|"}, {"gamertag": "|GodSent|-"}, {"gamertag": "a little to alot"},
        # ... (all the gamertags from the database query)
    ]
    
    # Extract just the gamertag strings
    db_gamertags = [item['gamertag'] for item in db_gamertags_data]
    
    print(f"Loaded {len(db_gamertags)} gamertags from database")
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

