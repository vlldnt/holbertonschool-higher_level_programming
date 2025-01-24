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

    def test_regular_max(self):
        '''Regular tests'''
        self.assertEqual(max_integer([2, 2, 2]), 2)
        self.assertEqual(max_integer([51]), 51)
        self.assertEqual(max_integer([51, -876, 987]), 987)

    def test_one_inf_zero_ony(self):
        '''integer < 0 test'''
        self.assertEqual(max_integer([-51]), -51)

    def test_none(self):
        '''None test'''
        self.assertEqual(max_integer([None]), None)
    
    def test_edge_case(self):
        '''infinity test'''
        self.assertEqual(max_integer([float('inf'), 8, -987]), float('inf'))