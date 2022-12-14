# # test cases for mean variance optimization
# """
# This module is a test module for Mean-Variance model.
# Class:
#   TestMV, a child class inheritted from unittest.TestCase
# Function:
#   test_smoke(): a smoke test to check if MeanVariance can work without systax and runtime
#                 error.
#   test_one_shot_1(), test_one_shot_2(): two one shot tests to check if knn
#                                         has the correct output.
# """
#
# import unittest
# import numpy as np
#
#
# from ..meanVariance import calculate_weight
#
#
# class TestMV(unittest.TestCase):
#     """
#     This is Class for testing Mean-Variance that inheritted from unittest.TestCase.
#     """
#     def test_smoke(self):
#         """
#         Simple smoke test to make sure Mean-Variance function runs without systax and
#         runtime error.
#         """
#         tickers = ["MRNA", "PFE", "JNJ", "GOOGL",
#                    "AAPL", "COST", "WMT", "KR", "JPM",
#                   "BAC"]
#         er = 0.5
#         calculate_weight(tickers, er)
#
#
#
#     def test_one_shot_1(self):
#         """
#         One shot test using the known case of the given input data.
#         Should return a dict the same as the known result.
#         """
#         tickers = ["MRNA", "PFE", "JNJ", "GOOGL",
#                    "AAPL", "COST", "WMT", "KR", "JPM",
#                   "BAC"]
#         er = 0.5
#         result = {'AAPL': 0.0, 'BAC': 0.05122, 'COST': 0.05085, 'GOOGL': 0.0, 'JNJ': 0.20852,
#                   'JPM': 0.1215, 'KR': 0.19507, 'MRNA': 0.01429, 'PFE': 0.21176, 'WMT': 0.1468}
#         target  = calculate_weight(tickers, er)
#         for i in result:
#             assert np.isclose(result[i], target[i])
#
#     def test_one_shot_2(self):
#         """
#         One shot test using the known case of the given input data.
#         Should return a dict the same as the known result.
#         """
#         tickers = ["AAPL", "COST", "KR", "JPM","BAC"]
#         er = 0.09
#         target  = calculate_weight(tickers, er)
#         result = {'AAPL': 0.07541, 'BAC': 0.0, 'COST': 0.11021, 'JPM': 0.46874, 'KR': 0.34564}
#         for i in result:
#             assert np.isclose(result[i], target[i])