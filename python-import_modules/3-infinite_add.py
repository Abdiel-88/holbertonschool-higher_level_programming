#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total = 0
    for arg in sys.argv[1:]:  # Skip the script name, start from the first actual argument
        total += int(arg)
    print(total)
