from models.wall import Wall
from models.food import Food
from settings import symbols


class Cell:

    def __init__(self, contents=None, vector=None):
        self.contents = contents
        self.symbol = None
        self.set_symbol()
        if vector is not None:
            self.vector = vector

    def empty_cell(self):
        self.contents = None
        self.set_symbol()
        return self

    def is_empty(self):
        return self.contents is None

    def __str__(self):
        return self.symbol

    def __repr__(self):
        return self.__str__()

    def set_symbol(self):
        if self.contents is None:
            self.symbol = symbols.EMPTY
        elif isinstance(self.contents, Food):
            self.symbol = symbols.FOODS
        elif isinstance(self.contents, Wall):
            self.symbol = symbols.WALL


def main():
    pass


if __name__ == '__main__':
    main()
