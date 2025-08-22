# CSV to JSON Converter (Python)
A simple Python script that reads a CSV file (like a contact list) and converts it into a JSON file. Useful for learning file handling and data formats.

## Features
- Reads any .csv file with headers.
- Converts to .json.
- Saves output in the same folder.
- Works from terminal/command line.

## How to Run
```bash
# Clone the repository
git clone https://github.com/alandudzinski/Learning-Python.git

# Go into the folder
cd Day5/

# Replace contents in contacts.csv

# Run the script
python csv_to_json.py

# You should now see a contacts.json version thereof!
```

## Example
Input CSV
```csv
id,name,email
1,Alice,alice@email.com
2,Bob,bob@email.com
```
Output JSON
```json
[
  {"id": "1", "name": "Alice", "email": "alice@email.com"},
  {"id": "2", "name": "Bob", "email": "bob@email.com"}
]
```
## Requirements
- Python 3.12+
- No external libraries needed (uses built-in csv and json libraries)

## Author & Credits
[Alan Dudzinski](https://github.com/alandudzinski)
Part of a 90-Day CPE + AI learning plan