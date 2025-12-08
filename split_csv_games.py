import csv
import re
import os

def split_csv_games(input_file, games_per_file=3):
    """
    Splits a CSV file containing basketball games into multiple files, 
    each containing a specified number of games.
    
    Args:
        input_file (str): Path to the input CSV file.
        games_per_file (int): Number of games per output file.
    """
    
    # Read the entire file content first to handle potential encoding/structure issues manually
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    if not lines:
        print("Input file is empty.")
        return

    header = lines[0]
    content_lines = lines[1:]
    
    # Identify game boundaries
    # A game starts when the first column has a date (MM/DD/YYYY)
    date_pattern = re.compile(r'^\d{1,2}/\d{1,2}/\d{4}')
    
    games = []
    current_game = []
    
    for line in content_lines:
        # Check if line starts with a date (start of a new game)
        # We look at the raw line string, expecting the date to be at the start
        # CSV format: Date,Time,Court...
        if date_pattern.match(line):
            if current_game:
                games.append(current_game)
            current_game = [line]
        else:
            current_game.append(line)
            
    # Append the last game
    if current_game:
        games.append(current_game)
    
    print(f"Total games found: {len(games)}")
    
    # Split into chunks and write files
    base_name = os.path.splitext(input_file)[0]
    
    for i in range(0, len(games), games_per_file):
        chunk = games[i:i + games_per_file]
        file_number = (i // games_per_file) + 1
        output_filename = f"{base_name}-{file_number:03d}.csv"
        
        with open(output_filename, 'w', encoding='utf-8') as out_f:
            out_f.write(header)
            for game in chunk:
                for line in game:
                    out_f.write(line)
        
        print(f"Created {output_filename} with {len(chunk)} games.")

if __name__ == "__main__":
    input_csv = "hall-of-fame-league-season-31-matches.csv"
    if os.path.exists(input_csv):
        split_csv_games(input_csv)
    else:
        print(f"Error: {input_csv} not found.")
