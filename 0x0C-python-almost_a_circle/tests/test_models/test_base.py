#!/usr/bin/python3
"""Unittest for Base Class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unittest for Base Class"""

    def test_base_class(self):
        """Test for Base Class"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)


if __name__ == '__main__':
    unittest.main()
