import unittest
from matrix_bombing_plan import *


class TestMatrix(unittest.TestCase):

    def setUp(self):
        self.matrix = [
                      [1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]
        ]

    def test_sum_matrix(self):
        self.assertEqual(sum_matrix(self.matrix), 45)

    def test_validate_neighbours(self):
        self.assertTrue(validate_neighbours((1, 2), 3, 3))
        self.assertFalse(validate_neighbours((3, 2), 3, 3))

    def test_bomb_neighbours(self):
        self.assertEqual(bomb_neighbours((0, 0), self.matrix), 42)

    def test_matrix_bombing_plan(self):
        self.assertEqual(matrix_bombing_plan(self.matrix), {(0, 0): 42,
                                                            (0, 1): 36,
                                                            (0, 2): 37,
                                                            (1, 0): 30,
                                                            (1, 1): 15,
                                                            (1, 2): 23,
                                                            (2, 0): 29,
                                                            (2, 1): 15,
                                                            (2, 2): 26})


if __name__ == "__main__":
    unittest.main()
