from models.cell import Cell
from models.food import Food

from settings import symbols

import unittest


class TestCell(unittest.TestCase):

    def setUp(self):
        self.cell = Cell(Food())

    def test_is_empty_cell_on_full_one(self):
        self.assertFalse(self.cell.is_empty())

    def test_emptying_the_cell(self):
        self.cell.empty_cell()
        self.assertEqual(self.cell.symbol, symbols.EMPTY)


if __name__ == '__main__':
    unittest.main()
