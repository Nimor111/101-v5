import unittest
from game_of_life import validate_coordinates, check_neighbours, ALIVE, DEAD


class TestGame(unittest.TestCase):

    def setUp(self):
        game_matrix = [[DEAD for i in range(9)] for j in range(9)]
        game_matrix[1][1] = ALIVE
        game_matrix[2][2] = ALIVE
        game_matrix[5][4] = ALIVE
        game_matrix[6][7] = ALIVE
        game_matrix[3][4] = ALIVE
        game_matrix[2][3] = ALIVE

    def test_validate_coordinates(self):
        self.assertEqual(validate_coordinates((1, 2)), True)
        self.assertEqual(validate_coordinates((10, 2)), False)

    def test_check_neighbours(self):
        self.assertEqual(check_neighbours(1, 2),
                         [
            ['■', '□', '□', '□', '□', '□', '□', '□', '□'],
            ['□', '■', '■', '□', '□', '□', '□', '□', '□'],
            ['□', '□', '□', '■', '□', '□', '□', '□', '□'],
            ['□', '□', '□', '□', '□', '□', '□', '□', '□'],
            ['□', '□', '□', '■', '□', '□', '□', '□', '□'],
            ['□', '□', '□', '□', '□', '□', '■', '□', '□'],
            ['□', '□', '□', '□', '□', '□', '□', '□', '□'],
            ['□', '□', '□', '□', '□', '□', '□', '□', '□'],
            ['□', '□', '□', '□', '□', '□', '□', '□', '□']])


if __name__ == '__main__':
    unittest.main()
