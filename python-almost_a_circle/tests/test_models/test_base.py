#!/usr/bin/python3
"""
Unit tests for the Base class.

This test file will validate the functionality of the Base class,
focusing on testing id assignment and management.
"""

import unittest
from models.base import Base
import json


class TestBase(unittest.TestCase):
    """
    Test suite for the Base class.

    This suite tests various scenarios of id assignment to ensure correct
    behavior of the Base class constructor, including automatic and manual
    id assignment.
    """

    def setUp(self):
        """Reset the class attribute before each test."""
        Base._Base__nb_objects = 0

    def test_id_auto_assignment(self):
        """Test that id is correctly auto-assigned when not provided."""
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1, "Auto-assigned id should be 1")
        self.assertEqual(base2.id, 2, "Auto-assigned id should be 2")

    def test_id_manual_assignment(self):
        """Test that a manually assigned id is correctly used."""
        base3 = Base(10)
        base4 = Base(20)
        self.assertEqual(base3.id, 10, "Manually assigned id should be 10")
        self.assertEqual(base4.id, 20, "Manually assigned id should be 20")

    def test_id_mixed_assignment(self):
        """Test a mix of manually and auto-assigned ids."""
        base5 = Base()
        base6 = Base(100)
        base7 = Base()
        self.assertEqual(base5.id, 1, "Auto-assigned id should be 1")
        self.assertEqual(base6.id, 100, "Manually assigned id should be 100")
        self.assertEqual(base7.id, 2, "Next auto-assigned id should be 2")

    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0  # Reset the number of objects before tests

    def test_to_json_string(self):
        """Test conversion of list of dictionaries to JSON string."""
        list_dicts = [{'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 1},
                      {'id': 2, 'width': 2, 'height': 4, 'x': 0, 'y': 0}]
        json_str = Base.to_json_string(list_dicts)
        self.assertEqual(json_str, json.dumps(list_dicts))

    def test_to_json_string_empty_list(self):
        """Test conversion of an empty list to JSON string."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_none(self):
        """Test conversion of None to JSON string."""
        self.assertEqual(Base.to_json_string(None), "[]")


if __name__ == "__main__":
    unittest.main()
