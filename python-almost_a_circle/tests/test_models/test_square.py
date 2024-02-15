#!/usr/bin/python3
"""
Unit tests for the Square class from models.square
"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Test suite for validating the Square class functionality.
    """

    def test_square_initialization(self):
        """Test the initialization of a Square."""
        s1 = Square(5, 1, 2, 3)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 2)
        self.assertEqual(s1.id, 3)

    def test_square_str(self):
        """Test the string representation of a Square."""
        s2 = Square(4, 2, 1, 4)
        self.assertEqual(str(s2), "[Square] (4) 2/1 - 4")

    def test_size_getter(self):
        """Test the size getter."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        """Test the size setter."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_validation_type(self):
        """Test the size setter for type validation."""
        s = Square(5)
        with self.assertRaises(TypeError):
            s.size = "10"

    def test_size_validation_value(self):
        """Test the size setter for value validation (must be > 0)."""
        s = Square(5)
        with self.assertRaises(ValueError):
            s.size = -10

    def test_square_area(self):
        """Test the area method for a Square."""
        s3 = Square(3)
        self.assertEqual(s3.area(), 9)

    def test_update_square(self):
        """Test the update method on a Square."""
        s4 = Square(1, 0, 0, 1)
        s4.update(2, 3, 4, 5)
        self.assertEqual(s4.id, 2)
        self.assertEqual(s4.size, 3)
        self.assertEqual(s4.x, 4)
        self.assertEqual(s4.y, 5)

    def test_update_square_kwargs(self):
        """Test the update method with keyword arguments for a Square."""
        s5 = Square(1)
        s5.update(size=7, id=10, y=3, x=2)
        self.assertEqual(s5.id, 10)
        self.assertEqual(s5.size, 7)
        self.assertEqual(s5.x, 2)
        self.assertEqual(s5.y, 3)

    # Tests for error handling, such as invalid sizes or coordinates,
    # can also be included, similar to those for the Rectangle class.


if __name__ == "__main__":
    unittest.main()
