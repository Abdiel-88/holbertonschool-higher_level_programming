#!/usr/bin/python3
"""
Unit tests for the Base class.

This test file validates the functionality of the Base class,
including id assignment, JSON string conversion, and deserialization.
"""

import unittest
from models.base import Base
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


if __name__ == "__main__":
    unittest.main()
