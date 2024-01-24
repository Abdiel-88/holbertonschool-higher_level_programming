#!/usr/bin/python3

# Initialize an empty string
alphabet = ''

# Append each character to the string within the loop
for i in range(97, 123):
    alphabet += chr(i)

# Use only one print function with string formatting
print(f"{alphabet}", end='')
