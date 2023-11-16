#!/usr/bin/python3
"""
Test cases for the Base class.
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test cases for the Base class.
    """
    def test_init(self):
        """Test Base initialization."""
        b = Base()
        self.assertIsInstance(b, Base)
        self.assertIsInstance(b.id, int)
