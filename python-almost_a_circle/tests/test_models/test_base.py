#!/usr/bin/python3
"""
Unit tests for the Base class in the models module.
"""

import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Defines test cases for the Base class functionality.
    """
    @classmethod
    def setUpClass(cls):
        """Resets the Base class counter before any tests run."""
        Base._Base__nb_objects = 0

    @classmethod
    def tearDownClass(cls):
        """Cleanup actions (if any) after all tests are done."""
        pass

    def setUp(self):
        """Resets the Base class counter before each test."""
        Base._Base__nb_objects = 0
        # Ensure any test files are removed before starting a test
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def tearDown(self):
        """Clean up files after tests."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_id_auto_assignment(self):
        """Tests automatic ID assignment."""
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_id_manual_assignment(self):
        """Tests manual ID assignment."""
        base3 = Base(12)
        self.assertEqual(base3.id, 12)

    def test_to_json_string(self):
        """Tests converting list of dictionaries to JSON string."""
        dict_list = [{'id': 2}, {'id': 3}]
        json_str = Base.to_json_string(dict_list)
        self.assertEqual(json_str, json.dumps(dict_list))

    def test_from_json_string(self):
        """Tests converting JSON string to list of dictionaries."""
        json_str = '[{"id": 2}, {"id": 3}]'
        dict_list = Base.from_json_string(json_str)
        self.assertEqual(dict_list, json.loads(json_str))

    def test_save_to_file(self):
        """Tests saving to file."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r1])
        self.assertTrue(os.path.exists('Rectangle.json'))

    def test_load_from_file_no_file(self):
        """Tests loading from a file that doesn't exist."""
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_with_data(self):
        """Tests loading from a file with data."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r1])
        objects = Rectangle.load_from_file()
        self.assertIsInstance(objects[0], Rectangle)
        self.assertEqual(objects[0].to_dictionary(), r1.to_dictionary())


if __name__ == "__main__":
    unittest.main()
