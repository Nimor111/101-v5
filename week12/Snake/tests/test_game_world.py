from models.game_world import GameWorld
from models.food import Food
from models.cell import Cell
from models.vector2D import Vector2D

import unittest


class TestGameWorld(unittest.TestCase):

    def setUp(self):
        self.game_world = GameWorld(5)

    def test_no_food_board_on_empty_world(self):
        self.assertTrue(self.game_world.no_food_board())

    def test_no_food_board_on_set_food_cell(self):
        self.game_world.set_cell(Cell(Food(), Vector2D(3, 4)))

        self.assertFalse(self.game_world.no_food_board())


if __name__ == '__main__':
    unittest.main()
