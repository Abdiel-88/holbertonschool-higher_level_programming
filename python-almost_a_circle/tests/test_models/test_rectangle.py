#!/usr/bin/python3
"""
Unit tests for the Rectangle class.

This test file will test the validation of
attribute values in the Rectangle class.
It includes tests for type and value errors
for width, height, x, and y attributes.
"""

import unittest
import io
import sys
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

    def setUp(self):
        """Redirect stdout to capture print outputs and reset __nb_objects."""
        self.capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = self.capturedOutput     # Redirect stdout.
        Rectangle._Base__nb_objects = 0      # Reset __nb_objects for id

    def tearDown(self):
        """Reset stdout to default."""
        sys.stdout = sys.__stdout__

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

    def test_attribute_assignment(self):
        """Test correct assignment of attributes."""
        r1 = Rectangle(10, 2, 1, 1, 99)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.id, 99)

    def test_area(self):
        """Test the area method."""
        r2 = Rectangle(3, 2)
        self.assertEqual(r2.area(), 6, "Area should be 6 for a 3x2 Rectangle")

        r3 = Rectangle(8, 7)
        self.assertEqual(r3.area(), 56, "Area should be 56 for an 8x7.")

    def test_display_simple(self):
        """Test the display method with a simple rectangle."""
        r1 = Rectangle(2, 3)
        r1.display()
        expected_output = "##\n##\n##\n"
        self.assertEqual(self.capturedOutput.getvalue(), expected_output)

    def test_display_larger(self):
        """Test the display method with a larger rectangle."""
        self.capturedOutput.truncate(0)  # Clear the previous output
        self.capturedOutput.seek(0)
        r2 = Rectangle(4, 2)
        r2.display()
        expected_output = "####\n####\n"
        self.assertEqual(self.capturedOutput.getvalue(), expected_output)

    def test_area_calculation(self):
        """
        Test the area calculation method of the Rectangle class.
        """
        rect = Rectangle(3, 4)
        self.assertEqual(rect.area(), 12)

    def test_display_output(self):
        """
        Test the display method's output of the Rectangle class.
        """
        rect = Rectangle(2, 3)
        rect.display()
        expected_output = "##\n##\n##\n"
        self.assertEqual(self.capturedOutput.getvalue(), expected_output)

    def test_str_method(self):
        """
        Test the __str__ method output of the Rectangle class.
        """
        rect = Rectangle(4, 6, 2, 2, 50)
        self.assertEqual(str(rect), "[Rectangle] (50) 2/2 - 4/6")

    def test_display_with_xy(self):
        """
        Test the display method's output considering x and y attributes.
        """
        r1 = Rectangle(2, 3, 2, 2)
        r1.display()
        expected_output = "\n\n" + ("  ##\n" * 3)
        self.assertEqual(self.capturedOutput.getvalue(), expected_output)

        self.capturedOutput.truncate(0)
        self.capturedOutput.seek(0)

        r2 = Rectangle(4, 1, 1, 1)
        r2.display()
        expected_output = "\n" + (" ####\n")
        self.assertEqual(self.capturedOutput.getvalue(), expected_output)

    def test_update_id(self):
        """Test updating the id attribute."""
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(1)
        self.assertEqual(r1.id, 1)

    def test_update_width_height(self):
        """Test updating width and height."""
        r2 = Rectangle(10, 10, 10, 10)
        r2.update(1, 2, 3)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 3)

    def test_update_x_y(self):
        """Test updating x and y."""
        r3 = Rectangle(10, 10, 10, 10)
        r3.update(1, 2, 3, 4, 5)
        self.assertEqual(r3.x, 4)
        self.assertEqual(r3.y, 5)

    def test_update_all_attributes(self):
        """Test updating all attributes."""
        r4 = Rectangle(10, 10, 10, 10)
        r4.update(89, 2, 3, 4, 5)
        self.assertEqual(r4.id, 89)
        self.assertEqual(r4.width, 2)
        self.assertEqual(r4.height, 3)
        self.assertEqual(r4.x, 4)
        self.assertEqual(r4.y, 5)

    def test_update_args(self):
        """Test updating attributes using *args."""
        r1 = Rectangle(1, 1, 1, 1, 1)
        r1.update(2, 3, 4, 5, 6)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 6)

    def test_update_kwargs(self):
        """Test updating attributes using **kwargs."""
        r2 = Rectangle(1, 1, 1, 1, 1)
        r2.update(height=10, width=9, y=8, x=7, id=6)
        self.assertEqual(r2.id, 6)
        self.assertEqual(r2.width, 9)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 7)
        self.assertEqual(r2.y, 8)

    def test_update_args_and_kwargs(self):
        """Test that *args takes precedence over **kwargs."""
        r3 = Rectangle(1, 1, 1, 1, 1)
        r3.update(2, 3, 4, id=6, width=9, height=10)
        self.assertEqual(r3.id, 2)  # Updated by *args, not **kwargs
        self.assertEqual(r3.width, 3)  # Updated by *args, not **kwargs
        self.assertEqual(r3.height, 4)  # Updated by *args, not **kwargs
        # x and y not updated by *args, so they remain unchanged
        self.assertEqual(r3.x, 1)
        self.assertEqual(r3.y, 1)

    def test_to_dictionary(self):
        """
        Test that to_dictionary method returns
        the correct dictionary representation.
        """
        rect = Rectangle(10, 7, 2, 8, 1)
        expected_dict = {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}
        self.assertEqual(
            rect.to_dictionary(), expected_dict,
            "The dictionary representation does not match expected values.")


if __name__ == "__main__":
    unittest.main()
