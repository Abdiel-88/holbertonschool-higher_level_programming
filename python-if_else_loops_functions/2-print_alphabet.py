#!/usr/bin/python3

# Looping from 97 to 123, which are the ASCII values for 'a' to 'z'
for i in range(97, 123):
    # Using string formatting to print each character directly
    print("{}".format(chr(i)), end='')
