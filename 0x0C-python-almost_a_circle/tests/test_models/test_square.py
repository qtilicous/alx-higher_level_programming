#!/usr/bin/python3
"""
Test cases for the Square class.
"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Test cases for the Square class.
    """
    def test_init(self):
        """Test Square initialization."""
        s = Square(3, 1, 2, 4)
        self.assertIsInstance(s, Square)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 4)
