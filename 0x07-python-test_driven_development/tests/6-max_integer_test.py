#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from max_integer import max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        # Test with a list of integers
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

        # Test with an empty list
        self.assertIsNone(max_integer([]))

        # Test with a list containing one integer
        self.assertEqual(max_integer([5]), 5)

        # Test with a list of negative integers
        self.assertEqual(max_integer([-3, -1, -5, -2]), -1)

        # Test with a list containing mixed positive and negative integers
        self.assertEqual(max_integer([-3, 2, -5, 4]), 4)


if __name__ == "__main__":
    unittest.main()
