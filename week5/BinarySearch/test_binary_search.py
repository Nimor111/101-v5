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

    def test_find_turning_point(self):
        xs = [1, 2, 3, 4, 0, 1, 3, 4]
        self.assertEqual(find_turning_point(xs, 0, 7),
                         'Turning point is 4 on index 3.')
        xs2 = [8, 6, 5, 4]
        self.assertEqual(find_turning_point(xs2, 0, 3),
                         'Turning point is 6 on index 1.')
        xs3 = [5, 6, 4, 1, 3]
        self.assertEqual(find_turning_point(xs3, 0, 4),
                         'Turning point is 4 on index 2.')
        xs4 = [0, 1, 2, 3, 4, 1, 2]
        self.assertEqual(find_turning_point(xs4, 0, 6),
                         'Turning point is 1 on index 5.')
        xs6 = [1, 3, 4, 2]
        self.assertEqual(find_turning_point(xs6, 0, 3),
                         'Turning point is 2 on index 3.')
        xs5 = [0, 1, 3, 4, 5, 2]
        self.assertEqual(find_turning_point(xs5, 0, 5),
                         'Turning point is 2 on index 5.')


if __name__ == '__main__':
    unittest.main()
