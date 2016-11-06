import unittest as unit
from sudoku import *


class TestSudoku(unit.TestCase):
    def setUp(self):
        self.matrix = [
            [4, 5, 2, 3, 8, 9, 7, 1, 6],
            [3, 8, 7, 4, 6, 1, 2, 9, 5],
            [6, 1, 9, 2, 5, 7, 3, 4, 8],
            [9, 3, 5, 1, 2, 6, 8, 7, 4],
            [7, 6, 4, 9, 3, 8, 5, 2, 1],
            [1, 2, 8, 5, 7, 4, 6, 3, 9],
            [5, 7, 1, 8, 9, 2, 4, 6, 3],
            [8, 9, 6, 7, 4, 3, 1, 5, 2],
            [2, 4, 3, 6, 1, 5, 9, 8, 7]
        ]

    def test_transpose(self):
        self.assertEqual(transpose(self.matrix),
                         [
            [4, 3, 6, 9, 7, 1, 5, 8, 2],
            [5, 8, 1, 3, 6, 2, 7, 9, 4],
            [2, 7, 9, 5, 4, 8, 1, 6, 3],
            [3, 4, 2, 1, 9, 5, 8, 7, 6],
            [8, 6, 5, 2, 3, 7, 9, 4, 1],
            [9, 1, 7, 6, 8, 4, 2, 3, 5],
            [7, 2, 3, 8, 5, 6, 4, 1, 9],
            [1, 9, 4, 7, 2, 3, 6, 5, 8],
            [6, 5, 8, 4, 1, 9, 3, 2, 7]
        ])

    def test_check_threes(self):
        self.assertTrue(check_threes(0, 0, self.matrix))

    def test_sudoku_solved(self):
        self.assertTrue(sudoku_solved(self.matrix))


if __name__ == "__main__":
    unit.main()
