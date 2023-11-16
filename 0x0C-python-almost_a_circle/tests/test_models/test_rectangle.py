#!/usr/bin/python3
"""
Test cases for the Rectangle class.
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class.
    """
    def test_init(self):
        """Test Rectangle initialization."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)
