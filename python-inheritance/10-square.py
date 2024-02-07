#!/usr/bin/python3
"""
This module defines the Square class that inherits from Rectangle.
"""

Square = __import__('10-square').Square

s = Square(13)

print(s)  # Uses the __str__ method
print(s.area())  # Calls the area method
