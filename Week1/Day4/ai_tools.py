# ai_tools.py - A program that saves and loads a list using json

import json

favorite_tools = ["ChatGPT", "Copilot", "Gemini", "Claude", "Grok"]

# Save list
with open("favorite_tools.json", "w") as f:
    json.dump(favorite_tools, f)

# Load list
with open("favorite_tools.json", "r") as f:
    tools = json.load(f)

# Print tools
for tool in tools:
    print(tool)