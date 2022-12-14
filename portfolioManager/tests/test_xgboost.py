"""
Test cases for XGBoost Algorithm
"""

import unittest
from ..XGboost import xgb_model


class TestXGBoost(unittest.TestCase):
    """
    This class manages the test for XGBoost Algorithm.
    """
    @staticmethod
    def test_smoke():
        """
        Simple smoke test to make sure function runs.
        """
        xgb_model('AAPL')

    def test_edge_invalid_ticker(self):
        """
        Edge test that tests ValueError caused by invalid input ticker.
        """
        with self.assertRaises(ValueError):
            xgb_model('123')
