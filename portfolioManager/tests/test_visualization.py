"""
This module is a test module for visulizaiton module.
Class:
   TestVisualization, a child class inheritted from unittest.TestCase
Function:
  test_smoke(): a smoke test to check if plot function can work without systax and runtime
                error.
"""

import unittest
import numpy as np

from ..visualization import plot
from ..XGboost import xgb_model


class TestVisualization(unittest.TestCase):
    """
    This is Class for testing Mean-Variance that inheritted from unittest.TestCase.
    """

    def test_smoke(self):
        """
        Simple smoke test to make sure Mean-Variance function runs without systax and
        runtime error.
        """
        data = xgb_model("XLY")
        plot(data)
