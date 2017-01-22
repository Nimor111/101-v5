from models.cell import Cell
from models.food import Food
from models.wall import Wall
from models.vector2D import Vector2D
from python.python import Python
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

    def set_cell(self, cell):
        try:
            self.world[cell.vector.x][cell.vector.y] = cell
        except IndexError:
            print("Coordinates go out of the game board!")

    def add_content(self, cells):
        for cell in cells:
            self.set_cell(cell)


def main():
    game = GameWorld(10)
    cell1 = Cell(Food(), Vector2D(4, 4))
    cell2 = Cell(Wall(), Vector2D(5, 5))
    game.add_content([cell1, cell2])
    p = Python(game, (5, 2), 5)
    p.set_head()
    p.set_body()
    game.print_world()
    print("Where to move?")
    direction = getch.getch()
    while direction:
        os.system('clear')
        p.move(direction)
        if (p.is_dead()):
            print("You dead mate!")
            break
        game.print_world()
        print("Where to move?")
        direction = getch.getch()


if __name__ == '__main__':
    main()
