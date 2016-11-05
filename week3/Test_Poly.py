import unittest
from Polynom_2 import Polynom


class TestPolynom(unittest.TestCase):
    def setUp(self):
        self.polynom = Polynom('3x^4+x^4+x+7')

    def test_polynom_init(self):
        self.assertEqual(self.polynom.polynom, ['3x^4', 'x^4', 'x', '7'])

    def test_polynom_split_x(self):
        self.assertEqual(self.polynom.split_x(),
                         [(1, 1), (4, 4)])

    def test_polynom_solve(self):
        self.assertEqual(self.polynom.solve(), [[16, 3], [1, 0]])


if __name__ == '__main__':
    unittest.main()
