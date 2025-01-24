#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        '''First tests unittest '''
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([2, 2, 2]), 2)
        self.assertEqual(max_integer([51]), 51)
        self.assertEqual(max_integer([51, -876, 987]), 987)
        self.assertEqual(max_integer([-51]), -51)
        self.assertEqual(max_integer([None]), None)
        self.assertEqual(max_integer(['i', 'o']), 'o')
        self.assertEqual(max_integer(['zephir', 'Zephir', 'zéphir']), 'zéphir')
        self.assertEqual(max_integer([float('inf'), 8, -987]), float('inf'))
