"""
This module is a test module for Factor_Score model.
Class:
   Test_Factor_Score, a child class inheritted from unittest.TestCase
Function:
  test_smoke(): a smoke test to check if MeanVariance can work without systax and runtime
                error.
  test_one_shot_() : one shot tests to check if get_sector_stock has the correct output.
"""

import unittest
import numpy as np


from ..factorScore import *


class Test_Factor_Score(unittest.TestCase):
    """
    This is Class for testing Mean-Variance that inheritted from unittest.TestCase.
    """
    def test_smoke(self):
        """
        Simple smoke test to make sure get_sector_stock function runs without systax and
        runtime error.
        """
        sectors_list = ['XLB', 'XLF']
        n = 2
        get_sector_factor_table('XLB')
        get_sector_stock(n, sectors_list)

    def test_edge_large_n(self):
        """
        Edge case test to see if it is handled properly when n is larger than
        the number of sector components.
        """
        sectors_list = ['XLB', 'XLF']
        n = 11
        with self.assertRaises(ValueError):
            get_sector_stock(n, sectors_list)


    def test_one_shot_(self):
        """
        One shot test using the known case of the given input data.
        Should return a list the same as the known result.
        """
        sectors_list = ['XLB', 'XLF']
        n = 2
        result = ['DOW', 'APD', 'GS', 'JPM']
        target = get_sector_stock(n, sectors_list)
        self.assertEqual(len(result), len(target))
        for i in range(len(result)):
            self.assertEqual(result[i], target[i])
