#!/usr/bin/python3
"""
Unit tests for the Base class.

This test file validates the functionality of the Base class,
focusing on testing id assignment, JSON string conversion,
and instance creation from dictionaries.
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os
import json


class TestBase(unittest.TestCase):
    """
    Test suite for the Base class.
    """

    @classmethod
    def setUpClass(cls):
        """Reset the Base class counter before the tests run."""
        Base._Base__nb_objects = 0

    def setUp(self):
        """Reset the class attribute before each test."""
        Base._Base__nb_objects = 0

    def test_id_auto_assignment(self):
        """Test automatic id assignment."""
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_id_manual_assignment(self):
        """Test manual id assignment."""
        base3 = Base(10)
        base4 = Base(20)
        self.assertEqual(base3.id, 10)
        self.assertEqual(base4.id, 20)

    def test_id_mixed_assignment(self):
        """Test mixing manual and automatic id assignment."""
        base5 = Base()
        base6 = Base(100)
        base7 = Base()
        self.assertEqual(base5.id, 1)
        self.assertEqual(base6.id, 100)
        self.assertEqual(base7.id, 2)

    def test_to_json_string(self):
        """Test converting a list of dictionaries to a JSON string."""
        list_dicts = [{'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 1},
                      {'id': 2, 'width': 2, 'height': 4, 'x': 0, 'y': 0}]
        json_str = Base.to_json_string(list_dicts)
        self.assertEqual(json_str, json.dumps(list_dicts))

    def test_to_json_string_empty_list(self):
        """Test converting an empty list to a JSON string."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_none(self):
        """Test converting None to a JSON string."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_from_json_string(self):
        """Test converting a JSON string to a list of dictionaries."""
        json_str = (
            '[{"id": 1, "width": 10, "height": 7}, '
            '{"id": 2, "width": 2, "height": 4}]'
            )
        expected = [
            {"id": 1, "width": 10, "height": 7},
            {"id": 2, "width": 2, "height": 4}
            ]
        self.assertEqual(Base.from_json_string(json_str), expected)

    def test_from_json_string_empty(self):
        """Test converting an empty string to a list."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_none(self):
        """Test converting None to a list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_create_rectangle(self):
        """Test creating a Rectangle instance from a dictionary."""
        r_dict = {'width': 3, 'height': 4, 'x': 1, 'y': 2}
        rectangle = Rectangle.create(**r_dict)
        self.assertIsInstance(rectangle, Rectangle)
        self.assertEqual(rectangle.width, 3)
        self.assertEqual(rectangle.height, 4)
        self.assertEqual(rectangle.x, 1)
        self.assertEqual(rectangle.y, 2)

    def test_create_square(self):
        """Test creating a Square instance from a dictionary."""
        s_dict = {'size': 5, 'x': 1, 'y': 2}
        square = Square.create(**s_dict)
        self.assertIsInstance(square, Square)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)


if __name__ == "__main__":
    unittest.main()
