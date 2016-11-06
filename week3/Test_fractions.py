import unittest
from fractions import Fraction


class TestFraction(unittest.TestCase):
    def setUp(self):
        self.fraction = Fraction(3, 4)

    def test_smallest_denom(self):
        self.assertEqual(self.fraction.smallest_denom(self.fraction.numerator,
                         self.fraction.denominator), 12)

    def test_fraction_init(self):
        self.assertEqual(self.fraction.numerator, 3)
        self.assertEqual(self.fraction.denominator, 4)

    def test_fraction_str(self):
        self.assertEqual(str(self.fraction), "3 / 4")

    def test_fraction_eq(self):
        fraction2 = Fraction(3, 4)
        fraction3 = Fraction(4, 5)
        self.assertNotEqual(self.fraction, fraction3)
        self.assertEqual(self.fraction, fraction2)

    def test_fraction_mul(self):
        fraction2 = Fraction(6, 7)
        self.assertEqual(self.fraction.__mul__(fraction2), Fraction(9, 14))

    def test_fraction_add(self):
        fraction2 = Fraction(6, 7)
        self.assertEqual(self.fraction.__add__(fraction2), Fraction(45, 28))

    def test_fraction_sub(self):
        fraction2 = Fraction(6, 7)
        self.assertEqual(self.fraction.__sub__(fraction2), Fraction(-3, 28))


if __name__ == "__main__":
    unittest.main()
