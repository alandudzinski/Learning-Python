# exercise4.py - A program that saves & loads data
import json

data = {"course": "Python 101", "duration": "4 weeks"}

# Save dict to a file called course.json
with open("course.json", "w") as f:
    json.dump(data, f)

# Load dict back into Python as a variable called loaded_data
with open("course.json", "r") as f:
    loaded_data = json.load(f)