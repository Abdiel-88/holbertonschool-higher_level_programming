#!/usr/bin/python3
"""Script to test the Base class from models.base"""

from models.base import Base

def test_base():
    # Test with no id given; should auto-assign starting with 1
    b1 = Base()
    print(b1.id)  # Expected output: 1

    # Test with no id again; should increment to 2
    b2 = Base()
    print(b2.id)  # Expected output: 2

    # Test with no id once more; should increment to 3
    b3 = Base()
    print(b3.id)  # Expected output: 3

    # Test with a specific id
    b4 = Base(12)
    print(b4.id)  # Expected output: 12

    # Test with no id again; should continue incrementing automatically, not affected by custom id
    b5 = Base()
    print(b5.id)  # Expected output: 4

if __name__ == "__main__":
    test_base()
