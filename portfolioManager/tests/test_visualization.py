# # test cases for mean variance optimization
# """
# This module is a test module for Mean-Variance model.
# Class:
#   TestKnn, a child class inheritted from unittest.TestCase
# Function:
#   test_smoke(): a smoke test to check if knn can work without systax and runtime
#                 error.
#   test_edge_multi_dimensional_query(): a edge test to check if 2D query
#                                        is handled properly.
#   test_edge_no_match_shape(): a edge test to check if no shape between query and
#                             data is handled properly.
#   test_one_shot_1(), test_one_shot_2(): two one shot tests to check if knn
#                                         has the correct output.
# """
#
# import unittest
# import numpy as np
#
# from ..visualization import plot
# from ..XGboost import xgb_model
#
#
# class TestVisualization(unittest.TestCase):
#     """
#     This is Class for testing Mean-Variance that inheritted from unittest.TestCase.
#     """
#
#     def test_smoke(self):
#         """
#         Simple smoke test to make sure Mean-Variance function runs without systax and
#         runtime error.
#         """
#         data = xgb_model("XLY")
#         plot(data)
#
#     # def test_edge_multi_dimensional_query(self):
#     #     """
#     #     Edge test to make sure the function throws a ValueError
#     #     when the input quert is multi-dimensional.
#     #     """
#     #     data = np.array([[3,1,230],
#     #                     [6,2,745],
#     #                     [6,6,1080],
#     #                     [4,3,495],
#     #                     [2,5,260]])
#     #     query = np.array([[5,4],[6,5]])
#     #     k = 3
#     #     with self.assertRaises(ValueError):
#     #         knn_regression(k, data,query)
#
#     # def test_edge_no_match_shape(self):
#     #     """
#     #     Edge test to make sure the function throws a ValueError
#     #     when the input query and data does not match in shape.
#     #     """
#     #     data = np.array([[3,1,230],
#     #                     [6,2,745],
#     #                     [6,6,1080],
#     #                     [4,3,495],
#     #                     [2,5,260]])
#     #     query = np.array([5,4,3])
#     #     k = 3
#     #     with self.assertRaises(ValueError):
#     #         knn_regression(k, data,query)
#
#     # def test_one_shot_1(self):
#     #     """
#     #     One shot test using the known case of the given input data.
#     #     Should return 733.33.
#     #     """
#     #     data = np.array([[3,1,230],
#     #                     [6,2,745],
#     #                     [6,6,1080],
#     #                     [4,3,495],
#     #                     [2,5,260]])
#
#     #     query = np.array([5,4])
#     #     k = 3
#     #     assert np.isclose(knn_regression(k, data,query), 773.33)
#
#     # def test_one_shot_2(self):
#     #     """
#     #     One shot test using the known case of the given input data.
#     #     Should return 328.33.
#     #     """
#     #     data = np.array([[3,1,230],
#     #                     [6,2,745],
#     #                     [6,6,1080],
#     #                     [4,3,495],
#     #                     [2,5,260]])
#
#     #     query = np.array([0,0])
#     #     k = 3
#     #     assert np.isclose(knn_regression(k, data,query), 328.33)
