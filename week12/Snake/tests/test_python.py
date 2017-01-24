import unittest

from models.python.python_main import Python
from models.game_world import GameWorld
from models.food import Food
from models.vector2D import Vector2D
from models.cell import Cell

from exceptions import exceptions


class TestPython(unittest.TestCase):

    def setUp(self):
        self.game_world = GameWorld(10)
        self.python = Python(self.game_world, (5, 5), 4, Python.DOWN)

    def test_python_killed_with_wrong_direction(self):
        self.python.set_head()
        self.python.set_body()
        self.python.move('w')
        self.assertEqual(self.python.dead, 1)

    def test_eating_food_is_done_correctly(self):
        self.python.set_head()
        self.python.set_body()
        size = len(self.python.get_body_coords())
        self.game_world.set_cell(Cell(Food(), Vector2D(5, 6)))
        self.python.move('d')
        size_n = len(self.python.get_body_coords())
        self.assertEqual(size_n - size, 1)

    def test_get_direction_for_body(self):
        self.python.set_head()
        self.python.set_body()
        self.assertEqual(self.python.get_direction_for_body(Python.UP),
                         Python.DOWN)

    def test_out_of_board_cells_are_not_placed(self):
        self.python.start = Vector2D(0, 0)
        self.python.set_head()
        self.python.set_body()

        self.assertEqual(self.python.get_body_coords(),
                         [str(Vector2D()) for _ in range(4)])

    def test_ascii_code_is_correct(self):
        self.assertEqual(self.python.direction_by_ascii_code('w'), 'up')
        self.assertEqual(self.python.direction_by_ascii_code('d'), 'right')
        self.assertEqual(self.python.direction_by_ascii_code('a'), 'left')
        self.assertEqual(self.python.direction_by_ascii_code('s'), 'down')


if __name__ == '__main__':
    unittest.main()
