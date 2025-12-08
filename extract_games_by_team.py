import csv
import os
import re
from collections import defaultdict

def sanitize_filename(name):
    """Sanitizes a string to be safe for filenames."""
    # Replace slashes with dashes
    name = name.replace('/', '-')
    # Remove characters that aren't alphanumerics, underscores, or dashes
    name = re.sub(r'[^a-zA-Z0-9_\- ]', '', name)
    # Replace spaces with underscores
    name = name.strip().replace(' ', '_')
    return name

def parse_date(date_str):
    """Parses MM/DD/YYYY to YYYY-MM-DD for sorting."""
    try:
        parts = date_str.split('/')
        if len(parts) == 3:
            return f"{parts[2]}-{parts[0].zfill(2)}-{parts[1].zfill(2)}"
    except:
        pass
    return sanitize_filename(date_str)

def extract_games(input_file, output_dir="extracted_games"):
    """
    Splits the input CSV into separate game files organized by Date and Team.
    For each (Date, Team) combination, it generates numbered game files.
    """
    
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    # Create output directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if not lines:
        print("File is empty.")
        return

    header = lines[0]
    
    # Data structure: games[date][team_name] = [list_of_game_blocks]
    games_by_date_team = defaultdict(lambda: defaultdict(list))
    
    current_game_lines = []
    
    # Regex to identify date at start of line (MM/DD/YYYY)
    date_pattern = re.compile(r'^\d{1,2}/\d{1,2}/\d{4}')

    def process_game(game_lines):
        if not game_lines:
            return

        # Parse CSV lines to find teams
        # We use csv.reader to handle quoted fields correctly
        reader = csv.reader(game_lines)
        parsed_lines = list(reader)
        
        if not parsed_lines:
            return

        # Line 0 is the Primary Team line
        # Date is col 0, Team is col 3
        primary_row = parsed_lines[0]
        if len(primary_row) < 4:
            return # Malformed

        date_str = primary_row[0]
        team1_name = primary_row[3]
        
        # Find Team 2 (Opponent)
        # Look for a line where col 0 is empty but col 3 is not empty
        team2_name = None
        for row in parsed_lines[1:]:
            if len(row) >= 4:
                # Check if it's a team line (not a player line)
                # Player lines have col 3 empty (based on observation)
                # Team lines have col 3 non-empty
                # Both have col 0 empty
                if not row[0] and row[3]:
                    # This is likely the opponent team line
                    team2_name = row[3]
                    break
        
        if date_str and team1_name:
            # Store for Team 1
            games_by_date_team[date_str][team1_name].append(game_lines)
            
        if date_str and team2_name:
             # Store for Team 2
            games_by_date_team[date_str][team2_name].append(game_lines)


    # Iterate lines to group into games
    # Skip header line in loop, we handled it
    for line in lines[1:]:
        if date_pattern.match(line):
            # New game starts
            if current_game_lines:
                process_game(current_game_lines)
            current_game_lines = [line]
        else:
            current_game_lines.append(line)
            
    # Process last game
    if current_game_lines:
        process_game(current_game_lines)

    # Write files
    files_created = 0
    
    for date_str, teams in games_by_date_team.items():
        formatted_date = parse_date(date_str)
        
        for team, game_list in teams.items():
            safe_team = sanitize_filename(team)
            
            # Create a folder for the date? Or just flat?
            # User said "split by date team". 
            # Let's put them in a folder structure: output_dir/Date/Team/
            # Or just filenames: Date_Team_GameX.csv
            
            # Creating subdirectories for better organization
            team_dir = os.path.join(output_dir, formatted_date, safe_team)
            if not os.path.exists(team_dir):
                os.makedirs(team_dir)
            
            for i, game_lines in enumerate(game_list):
                # i+1 for 1-based indexing
                filename = f"{formatted_date}_{safe_team}_game_{i+1}.csv"
                file_path = os.path.join(team_dir, filename)
                
                with open(file_path, 'w', encoding='utf-8') as out_f:
                    out_f.write(header)
                    out_f.write("".join(game_lines))
                
                files_created += 1

    print(f"Extraction complete. Created {files_created} game files in '{output_dir}'.")

if __name__ == "__main__":
    input_csv = "hall-of-fame-league-season-31-matches.csv"
    extract_games(input_csv)

