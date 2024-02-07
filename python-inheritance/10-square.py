#!/usr/bin/python3
Square = __import__('10-square').Square

s = Square(13)

print(s)  # Uses the __str__ method
print(s.area())  # Calls the area method
