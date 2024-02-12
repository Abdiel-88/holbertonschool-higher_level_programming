#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

class TestRectangleValidation(unittest.TestCase):
    def test_width_validation(self):
        """Test width validation."""
        with self.assertRaises(TypeError) as e:
            Rectangle("2", 10)
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(ValueError) as e:
            Rectangle(-2, 10)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_height_validation(self):
        """Test height validation."""
        with self.assertRaises(TypeError) as e:
            Rectangle(10, "2")
        self.assertEqual(str(e.exception), "height must be an integer")

        with self.assertRaises(ValueError) as e:
            Rectangle(10, -2)
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_x_validation(self):
        """Test x validation."""
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 2, "0")
        self.assertEqual(str(e.exception), "x must be an integer")

        with self.assertRaises(ValueError) as e:
            Rectangle(10, 2, -1)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_y_validation(self):
        """Test y validation."""
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 2, 0, "1")
        self.assertEqual(str(e.exception), "y must be an integer")

        with self.assertRaises(ValueError) as e:
            Rectangle(10, 2, 0, -1)
        self.assertEqual(str(e.exception), "y must be >= 0")

if __name__ == "__main__":
    unittest.main()
