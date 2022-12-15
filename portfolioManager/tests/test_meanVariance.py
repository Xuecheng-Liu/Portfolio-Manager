"""
This module is a test module for Mean-Variance model.
Class:
  TestMV, a child class inheritted from unittest.TestCase
Function:
  test_smoke(): a smoke test to check if MeanVariance can work without systax and runtime
                error.
  test_edge_large_return: an edge test to check if large return could be handled.

As Mean-Variance model computes with real-time stock price, and it may change dramatically
each day, it is hard to write one-shot test to see if output portfolio weight matches our expectation.
Therefore, we do not write any one-shot test here.
"""

import unittest
import numpy as np


from ..meanVariance import calculate_weight


class TestMV(unittest.TestCase):
    """
    This is Class for testing Mean-Variance that inheritted from unittest.TestCase.
    """
    def test_smoke(self):
        """
        Simple smoke test to make sure Mean-Variance function runs without systax and
        runtime error.
        """
        tickers = ["MRNA", "PFE", "JNJ", "GOOGL",
                   "AAPL", "COST", "WMT", "KR", "JPM",
                  "BAC"]
        er = 0.5
        calculate_weight(tickers, er)



    def test_edge_large_return(self):
        """
        One edge test to check if impossibly large return could be handled properly.
        """
        tickers = ["MRNA", "PFE", "JNJ", "GOOGL",
                   "AAPL", "COST", "WMT", "KR", "JPM",
                  "BAC"]
        er = 1
        with self.assertRaises(ValueError):
           calculate_weight(tickers, er)
