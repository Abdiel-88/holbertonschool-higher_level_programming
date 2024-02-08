#!/usr/bin/python3
"""
A script that adds all arguments to a Python list and saves them to a file.
The list is saved as a JSON representation in a file named add_item.json.
"""

import sys

# Assuming these functions are in the same directory as the script
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

try:
    # Attempt to load existing items from the file
    items = load_from_json_file(filename)
except FileNotFoundError:
    # Initialize items list if the file doesn't exist
    items = []

# Add command-line arguments to the list, skipping the script name
items.extend(sys.argv[1:])

# Save the updated items list back to the file
save_to_json_file(items, filename)
