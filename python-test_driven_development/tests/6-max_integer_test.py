#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines test cases for the max_integer function."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test a list where the max integer is at the beginning."""
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_one_element_list(self):
        """Test a list that contains only one element."""
        self.assertEqual(max_integer([1]), 1)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertIsNone(max_integer([]))

    def test_negative_integers(self):
        """Test a list of negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_floats_and_integers(self):
        """Test a list containing both floats and integers."""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4]), 4)

    def test_string(self):
        """Test with a list of strings to raise TypeError."""
        with self.assertRaises(TypeError):
            max_integer(["string", 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
