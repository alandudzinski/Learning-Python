# Import libraries
import csv
import json

# Add a Function Wrapper
def csv_to_json(csv_file, json_file):

    # Read a CSV File
    with open(csv_file, "r") as f:
        reader = csv.DictReader(f)
        data = list(reader)

    # Convert to JSON
    with open(json_file, "w") as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    csv_to_json("contacts.csv", "contacts.json")
    print("Successfully converted .csv to .json!")