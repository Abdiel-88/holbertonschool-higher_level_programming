#!/usr/bin/python3
"""
Module to add all command-line arguments to a list
and save them to 'add_item.json'.
Utilizes functions from 'save_to_json_file'
and 'load_from_json_file' modules.
"""


import sys

# Assuming these functions are in the same directory as the script
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

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
