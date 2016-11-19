import unittest
from binary_search import *


class BinarySearch(unittest.TestCase):

    def setUp(self):
        self.list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_binary_search(self):
        self.assertEqual(binary_search(self.list, 0, 10, 4), 3)
        self.assertEqual(binary_search(self.list, 0, 10, 1), 0)
        self.assertEqual(binary_search(self.list, 0, 10, 10), 9)
        self.assertEqual(binary_search(self.list, 0, 10, 6), 5)
        self.assertEqual(binary_search(self.list, 0, 10, 11), False)

    def test_turning_point(self):
        xs = [1, 2, 3, 4, 5, 3, 2, 1]
        self.assertEqual(turning_point(xs, 0, 7), 5)


if __name__ == '__main__':
    unittest.main()
