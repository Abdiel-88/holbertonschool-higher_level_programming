#!/usr/bin/python3
"""
Unit tests for the Rectangle class.

This test file will test the validation of
attribute values in the Rectangle class.
It includes tests for type and value errors
for width, height, x, and y attributes.
"""

import unittest
from models.rectangle import Rectangle


class TestRectangleValidation(unittest.TestCase):
    """
    Defines the test suite for the Rectangle class attribute validation.

    Tests are included for:
    - Width validation (integer type and value > 0)
    - Height validation (integer type and value > 0)
    - x validation (integer type and value >= 0)
    - y validation (integer type and value >= 0)
    """

    def test_width_validation(self):
        """Test validation of the width attribute."""
        # Test for TypeError with non-integer width
        with self.assertRaises(TypeError) as e:
            Rectangle("2", 10)
        self.assertEqual(str(e.exception), "width must be an integer")

        # Test for ValueError with negative or zero width
        with self.assertRaises(ValueError) as e:
            Rectangle(-2, 10)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_height_validation(self):
        """Test validation of the height attribute."""
        # Test for TypeError with non-integer height
        with self.assertRaises(TypeError) as e:
            Rectangle(10, "2")
        self.assertEqual(str(e.exception), "height must be an integer")

        # Test for ValueError with negative or zero height
        with self.assertRaises(ValueError) as e:
            Rectangle(10, -2)
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_x_validation(self):
        """Test validation of the x attribute."""
        # Test for TypeError with non-integer x
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 2, "0")
        self.assertEqual(str(e.exception), "x must be an integer")

        # Test for ValueError with negative x
        with self.assertRaises(ValueError) as e:
            Rectangle(10, 2, -1)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_y_validation(self):
        """Test validation of the y attribute."""
        # Test for TypeError with non-integer y
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 2, 0, "1")
        self.assertEqual(str(e.exception), "y must be an integer")

        # Test for ValueError with negative y
        with self.assertRaises(ValueError) as e:
            Rectangle(10, 2, 0, -1)
        self.assertEqual(str(e.exception), "y must be >= 0")


if __name__ == "__main__":
    unittest.main()
