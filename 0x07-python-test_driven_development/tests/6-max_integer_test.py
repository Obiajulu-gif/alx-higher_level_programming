#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class for unittests
    """
    def test_max(self):
        """Test for max
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)
        self.assertEqual(max_integer([1, 2, 3, 4, float('inf')]), float('inf'))
        self.assertEqual(max_integer([1, 2, 3, 4, float('-inf')]), 4)
        self.assertEqual(max_integer([1, 2, 3, 4, float('nan')]), 4)
        self.assertEqual(max_integer([1, 2, 3, 4, 4]), 4)
        self.assertEqual(max_integer([1, 2, 3, 4, 4.0]), 4)
