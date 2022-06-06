#!/usr/bin/python3
"""Unittest for Base Class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Unittest for Base Class"""

    def test_base_class(self):
        """Test for Base Class"""
        b1 = Base(-1)
        b2 = Base(0)
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, -1)
        self.assertEqual(b2.id, 0)
        self.assertEqual(b3.id, 1)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 2)

    def test_to_json_string(self):
        """Test for to_json_string"""
        list_dictionaries = [{'id': 1, 'x': 2, 'y': 3},
                             {'id': 2, 'x': 4, 'y': 5}]
        self.assertEqual(Base.to_json_string(list_dictionaries),
                         '[{"id": 1, "x": 2, "y": 3}, {"id": 2, "x": 4, "y": 5}]')
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 1, 'x': 2, 'y': 3}]),
                         '[{"id": 1, "x": 2, "y": 3}]')
        self.assertEqual(Base.to_json_string([{'id': 1, 'x': 2, 'y': 3},
                                              {'id': 2, 'x': 4, 'y': 5}]),
                         '[{"id": 1, "x": 2, "y": 3}, {"id": 2, "x": 4, "y": 5}]')
        self.assertTrue(Base.to_json_string(list_dictionaries)
                        is not Base.to_json_string(None))
        self.assertTrue(Base.to_json_string(list_dictionaries)
                        is not Base.to_json_string([]))
        self.assertTrue(Base.to_json_string(list_dictionaries)
                        is not Base.to_json_string([{'id': 1, 'x': 2, 'y': 3}]))
        self.assertTrue(Base.to_json_string(list_dictionaries)
                        is not Base.to_json_string([{'id': 1, 'x': 2, 'y': 3},
                                                    {'id': 2, 'x': 4, 'y': 5}]))

    def test_save_to_file(self):
        """Test for save_to_file"""
        list_dictionaries = [{'id': 1, 'x': 2, 'y': 3},
                             {'id': 2, 'x': 4, 'y': 5}]
        self.assertTrue(Base.to_json_string(list_dictionaries) is not
                        Base.save_to_file(None))
        self.assertTrue(Base.to_json_string(list_dictionaries) is not
                        Base.save_to_file([]))


if __name__ == '__main__':
    unittest.main()
