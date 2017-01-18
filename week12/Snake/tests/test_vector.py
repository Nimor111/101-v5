from models.vector2D import Vector2D
import unittest


class TestVector(unittest.TestCase):

    def setUp(self):
        self.vector1 = Vector2D(1, 1)

    def test_add(self):
        v2 = self.vector1 + Vector2D(2, 2)
        self.assertEqual(v2.x, 3)
        self.assertEqual(v2.y, 3)

    def test_sub(self):
        v2 = self.vector1 - Vector2D(2, 2)
        self.assertEqual(v2.x, -1)
        self.assertEqual(v2.y, -1)

    def test_sub(self):
        v2 = self.vector1 * 3
        self.assertEqual(v2.x, 3)
        self.assertEqual(v2.y, 3)

    def test_div(self):
        v2 = self.vector1 / 3
        self.assertEqual(v2.x, 1/3)
        self.assertEqual(v2.y, 1/3)

    def test_neg(self):
        v2 = -self.vector1
        self.assertEqual(v2.x, -1)
        self.assertEqual(v2.y, -1)


if __name__ == '__main__':
    unittest.main()
