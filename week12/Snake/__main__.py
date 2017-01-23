from datetime import datetime

from models.cell import Cell
from models.food import Food
from models.wall import Wall
from models.black_hole import BlackHole
from models.vector2D import Vector2D
from models.python.python_main import Python
from models.game_world import GameWorld
from exceptions.exceptions import DeathError
from context_managers.context_managers import (
    start_log, end_log, move_log, food_log
)
import getch
import os


def main():
    game = GameWorld(20)
    cell1 = Cell(Food(), Vector2D(4, 4))
    cell2 = Cell(Food(), Vector2D(6, 7))
    cell3 = Cell(Food(), Vector2D(6, 8))
    cell4 = Cell(Food(), Vector2D(2, 1))
    cell5 = Cell(Food(), Vector2D(0, 17))
    cell6 = Cell(Food(), Vector2D(13, 15))
    cell7 = Cell(Food(), Vector2D(14, 2))
    cell8 = Cell(Wall(), Vector2D(5, 5))
    cell9 = Cell(Wall(), Vector2D(7, 6))
    cell10 = Cell(Wall(), Vector2D(8, 9))
    cell11 = Cell(Wall(), Vector2D(11, 15))
    cell12 = Cell(Wall(), Vector2D(18, 12))
    cell13 = Cell(Wall(), Vector2D(19, 1))
    cell14 = Cell(BlackHole(), Vector2D(2, 2))
    game.add_content([cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8,
                      cell9, cell10, cell11, cell12, cell13, cell14])
    p = Python(game, (5, 2), 5, Python.DOWN)
    p.set_head()
    p.set_body()
    game.print_world()
    direction = getch.getch()
    with start_log('game_start.txt', 'a') as s:
        pass
    while direction:
        os.system('clear')
        p.move(direction)
        with move_log('move_log.txt', 'a',
                      p.direction_by_ascii_code(direction)) as f:
            pass
        flag = p.is_dead()
        try:
            if not flag:
                game.print_world()
                direction = getch.getch()
            else:
                raise DeathError
        except DeathError:
            with end_log('game_end.txt', 'a') as e:
                pass
            print("GAME OVER")
            break
        if game.no_food_board():
            print("GAME WON!")
            break


if __name__ == '__main__':
    main()
