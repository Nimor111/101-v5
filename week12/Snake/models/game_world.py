from models.cell import Cell
from models.food import Food
from models.wall import Wall
from models.black_hole import BlackHole
from models.vector2D import Vector2D
from models.python.python_main import Python
import getch
import os


class GameWorld:

    def __init__(self, size):
        self.size = size
        self.world = [[Cell() for _ in range(size)] for _ in range(size)]

    def print_world(self):
        for i in range(len(self.world)):
            for j in self.world[i]:
                print("{} ".format(j), end='')
            print()

    def __getitem__(self, idx):
        return self.world[idx]

    def no_food_board(self):
        for cell in self.world:
            for c in cell:
                if isinstance(c.contents, Food):
                    return False
        return True

    def set_cell(self, cell):
        try:
            if (cell.vector.x >= 0 and cell.vector.y >= 0):
                self.world[cell.vector.x][cell.vector.y] = cell
        except IndexError:
            print("Coordinates go out of the game board!")

    def add_content(self, cells):
        for cell in cells:
            self.set_cell(cell)


def main():
    pass


if __name__ == '__main__':
    main()
