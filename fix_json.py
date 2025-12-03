import pathlib

p = pathlib.Path('db_gamertags.json')
if p.exists():
    content = p.read_text(encoding='utf-8')
    # Fix the specific issue where a backslash precedes the closing quote of the value
    # The pattern in the file is likely `...text\"},` which is invalid JSON if the backslash is meant to be a literal
    # If it was meant to be a literal backslash, it should be `\\`.
    # Given the context, it's likely an artifact.
    fixed = content.replace('\\"},', '"},') 
    p.write_text(fixed, encoding='utf-8')
    print("Fixed db_gamertags.json")
else:
    print("db_gamertags.json not found")

