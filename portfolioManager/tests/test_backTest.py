# to do
"""
This module is a test module for backtest model.
Class:
    Test_Back_Test, a child class inheritted from unittest.TestCase
Function:
  test_smoke(): a smoke test to check if MeanVariance can work without systax and runtime
                error.
  test_one_shot_1(), test_one_shot_2(): two one shot tests to check if knn
                                        has the correct output.
"""

import unittest


from ..backTest import*


class Test_Back_Test(unittest.TestCase):
    """
    This is Class for testing Mean-Variance that inheritted from unittest.TestCase.
    """
    def test_smoke(self):
        """
        Simple smoke test to make sure backtest function runs without systax and
        runtime error.
        """
        ticker_list = ['DOW', 'APD', 'GOOGL', 'T', 'PXD']
        weight_list = [0.13, 0.28, 0.45, 0.10, 0.04]
        backtest(ticker_list, weight_list)