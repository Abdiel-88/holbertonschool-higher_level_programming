#!/usr/bin/python3
"""
Unit tests for the Base class.

This test file will validate the functionality of the Base class,
focusing on testing id assignment and management, JSON string conversion,
and writing JSON strings to files.
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle  # Adjust if using a different class
import json
import os


class TestBase(unittest.TestCase):
    """
    Test suite for the Base class, covering id assignment, JSON conversion,
    and file operations.
    """

    @classmethod
    def setUpClass(cls):
        """Reset the Base class counter before the tests run."""
        Base._Base__nb_objects = 0
        cls.filepath = "Rectangle.json"

    @classmethod
    def tearDownClass(cls):
        """Clean up: remove files created by the save_to_file tests."""
        try:
            os.remove(cls.filepath)
        except FileNotFoundError:
            pass

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

    def test_save_to_file_with_rectangles(self):
        """Test saving a list of Rectangle objects to a file."""
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([rect1, rect2])
        with open(self.filepath, 'r') as file:
            content = file.read()
            list_objs = json.loads(content)
            expected = [rect1.to_dictionary(), rect2.to_dictionary()]
            self.assertCountEqual(list_objs, expected)

    def test_save_to_file_none(self):
        """Test saving None, expecting an empty list in the file."""
        Rectangle.save_to_file(None)
        with open(self.filepath, 'r') as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_save_to_file_empty_list(self):
        """Test saving an empty list, expecting an empty list in the file."""
        Rectangle.save_to_file([])
        with open(self.filepath, 'r') as file:
            content = file.read()
            self.assertEqual(content, "[]")


if __name__ == "__main__":
    unittest.main()
