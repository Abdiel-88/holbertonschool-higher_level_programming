#!/usr/bin/python3

def uppercase(str):
    for char in str:
        # Check if the character is lowercase
        if 'a' <= char <= 'z':
            # Convert to uppercase by subtracting 32 from ASCII value
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print()  # Print a new line after the string

# Example usage (these lines are for testing and should be in a separate file)
# uppercase("best")
# uppercase("Best School 98 Battery street")
