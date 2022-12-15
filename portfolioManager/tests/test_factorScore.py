"""
This module is a test module for Factor_Score model.
Class:
   Test_Factor_Score, a child class inheritted from unittest.TestCase
Function:
  test_smoke(): a smoke test to check if MeanVariance can work without systax and runtime
                error.
  test_edge_large_n, test_edge_few_n_sectors : two edge tests to check if larger n or too few
  stocks and sectors is handled properly.

As factorScore model compute by real-time stock factors, and it may change after company disclose
latest financial statement, it is hard to write one-shot test to see if output sotcks matches our expectation.
Therefore, we do not write any one-shot test here.
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

    def test_edge_few_n_sectors(self):
        """
        Edge case test to see if it is handled properly when only 1 sector and
        n = 1 happens.
        """
        sectors_list = ['XLB']
        n = 1
        with self.assertRaises(ValueError):
            get_sector_stock(n, sectors_list)
